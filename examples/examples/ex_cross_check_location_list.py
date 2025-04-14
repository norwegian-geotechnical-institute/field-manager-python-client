from typing import Optional
import pandas as pd
import os

from field_manager_python_client.api.projects import (
    get_project_summary_projects_project_id_summary_get,
    get_project_projects_project_id_get,
)
from field_manager_python_client.models import (
    Project,
    LocationSummary,
    ProjectInfo,
)
from examples.setup_auto_fetch_token import authenticate


def get_project_by_id(client, project_id: str) -> Optional[ProjectInfo]:
    """Get project by its ID."""
    return get_project_projects_project_id_get.sync(
        client=client,
        project_id=project_id,
    )


def get_all_locations(
    client, project: Project | ProjectInfo
) -> tuple[list[LocationSummary], str, str]:
    """Get all locations for a project. If an error occurs, log the project name and ID, and return an empty list."""
    try:
        project_summary = get_project_summary_projects_project_id_summary_get.sync(
            client=client,
            project_id=project.project_id,
        )
        return project_summary.locations, project.project_id, project.name
    except Exception as e:
        print(
            f"Error getting locations for project {project.project_id} {project.name}: {e}"
        )
        return [], project.project_id, project.name


def save_to_excel(df, filename):
    """Save dataframe to Excel file and return the absolute path."""
    output_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(output_dir, filename)
    df.to_excel(filepath, index=False)
    return filepath


def main(project_id: str = None):
    client = authenticate()

    # Load the Excel file with the parent locations
    # Parent locations format:
            # LOC_ID, Easting, Northing
    try:
        excel_path = "Parent_file_locations.xlsx"
        parent_locations_df = pd.read_excel(excel_path)

        # Print the first row
        if not parent_locations_df.empty:
            print("\nExcel file first row:")
            first_row = parent_locations_df.iloc[0].to_dict()
            print(first_row)
            
        else:
            print("Excel file is empty.")
    except Exception as e:
        print(f"Error loading Excel file: {e}")

    with client:
        try:
            # Step 1: Get project info by ID
            if not (project_info := get_project_by_id(client, project_id)):
                print(f"Project with id '{project_id}' not found")
                return
            print(f"Project: {project_info.name} ({project_info.project_id})")

            # Step 2: get all locations for the project
            locations, project_id, project_name = get_all_locations(
                client, project_info
            )
            if not locations:
                print(f"No locations found for project {project_name} ({project_id})")
                return
            print(f"Locations found: {len(locations)}")
            # create a new locations list based on the locations, to keep only the fileds: name, point_easting, point_northing
            simplified_locations = [
                {
                    "name": loc.name,
                    "point_easting": loc.point_easting,
                    "point_northing": loc.point_northing,
                }
                for loc in locations
            ]

            print(
                f"Simplified locations: {simplified_locations[0] if simplified_locations else None}"
            )

            # Compare the two location sets
            # Convert simplified_locations to a dataframe for easier comparison
            simplified_df = pd.DataFrame(simplified_locations)
            
            # Extract location IDs from both datasets
            excel_location_ids = set(parent_locations_df['LOC_ID'].astype(str))
            api_location_names = set(simplified_df['name'])
            
            # Find locations in Excel but not in API
            in_excel_not_in_api = excel_location_ids - api_location_names
            # Find locations in API but not in Excel
            in_api_not_in_excel = api_location_names - excel_location_ids
            
            # Print the results
            print("\n=== Comparison Results ===")
            print(f"Total locations in Excel: {len(excel_location_ids)}")
            print(f"Total locations in API: {len(api_location_names)}")
            print(f"Locations in both: {len(excel_location_ids.intersection(api_location_names))}")
            
            print("\nLocations in Excel but not in API:")
            if in_excel_not_in_api:
                for loc_id in list(in_excel_not_in_api)[:10]:  # Limit to first 10 for readability
                    row = parent_locations_df[parent_locations_df['LOC_ID'].astype(str) == loc_id].iloc[0]
                    print(f"  - LOC_ID: {loc_id}, Easting: {row['Easting']}, Northing: {row['Northing']}")
                if len(in_excel_not_in_api) > 10:
                    print(f"  ... and {len(in_excel_not_in_api) - 10} more")
                
                # Save Excel-only locations to a file
                excel_only_df = parent_locations_df[parent_locations_df['LOC_ID'].astype(str).isin(in_excel_not_in_api)]
                excel_only_filepath = save_to_excel(excel_only_df, "locations_in_excel_not_in_api.xlsx")
                print(f"\nSaved {len(excel_only_df)} locations found only in Excel to: {excel_only_filepath}")
            else:
                print("  None")
                
            print("\nLocations in API but not in Excel:")
            if in_api_not_in_excel:
                for name in list(in_api_not_in_excel)[:10]:  # Limit to first 10 for readability
                    row = simplified_df[simplified_df['name'] == name].iloc[0]
                    print(f"  - Name: {name}, Easting: {row['point_easting']}, Northing: {row['point_northing']}")
                if len(in_api_not_in_excel) > 10:
                    print(f"  ... and {len(in_api_not_in_excel) - 10} more")
                
                # Save API-only locations to a file
                api_only_df = simplified_df[simplified_df['name'].isin(in_api_not_in_excel)]
                api_only_filepath = save_to_excel(api_only_df, "locations_in_api_not_in_excel.xlsx")
                print(f"\nSaved {len(api_only_df)} locations found only in API to: {api_only_filepath}")
            else:
                print("  None")

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    project_id = "69120781-bbe5-48cd-b559-6b9730fdffea"
    main(project_id)
