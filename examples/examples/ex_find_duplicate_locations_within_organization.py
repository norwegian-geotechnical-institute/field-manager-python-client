from typing import Optional
from pathlib import Path
import folium
from folium.plugins import MarkerCluster

from field_manager_python_client.api.organizations import (
    get_organizations_organizations_get,
    get_organization_projects_organizations_organization_id_projects_get,
)
from field_manager_python_client.api.projects import (
    get_project_summary_projects_project_id_summary_get,
)
from field_manager_python_client.models import Organization, Project, LocationSummary
from examples.find_duplicate_locations import create_duplicate_layers, detect_duplicates
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
        limit=1500,  # Adjust based on your pagination needs
    )


def get_all_locations(client, project: Project) -> tuple[list[LocationSummary], str, str]:
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


def create_location_map(
    location_data: list[tuple[LocationSummary, str, str]], output_file: Path
) -> folium.Map:

    # Center the map on the North Sea off Norway (approx 60°N, 4°E). 
    # You can tweak the latitude, longitude, or zoom_start as desired.
    m = folium.Map(location=[60, 4], zoom_start=6)

    # MarkerCluster layer
    cluster_layer = MarkerCluster(name="Clustered Markers", show=True)
    
    # Optional: Non-clustered layer
    non_cluster_layer = folium.FeatureGroup(name="Individual Markers", show=False)
    
    #  # Detect duplicates
    duplicates = detect_duplicates(location_data)

    # # Create duplicate layers
    duplicate_layers = create_duplicate_layers(location_data, duplicates)

    # Add markers to both layers
    for loc, project_id, project_name in location_data:
        if loc.point_y_wgs84_web and loc.point_x_wgs84_web:
            coords = [loc.point_y_wgs84_web, loc.point_x_wgs84_web]
            
            # Common popup
            popup_content = f"""
                <b>Project:</b> {project_name}<br>
                <b>Location:</b> {loc.name}<br>
                <a href="https://app.fieldmanager.io/project/{project_id}" target="_blank">View Project</a><br>
                <a href="https://app.fieldmanager.io/project/{project_id}/locations/{loc.location_id}" target="_blank">View Location</a>
            """
            
            folium.Marker(
                location=coords,
                popup=folium.Popup(popup_content, max_width=300),
                icon=folium.Icon(color="blue"),
            ).add_to(cluster_layer)
            
            folium.Marker(
                location=coords,
                popup=folium.Popup(popup_content, max_width=300),
                icon=folium.Icon(color="green", icon_size=(15, 25)),
            ).add_to(non_cluster_layer)

    # Add the layers to the map
    cluster_layer.add_to(m)
    non_cluster_layer.add_to(m)
    for layer in duplicate_layers.values():
        layer.add_to(m)
    
    # Add layer control to toggle them
    folium.LayerControl().add_to(m)

    # Save
    m.save(output_file)
    return m


def main(org_name: str = "AkerBP"):
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
            # List to store tuples of (location, project_id, project_name)
            all_location_data = []

            for count, project in enumerate(projects, start=1):
                locations, project_id, project_name = get_all_locations(client, project)
                if locations:
                    for loc in locations:
                        all_location_data.append((loc, project_id, project_name))

            # Step 3: Create and save map
            if not all_location_data:
                print("No locations found to plot")
                return

            print(f"Creating map with {len(all_location_data)} locations...")
            duplicate_locations_data = detect_duplicates(all_location_data)
            print(f"Detected {sum(len(v) for v in duplicate_locations_data.values())} duplicates")
            create_location_map(all_location_data, output_file)
            print(f"Map saved to {output_file.absolute()}")

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
