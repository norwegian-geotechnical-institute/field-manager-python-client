"""
Example: Find Duplicate Locations Within Organization

This example shows how to:
1. Connect to the Field Manager API
2. Get all locations within an organization
3. Detect duplicate locations (same coordinates)
4. Create an interactive map showing all locations
5. Save results to the output directory

Run this example:
    python examples/ex_find_duplicate_locations_within_organization.py
"""

from typing import Optional
from pathlib import Path
import folium
from folium.plugins import MarkerCluster
import os
from dotenv import load_dotenv

from field_manager_python_client import get_prod_client
from field_manager_python_client.api.organizations import (
    get_organizations_organizations_get,
    get_organization_projects_organizations_organization_id_projects_get,
)
from field_manager_python_client.api.projects import (
    get_project_summary_projects_project_id_summary_get,
)
from field_manager_python_client.models import Organization, Project, LocationSummary

# Load environment variables
load_dotenv()
DEFAULT_EMAIL = os.getenv("DEFAULT_EMAIL", "your.email@example.com")

# Output directory - save to examples/output/
OUTPUT_DIR = Path(__file__).parent.parent / "output"
OUTPUT_DIR.mkdir(exist_ok=True)


def detect_duplicates(location_data: list[tuple[LocationSummary, str, str]]) -> dict:
    """
    Detect duplicate locations based on coordinates.

    Args:
        location_data: List of (location, project_id, project_name) tuples

    Returns:
        Dictionary mapping coordinate tuples to lists of duplicate locations
    """
    coordinate_map = {}

    for loc, project_id, project_name in location_data:
        if loc.point_easting and loc.point_northing:
            # Round coordinates to avoid floating point precision issues
            coords = (round(loc.point_easting, 2), round(loc.point_northing, 2))

            if coords not in coordinate_map:
                coordinate_map[coords] = []
            coordinate_map[coords].append((loc, project_id, project_name))

    # Return only coordinates with multiple locations
    return {coords: locs for coords, locs in coordinate_map.items() if len(locs) > 1}


def create_duplicate_layers(
    location_data: list[tuple[LocationSummary, str, str]], duplicates: dict
) -> dict:
    """
    Create separate layers for duplicate locations.

    Args:
        location_data: List of all location data
        duplicates: Dictionary of duplicate coordinates

    Returns:
        Dictionary of folium layers for duplicates
    """
    duplicate_layers = {}
    colors = ["red", "orange", "purple", "darkred", "lightred", "darkblue", "darkgreen"]

    for i, (coords, duplicate_locs) in enumerate(duplicates.items()):
        if len(duplicate_locs) > 1:
            color = colors[i % len(colors)]
            layer_name = f"Duplicates at {coords[0]:.0f}, {coords[1]:.0f} ({len(duplicate_locs)} locations)"
            layer = folium.FeatureGroup(name=layer_name, show=True)

            for loc, project_id, project_name in duplicate_locs:
                if loc.point_y_wgs84_web and loc.point_x_wgs84_web:
                    popup_content = f"""
                        <b>DUPLICATE LOCATION</b><br>
                        <b>Project:</b> {project_name}<br>
                        <b>Location:</b> {loc.name}<br>
                        <b>Coordinates:</b> {coords[0]:.2f}, {coords[1]:.2f}<br>
                        <a href="https://app.fieldmanager.io/project/{project_id}" target="_blank">View Project</a><br>
                        <a href="https://app.fieldmanager.io/project/{project_id}/locations/{loc.location_id}" target="_blank">View Location</a>
                    """

                    folium.Marker(
                        location=[loc.point_y_wgs84_web, loc.point_x_wgs84_web],
                        popup=folium.Popup(popup_content, max_width=300),
                        icon=folium.Icon(color=color, icon="warning-sign"),
                    ).add_to(layer)

            duplicate_layers[coords] = layer

    return duplicate_layers


def get_organization_by_name(client, org_name: str) -> Optional[Organization]:
    """Get organization by its short name."""
    orgs = get_organizations_organizations_get.sync(client=client)
    return next(
        (org for org in orgs if org.short_name.lower() == org_name.lower()), None
    )


def get_all_projects(client, organization: Organization) -> list[Project]:
    """Get all projects for an organization."""
    return get_organization_projects_organizations_organization_id_projects_get.sync(
        client=client,
        organization_id=organization.organization_id,
        limit=1500,  # Adjust based on your pagination needs
    )


def get_all_locations(
    client, project: Project
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
            f"⚠️  Error getting locations for project {project.project_id} {project.name}: {e}"
        )
        return [], project.project_id, project.name


