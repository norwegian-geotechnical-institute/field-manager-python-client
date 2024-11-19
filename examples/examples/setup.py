"""
This setup script configures the AuthenticatedClient for interacting with the Field Manager API.

Usage:
- Replace `access_token` with a valid access token to authenticate requests.
- The `base_url` is the API endpoint for the Field Manager API.
- The `client` instance can then be used in other scripts to make authenticated requests.

Requirements:
- Ensure that the `field_manager_data_api_client` library is installed in your environment.
"""

from field_manager_data_api_client import AuthenticatedClient

# Set up the client with the base URL and access token
base_url = "https://app.test.fieldmanager.io/api/location"  # Base URL for the Field Manager API
access_token = "REPLACE_WITH_YOUR_ACCESS_TOKEN"  # Replace with your actual access token for authentication

# Initialize the authenticated client instance
client = AuthenticatedClient(base_url=base_url, token=access_token)
