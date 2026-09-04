# Field Manager API - Examples

Ready-to-use examples for working with the Field Manager API. Get started in 3 simple steps!

## 🚀 Quick Start

### 1. Install Python Package

```bash
pip install field-manager-python-client
```

### 2. Run Your First Example

```bash
python examples/examples/ex_device_code_auth.py
```

That's it! 🎉

## 📁 Available Examples

### 🏢 Organization & Project Data
- **`ex_organizations.py`** - List organizations and projects
- **`ex_get_project_info_by_id.py`** - Get specific project details
- **`ex_save_organizations_to_file.py`** - Export data to CSV/JSON files

### 📊 Data Analysis  
- **`ex_historical_projects.py`** - Analyze historical project data
- **`ex_find_duplicate_locations_within_organization.py`** - Find duplicate locations
- **`ex_cross_check_location_list.py`** - Cross-validate location data
- **`ex_get_piezometer_data.py`** - Find PZ methods and preview piezometer data rows

### 🔐 Authentication Examples
- **`ex_device_code_auth.py`** - Preferred device-code authentication example
- **`ex_service_account_access_check.py`** - Test a dedicated service account and list accessible organizations and projects

## 🌍 Environments

Choose your environment when running examples:

```python
# Production environment (default for end users)
from field_manager_python_client import get_prod_device_code_client
client = get_prod_device_code_client()

# Test environment (for development)
from field_manager_python_client import get_test_device_code_client
client = get_test_device_code_client()
```

## 📄 Where Are My Files?

All generated outputs (Excel files, maps, charts) are saved to:
```
examples/output/
├── organizations_20241220_143052.json
├── locations_map.html  
├── analysis_results.xlsx
└── ...
```

## 🛠️ For Developers

### Using Local Development Version

If you're working on the field-manager-python-client itself:

```bash
cd field-manager-python-client
poetry install
poetry run python ../examples/examples/ex_device_code_auth.py
```

### Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate it
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt
```

## 🔐 Authentication

The recommended path is device-code authentication. The script prints a verification URL, you sign in in the browser, and the token is cached locally for reuse.

## ❓ Troubleshooting

### Common Issues

**"No module named 'field_manager_python_client'"**
```bash
pip install field-manager-python-client
```

**"python-keycloak is required"**  
```bash
pip install python-keycloak
```

**Authentication fails**
- Check your email address is correct
- Verify you can access Field Manager through the web interface
- Try both production and test environments

**Import errors when using local development**
- Make sure you've edited `requirements.txt` correctly
- Run `pip install -r requirements.txt --force-reinstall`

### Need Help?

1. **Check your setup**: Try the simplest example first (`ex_organizations.py`)
2. **Verify access**: Can you log into Field Manager via web browser?
3. **Environment**: Are you using the right environment (production vs test)?

## 📖 Example Code Pattern

All examples follow this simple pattern:

```python
from field_manager_python_client import get_prod_device_code_client

# 1. Authenticate  
client = get_prod_device_code_client()

# 2. Use the API
with client as client:
    data = some_api_function.sync(client=client)

# 3. Work with your data
print(f"Found {len(data)} items")
```

## 🎯 Next Steps

1. **Start simple**: Run `ex_device_code_auth.py`
2. **Explore data**: Try `ex_save_organizations_to_file.py`  
3. **Build your own**: Copy an example and modify it for your needs
4. **Read the docs**: Check the authentication guide for advanced features

---

**Happy coding! 🎉**

*Questions? Issues? Check the troubleshooting section above or examine the example code for patterns.*
