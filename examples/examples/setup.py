from field_manager_data_api_client import AuthenticatedClient

# Set up the client
base_url = "https://app.test.fieldmanager.io/api/location"
access_token="REPLACE_WITH_YOUR_ACCESS_TOKEN"
client = AuthenticatedClient(base_url=base_url, token=access_token)