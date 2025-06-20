#!/usr/bin/env python3
"""
Example: Authentication Demo

This example demonstrates the authentication methods available in the Field Manager Python client.
It shows how to use both the manual authenticate() function and the convenience helper functions
to connect to the Field Manager API.

Features demonstrated:
1. Manual authentication with full control
2. Convenience helper functions (get_prod_client, get_test_client)
3. Automatic token caching and refresh
4. Non-interactive authentication mode

Run this example:
    python ex_authentication_demo.py
"""

import os
from dotenv import load_dotenv
from field_manager_python_client import authenticate, get_prod_client
from field_manager_python_client.api.organizations import (
    get_organizations_organizations_get,
)

# Load environment variables
load_dotenv()
DEFAULT_EMAIL = os.getenv("DEFAULT_EMAIL", "your.email@example.com")


def main():
    """Demonstrate different authentication methods."""
    print("🔐 Field Manager Authentication Examples")
    print()

    # Use default email from environment
    email = DEFAULT_EMAIL
    print(f"Using email: {email}")
    print()

    # Method 1: Manual authentication with environment selection
    print("Method 1: Manual authentication")
    try:
        # You can specify environment and email
        client = authenticate(environment="prod", email=email)

        # Test the client
        with client as client:
            orgs = get_organizations_organizations_get.sync(client=client)
            print(f"✅ Found {len(orgs)} organizations using manual auth")
    except Exception as e:
        print(f"❌ Manual auth failed: {e}")

    print()

    # Method 2: Using get_prod_client() helper function
    print("Method 2: Using get_prod_client() helper function")
    try:
        # Simplified production client creation
        prod_client = get_prod_client(email=email)

        # Test the client
        with prod_client as client:
            orgs = get_organizations_organizations_get.sync(client=client)
            print(f"✅ Found {len(orgs)} organizations using prod helper")
    except Exception as e:
        print(f"❌ Prod client failed: {e}")

    print()
    print("💡 Both methods work the same way!")
    print("   • Use authenticate() for more control")
    print("   • Use get_prod_client() for simplicity")

    print("\n=== Demo completed ===")

    # Additional features demonstration
    print("\nAdditional features:")
    print("- Automatic token caching and refresh")
    print("- Support for both SSO and password authentication")
    print("- Email loaded from .env file (DEFAULT_EMAIL)")
    print("- Built-in environment configurations")
    print("- Type hints and proper error handling")

    print("\n💡 To use your own email, create a .env file with:")
    print("   DEFAULT_EMAIL=your.email@example.com")


if __name__ == "__main__":
    main()
