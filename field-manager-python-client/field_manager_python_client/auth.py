"""
Authentication module for Field Manager Python Client.

This module provides easy authentication with Keycloak for both test and production environments.
"""

import json
import os
import time
import webbrowser
from getpass import getpass
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Any, Literal, Optional
from urllib.parse import parse_qs, urlparse

try:
    from keycloak import KeycloakOpenID
except ImportError:
    raise ImportError("python-keycloak is required for authentication. Install it with: pip install python-keycloak")

from .api.public import (
    get_organization_by_email_address_public_organizations_email_address_get,
    get_organization_information_public_organizations_organization_id_information_get,
)
from .client import AuthenticatedClient, Client

# Environment configurations
ENVIRONMENTS = {
    "test": {
        "KEYCLOAK_SERVER_URL": "https://keycloak.test.ngiapi.no/auth/",
        "KEYCLOAK_REALM": "tenant-geohub-public",
        "KEYCLOAK_CLIENT_ID": "fieldmanager-client",
        "BASE_URL": "https://app.test.fieldmanager.io/api/location",
    },
    "prod": {
        "KEYCLOAK_SERVER_URL": "https://keycloak.ngiapi.no/auth/",
        "KEYCLOAK_REALM": "tenant-geohub-public",
        "KEYCLOAK_CLIENT_ID": "fieldmanager-client",
        "BASE_URL": "https://app.fieldmanager.io/api/location",
    },
}

DEFAULT_SCOPE = "openid"


class TokenManager:
    """Manages OAuth2 tokens with automatic refresh capabilities."""

    def __init__(
        self,
        keycloak_openid: KeycloakOpenID,
        initial_token: Optional[dict[str, Any]] = None,
        token_file: Optional[str] = None,
    ):
        """
        Initialize the TokenManager.

        Args:
            keycloak_openid: The Keycloak OpenID client
            initial_token: Optional initial token data
            token_file: Optional path to token storage file
        """
        self.keycloak = keycloak_openid
        self.token_file = token_file or "token_store.json"

        if initial_token:
            self.access_token = initial_token["access_token"]
            self.refresh_token = initial_token["refresh_token"]
            self.expires_at = time.time() + initial_token["expires_in"]
        else:
            self.access_token = None
            self.refresh_token = None
            self.expires_at = 0

    def save_tokens(self) -> None:
        """Save tokens to a file."""
        try:
            with open(self.token_file, "w") as f:
                json.dump(
                    {
                        "access_token": self.access_token,
                        "refresh_token": self.refresh_token,
                        "expires_at": self.expires_at,
                    },
                    f,
                )
        except Exception as e:
            print(f"Unable to save tokens. Error: {e}")

    def load_tokens(self) -> None:
        """Load tokens from a file if it exists."""
        if os.path.exists(self.token_file):
            try:
                with open(self.token_file) as f:
                    data = json.load(f)
                    self.access_token = data.get("access_token")
                    self.refresh_token = data.get("refresh_token")
                    self.expires_at = data.get("expires_at", 0)
            except Exception as e:
                print(f"Unable to load tokens. Error: {e}")

    def is_access_token_valid(self) -> bool:
        """Check if the access token is still valid (with 60-second buffer)."""
        return time.time() < self.expires_at - 60

    def refresh_access_token(self) -> bool:
        """Attempt to refresh the token using the refresh token."""
        if not self.refresh_token:
            return False
        try:
            new_token = self.keycloak.refresh_token(self.refresh_token)
            self.access_token = new_token["access_token"]
            self.refresh_token = new_token.get("refresh_token", self.refresh_token)
            self.expires_at = time.time() + new_token["expires_in"]
            self.save_tokens()
            return True
        except Exception as e:
            print(f"Failed to refresh access token. Error: {e}")
            return False

    def get_valid_token(self) -> Optional[str]:
        """Return a valid access token, refreshing if necessary."""
        if self.is_access_token_valid():
            return self.access_token
        elif self.refresh_access_token():
            return self.access_token
        else:
            return None


class AuthCodeHandler(BaseHTTPRequestHandler):
    """HTTP request handler for OAuth2 authorization code flow."""

    def do_GET(self):
        query = parse_qs(urlparse(self.path).query)
        self.server.auth_code = query.get("code", [None])[0]
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Authorization code received. You may close this window.")

    def log_message(self, format, *args):
        # Suppress log messages
        pass


def _start_local_server() -> Optional[str]:
    """Start a local server to capture the authorization code."""
    server = HTTPServer(("localhost", 8000), AuthCodeHandler)
    print("Waiting for authorization code...")
    server.handle_request()
    return getattr(server, "auth_code", None)


def _get_auth_method(email: str, base_url: str) -> dict[str, Any]:
    """
    Determine if organization uses SSO or password-based auth.

    Args:
        email: User's email address
        base_url: Base URL for the API

    Returns:
        Dictionary with auth_method and authentication_alias
    """
    try:
        public_client = Client(base_url=base_url)

        organization = get_organization_by_email_address_public_organizations_email_address_get.sync(
            client=public_client, email_address=email
        )
        org_id = organization.organization_id

        org_info = get_organization_information_public_organizations_organization_id_information_get.sync(
            client=public_client, organization_id=org_id
        )
        authentication_alias = org_info.authentication_alias
        auth_method = "sso" if authentication_alias else "password"
        return {
            "auth_method": auth_method,
            "authentication_alias": authentication_alias,
        }
    except Exception as e:
        print(f"Unable to fetch org info. Defaulting to password. Error: {e}")
        return {"auth_method": "password", "authentication_alias": None}


