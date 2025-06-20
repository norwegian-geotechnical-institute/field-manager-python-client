# field-manager-python-client
A client library for accessing Field Manager Data API

## 🚀 Quick Start

### Installation

```bash
pip install field_manager_python_client python-keycloak
```

### Authentication

The easiest way to get started is using the built-in authentication functions:

```python
from field_manager_python_client import get_prod_client

# Authenticate with your Field Manager account
client = get_prod_client(email="your.email@example.com")
```

### Basic Usage

```python
from field_manager_python_client.api.projects import get_project_projects_project_id_get

# Use the authenticated client
project_info = get_project_projects_project_id_get.sync(
    client=client, 
    project_id="your-project-id"
)
print(f"Project: {project_info.name}")
```

## 🔐 Authentication Options

### 1. Integrated Authentication (Recommended)
```python
from field_manager_python_client import authenticate

client = authenticate(environment="prod", email="user@example.com")
```

### 2. Manual Token Setup
```python
from field_manager_python_client import AuthenticatedClient

client = AuthenticatedClient(
    base_url="https://app.fieldmanager.io/api/location", 
    token="your-access-token"
)
```

### 3. Service Account (for automation)
See the [main repository](https://github.com/norwegian-geotechnical-institute/field-manager-python-client) for service account setup.

## 📖 API Usage Patterns

### Synchronous Operations
```python
from field_manager_python_client.api.organizations import get_organizations_organizations_get

# Simple request - returns data or None
organizations = get_organizations_organizations_get.sync(client=client)

# Detailed request - returns Response object with status code, headers, etc.
from field_manager_python_client.types import Response
response: Response = get_organizations_organizations_get.sync_detailed(client=client)
if response.status_code == 200:
    organizations = response.parsed
```

### Asynchronous Operations
```python
import asyncio
from field_manager_python_client.api.organizations import get_organizations_organizations_get

async def fetch_organizations():
    # Simple async request
    organizations = await get_organizations_organizations_get.asyncio(client=client)
    
    # Detailed async request
    response = await get_organizations_organizations_get.asyncio_detailed(client=client)
    return response.parsed

# Run async function
organizations = asyncio.run(fetch_organizations())
```

## 🛠️ Advanced Features

### SSL Configuration
```python
from field_manager_python_client import AuthenticatedClient

# Custom certificate bundle
client = AuthenticatedClient(
    base_url="https://internal.example.com/api", 
    token="token",
    verify_ssl="/path/to/certificate_bundle.pem"
)

# Disable SSL verification (not recommended for production)
client = AuthenticatedClient(
    base_url="https://internal.example.com/api", 
    token="token",
    verify_ssl=False
)
```

### Custom HTTP Configuration
```python
from field_manager_python_client import AuthenticatedClient

def log_request(request):
    print(f"Request: {request.method} {request.url}")

def log_response(response):
    print(f"Response: {response.status_code}")

client = AuthenticatedClient(
    base_url="https://api.example.com",
    token="token",
    httpx_args={"event_hooks": {"request": [log_request], "response": [log_response]}}
)
```

## 📚 Learn More

For comprehensive documentation, examples, and contribution guidelines, visit the main repository:
**[https://github.com/norwegian-geotechnical-institute/field-manager-python-client](https://github.com/norwegian-geotechnical-institute/field-manager-python-client)**

The repository includes:
- 📖 Complete authentication guide
- 🔧 Advanced usage examples  
- 🚀 Real-world code samples
- 🤝 Contributing guidelines
- 📋 Issue tracking and support

## 🔍 API Reference

Every endpoint becomes a Python function with four variants:
- `sync`: Blocking request returning parsed data or `None`
- `sync_detailed`: Blocking request returning full `Response` object
- `asyncio`: Async version of `sync`  
- `asyncio_detailed`: Async version of `sync_detailed`

All path/query parameters and request bodies become function arguments.
Functions are organized by API tags in `field_manager_python_client.api.*` modules.
