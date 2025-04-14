import os
from typing import Optional

import pandas as pd

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
    """
    Retrieve a project by its ID using the Field Manager client.

    :param client: Authenticated Field Manager client.
    :param project_id: The ID of the project to retrieve.
    :return: ProjectInfo object if found, otherwise None.
    """
    return get_project_projects_project_id_get.sync(
        client=client,
        project_id=project_id,
    )


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
            f"Error retrieving locations for project {project.project_id} '{project.name}': {e}"
        )
        return [], project.project_id, project.name


def save_to_excel(df: pd.DataFrame, filename: str) -> str:
    """
    Save a pandas DataFrame to an Excel file.

    :param df: The DataFrame to save.
    :param filename: Name of the output Excel file.
    :return: The absolute path to the saved file.
    """
    output_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(output_dir, filename)
    df.to_excel(filepath, index=False)
    return filepath


def main(project_id: str) -> None:
    """
    Main entry point of the script. Authenticates with Field Manager, loads parent
    locations from Excel, retrieves project data via API, compares the two sets of
    locations, and saves any discrepancies to Excel files.

    :param project_id: The ID of the project to process.
    """
    # Authenticate using the Field Manager client
    client = authenticate()

    # Load parent locations from an Excel file
    # Parent_file_locations.xlsx should be in the following format:
    # | LOC_ID | Easting | Northing |
    excel_path = "Parent_file_locations.xlsx"
    try:
        parent_locations_df = pd.read_excel(excel_path)
        if not parent_locations_df.empty:
            print("\nFirst row in Excel:")
            print(parent_locations_df.iloc[0].to_dict())
        else:
            print("Excel file is empty.")
    except Exception as e:
        print(f"Error loading Excel file '{excel_path}': {e}")
        return

    with client:
        try:
            # Get project info by ID
            if not (project_info := get_project_by_id(client, project_id)):
                print(f"Project with ID '{project_id}' not found.")
                return
            print(f"Project: {project_info.name} ({project_info.project_id})")

            # Retrieve all locations for the project
            locations, pid, pname = get_all_locations(client, project_info)
            if not locations:
                print(f"No locations found for project '{pname}' ({pid}).")
                return
            print(f"Number of locations found: {len(locations)}")

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
            print("\n=== Comparison Results ===")
            print(f"Total locations in Excel: {len(excel_location_ids)}")
            print(f"Total locations in API: {len(api_location_names)}")
            print(
                f"Locations in both: {len(excel_location_ids.intersection(api_location_names))}"
            )

            # Locations only in Excel
            print("\nLocations in Excel but not in API:")
            if in_excel_not_in_api:
                for loc_id in list(in_excel_not_in_api)[:10]:
                    row = parent_locations_df[
                        parent_locations_df["LOC_ID"].astype(str) == loc_id
                    ].iloc[0]
                    print(
                        f"  - LOC_ID: {loc_id}, Easting: {row['Easting']}, Northing: {row['Northing']}"
                    )
                if len(in_excel_not_in_api) > 10:
                    print(f"  ... and {len(in_excel_not_in_api) - 10} more")

                excel_only_df = parent_locations_df[
                    parent_locations_df["LOC_ID"].astype(str).isin(in_excel_not_in_api)
                ]
                excel_only_filepath = save_to_excel(
                    excel_only_df, "locations_in_excel_not_in_api.xlsx"
                )
                print(
                    f"\nSaved {len(excel_only_df)} locations found only in Excel to: {excel_only_filepath}"
                )
            else:
                print("  None")

            # Locations only in API
            print("\nLocations in API but not in Excel:")
            if in_api_not_in_excel:
                for name in list(in_api_not_in_excel)[:10]:
                    row = simplified_df[simplified_df["name"] == name].iloc[0]
                    print(
                        f"  - Name: {name}, Easting: {row['point_easting']}, Northing: {row['point_northing']}"
                    )
                if len(in_api_not_in_excel) > 10:
                    print(f"  ... and {len(in_api_not_in_excel) - 10} more")

                api_only_df = simplified_df[
                    simplified_df["name"].isin(in_api_not_in_excel)
                ]
                api_only_filepath = save_to_excel(
                    api_only_df, "locations_in_api_not_in_excel.xlsx"
                )
                print(
                    f"\nSaved {len(api_only_df)} locations found only in API to: {api_only_filepath}"
                )
            else:
                print("  None")

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    # Example project ID; replace with a valid ID as needed
    PROJECT_ID = "69120781-bbe5-48cd-b559-6b9730fdffea"
    main(PROJECT_ID)
