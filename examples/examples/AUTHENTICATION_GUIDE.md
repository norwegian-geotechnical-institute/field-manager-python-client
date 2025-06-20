# Field Manager Python Client - Authentication Guide

## Overview

The authentication system has been improved and integrated directly into the main `field-manager-python-client` package. You no longer need to deal with separate `.env` files or complex setup scripts.

## Quick Start

### Installation

Make sure you have the required dependency for authentication:

```bash
pip install python-keycloak
```

### Basic Usage

```python
from field_manager_python_client import authenticate, get_test_client, get_prod_client

# Method 1: Using the general authenticate function
client = authenticate(environment="test", email="your.email@example.com")

# Method 2: Using convenience functions
test_client = get_test_client(email="your.email@example.com")
prod_client = get_prod_client(email="your.email@example.com")
```

## Available Functions

### `authenticate(environment, email, scope, token_file, interactive)`

Main authentication function with full control over parameters.

**Parameters:**
- `environment` (str): Either "test" or "prod"
- `email` (str, optional): User's email address. Will prompt if not provided and interactive=True
- `scope` (str, optional): OAuth2 scope (default: "openid")
- `token_file` (str, optional): Path to token storage file (default: "token_store.json")
- `interactive` (bool, optional): Whether to allow interactive prompts (default: True)

**Returns:** `AuthenticatedClient` ready to use

**Example:**
```python
client = authenticate(
    environment="test",
    email="user@example.com",
    scope="openid offline_access",  # Optional: for refresh tokens
    token_file="my_tokens.json"     # Optional: custom token file
)
```

### `get_test_client(email, **kwargs)`

Convenience function for test environment authentication.

**Example:**
```python
client = get_test_client(email="user@example.com")
```

### `get_prod_client(email, **kwargs)`

Convenience function for production environment authentication.

**Example:**
```python 
client = get_prod_client(email="user@example.com")
```

## Environment Configurations

The system has built-in configurations for both environments:

### Test Environment
- **Keycloak Server:** `https://keycloak.test.ngiapi.no/auth/`
- **API Base URL:** `https://app.test.fieldmanager.io/api/location`
- **Realm:** `tenant-geohub-public`
- **Client ID:** `fieldmanager-client`

### Production Environment
- **Keycloak Server:** `https://keycloak.ngiapi.no/auth/`
- **API Base URL:** `https://app.fieldmanager.io/api/location`
- **Realm:** `tenant-geohub-public`
- **Client ID:** `fieldmanager-client`

## Authentication Methods

The system automatically detects your organization's authentication method:

### SSO (Single Sign-On)
If your organization uses an external identity provider (like Azure AD), the system will:
1. Open your default browser
2. Redirect you to your organization's login page
3. Handle the OAuth2 authorization code flow
4. Save tokens for future use

### Password-based Authentication
If your organization uses Keycloak directly, you'll be prompted for:
1. Email address
2. Password

## Token Management

### Automatic Token Caching
- Tokens are automatically saved to a local file (default: `token_store.json`)
- Subsequent authentication attempts will use cached tokens if still valid
- Custom token file path can be specified

### Automatic Token Refresh
- Tokens are automatically refreshed when they expire
- 60-second buffer ensures tokens don't expire during API calls
- Failed refresh attempts trigger re-authentication

### Token Storage Location
By default, tokens are stored in the current working directory as `token_store.json`. You can customize this:

```python
client = authenticate(
    environment="test",
    email="user@example.com",
    token_file="/path/to/my/tokens.json"
)
```

## Migration from Old System

If you're migrating from the old examples-based authentication:

### Old Way (examples/setup_auto_fetch_token.py)
```python
from examples.setup_auto_fetch_token import authenticate
client = authenticate()
```

### New Way (integrated)
```python
from field_manager_python_client import get_test_client
client = get_test_client(email="your.email@example.com")
```

## Error Handling

Common exceptions and how to handle them:

```python
from field_manager_python_client import authenticate

try:
    client = authenticate(environment="test", email="user@example.com")
    # Use client for API calls
except ValueError as e:
    # Invalid environment or missing required parameters
    print(f"Configuration error: {e}")
except RuntimeError as e:
    # Authentication failed
    print(f"Authentication failed: {e}")
except ImportError as e:
    # Missing python-keycloak dependency
    print(f"Missing dependency: {e}")
```

## Advanced Usage

### Non-interactive Authentication
For scripts or automated environments:

```python
client = authenticate(
    environment="prod",
    email="service-account@example.com",
    interactive=False  # Will raise ValueError if email not provided
)
```

### Custom Scopes
For organizations with offline access enabled:

```python
client = authenticate(
    environment="test",
    email="user@example.com",
    scope="openid offline_access"  # Enables refresh tokens
)
```

### Using the TokenManager directly
For advanced token management:

```python
from field_manager_python_client import TokenManager
from keycloak import KeycloakOpenID

keycloak_openid = KeycloakOpenID(
    server_url="https://keycloak.test.ngiapi.no/auth/",
    client_id="fieldmanager-client",
    realm_name="tenant-geohub-public"
)

token_manager = TokenManager(keycloak_openid, token_file="custom_tokens.json")
token_manager.load_tokens()

if token_manager.get_valid_token():
    print("Valid token available")
else:
    print("Need to authenticate")
```

## Troubleshooting

### Common Issues

1. **Import Error: "python-keycloak is required"**
   ```bash
   pip install python-keycloak
   ```

2. **Browser doesn't open for SSO**
   - Check if you're in a headless environment
   - Try copying the auth URL manually from the console output

3. **Token refresh fails**
   - Delete the token file and re-authenticate
   - Check if your organization's IdP supports refresh tokens

4. **"Unable to fetch org info" message**
   - Check your internet connection
   - Verify the API endpoints are accessible
   - The system will fallback to password authentication

### Getting Help

If you encounter issues:
1. Check this guide for common solutions
2. Verify your organization's authentication setup
3. Test with the basic examples first
4. Check if you're using the correct environment (test vs prod)

## Security Notes

- Tokens are stored locally in JSON format
- Token files should be kept secure and not committed to version control
- Consider adding `token_store.json` to your `.gitignore`
- For production use, consider using environment variables or secure credential stores 