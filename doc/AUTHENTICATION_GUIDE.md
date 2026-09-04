# Field Manager Python Client - Authentication Guide

## Overview

This guide explains how to authenticate with the Field Manager API using the Python client. We support three authentication methods to suit different use cases:

1. **📱 Device Code Authentication** - Preferred for external users and scripting
2. **🔑 Manual Token Setup** - Legacy copy/paste token usage
3. **🤖 Service Account** - For automated workflows and CI/CD pipelines

## Quick Start

### Installation

```bash
pip install field-manager-python-client python-keycloak
```

### Choose Your Authentication Method

Pick the method that best fits your needs:

- **External users or simple scripts**: Use the Device Code Authentication section below
- **Testing or legacy setups**: Use the Manual Token Setup section below
- **Production automation**: Use the Service Account Authentication section below

---

## 1. Device Code Authentication 📱

**Best for:** Scripts and testing.

Uses browser-based sign-in with token caching

### Basic Usage

```python
from field_manager_python_client import get_prod_device_code_client

client = get_prod_device_code_client()
```

### Example Script

See [`ex_device_code_auth.py`](../examples/examples/ex_device_code_auth.py) for a shareable example that support can link to directly.

---

## 2. Manual Token Setup (Legacy) 🔑

**Best for:** Existing setups that already have a token provisioning process.

### Step 1: Get Your Access Token

1. **Log into Field Manager:**

   - Go to https://app.fieldmanager.io

