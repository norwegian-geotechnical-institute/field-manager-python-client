# Field Manager Python Client 🚀

**A lightweight, Pythonic library for interacting with the [Field Manager API](https://app.fieldmanager.io/developer) — quickly retrieve project data, manage locations, and automate workflows, all from Python.**

## ✨ Why Use This Client?

- **Easy Integration:** Each endpoint is ready to use—no manual HTTP calls needed.
- **Auto-Generated & Up-to-Date:** Always in sync with the latest Field Manager API updates.
- **Full Coverage:** Access every endpoint and model the Field Manager platform provides.

## ⚙️ Installation & Setup

1. **Install** the package:

   ```bash
   pip install field-manager-python-client
   ```

2. **Authenticate**: - Use the `authenticate` function to handle token retrieval automatically. This function will fetch a new token if the current one is expired or missing.

   ```python
   from field_manager_python_client.api.projects import get_project_projects_project_id_get
   from examples.setup_auto_fetch_token import authenticate

   client = authenticate()  # Handles token retrieval
   ```

## 🚀 Quick Example

1. Here's a [quick example](./examples/examples/ex_get_project_info_by_id.py) of how to fetch project information using the client:

   ```python
   from field_manager_python_client.api.projects import get_project_projects_project_id_get
   from examples.setup_auto_fetch_token import authenticate

   client = authenticate()
   project_id = "your-project-id"
   project_info = get_project_projects_project_id_get.sync(client=client, project_id=project_id)

   print(f"Project Name: {project_info.name}")
   ```

## 📂 Explore More Examples

- Check out the [examples folder](./examples/examples/) for scripts demonstrating how to:

  - Fetch organization(s)

  - Manage locations

  - Compare data sets and more

## 🤝 Contributing

We welcome issues, bug reports, and feature requests!

---

Have fun building with the Field Manager Python Client! If you have questions or need help, feel free to open an issue. Happy coding! ✨
