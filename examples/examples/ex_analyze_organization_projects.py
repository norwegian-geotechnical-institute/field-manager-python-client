"""
Example: Historical Project Analysis

This example shows how to:
1. Connect to the Field Manager API
2. Analyze historical project data
3. Generate statistics and visualizations
4. Save results to the output directory

Run this example:
    python examples/ex_historical_projects.py
"""

from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from dotenv import load_dotenv

from field_manager_python_client import get_prod_device_code_client
from field_manager_python_client.api.organizations import (
    get_organization_projects_organizations_organization_id_projects_get,
    get_organizations_organizations_get,
)
from field_manager_python_client.models import Organization, Project

# Load environment variables
load_dotenv()
# Output directory - save to examples/output/
OUTPUT_DIR = Path(__file__).parent.parent / "output"
OUTPUT_DIR.mkdir(exist_ok=True)


def project_statistics_calculate_and_save(
    projects: list[Project], org_name: str
) -> None:
    """
    Calculate and save statistics and visualizations for a list of projects.

    Args:
        projects (list[Project]): List of Project objects to analyze.
        org_name (str): Name of the organization for file naming.
    """
    if not projects:
        print("❌ No projects to analyze")
        return

    print(f"📊 Analyzing {len(projects)} projects...")

    # Sort projects by number of locations in descending order
    projects.sort(key=lambda x: x.number_of_locations, reverse=True)

    # Collect project information for saving to Excel
    project_info = [
        {
            "project_name": project.name,
            "number_of_locations": project.number_of_locations,
            "created_at": str(project.created_at) if project.created_at else "Unknown",
            "status": project.status if hasattr(project, "status") else "Unknown",
        }
        for project in projects
    ]

    # Extract number of locations for histogram and statistics
    number_of_locations = [project.number_of_locations for project in projects]

    # Plot histogram of the number of locations
    plt.figure(figsize=(10, 6))
    plt.hist(
        number_of_locations,
        bins=min(50, len(set(number_of_locations))),
        edgecolor="black",
        alpha=0.7,
    )
    plt.title(f"Distribution of Locations per Project - {org_name}")
    plt.xlabel("Number of Locations")
    plt.ylabel("Number of Projects")
    plt.grid(True, alpha=0.3)

    # Save histogram
    histogram_path = (
        OUTPUT_DIR
        / f"project_locations_histogram_{org_name.lower().replace(' ', '_')}.png"
    )
    plt.savefig(histogram_path, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"📈 Histogram saved: {histogram_path}")

    # Calculate statistics
    total_projects = len(projects)
    total_locations = sum(number_of_locations)
    average_locations = np.mean(number_of_locations)
    median_locations = np.median(number_of_locations)
    max_locations = np.max(number_of_locations)
    min_locations = np.min(number_of_locations)

    # Print statistics
    print()
    print(f"📋 Project Statistics for {org_name}:")
    print(f"   • Total projects: {total_projects}")
    print(f"   • Total locations: {total_locations}")
    print(f"   • Average locations per project: {average_locations:.2f}")
    print(f"   • Median locations per project: {median_locations}")
    print(f"   • Maximum locations in a project: {max_locations}")
    print(f"   • Minimum locations in a project: {min_locations}")

    # Top 5 projects by location count
    print("   • Top 5 projects by location count:")
    for i, project in enumerate(projects[:5]):
        print(f"     {i + 1}. {project.name}: {project.number_of_locations} locations")

    # Save statistics to Excel
    stats = {
        "Metric": [
            "Total Projects",
            "Total Locations",
            "Average Locations per Project",
            "Median Locations per Project",
            "Maximum Locations in a Project",
            "Minimum Locations in a Project",
        ],
        "Value": [
            total_projects,
            total_locations,
            round(average_locations, 2),
            median_locations,
            max_locations,
            min_locations,
        ],
    }
    df_stats = pd.DataFrame(stats)
    stats_path = (
        OUTPUT_DIR / f"project_statistics_{org_name.lower().replace(' ', '_')}.xlsx"
    )

    # Save to Excel with multiple sheets
    with pd.ExcelWriter(stats_path, engine="openpyxl") as writer:
        df_stats.to_excel(writer, sheet_name="Statistics", index=False)
        df_projects = pd.DataFrame(project_info)
        df_projects.to_excel(writer, sheet_name="Project Details", index=False)

    print(f"📊 Statistics saved: {stats_path}")
    print()


def main() -> None:
    """
    Main function to fetch organization and project data, then calculate and save statistics.
    """
    print("📈 Historical Project Analysis")
    print()

    client = get_prod_device_code_client()

    with client as client:
        try:
            # Fetch organizations
            organizations: list[Organization] = (
                get_organizations_organizations_get.sync(client=client)
            )

            if not organizations:
                print("❌ No organizations found")
                return

            print("🏢 Available organizations:")
            for i, org in enumerate(organizations):
                print(f"{i + 1}. {org.name} ({org.number_of_projects} projects)")

            # Analyze first organization with projects for demonstration
            selected_org = None
            for org in organizations:
                if org.number_of_projects > 0:
                    selected_org = org
                    break

            if selected_org:
                print(
                    f"\n🔍 Analyzing {selected_org.name} (first org with projects)..."
                )
                projects: list[Project] = (
                    get_organization_projects_organizations_organization_id_projects_get.sync(
                        client=client,
                        organization_id=selected_org.organization_id,
                        limit=100000,
                    )
                )
                project_statistics_calculate_and_save(projects, selected_org.name)
            else:
                print("❌ No organizations with projects found")
                return

            print("✅ Analysis complete! Check the output directory for results.")

        except Exception as e:
            print(f"❌ An error occurred: {e}")


if __name__ == "__main__":
    main()
