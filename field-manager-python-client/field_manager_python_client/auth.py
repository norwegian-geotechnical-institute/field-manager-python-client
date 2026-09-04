"""Authentication helpers for the Field Manager Python Client."""

import json
import os
import time
import webbrowser
from typing import Any, Literal

import httpx

try:
    from keycloak import KeycloakOpenID
except ImportError:
    raise ImportError("python-keycloak is required for authentication. Install it with: pip install python-keycloak")

from .client import AuthenticatedClient

# Environment configurations
ENVIRONMENTS = {
    "test": {
        "KEYCLOAK_SERVER_URL": "https://keycloak.test.ngiapi.no/auth/",
        "KEYCLOAK_REALM": "tenant-geohub-public",
        "KEYCLOAK_DEVICE_CLIENT_ID": "fieldmanager-devicecode-client",
        "BASE_URL": "https://app.test.fieldmanager.io/api/location",
    },
    "prod": {
        "KEYCLOAK_SERVER_URL": "https://keycloak.ngiapi.no/auth/",
        "KEYCLOAK_REALM": "tenant-geohub-public",
        "KEYCLOAK_DEVICE_CLIENT_ID": "fieldmanager-devicecode-client",
        "BASE_URL": "https://app.fieldmanager.io/api/location",
    },
}

DEFAULT_SCOPE = "openid"


