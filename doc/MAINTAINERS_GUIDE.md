# Maintainers Guide

See the [Makefile](./Makefile) if you need to install and test locally. Just type `make` to get the help.

## 🚀 Release & Publishing

### Automated Release Process (Default)

The system automatically checks for new OpenAPI specifications daily:

1. **Nightly Check**: GitHub Actions runs at midnight UTC to check for API changes
2. **PR Creation**: If changes are detected, a PR is automatically created with the new version
3. **Manual Review**: A developer manually reviews and approves/rejects the PR
4. **Release Creation**: If approved, developer creates a GitHub release with the version tag from `pyproject.toml`
5. **Auto-Publish**: The release triggers `release.yaml` workflow, which publishes to PyPI

### Manual Release Process (Override)

For urgent fixes or custom releases (like `4.6.25.post1`):

1. **Update Version Override**:
   ```bash
   # Edit config.yaml
   package_version_override: 4.6.25.post1
   ```

2. **Generate Client**:
   ```bash
   make generate
   ```

3. **Commit Changes**:
   ```bash
   git add field-manager-python-client/pyproject.toml
   git commit -m "Update version to 4.6.25.post1 - reason for release"
   git push origin trunk
   ```

4. **Create GitHub Release**:
   - Go to: https://github.com/norwegian-geotechnical-institute/field-manager-python-client/releases
   - Click "Create a new release"
   - **Tag**: `v4.6.25.post1` (must match pyproject.toml version with `v` prefix)
   - **Title**: `4.6.25.post1 - Brief description`
   - **Description**: What changed and why
   - Click "Publish release"

5. **Monitor Publication**:
   - Watch GitHub Actions: https://github.com/norwegian-geotechnical-institute/field-manager-python-client/actions
   - Verify on PyPI: https://pypi.org/project/field-manager-python-client/

### Release Troubleshooting

**Common Issues:**
- **Missing PYPI_TOKEN**: Ensure repository has the secret configured
- **Version conflict**: PyPI won't allow republishing the same version number
- **Tag mismatch**: GitHub release tag must match `pyproject.toml` version (with `v` prefix)

## 🔧 Development Workflow

### OpenAPI Client Generation

The client is auto-generated from OpenAPI specifications. Key points:

**✅ Files Preserved During Generation:**
- `field_manager_python_client/auth.py` - Custom authentication module
- `field_manager_python_client/__init__.py` - Preserved via custom template

**⚠️ Files Automatically Regenerated:**
- `field_manager_python_client/api/` - All API endpoints
- `field_manager_python_client/models/` - All data models
- `field_manager_python_client/client.py`, `errors.py`, `types.py`

### Local Development

```bash
# Generate client from latest API
make generate

# Verify auth module is preserved
ls field-manager-python-client/field_manager_python_client/auth.py

# Check auth imports are included
grep "from .auth import" field-manager-python_client/field_manager_python_client/__init__.py
```

### Custom Templates

The `templates/` directory contains Jinja2 templates that preserve custom code:
- `templates/package_init.py.jinja` - Ensures auth imports in `__init__.py`
- `templates/pyproject.toml.jinja` - Package metadata
- `templates/README.md.jinja` - Package documentation

## 📚 Examples Management

### Structure
```
examples/
├── setup.py              # Automated setup script
├── requirements.txt       # Package dependencies
├── examples/             # Example scripts
├── output/               # Git-ignored outputs
└── venv/                 # Git-ignored virtual environment
```

### Testing Examples

```bash
cd examples

# Test with published version
python setup.py
source venv/bin/activate
python examples/ex_authentication_demo.py

# Test with local development version
python setup.py --local
python examples/ex_authentication_demo.py
```

Poetry-based local testing from the package checkout:

```bash
cd field-manager-python-client
poetry install --with examples
poetry run python ../examples/examples/ex_authentication_demo.py
```

### Adding New Examples

1. Create script in `examples/examples/`
2. Use device-code authentication: `from field_manager_python_client import get_test_device_code_client`
3. Save outputs to `output/` directory (git-ignored)
4. Include clear documentation and error handling

## 🔐 Authentication System

### Core Components
- **Module**: `field_manager_python_client/auth.py`
- **Main Functions**: `authenticate_with_device_code()`, `get_test_device_code_client()`, `get_prod_device_code_client()`
- **Token Management**: `TokenManager` class with auto-refresh
- **Environments**: Built-in configs for test/production

### Key Features
- Automatic token caching and refresh
- Device-code authentication for interactive scripting
- Environment-specific configurations

## ✅ Pre-Release Checklist

Before any release:

```bash
# 1. Ensure auth module is preserved
make generate
git status  # auth.py should be unchanged

# 2. Test examples work
cd examples
python setup.py --local
source venv/bin/activate
python examples/ex_authentication_demo.py

# 3. Verify auth imports
python -c "from field_manager_python_client import authenticate_with_device_code; print('✅ Auth module working')"
```

Poetry-based example verification:

```bash
cd field-manager-python-client
poetry install --with examples
poetry run python ../examples/examples/ex_authentication_demo.py
```

## 🐛 Common Issues

### Auth Module Missing After Generation
```bash
# Restore from git if accidentally removed
git checkout field-manager-python_client/field_manager_python_client/auth.py
```

### Missing Auth Imports
```bash
# Check template exists
cat templates/package_init.py.jinja

# Regenerate with custom template
make generate
```

### Examples Not Working
```bash
cd examples
rm -rf venv  # Clean slate
python setup.py
```

---

**Quick Commands Reference:**
- `make generate` - Regenerate client from OpenAPI
- `make help` - Show all available commands
- `cd examples && python setup.py` - Set up examples environment
- `git push origin trunk` - Push changes
- Create GitHub release → Auto-publish to PyPI