2. **Generate Token:**
   - Navigate to the [Developer Portal](https://app.fieldmanager.io/developer)
   - Click "Generate New Token" or "Get API Token"
   - Copy the access token

### Step 2: Use the Token in Your Code

```python
from field_manager_python_client import AuthenticatedClient

# Production environment (recommended)
client = AuthenticatedClient(
    base_url="https://app.fieldmanager.io/api/location",
    token="your-access-token-here"
)

# Test environment (for internal development)
# client = AuthenticatedClient(
#     base_url="https://app.test.fieldmanager.io/api/location",
#     token="your-access-token-here"
# )
```

### Example Script

Save this as `manual_token_example.py`:

```python
from field_manager_python_client import AuthenticatedClient
from field_manager_python_client.api.organizations import get_organizations_organizations_get

# Replace with your actual token
ACCESS_TOKEN = "your-access-token-here"

client = AuthenticatedClient(
    base_url="https://app.fieldmanager.io/api/location",
    token=ACCESS_TOKEN
)

# Test the connection
organizations = get_organizations_organizations_get.sync(client=client)
if organizations:
    print(f"✅ Successfully connected! Found {len(organizations)} organizations.")
else:
    print("❌ Connection failed. Check your token.")
```

**Reference:** See [`manual_token_setup.py`](../examples/examples/manual_token_setup.py) for the basic setup template.

---

## 3. Service Account Authentication 🤖

**Best for:** Automated workflows, CI/CD pipelines, production systems.

**Features:**

- No user interaction required
- Suitable for server-to-server communication
- Uses client credentials OAuth2 flow
- Recommended for production automation

### Prerequisites

#### 1. Request a Dedicated Service Account Client

1a. **For external users: Ask the Field Manager team to create a dedicated confidential client for your integration**

1b. **For Field Manager team**
   1.  **Access Keycloak Admin Console:**

   - Test: https://keycloak.test.ngiapi.no/auth/admin/
   - Production: https://keycloak.ngiapi.no/auth/admin/

   2. **Verify the dedicated client configuration:**

   - Go to Clients → `your-dedicated-client-id`
   - Enable "Service Accounts Enabled"
   - Save the configuration

   3. **Get Client Secret:**

   - Go to Credentials tab
   - Copy the Client Secret

   4. **Set Permissions:**
   - Go to Service Account Roles tab
   - Assign appropriate roles 

### Implementation

```python
from field_manager_python_client import get_service_account_client

def build_service_account_client(environment: str = "prod"):
    """Get an authenticated client using a dedicated service account."""
    return get_service_account_client(
        environment=environment,
        client_id="your-dedicated-client-id",
        client_secret="your-dedicated-client-secret",
    )

# Usage
client = build_service_account_client("prod")
```

### Environment Setup

#### Option 1: Environment Variables

```bash
# .env file
KEYCLOAK_CLIENT_ID=your-dedicated-client-id
KEYCLOAK_CLIENT_SECRET=your-service-account-client-secret

# Load in Python
from dotenv import load_dotenv
load_dotenv()
```

#### Option 2: CI/CD Pipeline

```yaml
# GitHub Actions example
env:
  KEYCLOAK_CLIENT_ID: ${{ secrets.KEYCLOAK_CLIENT_ID }}
  KEYCLOAK_CLIENT_SECRET: ${{ secrets.KEYCLOAK_CLIENT_SECRET }}

# GitLab CI example
variables:
  KEYCLOAK_CLIENT_ID: $KEYCLOAK_CLIENT_ID
  KEYCLOAK_CLIENT_SECRET: $KEYCLOAK_CLIENT_SECRET
```

### Advanced Service Account Usage

Note: Client-credentials tokens cannot be refreshed; call `get_service_account_client` again to obtain a new token when needed.

```python
import os
from field_manager_python_client import get_service_account_client

class ServiceAccountManager:
    def __init__(self, environment: str = "prod"):
        self.environment = environment
        self.client_id = os.getenv("KEYCLOAK_CLIENT_ID")
        self.client_secret = os.getenv("KEYCLOAK_CLIENT_SECRET")
        self.client = None

        if not self.client_id:
            raise ValueError("KEYCLOAK_CLIENT_ID environment variable is required")
        if not self.client_secret:
            raise ValueError("KEYCLOAK_CLIENT_SECRET environment variable is required")

    def get_client(self):
        """Get an authenticated client."""
        self.client = get_service_account_client(
            environment=self.environment,
            client_id=self.client_id,
            client_secret=self.client_secret,
        )
        return self.client

# Usage
manager = ServiceAccountManager("prod")
client = manager.get_client()
```

### Complete Example

```python
#!/usr/bin/env python3
"""
Service Account Example
Run with:
  KEYCLOAK_CLIENT_ID=your-dedicated-client-id \
  KEYCLOAK_CLIENT_SECRET=your-secret \
  python service_account_example.py
"""

import os
from field_manager_python_client import get_service_account_client
from field_manager_python_client.api.organizations import get_organizations_organizations_get

def main():
    # Check environment variables
    client_id = os.getenv("KEYCLOAK_CLIENT_ID")
    client_secret = os.getenv("KEYCLOAK_CLIENT_SECRET")
    if not client_id:
        print("❌ Error: KEYCLOAK_CLIENT_ID environment variable is required")
        print("Set it with: export KEYCLOAK_CLIENT_ID=your-dedicated-client-id")
        return
    if not client_secret:
        print("❌ Error: KEYCLOAK_CLIENT_SECRET environment variable is required")
        print("Set it with: export KEYCLOAK_CLIENT_SECRET=your-secret")
        return

    try:
        client = get_service_account_client(
            environment="prod",
            client_id=client_id,
            client_secret=client_secret,
        )

        # Test the connection
        organizations = get_organizations_organizations_get.sync(client=client)
        print(f"✅ Service account authentication successful!")
        print(f"Found {len(organizations)} organizations")

    except Exception as e:
        print(f"❌ Authentication failed: {e}")

if __name__ == "__main__":
    main()
```

---

## Troubleshooting

### Common Issues

#### 1. Import Error: "python-keycloak is required"

```bash
pip install python-keycloak
```

#### 2. Browser doesn't open for device-code sign-in

- Check if you're in a headless environment
- Copy the verification URL from console output
- Paste it into a browser manually

#### 3. Token refresh fails

- Delete your token file (usually `token_store.json`)
- Re-authenticate from scratch
- Check if your organization supports refresh tokens

#### 4. Service account permission denied

- User: Ensure client secret is correct
- Field Manager Team: Verify service accounts are enabled on the dedicated client created for your integration
- Field Manager Team: Check that appropriate roles are assigned


#### 5. Token refresh fails or no refresh token is returned

- Delete your token file and authenticate again
- Some device-code responses may not include a refresh token
- In that case, rerun authentication when the cached access token expires

### Debug Mode

Enable debug logging for troubleshooting:

```python
import logging
logging.basicConfig(level=logging.DEBUG)

# Your authentication code here
```

### Testing Your Setup

Use this script to test any authentication method:

```python
#!/usr/bin/env python3
"""Test authentication setup"""

def test_connection(client):
    """Test if the client can connect to the API."""
    try:
        from field_manager_python_client.api.organizations import get_organizations_organizations_get

        organizations = get_organizations_organizations_get.sync(client=client)
        if organizations:
            print(f"✅ Connection successful! Found {len(organizations)} organizations.")
            return True
        else:
            print("❌ Connection failed - no organizations returned.")
            return False
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        return False

# Test your chosen authentication method
if __name__ == "__main__":
    # Method 1: Manual token
    # from field_manager_python_client import AuthenticatedClient
    # client = AuthenticatedClient(
    #     base_url="https://app.test.fieldmanager.io/api/location",
    #     token="your-token-here"
    # )

    # Method 2: Device-code authentication
    from field_manager_python_client import get_prod_device_code_client
    client = get_prod_device_code_client()

    # Method 3: Service account
    # from field_manager_python_client import get_service_account_client
    # client = get_service_account_client(
    #     "prod",
    #     client_id="your-dedicated-client-id",
    #     client_secret="your-dedicated-client-secret",
    # )

    test_connection(client)
```

---

## Next Steps

1. **Choose your authentication method** based on your use case
2. **Test the connection** using the test script above
3. **Explore the examples** in the [`../examples/examples/`](../examples/examples/) directory
4. **Read the [Advanced User Guide](./ADVANCED_USER_GUIDE.md)** for more sophisticated use cases

### Additional Resources

- **[Advanced User Guide](./ADVANCED_USER_GUIDE.md)** - Covers sync/async operations, error handling, and production considerations
- **[Examples Overview](../examples/EXAMPLES_OVERVIEW.md)** - Real-world usage examples
- **[Main Repository](https://github.com/norwegian-geotechnical-institute/field-manager-python-client)** - Source code, issues, and contributions

### Getting Help

If you encounter issues:

1. Check this guide for solutions
2. Test with the basic examples first
3. Verify you're using the correct environment (test vs prod)
4. Open an issue on [GitHub](https://github.com/norwegian-geotechnical-institute/field-manager-python-client/issues)

---

## Security Notes

- **Token Storage**: Tokens are stored locally in JSON format
- **Token Files**: Keep token files secure and add them to `.gitignore`
- **Environment Variables**: Use environment variables for secrets in production
- **Service Accounts**: Use service accounts for automated systems
- **SSL Verification**: Always verify SSL certificates in production
