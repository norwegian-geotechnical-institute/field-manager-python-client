from getpass import getpass
from field_manager_data_api_client import AuthenticatedClient
from keycloak import KeycloakOpenID
import webbrowser
import requests
from urllib.parse import urlparse, parse_qs
from http.server import BaseHTTPRequestHandler, HTTPServer

# Keycloak and Field Manager API configuration
KEYCLOAK_SERVER_URL = "https://keycloak.test.ngiapi.no/auth/"
KEYCLOAK_REALM = "tenant-geohub-public"
KEYCLOAK_CLIENT_ID = "fieldmanager-client"

# Base URL for the Field Manager API
base_url = "https://app.test.fieldmanager.io/api/location"
ORG_API_BASE = f"{base_url}/public/organizations"

# Function to check if the organization uses SSO based on authentication_alias presence
def get_auth_method(email):
    """Determine if the organization associated with the email uses SSO based on authentication_alias."""
    org_response = requests.get(f"{ORG_API_BASE}/{email}")
    org_response.raise_for_status()
    organization = org_response.json()
    organization_id = organization.get("organization_id")

    info_response = requests.get(f"{ORG_API_BASE}/{organization_id}/information")
    info_response.raise_for_status()
    organization_info = info_response.json()

    authentication_alias = organization_info.get("authentication_alias")
    auth_method = "sso" if authentication_alias else "password"
    return {
        "auth_method": auth_method,
        "authentication_alias": authentication_alias
    }

# HTTP request handler to capture the authorization code
class AuthCodeHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse the query parameters to get the authorization code
        query = parse_qs(urlparse(self.path).query)
        self.server.auth_code = query.get("code", [None])[0]
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Authorization code received. You may close this window.")

# Function to start a local server and capture the auth code
def start_local_server():
    server = HTTPServer(("localhost", 8000), AuthCodeHandler)
    print("Waiting for authorization code...")
    server.handle_request()
    return server.auth_code

# Prompt the user for email to determine their organization’s authentication method
email = input("Enter your email address: ")
auth_info = get_auth_method(email)
auth_method = auth_info["auth_method"]
authentication_alias = auth_info.get("authentication_alias")

# Initialize Keycloak client
keycloak_openid = KeycloakOpenID(
    server_url=KEYCLOAK_SERVER_URL,
    client_id=KEYCLOAK_CLIENT_ID,
    realm_name=KEYCLOAK_REALM,
)

if auth_method == "sso":
    # SSO Authentication with local redirect URI
    redirect_uri = "http://localhost:8000"
    auth_url = keycloak_openid.auth_url(
        redirect_uri=redirect_uri,
        scope="openid"
    )
    if authentication_alias:
        auth_url += f"&kc_idp_hint={authentication_alias}"

    print("Please log in through your browser.")
    print(f"Opening browser at: {auth_url}")
    webbrowser.open_new(auth_url)

    # Start local server to capture authorization code
    code = start_local_server()
    if not code:
        print("Failed to obtain authorization code.")
        exit(1)

    # Exchange the authorization code for an access token
    token = keycloak_openid.token(
        grant_type="authorization_code",
        code=code,
        redirect_uri=redirect_uri,
    )
    access_token = token["access_token"]

elif auth_method == "password":
    # Username/Password Authentication (Resource Owner Password Credentials Flow)
    username = input("Enter Username: ")
    password = getpass("Enter Password: ")

    # Get access token using username and password
    token = keycloak_openid.token(username=username, password=password)
    access_token = token["access_token"]

else:
    print("Unable to determine authentication method for this organization.")
    exit(1)

# Initialize the authenticated client instance with the obtained access token
client = AuthenticatedClient(base_url=base_url, token=access_token)
print("Authentication successful. Client is ready to use.")
