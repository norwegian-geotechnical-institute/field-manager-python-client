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

# -----------------------------
# Load environment variables
# -----------------------------
load_dotenv()

KEYCLOAK_SERVER_URL = os.getenv(
    "KEYCLOAK_SERVER_URL", "https://keycloak.test.ngiapi.no/auth/"
)
KEYCLOAK_REALM = os.getenv("KEYCLOAK_REALM", "tenant-geohub-public")
KEYCLOAK_CLIENT_ID = os.getenv("KEYCLOAK_CLIENT_ID", "fieldmanager-client")
DEFAULT_SCOPE = os.getenv("KEYCLOAK_SCOPE", "openid")
BASE_URL = os.getenv("BASE_URL", "https://app.test.fieldmanager.io/api/location")
DEFAULT_EMAIL = os.getenv("DEFAULT_EMAIL", "test.user@example.com")
TOKEN_STORE_FILE = "token_store.json"

# Initialize public client
public_client = Client(base_url=BASE_URL)


# ---------------------------------------------------
# Token manager class to handle token caching/refresh
# ---------------------------------------------------
class TokenManager:
    def __init__(self, keycloak_openid, initial_token=None):
        self.keycloak = keycloak_openid
        if initial_token:
            self.access_token = initial_token["access_token"]
            self.refresh_token = initial_token["refresh_token"]
            self.expires_at = time.time() + initial_token["expires_in"]
        else:
            self.access_token = None
            self.refresh_token = None
            self.expires_at = 0

    def save_tokens(self):
        """Save tokens to a file."""
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
        """Load tokens from a file if it exists."""
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
        """Check if the access token is still valid (with 60-second buffer)."""
        return time.time() < self.expires_at - 60

    def refresh_access_token(self):
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

    def get_valid_token(self):
        """Return a valid access token, refreshing if necessary."""
        if self.is_access_token_valid():
            return self.access_token
        elif self.refresh_access_token():
            return self.access_token
        else:
            return None


# --------------------------------------------
# Main function to authenticate & get a client
# --------------------------------------------
def authenticate():
    """Authenticate with Keycloak and return an AuthenticatedClient."""
    keycloak_openid = KeycloakOpenID(
        server_url=KEYCLOAK_SERVER_URL,
        client_id=KEYCLOAK_CLIENT_ID,
        realm_name=KEYCLOAK_REALM,
    )

    # Load cached tokens if any
    token_manager = TokenManager(keycloak_openid)
    token_manager.load_tokens()

    # Check if cached tokens are still valid
    valid_token = token_manager.get_valid_token()
    if valid_token:
        print("Using cached tokens.")
        return AuthenticatedClient(base_url=BASE_URL, token=valid_token)

    # No valid cached token, proceed with interactive login
    print(f"The default email is: {DEFAULT_EMAIL}")
    use_default = input("Do you want to use the default email? (y/n): ").strip().lower()
    email = (
        DEFAULT_EMAIL
        if use_default == "y"
        else input("Enter your email address: ").strip()
    )
    print(f"Using email: {email}")

    # Determine organization method
    auth_info = get_auth_method(email)
    auth_method = auth_info["auth_method"]
    authentication_alias = auth_info.get("authentication_alias")

    # Run the appropriate flow
    if auth_method == "sso":
        token_manager = authenticate_with_sso(keycloak_openid, authentication_alias)
    elif auth_method == "password":
        token_manager = authenticate_with_password(keycloak_openid, email)
    else:
        raise ValueError("Cannot determine auth method for this organization.")

    # Save tokens & return an AuthenticatedClient
    token_manager.save_tokens()
    client = AuthenticatedClient(
        base_url=BASE_URL, token=token_manager.get_valid_token()
    )
    print("Authentication successful. Client is ready to use.")
    return client


# ---------------------------
# SSO / Authorization Code Flow
# ---------------------------
def authenticate_with_sso(keycloak_openid, authentication_alias):
    redirect_uri = "http://localhost:8000"
    # Use the scope from .env (defaults to "openid")
    auth_url = keycloak_openid.auth_url(
        redirect_uri=redirect_uri,
        scope=DEFAULT_SCOPE,  # <--- from environment variable
    )

    # If there's an external IdP alias
    if authentication_alias:
        auth_url += f"&kc_idp_hint={authentication_alias}"

    print("Please log in through your browser.")
    print(f"Opening browser at: {auth_url}")
    webbrowser.open_new(auth_url)

    code = start_local_server()
    if not code:
        raise RuntimeError("Failed to obtain authorization code.")

    # Exchange the auth code for tokens
    token = keycloak_openid.token(
        grant_type="authorization_code",
        code=code,
        redirect_uri=redirect_uri,
        scope=DEFAULT_SCOPE,  # <--- from environment variable
    )
    return TokenManager(keycloak_openid, token)


# -----------------------------------------
# Password / Resource Owner Password Grant
# -----------------------------------------
def authenticate_with_password(keycloak_openid, email):
    password = getpass("Enter Password: ")

    # If your external IdP doesn't allow offline_access, keep the scope as "openid" only.
    token = keycloak_openid.token(
        username=email,
        password=password,
        scope=DEFAULT_SCOPE,  # <--- from environment variable
    )
    return TokenManager(keycloak_openid, token)


# ----------------------------------------------------------------
# Local server & request handler to capture the Keycloak auth code
# ----------------------------------------------------------------
def start_local_server():
    server = HTTPServer(("localhost", 8000), AuthCodeHandler)
    print("Waiting for authorization code...")
    server.handle_request()
    return server.auth_code


class AuthCodeHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        query = parse_qs(urlparse(self.path).query)
        self.server.auth_code = query.get("code", [None])[0]
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Authorization code received. You may close this window.")


# ---------------------------------------------------------
# Determine if organization uses SSO or password-based auth
# ---------------------------------------------------------
def get_auth_method(email):
    """Check if the organization has an authentication_alias => SSO, else password."""
    try:
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


# ----------------------------------------------
# __main__ block to demonstrate usage (optional)
# ----------------------------------------------
if __name__ == "__main__":
    client = authenticate()
    # Now you have a ready-to-use AuthenticatedClient instance.
