from getpass import getpass
from field_manager_data_api_client import AuthenticatedClient
from keycloak import KeycloakOpenID
import webbrowser

# Keycloak configuration (common for both login types)
KEYCLOAK_SERVER_URL = "https://keycloak.test.ngiapi.no/auth/"
KEYCLOAK_REALM = "tenant-geohub-public"
KEYCLOAK_CLIENT_ID = "fieldmanager-client"

# Base URL for the Field Manager API
base_url = "https://app.test.fieldmanager.io/api/location"

# Initialize Keycloak client
keycloak_openid = KeycloakOpenID(
    server_url=KEYCLOAK_SERVER_URL,
    client_id=KEYCLOAK_CLIENT_ID,
    realm_name=KEYCLOAK_REALM,
)

# Prompt the user to choose a login method
login_method = input("Select login method (1 for SSO, 2 for Username/Password): ")

if login_method == "1":
    # SSO Authentication (Authorization Code Flow)
    redirect_uri = (
        "https://app.test.fieldmanager.io/"  # Update with your app's callback URI
    )
    auth_url = keycloak_openid.auth_url(redirect_uri=redirect_uri, scope="openid")
    print("Please log in through your browser.")
    webbrowser.open(auth_url)

    # After login, Keycloak will redirect to `redirect_uri` with a code.
    # In a real app, you would capture this code from the redirect URI
    # Here, we prompt for it manually
    code = input("Enter the authorization code from the redirect URL: ")

    # Exchange the authorization code for an access token
    token = keycloak_openid.token(
        grant_type="authorization_code",
        code=code,
        redirect_uri=redirect_uri,
    )
    access_token = token["access_token"]

elif login_method == "2":
    # Username/Password Authentication (Resource Owner Password Credentials Flow)
    username = input("Enter Username: ")
    password = getpass("Enter Password: ")

    # Get access token using username and password
    token = keycloak_openid.token(username=username, password=password)
    access_token = token["access_token"]

else:
    print("Invalid login method selected.")
    exit(1)

# Initialize the authenticated client instance with the obtained access token
client = AuthenticatedClient(base_url=base_url, token=access_token)
print("Authentication successful. Client is ready to use.")
