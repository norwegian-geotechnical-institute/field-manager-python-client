"""
Example: Cross-Check Location Lists

This example shows how to:
1. Connect to the Field Manager API
2. Load location data from an Excel file
3. Compare Excel locations with API locations
4. Identify discrepancies and save results

Run this example:
    python examples/ex_cross_check_location_list.py

Required: Create a file named 'Parent_file_locations.xlsx' in examples/output/ with columns:
    LOC_ID | Easting | Northing
"""

import os
from pathlib import Path
from typing import Optional
import pandas as pd
from dotenv import load_dotenv

from field_manager_python_client import get_prod_device_code_client
from field_manager_python_client.api.projects import (
    get_project_summary_projects_project_id_summary_get,
    get_project_projects_project_id_get,
)
from field_manager_python_client.api.organizations import (
    get_organizations_organizations_get,
)
from field_manager_python_client.models import (
    Project,
    LocationSummary,
    ProjectInfo,
)

# Load environment variables
load_dotenv()
# Output directory - save to examples/output/
OUTPUT_DIR = Path(__file__).parent.parent / "output"
OUTPUT_DIR.mkdir(exist_ok=True)


def get_project_by_id(client, project_id: str) -> Optional[ProjectInfo]:
    """
    Retrieve a project by its ID using the Field Manager client.

    :param client: Authenticated Field Manager client.
    :param project_id: The ID of the project to retrieve.
    :return: ProjectInfo object if found, otherwise None.
    """
    try:
        return get_project_projects_project_id_get.sync(
            client=client,
            project_id=project_id,
        )
    except Exception as e:
        print(f"❌ Error getting project {project_id}: {e}")
        return None


def get_all_locations(
    client, project: Project | ProjectInfo
) -> tuple[list[LocationSummary], str, str]:
    """
    Retrieve all locations for a given project.

    :param client: Authenticated Field Manager client.
    :param project: A Project or ProjectInfo object representing the project.
    :return: A tuple containing:
             - A list of LocationSummary objects (or an empty list on error).
             - The project ID.
             - The project name.
    """
    try:
        project_summary = get_project_summary_projects_project_id_summary_get.sync(
            client=client,
            project_id=project.project_id,
        )
        return project_summary.locations, project.project_id, project.name
    except Exception as e:
        print(
            f"❌ Error retrieving locations for project {project.project_id} '{project.name}': {e}"
        )
        return [], project.project_id, project.name


def save_to_excel(df: pd.DataFrame, filename: str) -> str:
    """
    Save a pandas DataFrame to an Excel file in the output directory.

    :param df: The DataFrame to save.
    :param filename: Name of the output Excel file.
    :return: The absolute path to the saved file.
    """
    filepath = OUTPUT_DIR / filename
    df.to_excel(filepath, index=False)
    return str(filepath)


def show_available_projects(client):
    """Show available projects to help user choose a project ID."""
    print("📋 Available projects:")
    try:
        organizations = get_organizations_organizations_get.sync(client=client)
        all_projects = []

        for org in organizations:
            from field_manager_python_client.api.organizations import (
                get_organization_projects_organizations_organization_id_projects_get,
            )

            projects = get_organization_projects_organizations_organization_id_projects_get.sync(
                client=client, organization_id=org.organization_id
            )
            if projects:
                for project in projects:
                    all_projects.append((project, org.name))

        if not all_projects:
            print("❌ No projects found")
            return None

        for i, (project, org_name) in enumerate(all_projects[:10]):  # Show first 10
            print(f"{i + 1}. {project.name}")
            print(f"   ID: {project.project_id}")
            print(f"   Organization: {org_name}")
            print(f"   Locations: {project.number_of_locations}")
            print()

        if len(all_projects) > 10:
            print(f"... and {len(all_projects) - 10} more projects")

        return all_projects
    except Exception as e:
        print(f"❌ Error getting projects: {e}")
        return None


