from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from field_manager_python_client.api.organizations import (
    get_organization_projects_organizations_organization_id_projects_get,
    get_organizations_organizations_get,
)
from field_manager_python_client.models import Organization, Project

# Import client setup
from examples.setup_auto_fetch_token import authenticate

# Constants
OUTPUT_DIR = Path(__file__).parent / '_to_delete'
OUTPUT_DIR.mkdir(exist_ok=True)


def project_statistics_calculate_and_save(projects: list[Project]) -> None:
    """
    Calculate and save statistics and visualizations for a list of projects.

    Args:
        projects (list[Project]): List of Project objects to analyze.
    """
    # Sort projects by number of locations in descending order
    projects.sort(key=lambda x: x.number_of_locations, reverse=True)

    # Collect project information for printing and saving to Excel
    project_info = [{
        "nr. of locations": project.number_of_locations,
        "project name": project.name
    } for project in projects]

    # Extract number of locations for histogram and statistics
    number_of_locations = [project.number_of_locations for project in projects]

    # Plot histogram of the number of locations
    plt.figure()
    plt.hist(number_of_locations, bins=np.logspace(np.log10(1), np.log10(max(number_of_locations)), 50), edgecolor="black")
    plt.xscale('log')
    plt.title("Histogram of Number of Locations in Projects")
    plt.xlabel("Number of Locations (log scale)")
    plt.ylabel("Frequency")
    histogram_path = OUTPUT_DIR / 'histogram.png'
    plt.savefig(histogram_path)
    plt.close()
    print(f"Histogram saved as '{histogram_path}'")

    # Calculate statistics
    total_projects = len(projects)
    average_locations = np.mean(number_of_locations)
    max_locations = np.max(number_of_locations)
    min_locations = np.min(number_of_locations)

    # Print statistics
    print(f"Total projects: {total_projects}")
    print(f"Average number of locations: {average_locations:.2f}")
    print(f"Maximum number of locations: {max_locations}")
    print(f"Minimum number of locations: {min_locations}")

    # Save statistics to an Excel file
    stats = {
        "Total Projects": [total_projects],
        "Average Number of Locations": [average_locations],
        "Maximum Number of Locations": [max_locations],
        "Minimum Number of Locations": [min_locations]
    }
    df_stats = pd.DataFrame(stats)
    stats_path = OUTPUT_DIR / 'project_statistics.xlsx'
    df_stats.to_excel(stats_path, index=False)
    print(f"Statistics saved as '{stats_path}'")

    # Save project information to an Excel file
    df_projects = pd.DataFrame(project_info)
    projects_path = OUTPUT_DIR / 'foobar_projects.xlsx'
    df_projects.to_excel(projects_path, index=False)
    print(f"Project information saved as '{projects_path}'")


def main() -> None:
    """
    Main function to fetch organization and project data, then calculate and save statistics.
    """
    client = authenticate()

    with client:
        try:
            # Fetch organizations
            my_orgs: list[Organization] = get_organizations_organizations_get.sync(client=client)
            foobar_org: Organization | None = next((org for org in my_orgs if org.short_name == "foobar"), None)

            if not foobar_org:
                print("Organization 'foobar' not found.")
                return

            print(f"{foobar_org.name} has {foobar_org.number_of_projects} projects.")

            # Fetch projects for the organization
            foobar_projects: list[Project] = (
                get_organization_projects_organizations_organization_id_projects_get.sync(
                    client=client, organization_id=foobar_org.organization_id, limit=100000
                )
            )
            print(f"Found {len(foobar_projects)} projects in {foobar_org.name}.")

            # Calculate and save project statistics
            project_statistics_calculate_and_save(foobar_projects)

        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()