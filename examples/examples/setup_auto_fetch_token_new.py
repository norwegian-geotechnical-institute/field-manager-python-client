import os
import json
import time
from getpass import getpass
from dotenv import load_dotenv
from field_manager_python_client import AuthenticatedClient, Client
from field_manager_python_client.api.public import (
    get_organization_by_email_address_public_organizations_email_address_get,
    get_organization_information_public_organizations_organization_id_information_get,
)
from keycloak import KeycloakOpenID
import webbrowser
from urllib.parse import urlparse, parse_qs
from http.server import BaseHTTPRequestHandler, HTTPServer

# Load environment variables from .env
load_dotenv()

# Retrieve values from environment or use sensible defaults
KEYCLOAK_SERVER_URL = os.getenv(
    "KEYCLOAK_SERVER_URL", "https://keycloak.test.ngiapi.no/auth/"
)
KEYCLOAK_REALM = os.getenv("KEYCLOAK_REALM", "tenant-geohub-public")
KEYCLOAK_CLIENT_ID = os.getenv("KEYCLOAK_CLIENT_ID", "fieldmanager-client")
base_url = os.getenv("BASE_URL", "https://app.test.fieldmanager.io/api/location")

# Default email loaded from .env (fallback is "test.user@example.com")
default_email = os.getenv("DEFAULT_EMAIL", "test.user@example.com")
TOKEN_STORE_FILE = "token_store.json"

# Initialize public client
public_client = Client(base_url=base_url)


# Token manager class to handle token caching and refresh
class TokenManager:
    def __init__(self, keycloak_openid, initial_token=None):
        self.keycloak = keycloak_openid
        self.access_token = initial_token["access_token"] if initial_token else None
        self.refresh_token = initial_token["refresh_token"] if initial_token else None
        self.expires_at = time.time() + initial_token["expires_in"] if initial_token else 0

    def save_tokens(self):
        """Save tokens to a file for future use."""
        try:
            with open(TOKEN_STORE_FILE, "w") as f:
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

    def load_tokens(self):
        """Load tokens from a file."""
        if os.path.exists(TOKEN_STORE_FILE):
            try:
                with open(TOKEN_STORE_FILE, "r") as f:
                    data = json.load(f)
                    self.access_token = data.get("access_token")
                    self.refresh_token = data.get("refresh_token")
                    self.expires_at = data.get("expires_at", 0)
            except Exception as e:
                print(f"Unable to load tokens. Error: {e}")

    def is_access_token_valid(self):
        """Check if the access token is still valid."""
        return time.time() < self.expires_at - 60  # Refresh 60 seconds before expiry

    def refresh_access_token(self):
        """Refresh the access token using the refresh token."""
        if not self.refresh_token:
            return False

        try:
            token = self.keycloak.refresh_token(
                self.refresh_token,
            )
            self.access_token = token["access_token"]
            self.refresh_token = token.get("refresh_token", self.refresh_token)  # Preserve if no new refresh token
            self.expires_at = time.time() + token["expires_in"]
            self.save_tokens()
            return True
        except Exception as e:
            print(f"Failed to refresh access token. Error: {e}")
            return False

    def get_valid_token(self):
        """Return a valid access token, refreshing if necessary."""
        if self.is_access_token_valid():
            return self.access_token
        elif self.refresh_access_token():
            return self.access_token
        else:
            return None


# Function to authenticate and return a client
def authenticate():
    """Authenticate with Keycloak and return an authenticated client."""
    keycloak_openid = KeycloakOpenID(
        server_url=KEYCLOAK_SERVER_URL,
        client_id=KEYCLOAK_CLIENT_ID,
        realm_name=KEYCLOAK_REALM,
    )

    # Load cached tokens if available
    token_manager = TokenManager(keycloak_openid)
    token_manager.load_tokens()

    # Check if cached tokens are valid
    valid_token = token_manager.get_valid_token()
    if valid_token:
        print("Using cached tokens.")
        return AuthenticatedClient(base_url=base_url, token=valid_token)

    # Prompt the user for email
    print(f"The default email is: {default_email}")
    use_default = input("Do you want to use the default email? (y/n): ").strip().lower()
    email = default_email if use_default == "y" else input("Enter your email address: ").strip()
    print(f"Using email: {email}")

    # Determine authentication method
    auth_info = get_auth_method(email)
    auth_method = auth_info["auth_method"]
    authentication_alias = auth_info.get("authentication_alias")

    if auth_method == "sso":
        token_manager = authenticate_with_sso(keycloak_openid, authentication_alias)
    elif auth_method == "password":
        token_manager = authenticate_with_password(keycloak_openid, email)
    else:
        raise ValueError("Unable to determine authentication method for this organization.")

    # Save tokens for future use
    token_manager.save_tokens()

    # Create and return authenticated client
    client = AuthenticatedClient(
        base_url=base_url,
        token=token_manager.get_valid_token(),
    )
    print("Authentication successful. Client is ready to use.")
    return client


# Helper functions for authentication flows
def authenticate_with_sso(keycloak_openid, authentication_alias):
    redirect_uri = "http://localhost:8000"
    auth_url = keycloak_openid.auth_url(
        redirect_uri=redirect_uri,
        scope="openid offline_access",
    )
    
    # Append the parameter to pre-check "Remember Me"
    auth_url += "&kc_remember_me=1"
    
    # Append kc_idp_hint if authentication_alias is provided
    if authentication_alias:
        auth_url += f"&kc_idp_hint={authentication_alias}"

    print("Please log in through your browser.")
    print(f"Opening browser at: {auth_url}")
    webbrowser.open_new(auth_url)
    code = start_local_server()

    token = keycloak_openid.token(
        grant_type="authorization_code",
        code=code,
        redirect_uri=redirect_uri,
        scope="openid offline_access",
    )
    return TokenManager(keycloak_openid, token)


def authenticate_with_password(keycloak_openid, email):
    password = getpass("Enter Password: ")
    token = keycloak_openid.token(
        username=email,
        password=password,
        scope="openid offline_access",
    )
    return TokenManager(keycloak_openid, token)


# Function to start a local server and capture the auth code
def start_local_server():
    server = HTTPServer(("localhost", 8000), AuthCodeHandler)
    print("Waiting for authorization code...")
    server.handle_request()
    return server.auth_code


# HTTP request handler to capture the authorization code
class AuthCodeHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        query = parse_qs(urlparse(self.path).query)
        self.server.auth_code = query.get("code", [None])[0]
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Authorization code received. You may close this window.")


# Function to determine authentication method
def get_auth_method(email):
    """Determine if the organization associated with the email uses SSO."""
    try:
        organization = get_organization_by_email_address_public_organizations_email_address_get.sync(
            client=public_client, email_address=email
        )
        organization_id = organization.organization_id

        organization_info = get_organization_information_public_organizations_organization_id_information_get.sync(
            client=public_client, organization_id=organization_id
        )
        authentication_alias = organization_info.authentication_alias
        auth_method = "sso" if authentication_alias else "password"
        return {"auth_method": auth_method, "authentication_alias": authentication_alias}

    except Exception as e:
        print(f"Unable to fetch organization information. Defaulting to password login. Error: {e}")
        return {"auth_method": "password", "authentication_alias": None}


# Main block for testing
if __name__ == "__main__":
    client = authenticate()