def _authenticate_with_sso(
    keycloak_openid: KeycloakOpenID, authentication_alias: Optional[str], scope: str = DEFAULT_SCOPE
) -> TokenManager:
    """Authenticate using SSO (Authorization Code Flow)."""
    redirect_uri = "http://localhost:8000"
    auth_url = keycloak_openid.auth_url(
        redirect_uri=redirect_uri,
        scope=scope,
    )

    # If there's an external IdP alias
    if authentication_alias:
        auth_url += f"&kc_idp_hint={authentication_alias}"

    print("Please log in through your browser.")
    print(f"Opening browser at: {auth_url}")
    webbrowser.open_new(auth_url)

    code = _start_local_server()
    if not code:
        raise RuntimeError("Failed to obtain authorization code.")

    # Exchange the auth code for tokens
    token = keycloak_openid.token(
        grant_type="authorization_code",
        code=code,
        redirect_uri=redirect_uri,
        scope=scope,
    )
    return TokenManager(keycloak_openid, token)


def _authenticate_with_password(
    keycloak_openid: KeycloakOpenID, email: str, scope: str = DEFAULT_SCOPE
) -> TokenManager:
    """Authenticate using password (Resource Owner Password Grant)."""
    password = getpass("Enter Password: ")

    token = keycloak_openid.token(
        username=email,
        password=password,
        scope=scope,
    )
    return TokenManager(keycloak_openid, token)


def authenticate(
    environment: Literal["test", "prod"] = "test",
    email: Optional[str] = None,
    scope: str = DEFAULT_SCOPE,
    token_file: Optional[str] = None,
    interactive: bool = True,
) -> AuthenticatedClient:
    """
    Authenticate with Field Manager and return an AuthenticatedClient.

    Args:
        environment: Either "test" or "prod" environment
        email: User's email address (will prompt if not provided and interactive=True)
        scope: OAuth2 scope (default: "openid")
        token_file: Path to token storage file (default: "token_store.json")
        interactive: Whether to allow interactive prompts (default: True)

    Returns:
        AuthenticatedClient instance ready to use

    Raises:
        ValueError: If environment is invalid or required parameters are missing
        RuntimeError: If authentication fails

    Example:
        >>> client = authenticate(environment="test", email="user@example.com")
        >>> # Use client for API calls
    """
    if environment not in ENVIRONMENTS:
        raise ValueError(f"Environment must be one of: {list(ENVIRONMENTS.keys())}")

    env_config = ENVIRONMENTS[environment]

    # Initialize Keycloak client
    keycloak_openid = KeycloakOpenID(
        server_url=env_config["KEYCLOAK_SERVER_URL"],
        client_id=env_config["KEYCLOAK_CLIENT_ID"],
        realm_name=env_config["KEYCLOAK_REALM"],
    )

    # Initialize TokenManager
    token_manager = TokenManager(keycloak_openid, token_file=token_file)
    token_manager.load_tokens()

    # Check if cached tokens are still valid
    valid_token = token_manager.get_valid_token()
    if valid_token:
        print("Using cached tokens.")
        return AuthenticatedClient(base_url=env_config["BASE_URL"], token=valid_token)

    # No valid cached token, proceed with authentication
    if not email:
        if not interactive:
            raise ValueError("Email is required when interactive=False")
        email = input("Enter your email address: ").strip()

    if not email:
        raise ValueError("Email address is required")

    print(f"Using email: {email}")

    # Determine organization auth method
    auth_info = _get_auth_method(email, env_config["BASE_URL"])
    auth_method = auth_info["auth_method"]
    authentication_alias = auth_info.get("authentication_alias")

    # Run the appropriate authentication flow
    if auth_method == "sso":
        token_manager = _authenticate_with_sso(keycloak_openid, authentication_alias, scope)
    elif auth_method == "password":
        token_manager = _authenticate_with_password(keycloak_openid, email, scope)
    else:
        raise ValueError("Cannot determine auth method for this organization.")

    # Save tokens & return an AuthenticatedClient
    token_manager.save_tokens()
    client = AuthenticatedClient(base_url=env_config["BASE_URL"], token=token_manager.get_valid_token())
    print("Authentication successful. Client is ready to use.")
    return client


def get_test_client(email: Optional[str] = None, **kwargs) -> AuthenticatedClient:
    """
    Convenient method to get an authenticated client for the test environment.

    Args:
        email: User's email address
        **kwargs: Additional arguments passed to authenticate()

    Returns:
        AuthenticatedClient for test environment
    """
    return authenticate(environment="test", email=email, **kwargs)


def get_prod_client(email: Optional[str] = None, **kwargs) -> AuthenticatedClient:
    """
    Convenient method to get an authenticated client for the production environment.

    Args:
        email: User's email address
        **kwargs: Additional arguments passed to authenticate()

    Returns:
        AuthenticatedClient for production environment
    """
    return authenticate(environment="prod", email=email, **kwargs)
