import os
import json
import time
from getpass import getpass
from dotenv import load_dotenv
from urllib.parse import urlparse, parse_qs
from http.server import BaseHTTPRequestHandler, HTTPServer
import webbrowser

# Jupyter-compatible imports
try:
    from IPython.display import display, HTML
    from ipywidgets import widgets
    IN_JUPYTER = True
except ImportError:
    IN_JUPYTER = False

from field_manager_python_client import AuthenticatedClient, Client
from field_manager_python_client.api.public import (
    get_organization_by_email_address_public_organizations_email_address_get,
    get_organization_information_public_organizations_organization_id_information_get,
)
from keycloak import KeycloakOpenID

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
DEFAULT_EMAIL = os.getenv("DEFAULT_EMAIL", "default@ngi.no")

# -----------------------------------
# Set the token file under ~/.secrets/
# -----------------------------------
secret_folder = os.path.expanduser("~/.secrets")
os.makedirs(secret_folder, exist_ok=True)  # Create ~/.secrets if it doesn't exist
# os.chmod(secret_folder, 0o700)            # Ensure the folder has 700 (drwx------)

TOKEN_STORE_FILE = os.path.join(secret_folder, "field_manager_token_store.json")

# Initialize public client
public_client = Client(base_url=BASE_URL)

# ---------------------------------------------------
# Token manager class with complete implementation
# ---------------------------------------------------
class TokenManager:
    def __init__(self, keycloak_openid, initial_token=None):
        self.keycloak = keycloak_openid
        self.storage = JupyterStorage() if IN_JUPYTER else FileStorage(TOKEN_STORE_FILE)
        
        if initial_token:
            self._update_tokens(initial_token)
        else:
            self._load_tokens()

    def _update_tokens(self, token):
        self.access_token = token["access_token"]
        self.refresh_token = token.get("refresh_token")
        self.expires_at = time.time() + token["expires_in"]
        self._save_tokens()

    def _load_tokens(self):
        tokens = self.storage.load()
        self.access_token = tokens.get("access_token")
        self.refresh_token = tokens.get("refresh_token")
        self.expires_at = tokens.get("expires_at", 0)

    def _save_tokens(self):
        self.storage.save({
            "access_token": self.access_token,
            "refresh_token": self.refresh_token,
            "expires_at": self.expires_at
        })

    def is_access_token_valid(self):
        return time.time() < self.expires_at - 60

    def refresh_access_token(self):
        if not self.refresh_token:
            return False
        try:
            new_token = self.keycloak.refresh_token(self.refresh_token)
            self._update_tokens(new_token)
            return True
        except Exception as e:
            print(f"Failed to refresh token: {e}")
            return False

    def get_valid_token(self):
        if self.is_access_token_valid():
            return self.access_token
        if self.refresh_access_token():
            return self.access_token
        return None

# ---------------------------
# Storage implementations
# ---------------------------
class FileStorage:
    def __init__(self, filename):
        self.filename = filename

    def save(self, data):
        try:
            with open(self.filename, 'w') as f:
                json.dump(data, f)
        except Exception as e:
            print(f"Error saving tokens: {e}")

    def load(self):
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as f:
                    return json.load(f)
        except Exception as e:
            print(f"Error loading tokens: {e}")
        return {}

class JupyterStorage:
    def save(self, data):
        try:
            from IPython.core.interactiveshell import InteractiveShell
            InteractiveShell.instance().user_ns['_fm_tokens'] = data
        except Exception as e:
            print(f"Error saving to Jupyter storage: {e}")

    def load(self):
        try:
            from IPython.core.interactiveshell import InteractiveShell
            return InteractiveShell.instance().user_ns.get('_fm_tokens', {})
        except Exception as e:
            print(f"Error loading from Jupyter storage: {e}")
            return {}