def main() -> None:
    """
    Main entry point of the script. Authenticates with Field Manager, loads parent
    locations from Excel, retrieves project data via API, compares the two sets of
    locations, and saves any discrepancies to Excel files.
    """
    print("🔍 Cross-Check Location Lists")
    print()

    # Connect to production environment
    client = get_prod_device_code_client()

    # Load parent locations from Excel file
    excel_path = OUTPUT_DIR / "Parent_file_locations.xlsx"

    if not excel_path.exists():
        print(f"📄 Creating sample Excel file: {excel_path}")
        # Create a sample Excel file for demonstration
        sample_data = {
            "LOC_ID": ["NAU_004", "NAV_021", "GEY_458", "GEY_439", "GEY_456"],
            "Easting": [111537.20, 111597.58, 112041.11, 111987.40, 111910.40],
            "Northing": [1215635.29, 1215717.32, 1214956.46, 1214975.47, 1215088.27]
        }
        sample_df = pd.DataFrame(sample_data)
        sample_df.to_excel(excel_path, index=False)
        print(f"✅ Created sample Excel file with {len(sample_data['LOC_ID'])} locations")

    try:
        parent_locations_df = pd.read_excel(excel_path)
        if parent_locations_df.empty:
            print("❌ Excel file is empty.")
            return

        print(f"📊 Loaded {len(parent_locations_df)} locations from Excel")
        if not parent_locations_df.empty:
            print("First row in Excel:")
            print(parent_locations_df.iloc[0].to_dict())
        print()

    except Exception as e:
        print(f"❌ Error loading Excel file '{excel_path}': {e}")
        return

    with client as client:
        try:
            # Use first available project for demonstration
            projects = show_available_projects(client)
            if not projects:
                return
            
            # Use first project for demonstration
            project_id = projects[0][0].project_id
            print(f"\nUsing first project for demonstration: {project_id}")

            # Get project info by ID
            project_info = get_project_by_id(client, project_id)
            if not project_info:
                print(f"❌ Project with ID '{project_id}' not found.")
                return

            print(f"📁 Project: {project_info.name} ({project_info.project_id})")

            # Retrieve all locations for the project
            locations, pid, pname = get_all_locations(client, project_info)
            if not locations:
                print(f"❌ No locations found for project '{pname}' ({pid}).")
                return

            print(f"📍 Found {len(locations)} locations in API")

            # Build a simplified locations list
            simplified_locations = [
                {
                    "name": loc.name,
                    "point_easting": loc.point_easting,
                    "point_northing": loc.point_northing,
                }
                for loc in locations
            ]

            # Compare the location sets (Excel vs. API)
            simplified_df = pd.DataFrame(simplified_locations)
            excel_location_ids = set(parent_locations_df["LOC_ID"].astype(str))
            api_location_names = set(simplified_df["name"])

            in_excel_not_in_api = excel_location_ids - api_location_names
            in_api_not_in_excel = api_location_names - excel_location_ids

            # Print comparison summary
            print()
            print("📊 Comparison Results:")
            print(f"   • Total locations in Excel: {len(excel_location_ids)}")
            print(f"   • Total locations in API: {len(api_location_names)}")
            print(
                f"   • Locations in both: {len(excel_location_ids.intersection(api_location_names))}"
            )
            print(f"   • Only in Excel: {len(in_excel_not_in_api)}")
            print(f"   • Only in API: {len(in_api_not_in_excel)}")

            # Locations only in Excel
            if in_excel_not_in_api:
                print(
                    f"\n📋 Locations in Excel but not in API ({len(in_excel_not_in_api)}):"
                )
                for i, loc_id in enumerate(list(in_excel_not_in_api)[:5]):
                    row = parent_locations_df[
                        parent_locations_df["LOC_ID"].astype(str) == loc_id
                    ].iloc[0]
                    print(
                        f"   {i+1}. {loc_id} (E: {row['Easting']}, N: {row['Northing']})"
                    )

                if len(in_excel_not_in_api) > 5:
                    print(f"   ... and {len(in_excel_not_in_api) - 5} more")

                excel_only_df = parent_locations_df[
                    parent_locations_df["LOC_ID"].astype(str).isin(in_excel_not_in_api)
                ]
                excel_only_filepath = save_to_excel(
                    excel_only_df, "locations_in_excel_not_in_api.xlsx"
                )
                print(f"   💾 Saved to: {excel_only_filepath}")

            # Locations only in API
            if in_api_not_in_excel:
                print(
                    f"\n📍 Locations in API but not in Excel ({len(in_api_not_in_excel)}):"
                )
                for i, name in enumerate(list(in_api_not_in_excel)[:5]):
                    row = simplified_df[simplified_df["name"] == name].iloc[0]
                    print(
                        f"   {i+1}. {name} (E: {row['point_easting']}, N: {row['point_northing']})"
                    )

                if len(in_api_not_in_excel) > 5:
                    print(f"   ... and {len(in_api_not_in_excel) - 5} more")

                api_only_df = simplified_df[
                    simplified_df["name"].isin(in_api_not_in_excel)
                ]
                api_only_filepath = save_to_excel(
                    api_only_df, "locations_in_api_not_in_excel.xlsx"
                )
                print(f"   💾 Saved to: {api_only_filepath}")

            if not in_excel_not_in_api and not in_api_not_in_excel:
                print(
                    "\n✅ Perfect match! All locations are consistent between Excel and API."
                )
            else:
                print("\n✅ Cross-check complete! Results saved to output directory.")

        except Exception as e:
            print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()
