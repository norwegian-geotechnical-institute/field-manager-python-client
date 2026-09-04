# 🚀 Quick Start - Field Manager API

## 1. Install

```bash
pip install field-manager-python-client
```

## 2. Run Example

```bash
python examples/ex_list_organizations_and_projects.py
```

## 3. Your First Script

```python
from field_manager_python_client import get_prod_device_code_client

# Connect to production environment
client = get_prod_device_code_client()

# Get organizations
from field_manager_python_client.api.organizations import get_organizations_organizations_get

with client as client:
    organizations = get_organizations_organizations_get.sync(client=client)
    print(f"Found {len(organizations)} organizations")
```

That's it! 🎉

---

**Need help?** Check the main [README.md](README.md) for troubleshooting. 
