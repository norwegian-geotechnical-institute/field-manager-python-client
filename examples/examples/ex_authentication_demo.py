#!/usr/bin/env python3
"""
Example: Authentication Demo

This example demonstrates the recommended authentication methods available in
the Field Manager Python client.

Features demonstrated:
1. Device-code authentication for scripting
2. Convenience helper functions for production and test
3. Automatic token caching and refresh

Run this example:
    python ex_authentication_demo.py
"""

from dotenv import load_dotenv
from field_manager_python_client import (
    get_prod_device_code_client,
    get_test_device_code_client,
)
from field_manager_python_client.api.organizations import (
    get_organizations_organizations_get,
)

# Load environment variables
load_dotenv()


def main():
    """Demonstrate different authentication methods."""
    print("🔐 Field Manager Authentication Examples")
    print()

    # Method 1: Device-code authentication
    print("Method 1: Device-code authentication")
    try:
        device_code_client = get_prod_device_code_client()

        with device_code_client as client:
            orgs = get_organizations_organizations_get.sync(client=client)
            print(f"✅ Found {len(orgs)} organizations using device code")
    except Exception as e:
        print(f"❌ Device-code auth failed: {e}")

    print()

    # Method 2: Test environment device-code authentication
    print("Method 2: Device-code authentication for TEST-environment")
    try:
        test_client = get_test_device_code_client()
        with test_client as client:
            orgs = get_organizations_organizations_get.sync(client=client)
            print(f"✅ Found {len(orgs)} organizations using test device code")
    except Exception as e:
        print(
            f"❌ Test device-code auth for TEST-environment failed. If you do not have access to the TEST environment this is expected. {e}"
        )


if __name__ == "__main__":
    main()
