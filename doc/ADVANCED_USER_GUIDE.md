# 🚧 Field Manager Python Client - Advanced User Guide

> ⚠️ **Important Notice**: This guide covers advanced usage patterns and may not be fully tested in all scenarios. If you encounter issues or have questions about any of the examples, please contact our support team or create an issue on [GitHub](https://github.com/norwegian-geotechnical-institute/field-manager-python-client/issues) before implementing in production.

## Overview

This guide covers advanced features and usage patterns for the Field Manager Python Client. While these are more sophisticated use cases, we've tried to keep the examples simple and easy to follow.

**For authentication setup, please see the [Authentication Guide](./AUTHENTICATION_GUIDE.md) first.**

## Table of Contents

- [Understanding API Operation Types](#understanding-api-operation-types)
- [Working with Different Response Types](#working-with-different-response-types)
- [Asynchronous Operations](#asynchronous-operations)
- [Batch Operations](#batch-operations)
- [Error Handling Strategies](#error-handling-strategies)
- [Performance Tips](#performance-tips)
- [Production Considerations](#production-considerations)

## Understanding API Operation Types

The Field Manager Python Client provides four different ways to call each API endpoint. Here's what they do:

### Simple Operations

#### `sync` - Get Data Directly

Returns your data immediately or `None` if something goes wrong:

```python
from field_manager_python_client import get_prod_device_code_client
from field_manager_python_client.api.organizations import get_organizations_organizations_get

client = get_prod_device_code_client()

# Simple request - returns your data or None
organizations = get_organizations_organizations_get.sync(client=client)
if organizations:
    print(f"Found {len(organizations)} organizations")
else:
    print("Something went wrong or no data available")
```

#### `sync_detailed` - Get Full Response Information

Returns complete information about the request, including status codes and error details:

```python
from field_manager_python_client.types import Response
from field_manager_python_client.api.projects import get_projects_projects_get

# Get detailed response information
response: Response = get_projects_projects_get.sync_detailed(client=client)

print(f"Status: {response.status_code}")
if response.status_code == 200:
    projects = response.parsed
    print(f"Successfully got {len(projects)} projects")
elif response.status_code == 401:
    print("Authentication problem - check your credentials")
elif response.status_code == 403:
    print("You don't have permission to access this")
else:
    print(f"Something went wrong: {response.status_code}")
```

### Async Operations (for Advanced Users)

#### `asyncio` - Async Version of sync

Same as `sync` but works asynchronously:

```python
import asyncio
from field_manager_python_client.api.locations import get_locations_projects_project_id_locations_get

async def get_my_locations(project_id: str):
    # Async version - use 'await'
    locations = await get_locations_projects_project_id_locations_get.asyncio(
        client=client,
        project_id=project_id
    )

    if locations:
        print(f"Found {len(locations)} locations")
        return locations
    else:
        print("No locations found")
        return []

# Run the async function
project_id = "your-project-id"
locations = asyncio.run(get_my_locations(project_id))
```

#### `asyncio_detailed` - Async Version of sync_detailed

Async version with full response information:

```python
async def get_locations_with_details(project_id: str):
    response = await get_locations_projects_project_id_locations_get.asyncio_detailed(
        client=client,
        project_id=project_id
    )

    if response.status_code == 200:
        return response.parsed
    else:
        print(f"Request failed with status: {response.status_code}")
        return None

# Usage
locations = asyncio.run(get_locations_with_details("project-id"))
```

## Working with Different Response Types

### Handling Errors Properly

```python
from field_manager_python_client.api.projects import get_project_projects_project_id_get

def get_project_safely(project_id: str):
    """Get a project with proper error handling."""
    response = get_project_projects_project_id_get.sync_detailed(
        client=client,
        project_id=project_id
    )

    if response.status_code == 200:
        return response.parsed
    elif response.status_code == 404:
        print(f"Project '{project_id}' was not found")
        return None
    elif response.status_code == 403:
        print(f"You don't have permission to access project '{project_id}'")
        return None
    else:
        print(f"Error getting project: {response.status_code}")
        return None

# Usage
project = get_project_safely("my-project-id")
if project:
    print(f"Got project: {project.name}")
```

### Working with Paginated Results

```python
from field_manager_python_client.api.projects import get_projects_projects_get

def get_all_projects():
    """Get all projects, handling pagination."""
    all_projects = []
    offset = 0
    limit = 50  # Adjust based on your needs

    while True:
        response = get_projects_projects_get.sync_detailed(
            client=client,
            offset=offset,
            limit=limit
        )

        if response.status_code != 200:
            print(f"Error getting projects: {response.status_code}")
            break

        projects = response.parsed
        if not projects:
            break  # No more projects

        all_projects.extend(projects)

        # If we got fewer than limit, we're done
        if len(projects) < limit:
            break

        offset += limit
        print(f"Got {len(all_projects)} projects so far...")

    return all_projects

# Usage
all_projects = get_all_projects()
print(f"Total projects: {len(all_projects)}")
```

## Asynchronous Operations

Async operations are useful when you need to do multiple things at once or when working with large amounts of data.

### Simple Async Example

```python
import asyncio
from field_manager_python_client.api.projects import get_project_projects_project_id_get

async def get_multiple_projects(project_ids: list[str]):
    """Get multiple projects at the same time."""

    # Create all the tasks
    tasks = [
        get_project_projects_project_id_get.asyncio(client=client, project_id=pid)
        for pid in project_ids
    ]

    # Run them all at once
    results = await asyncio.gather(*tasks, return_exceptions=True)

    # Process the results
    successful_projects = []
    for i, result in enumerate(results):
        if isinstance(result, Exception):
            print(f"Failed to get project {project_ids[i]}: {result}")
        elif result:
            successful_projects.append(result)

    return successful_projects

# Usage
project_ids = ["project-1", "project-2", "project-3"]
projects = asyncio.run(get_multiple_projects(project_ids))
print(f"Successfully retrieved {len(projects)} projects")
```

### Async with Error Handling

```python
async def get_projects_with_timeout():
    """Get projects with a timeout to avoid waiting forever."""
    try:
        # Set a 30-second timeout
        projects = await asyncio.wait_for(
            get_projects_projects_get.asyncio(client=client),
            timeout=30.0
        )
        return projects

    except asyncio.TimeoutError:
        print("Request took too long (over 30 seconds)")
        return None
    except Exception as e:
        print(f"Error getting projects: {e}")
        return None

# Usage
projects = asyncio.run(get_projects_with_timeout())
```

## Batch Operations

### Processing Multiple Items

```python
import asyncio
from field_manager_python_client.api.locations import get_locations_projects_project_id_locations_get

async def get_locations_for_all_projects(project_ids: list[str]):
    """Get locations for multiple projects efficiently."""

    async def get_project_locations(project_id: str):
        try:
            locations = await get_locations_projects_project_id_locations_get.asyncio(
                client=client,
                project_id=project_id
            )
            return project_id, locations or []
        except Exception as e:
            print(f"Error getting locations for project {project_id}: {e}")
            return project_id, []

    # Process all projects concurrently
    tasks = [get_project_locations(pid) for pid in project_ids]
    results = await asyncio.gather(*tasks)

    # Organize results
    project_locations = {}
    total_locations = 0

    for project_id, locations in results:
        project_locations[project_id] = locations
        total_locations += len(locations)
        print(f"Project {project_id}: {len(locations)} locations")

    print(f"Total locations across all projects: {total_locations}")
    return project_locations

# Usage
project_ids = ["proj-1", "proj-2", "proj-3"]
all_locations = asyncio.run(get_locations_for_all_projects(project_ids))
```

## Error Handling Strategies

### Retry Logic

```python
import time
import random
from field_manager_python_client.api.organizations import get_organizations_organizations_get

def get_organizations_with_retry(max_attempts: int = 3):
    """Get organizations with automatic retry on failure."""

    for attempt in range(max_attempts):
        try:
            organizations = get_organizations_organizations_get.sync(client=client)
            if organizations:
                return organizations
            else:
                print(f"Attempt {attempt + 1}: No data returned")

        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")

        # Wait before retrying (with some randomness)
        if attempt < max_attempts - 1:
            wait_time = (2 ** attempt) + random.uniform(0, 1)
            print(f"Waiting {wait_time:.1f} seconds before retry...")
            time.sleep(wait_time)

    print(f"Failed after {max_attempts} attempts")
    return None

# Usage
organizations = get_organizations_with_retry()
if organizations:
    print(f"Successfully got {len(organizations)} organizations")
```

### Graceful Error Handling

```python
def safe_api_call(api_function, *args, **kwargs):
    """Wrapper to make API calls safer."""
    try:
        result = api_function(*args, **kwargs)
        return result, None  # result, error
    except Exception as e:
        return None, str(e)  # result, error

# Usage
from field_manager_python_client.api.projects import get_projects_projects_get

projects, error = safe_api_call(get_projects_projects_get.sync, client=client)
if error:
    print(f"Error: {error}")
else:
    print(f"Got {len(projects)} projects")
```

## Performance Tips

### Connection Reuse

```python
# Use context managers to properly manage connections
with client as managed_client:
    # All requests reuse the same connection
    orgs = get_organizations_organizations_get.sync(client=managed_client)
    projects = get_projects_projects_get.sync(client=managed_client)
    # Connection is properly closed when done

# For async operations
async def do_multiple_requests():
    async with client as managed_client:
        orgs = await get_organizations_organizations_get.asyncio(client=managed_client)
        projects = await get_projects_projects_get.asyncio(client=managed_client)
    return orgs, projects

orgs, projects = asyncio.run(do_multiple_requests())
```

### Custom Timeouts

```python
import httpx
from field_manager_python_client import AuthenticatedClient

# Create client with custom timeout settings
client = AuthenticatedClient(
    base_url="https://app.fieldmanager.io/api/location",
    token="your-token",
    httpx_args={
        "timeout": httpx.Timeout(30.0, connect=10.0),  # 30s total, 10s to connect
    }
)
```

### Advanced HTTP Client Configuration

```python
import httpx
from field_manager_python_client import AuthenticatedClient

# Custom SSL and proxy configuration
client = AuthenticatedClient(
    base_url="https://app.fieldmanager.io/api/location",
    token="your-token",
    httpx_args={
        "timeout": httpx.Timeout(30.0),
        "limits": httpx.Limits(max_keepalive_connections=10, max_connections=20),
        "verify": "/path/to/cert.pem",  # Custom certificate
        "proxies": "http://proxy.example.com:8080"  # Proxy configuration
    }
)
```

## Production Considerations

### Logging and Monitoring

```python
import logging
from field_manager_python_client import AuthenticatedClient

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def log_requests(request):
    logger.info(f"API Request: {request.method} {request.url}")

def log_responses(response):
    logger.info(f"API Response: {response.status_code}")
    if response.status_code >= 400:
        logger.error(f"API Error: {response.status_code} - {response.text}")

# Create client with logging
client = AuthenticatedClient(
    base_url="https://app.fieldmanager.io/api/location",
    token="your-token",
    httpx_args={
        "event_hooks": {
            "request": [log_requests],
            "response": [log_responses]
        }
    }
)
```

### Rate Limiting

```python
import time
from typing import Callable, TypeVar

T = TypeVar('T')

def rate_limited_call(func: Callable[[], T], delay: float = 1.0) -> T:
    """Add a delay between API calls to avoid rate limiting."""
    result = func()
    time.sleep(delay)
    return result

# Usage
def get_orgs():
    return get_organizations_organizations_get.sync(client=client)

# Add 1-second delay between calls
organizations = rate_limited_call(get_orgs, delay=1.0)
```

### Configuration Management

```python
import os
from dataclasses import dataclass

@dataclass
class FieldManagerConfig:
    base_url: str
    timeout: float
    max_retries: int

    @classmethod
    def from_env(cls):
        return cls(
            base_url=os.getenv("FM_API_BASE_URL", "https://app.fieldmanager.io/api/location"),
            timeout=float(os.getenv("FM_TIMEOUT", "30.0")),
            max_retries=int(os.getenv("FM_MAX_RETRIES", "3"))
        )

# Usage
config = FieldManagerConfig.from_env()
```

## Getting Help

If you need assistance with any of these advanced patterns:

1. **Check the [Authentication Guide](./AUTHENTICATION_GUIDE.md)** for auth-related issues
2. **Look at the [examples](../examples/examples/)** for working code samples
3. **Contact support** before implementing in production systems
4. **Open an issue** on [GitHub](https://github.com/norwegian-geotechnical-institute/field-manager-python-client/issues) if you find bugs

Remember: These are advanced patterns. Start simple and add complexity as needed!
