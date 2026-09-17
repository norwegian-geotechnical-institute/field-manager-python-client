# Field Manager API Examples Overview

This directory contains examples demonstrating various Field Manager API capabilities. All examples have been renamed with descriptive, consistent names to make their purpose clear.

## 🔧 Setup

Before running any examples:

1. Install dependencies: `python simple_setup.py`
2. Set your email in environment variables (optional)

For local development from this repository with Poetry, use:
`poetry install --with examples`

## 📋 Available Examples

### 🔐 Authentication
- **`ex_authentication_demo.py`** - Demonstrates authentication methods
  - Shows device-code authentication usage
  - Shows token-based authentication

### 🏢 Organization Management
- **`ex_list_organizations_and_projects.py`** - List organizations and their projects
  - Connects to Field Manager API
  - Lists all accessible organizations
  - Shows project counts for each organization
  - Lists projects for the first organization with projects

- **`ex_export_organizations_data.py`** - Export organization data to files
  - Exports organization data to JSON, CSV, and text formats
  - Creates timestamped output files
  - Generates summary reports

### 📁 Project Analysis
- **`ex_get_project_details.py`** - Get detailed project information
  - Lists all available projects across organizations
  - Retrieves detailed information about specific projects
  - Displays project metadata (name, ID, description, creation date)

- **`ex_analyze_organization_projects.py`** - Statistical analysis of organization projects
  - Analyzes all projects within an organization
  - Calculates statistical metrics (total, average, median locations per project)
  - Generates histogram visualization (PNG)
  - Exports results to Excel with multiple sheets
  - Identifies top projects by location count

### 📍 Location Management
- **`ex_find_duplicate_locations.py`** - Find and visualize duplicate locations
  - Detects duplicate locations based on coordinate similarity
  - Creates interactive maps with multiple visualization layers
  - Generates detailed reports of duplicate findings
  - Exports results as HTML map files with clustering

- **`ex_compare_excel_api_locations.py`** - Compare Excel and API location data
  - Cross-checks location data between Excel files and API
  - Creates sample Excel file if missing
  - Identifies discrepancies between data sources
  - Exports discrepancy reports to separate Excel files

### Piezometer Data
- **`ex_get_piezometer_data.py`** - Get piezometer methods and data rows
  - Finds locations with piezometer (PZ) methods
  - Fetches PZ methods for each matching location
  - Retrieves and previews piezometer readings and calculated values
  - Supports optional `FIELD_MANAGER_PROJECT_ID` and limit environment variables

## 🎯 File Naming Convention

All examples follow the pattern: `ex_[verb]_[object]_[context].py`

Examples:
- `ex_list_organizations_and_projects.py` - Lists organizations and projects
- `ex_find_duplicate_locations.py` - Finds duplicate locations
- `ex_analyze_organization_projects.py` - Analyzes organization projects
- `ex_compare_excel_api_locations.py` - Compares Excel and API locations

## 📤 Output Files

Examples generate various output files in the `output/` directory:
- **Maps**: Interactive HTML files with location data
- **Statistics**: Excel files with analysis results and visualizations
- **Data Export**: JSON, CSV files with organization and project data
- **Reports**: Comparison and analysis reports

## 🚀 Quick Start

1. **Authentication Demo**: `python examples/ex_authentication_demo.py`
2. **List Organizations**: `python examples/ex_list_organizations_and_projects.py`
3. **Project Analysis**: `python examples/ex_analyze_organization_projects.py`

---

**Need help?** Check the main [README.md](../README.md) or individual example files for detailed usage instructions. 
