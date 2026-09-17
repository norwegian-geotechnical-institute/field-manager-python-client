# Field Manager Python Client 🚀

**A lightweight, Pythonic library for interacting with the [Field Manager API](https://app.fieldmanager.io/developer) — quickly retrieve project data, manage locations, and automate workflows, all from Python.**

## ✨ Why Use This Client?

- **Easy Integration:** Each endpoint is ready to use—no manual HTTP calls needed.
- **Seamless Authentication:** Built-in device-code authentication with token caching.
- **Auto-Generated & Up-to-Date:** Always in sync with the latest Field Manager API updates.
- **Full Coverage:** Access every endpoint and model the Field Manager platform provides.

## ⚙️ Installation & Setup

1. **Install** the package with authentication support:

   ```bash
   pip install field-manager-python-client python-keycloak
   ```

2. **Authenticate**: Use the built-in device-code helper for scripting access:

   ```python
   from field_manager_python_client import get_prod_device_code_client

   client = get_prod_device_code_client()
   ```

## 🚀 Quick Example

Here's how to fetch project information using the authenticated client:

```python
from field_manager_python_client import get_prod_device_code_client
from field_manager_python_client.api.projects import get_project_projects_project_id_get

# Authenticate and get client
client = get_prod_device_code_client()

# Use the client to fetch project data
project_id = "your-project-id"
project_info = get_project_projects_project_id_get.sync(client=client, project_id=project_id)

print(f"Project Name: {project_info.name}")
```

## 🔐 Authentication Options

The client supports multiple authentication methods:

1. **Device Code Authentication** (Recommended):

   ```python
   from field_manager_python_client import (
       authenticate_with_device_code,
       get_prod_device_code_client,
   )

   client = authenticate_with_device_code(environment="prod")
   # or
   client = get_prod_device_code_client()
   ```

2. **Manual Token Setup**:

   ```python
   from field_manager_python_client import AuthenticatedClient

   client = AuthenticatedClient(
       base_url="https://app.fieldmanager.io/api/location",
       token="your-access-token"
   )
   ```

3. **Service Account Authentication** (for automated workflows):
   - Use a dedicated Keycloak client created for your integration
   - See the [Authentication Guide](./doc/AUTHENTICATION_GUIDE.md) for details
   - Also covered in the [Advanced User Guide](./doc/ADVANCED_USER_GUIDE.md)

## 📂 Explore More Examples

Check out the [examples folder](./examples/examples/) for scripts demonstrating how to:

- **Authentication**: Multiple ways to authenticate with the API
- **Organizations**: Fetch and manage organization data
- **Projects**: Retrieve project details and metadata
- **Locations**: Manage field locations and associated data
- **Data Export**: Export project data in various formats
- **Advanced Usage**: Async operations, bulk operations, and more

## 📚 Documentation

For comprehensive documentation, see the [`./doc/`](./doc/) directory:

- **[Authentication Guide](./doc/AUTHENTICATION_GUIDE.md)**: Complete guide to all authentication methods
- **[Advanced User Guide](./doc/ADVANCED_USER_GUIDE.md)**: In-depth coverage of sync/async operations and customizations
- **[Troubleshooting Guide](./doc/TROUBLESHOOTING.md)**: Solutions for common issues, including Windows long path support
- **[Examples Overview](./examples/EXAMPLES_OVERVIEW.md)**: Detailed overview of all available examples

## 🏗️ For Developers

If you want to learn more about this library, contribute, or understand the internals, visit the main repository: [https://github.com/norwegian-geotechnical-institute/field-manager-python-client](https://github.com/norwegian-geotechnical-institute/field-manager-python-client)

The actual client package is auto-generated from the Field Manager API specification and includes:

- Full type hints and IDE support
- Comprehensive error handling
- Both synchronous and asynchronous operations
- Advanced customization options

## 🤝 Contributing

We welcome issues, bug reports, and feature requests! Please check our [contributing guidelines](./doc/MAINTAINERS_GUIDE.md) and feel free to open an issue or submit a pull request.

---

Have fun building with the Field Manager Python Client! If you have questions or need help, feel free to open an issue. Happy coding! ✨
