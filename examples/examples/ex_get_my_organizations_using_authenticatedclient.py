"""
Example: Get My Organizations using AuthenticatedClient

This example shows how to:
1. Set up an AuthenticatedClient with manual token configuration
2. Get all organizations you have access to
3. Display organization information

Usage:
- Replace the access_token with your actual Field Manager API token
- Run the script to see your organizations

Run this example:
    python ex_get_my_organizations_using_authenticatedclient.py
"""

from field_manager_python_client import AuthenticatedClient
from field_manager_python_client.api.organizations import (
    get_organizations_organizations_get,
)
from field_manager_python_client.models import Organization

# Configuration - Replace with your actual values
base_url = (
    "https://app.fieldmanager.io/api/location"  # Base URL for the Field Manager API
)
access_token = "eyJhxxx"  # Replace with your actual access token. You can get your token from https://app.fieldmanager.io/developer


def main():
    print("🚀 Getting my organizations using AuthenticatedClient...")
    print()

    # Initialize the authenticated client
    client = AuthenticatedClient(base_url=base_url, token=access_token)

    try:
        with client as client:
            # Get all organizations
            print("🏢 Fetching organizations...")
            organizations: list[Organization] = (
                get_organizations_organizations_get.sync(client=client)
            )

            if not organizations:
                print("❌ No organizations found. Check your access token and permissions.")
                return

            print(f"✅ Found {len(organizations)} organization(s)")
            print()

            # Display organizations
            print("� YOUR ORGANIZATIONS:")
            for i, org in enumerate(organizations, 1):
                print(f"{i}. {org.name}")
                print(f"   ID: {org.organization_id}")
                print()

            print("✅ Done!")

    except Exception as e:
        print(f"❌ Error connecting to API: {e}")
        print("💡 Check your access token and network connection.")


if __name__ == "__main__":
    main()