def create_location_map(
    location_data: list[tuple[LocationSummary, str, str]], output_file: Path
) -> folium.Map:
    """Create an interactive map with all locations and highlight duplicates."""
    # Center the map on Norway
    m = folium.Map(location=[60, 10], zoom_start=6)

    # MarkerCluster layer for all locations
    cluster_layer = MarkerCluster(name="All Locations (Clustered)", show=True)

    # Individual markers layer
    individual_layer = folium.FeatureGroup(
        name="All Locations (Individual)", show=False
    )

    # Detect duplicates
    duplicates = detect_duplicates(location_data)

    # Create duplicate layers
    duplicate_layers = create_duplicate_layers(location_data, duplicates)

    # Add markers to both layers
    for loc, project_id, project_name in location_data:
        if loc.point_y_wgs84_web and loc.point_x_wgs84_web:
            coords = [loc.point_y_wgs84_web, loc.point_x_wgs84_web]

            # Common popup
            popup_content = f"""
                <b>Project:</b> {project_name}<br>
                <b>Location:</b> {loc.name}<br>
                <b>Coordinates:</b> {loc.point_easting:.2f}, {loc.point_northing:.2f}<br>
                <a href="https://app.fieldmanager.io/project/{project_id}" target="_blank">View Project</a><br>
                <a href="https://app.fieldmanager.io/project/{project_id}/locations/{loc.location_id}" target="_blank">View Location</a>
            """

            # Add to cluster layer
            folium.Marker(
                location=coords,
                popup=folium.Popup(popup_content, max_width=300),
                icon=folium.Icon(color="blue"),
            ).add_to(cluster_layer)

            # Add to individual layer
            folium.Marker(
                location=coords,
                popup=folium.Popup(popup_content, max_width=300),
                icon=folium.Icon(color="green"),
            ).add_to(individual_layer)

    # Add all layers to the map
    cluster_layer.add_to(m)
    individual_layer.add_to(m)
    for layer in duplicate_layers.values():
        layer.add_to(m)

    # Add layer control to toggle them
    folium.LayerControl().add_to(m)

    # Save
    m.save(output_file)
    return m


def main() -> None:
    """Main workflow: Auth -> Get Org -> Get Projects -> Get Locations -> Plot Map"""
    print("🔍 Finding Duplicate Locations Within Organization")
    print()

    # Use default email directly (non-interactive mode)
    email = DEFAULT_EMAIL
    print(f"Using email: {email}")

    client = get_prod_client(email=email)

    with client as client:
        try:
            # Get available organizations
            organizations = get_organizations_organizations_get.sync(client=client)

            if not organizations:
                print("❌ No organizations found")
                return

            print("🏢 Available organizations:")
            for i, org in enumerate(organizations):
                print(
                    f"{i + 1}. {org.name} ({org.short_name}) - {org.number_of_projects} projects"
                )

            # Use first organization with projects for demonstration
            selected_org = None
            for org in organizations:
                if org.number_of_projects > 0:
                    selected_org = org
                    break

            if not selected_org:
                print("❌ No organizations with projects found")
                return

            print(f"\n🔍 Analyzing {selected_org.name} (first org with projects)...")

            # Get all projects and their locations
            projects = get_all_projects(client, selected_org)
            print(f"📁 Found {len(projects)} projects")

            # List to store tuples of (location, project_id, project_name)
            all_location_data = []

            for count, project in enumerate(projects, start=1):
                print(f"   Processing project {count}/{len(projects)}: {project.name}")
                locations, project_id, project_name = get_all_locations(client, project)
                if locations:
                    for loc in locations:
                        all_location_data.append((loc, project_id, project_name))

            if not all_location_data:
                print("❌ No locations found to analyze")
                return

            print(f"\n📍 Found {len(all_location_data)} total locations")

            # Detect duplicates
            duplicate_locations_data = detect_duplicates(all_location_data)
            duplicate_count = sum(len(v) for v in duplicate_locations_data.values())

            print("🔍 Analysis Results:")
            print(f"   • Total locations: {len(all_location_data)}")
            print(f"   • Duplicate locations: {duplicate_count}")
            print(
                f"   • Unique coordinate sets with duplicates: {len(duplicate_locations_data)}"
            )

            if duplicate_locations_data:
                print("\n⚠️  Duplicate coordinate sets:")
                for coords, locs in list(duplicate_locations_data.items())[:5]:
                    print(
                        f"   • {coords[0]:.2f}, {coords[1]:.2f}: {len(locs)} locations"
                    )
                    for loc, proj_id, proj_name in locs[:3]:
                        print(f"     - {loc.name} (Project: {proj_name})")
                    if len(locs) > 3:
                        print(f"     ... and {len(locs) - 3} more")

                if len(duplicate_locations_data) > 5:
                    print(
                        f"   ... and {len(duplicate_locations_data) - 5} more coordinate sets"
                    )

            # Create and save map
            output_file = (
                OUTPUT_DIR
                / f"duplicate_locations_map_{selected_org.short_name.lower()}.html"
            )
            print("\n🗺️  Creating interactive map...")

            create_location_map(all_location_data, output_file)
            print(f"✅ Map saved: {output_file}")
            print()
            print("💡 Open the HTML file in your browser to explore the map!")
            print("   • Use layer controls to toggle different views")
            print("   • Duplicate locations are highlighted in red/orange")
            print("   • Click markers for detailed information")

        except Exception as e:
            print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()
