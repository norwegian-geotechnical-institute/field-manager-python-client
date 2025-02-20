from field_manager_python_client.models import Organization, Project
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

from field_manager_python_client.api.organizations import (
    get_organizations_organizations_get,
    get_organization_projects_organizations_organization_id_projects_get,
)

# Import client setup
from examples.setup_auto_fetch_token import authenticate

client = authenticate()

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '_to_delete')
os.makedirs(OUTPUT_DIR, exist_ok=True)

def project_statistics_calculate_and_save(foobar_projects: list[Project]):
    # Collect project information for printing and saving to Excel
    project_info = []

    # Sort projects by number of locations
    foobar_projects.sort(key=lambda x: x.number_of_locations, reverse=True)

    for project in foobar_projects:
        print(
            "nr. of locations: ", project.number_of_locations, "        ", project.name
        )
        project_info.append({
            "nr. of locations": project.number_of_locations,
            "project name": project.name
        })

    # Draw a histogram of the number of locations in the projects
    number_of_locations = [project.number_of_locations for project in foobar_projects]

    plt.hist(number_of_locations, bins=np.logspace(np.log10(1), np.log10(max(number_of_locations)), 50), edgecolor="black")
    plt.xscale('log')
    plt.title("Histogram of Number of Locations in Projects")
    plt.xlabel("Number of Locations (log scale)")
    plt.ylabel("Frequency")
    histogram_path = os.path.join(OUTPUT_DIR, 'histogram.png')
    plt.savefig(histogram_path)
    print(f"Histogram saved as '{histogram_path}'")

    # Calculate statistics
    total_projects = len(foobar_projects)
    average_locations = sum(number_of_locations) / total_projects
    max_locations = max(number_of_locations)
    min_locations = min(number_of_locations)

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
    stats_path = os.path.join(OUTPUT_DIR, 'project_statistics.xlsx')
    df_stats.to_excel(stats_path, index=False)
    print(f"Statistics saved as '{stats_path}'")

    # Save project information to an Excel file
    df_projects = pd.DataFrame(project_info)
    projects_path = os.path.join(OUTPUT_DIR, 'foobar_projects.xlsx')
    df_projects.to_excel(projects_path, index=False)
    print(f"Project information saved as '{projects_path}'")


with client as client:
    my_orgs: list[Organization] = get_organizations_organizations_get.sync(
        client=client
    )

    foobar_org: Organization = next(
        org for org in my_orgs if org.short_name == "foobar"
    )
    print(foobar_org.name, "has", foobar_org.number_of_projects, "projects.")

    foobar_projects: list[Project] = (
        get_organization_projects_organizations_organization_id_projects_get.sync(
            client=client, organization_id=foobar_org.organization_id, limit=100000
        )
    )
    print("Projects in", len(foobar_projects), "projects:")

    project_statistics_calculate_and_save(foobar_projects)