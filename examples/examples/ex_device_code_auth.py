#!/usr/bin/env python3
"""
Example: Device Code Authentication

This example shows the preferred way for external users to authenticate for
scripting purposes. It uses OAuth2 device-code login, opens a browser-based
sign-in flow, caches tokens locally, and then calls the Field Manager API.

Run this example:
    python ex_device_code_auth.py
"""

from field_manager_python_client.api.organizations import (
    get_organizations_organizations_get,
)
from field_manager_python_client import get_prod_device_code_client


def main() -> None:
    """Authenticate with device code and call a simple API endpoint."""
    client = get_prod_device_code_client(token_file="device_code_tokens.json")

    with client as authenticated_client:
        organizations = get_organizations_organizations_get.sync(
            client=authenticated_client
        )
        print(f"Successfully authenticated. Found {len(organizations)} organizations.")
        print("Organization name(s)")
        for organization in organizations:
            print(organization.name)


if __name__ == "__main__":
    main()
