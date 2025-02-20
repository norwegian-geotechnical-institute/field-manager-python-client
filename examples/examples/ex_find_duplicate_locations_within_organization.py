from typing import Optional
from pathlib import Path
import folium

from field_manager_python_client.api.organizations import (
    get_organizations_organizations_get,
    get_organization_projects_organizations_organization_id_projects_get,
)
from field_manager_python_client.api.projects import (
    get_project_summary_projects_project_id_summary_get,
)
from field_manager_python_client.models import Organization, Project, Location, ProjectSummary, LocationSummary
from examples.setup_auto_fetch_token import authenticate

def get_organization_by_name(client, org_name: str) -> Optional[Organization]:
    """Get organization by its short name."""
    orgs = get_organizations_organizations_get.sync(client=client)
    return next((org for org in orgs if org.short_name == org_name), None)

def get_all_projects(client, organization: Organization) -> list[Project]:
    """Get all projects for an organization."""
    return get_organization_projects_organizations_organization_id_projects_get.sync(
        client=client,
        organization_id=organization.organization_id,
        limit=2  # Adjust based on your pagination needs
    )

def get_all_locations(client, project: Project) -> list[LocationSummary]:
    """Get all locations for a project."""
    return get_project_summary_projects_project_id_summary_get.sync(
        client=client,
        project_id=project.project_id,
    ).locations

def create_location_map(locations: list[LocationSummary], output_file: Path) -> folium.Map:
    """Create a Folium map with all locations plotted."""
    if not locations:
        raise ValueError("No locations to plot")
    
    # Use first location as map center
    first_loc = next(loc for loc in locations if loc.point_y_wgs84_web and loc.point_x_wgs84_web)
    m = folium.Map(location=[first_loc.point_y_wgs84_web, first_loc.point_x_wgs84_web], zoom_start=10)

    # Add all valid locations
    for loc in locations:
        if loc.point_y_wgs84_web and loc.point_x_wgs84_web:
            folium.Marker(
                location=[loc.point_y_wgs84_web, loc.point_x_wgs84_web],
                popup=f"{loc.name}",
                icon=folium.Icon(color="blue")
            ).add_to(m)

    # Save and return map
    m.save(output_file)
    return m

def main(org_name: str = "foobar"):
    """Main workflow: Auth -> Get Org -> Get Projects -> Get Locations -> Plot Map"""
    client = authenticate()
    output_file = Path("locations_map.html")

    with client:
        try:
            # Step 1: Get organization
            if not (org := get_organization_by_name(client, org_name)):
                print(f"Organization '{org_name}' not found")
                return

            # Step 2: Get all projects and their locations
            projects = get_all_projects(client, org)
            all_locations = []
            
            for project in projects:
                if locations := get_all_locations(client, project):
                    all_locations.extend(locations)
                    print(f"Found {len(locations)} locations in {project.name}")

            # Step 3: Create and save map
            if not all_locations:
                print("No locations found to plot")
                return

            print(f"Creating map with {len(all_locations)} locations...")
            create_location_map(all_locations, output_file)
            print(f"Map saved to {output_file.absolute()}")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()