# ---------------------------
# Authentication flows
# ---------------------------
def authenticate():
    keycloak_openid = KeycloakOpenID(
        server_url=KEYCLOAK_SERVER_URL,
        client_id=KEYCLOAK_CLIENT_ID,
        realm_name=KEYCLOAK_REALM,
    )

    token_manager = TokenManager(keycloak_openid)
    
    if valid_token := token_manager.get_valid_token():
        print("Using cached tokens")
        return AuthenticatedClient(base_url=BASE_URL, token=valid_token)

    email = _get_email_input()

    auth_info = get_auth_method(email)
    auth_method = auth_info["auth_method"]
    authentication_alias = auth_info.get("authentication_alias")

    if auth_method == "sso":
        token_manager = _sso_flow(keycloak_openid, authentication_alias)
    elif auth_method == "password":
        token_manager = _password_flow(keycloak_openid, email)
    else:
        raise ValueError("Unsupported authentication method")

    return AuthenticatedClient(base_url=BASE_URL, token=token_manager.get_valid_token())

def _sso_flow(keycloak_openid, authentication_alias):
    redirect_uri = "urn:ietf:wg:oauth:2.0:oob" if IN_JUPYTER else "http://localhost:8000"
    
    auth_url = keycloak_openid.auth_url(
        redirect_uri=redirect_uri,
        scope=DEFAULT_SCOPE,
    )
    
    if authentication_alias:
        auth_url += f"&kc_idp_hint={authentication_alias}"

    if IN_JUPYTER:
        _show_jupyter_auth_prompt(auth_url)
        code = input("Paste authorization code: ").strip()
    else:
        webbrowser.open_new(auth_url)
        code = _local_server_capture()

    token = keycloak_openid.token(
        grant_type="authorization_code",
        code=code,
        redirect_uri=redirect_uri,
        scope=DEFAULT_SCOPE,
    )
    return TokenManager(keycloak_openid, token)

def _password_flow(keycloak_openid, email):
    password = getpass("Enter password: ")
    token = keycloak_openid.token(
        username=email,
        password=password,
        scope=DEFAULT_SCOPE,
    )
    return TokenManager(keycloak_openid, token)

# ---------------------------
# Helper functions
# ---------------------------
def _get_email_input():
    if IN_JUPYTER:
        email_widget = widgets.Text(value=DEFAULT_EMAIL, description="Email:")
        display(email_widget)
        return email_widget.value
    else:
        print(f"Default email: {DEFAULT_EMAIL}")
        use_default = input("Use default? (y/n): ").strip().lower()
        return DEFAULT_EMAIL if use_default == 'y' else input("Enter email: ").strip()

def _show_jupyter_auth_prompt(auth_url):
    display(HTML(f'''
        <div style="border: 1px solid #e0e0e0; padding: 20px; border-radius: 5px; margin: 10px 0;">
            <h3 style="margin-top: 0;">🔑 SSO Authentication Required</h3>
            <p>1. <a href="{auth_url}" target="_blank" style="color: #0066cc; text-decoration: none;">
                Click here to authenticate
            </a></p>
            <p>2. After completing authentication, paste the authorization code below:</p>
        </div>
    '''))

def _local_server_capture():
    class AuthHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            query = parse_qs(urlparse(self.path).query)
            self.server.auth_code = query.get("code", [None])[0]
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Authentication complete. You may close this window.")

    server = HTTPServer(("localhost", 8000), AuthHandler)
    print("Waiting for authorization code in browser...")
    server.handle_request()
    print("Handled request.")
    return server.auth_code

def get_auth_method(email):
    try:
        org = get_organization_by_email_address_public_organizations_email_address_get.sync(
            client=public_client, email_address=email
        )
        org_info = get_organization_information_public_organizations_organization_id_information_get.sync(
            client=public_client, organization_id=org.organization_id
        )
        return {
            "auth_method": "sso" if org_info.authentication_alias else "password",
            "authentication_alias": org_info.authentication_alias
        }
    except Exception as e:
        print(f"Error determining auth method: {e}")
        return {"auth_method": "password", "authentication_alias": None}

# ---------------------------
# Entry point
# ---------------------------
if __name__ == "__main__":
    client = authenticate()
    print("Authentication successful. Client ready.")