class TokenManager:
    """Manages OAuth2 tokens with automatic refresh capabilities."""

    def __init__(
        self,
        keycloak_openid: KeycloakOpenID,
        initial_token: dict[str, Any] | None = None,
        token_file: str | None = None,
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
            self.refresh_token = initial_token.get("refresh_token")
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

    def get_valid_token(self) -> str | None:
        """Return a valid access token, refreshing if necessary."""
        if self.is_access_token_valid():
            return self.access_token
        elif self.refresh_access_token():
            return self.access_token
        else:
            return None


def _get_device_auth_url(env_config: dict[str, str]) -> str:
    realm = env_config["KEYCLOAK_REALM"]
    server_url = env_config["KEYCLOAK_SERVER_URL"].rstrip("/")
    return f"{server_url}/realms/{realm}/protocol/openid-connect/auth/device"


def _get_token_url(env_config: dict[str, str]) -> str:
    realm = env_config["KEYCLOAK_REALM"]
    server_url = env_config["KEYCLOAK_SERVER_URL"].rstrip("/")
    return f"{server_url}/realms/{realm}/protocol/openid-connect/token"


def _request_device_code(env_config: dict[str, str], scope: str = DEFAULT_SCOPE) -> dict[str, Any]:
    payload = {
        "client_id": env_config["KEYCLOAK_DEVICE_CLIENT_ID"],
        "scope": scope,
    }
    response = httpx.post(_get_device_auth_url(env_config), data=payload, timeout=30.0)
    response.raise_for_status()
    return response.json()


def _poll_for_device_token(
    env_config: dict[str, str], device_code: str, interval: int, expires_in: int
) -> dict[str, Any]:
    payload = {
        "grant_type": "urn:ietf:params:oauth:grant-type:device_code",
        "client_id": env_config["KEYCLOAK_DEVICE_CLIENT_ID"],
        "device_code": device_code,
    }
    deadline = time.time() + expires_in
    current_interval = interval

    while time.time() < deadline:
        response = httpx.post(_get_token_url(env_config), data=payload, timeout=30.0)
        data = response.json()

        if response.is_success and "access_token" in data:
            return data
        if data.get("error") == "authorization_pending":
            print("Waiting for user authorization...")
            time.sleep(current_interval)
            continue
        if data.get("error") == "slow_down":
            current_interval += 5
            time.sleep(current_interval)
            continue
        if data.get("error") == "expired_token":
            break

        raise RuntimeError(f"Device code token request failed: {data}")

    raise RuntimeError("Device code expired before authorization completed.")


def authenticate_with_device_code(
    environment: Literal["test", "prod"] = "test",
    scope: str = "openid profile email offline_access",
    token_file: str | None = None,
    open_browser: bool = True,
) -> AuthenticatedClient:
    """
    Authenticate with Field Manager using OAuth2 Device Authorization Grant.

    This flow is intended for interactive scripting, especially for external
    users who need an API token without using the Field Manager Developer Portal.

    Args:
        environment: Either "test" or "prod" environment
        scope: OAuth2 scope requested for the device-code flow
        token_file: Path to token storage file (default: "token_store.json")
        open_browser: Whether to automatically open the verification URL

    Returns:
        AuthenticatedClient instance ready to use
    """
    if environment not in ENVIRONMENTS:
        raise ValueError(f"Environment must be one of: {list(ENVIRONMENTS.keys())}")

    env_config = ENVIRONMENTS[environment]
    keycloak_openid = KeycloakOpenID(
        server_url=env_config["KEYCLOAK_SERVER_URL"],
        client_id=env_config["KEYCLOAK_DEVICE_CLIENT_ID"],
        realm_name=env_config["KEYCLOAK_REALM"],
    )

    token_manager = TokenManager(keycloak_openid, token_file=token_file)
    token_manager.load_tokens()

    valid_token = token_manager.get_valid_token()
    if valid_token:
        print("Using cached tokens.")
        return AuthenticatedClient(base_url=env_config["BASE_URL"], token=valid_token)

    print("Requesting device authorization...")
    device_data = _request_device_code(env_config, scope=scope)
    verification_uri_complete = device_data.get("verification_uri_complete")
    verification_uri = device_data.get("verification_uri")
    user_code = device_data.get("user_code")

    print("\n=== ACTION REQUIRED ===")
    if verification_uri_complete:
        print("Open this URL in your browser:")
        print(verification_uri_complete)
    if verification_uri:
        print("\nManual fallback URL:")
        print(verification_uri)
    if user_code:
        print(f"\nUser code: {user_code}")
    print("========================\n")

    if open_browser and verification_uri_complete:
        webbrowser.open_new(verification_uri_complete)

    token = _poll_for_device_token(
        env_config=env_config,
        device_code=device_data["device_code"],
        interval=int(device_data.get("interval", 5)),
        expires_in=int(device_data.get("expires_in", 600)),
    )

    token_manager = TokenManager(keycloak_openid, token, token_file=token_file)
    token_manager.save_tokens()
    print("Authentication successful. Client is ready to use.")
    return AuthenticatedClient(base_url=env_config["BASE_URL"], token=token_manager.get_valid_token())


def get_test_device_code_client(**kwargs) -> AuthenticatedClient:
    """Convenience method to get a device-code authenticated client for the test environment."""
    return authenticate_with_device_code(environment="test", **kwargs)


def get_prod_device_code_client(**kwargs) -> AuthenticatedClient:
    """Convenience method to get a device-code authenticated client for the production environment."""
    return authenticate_with_device_code(environment="prod", **kwargs)


def get_service_account_client(
    environment: Literal["test", "prod"] = "test",
    client_id: str | None = None,
    client_secret: str | None = None,
) -> AuthenticatedClient:
    """
    Authenticate using a dedicated Keycloak service-account client.

    This flow is intended for server-to-server automation. The client must be a
    dedicated confidential client created for the requesting integration, not
    the shared interactive `fieldmanager-client`.

    Args:
        environment: Either "test" or "prod" environment
        client_id: Dedicated Keycloak client ID. Falls back to the
            KEYCLOAK_CLIENT_ID environment variable.
        client_secret: Dedicated Keycloak client secret. Falls back to the
            KEYCLOAK_CLIENT_SECRET environment variable.

    Returns:
        AuthenticatedClient for the requested environment

    Raises:
        ValueError: If environment is invalid or required parameters are missing
    """
    if environment not in ENVIRONMENTS:
        raise ValueError(f"Environment must be one of: {list(ENVIRONMENTS.keys())}")

    env_config = ENVIRONMENTS[environment]
    resolved_client_id = client_id or os.getenv("KEYCLOAK_CLIENT_ID")
    resolved_client_secret = client_secret or os.getenv("KEYCLOAK_CLIENT_SECRET")

    if not resolved_client_id:
        raise ValueError("A dedicated service-account client ID is required. Pass client_id or set KEYCLOAK_CLIENT_ID.")
    if resolved_client_id == env_config["KEYCLOAK_CLIENT_ID"]:
        raise ValueError(
            "Service-account authentication requires a dedicated client ID, "
            f"not the shared interactive client {env_config['KEYCLOAK_CLIENT_ID']!r}."
        )
    if not resolved_client_secret:
        raise ValueError(
            "A dedicated service-account client secret is required. Pass client_secret or set KEYCLOAK_CLIENT_SECRET."
        )

    keycloak_openid = KeycloakOpenID(
        server_url=env_config["KEYCLOAK_SERVER_URL"],
        client_id=resolved_client_id,
        realm_name=env_config["KEYCLOAK_REALM"],
        client_secret_key=resolved_client_secret,
    )
    token = keycloak_openid.token(grant_type="client_credentials")
    return AuthenticatedClient(base_url=env_config["BASE_URL"], token=token["access_token"])
