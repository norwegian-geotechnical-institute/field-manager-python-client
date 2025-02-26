from collections import defaultdict
from math import atan2, cos, radians, sin, sqrt

import folium
from field_manager_python_client.models import LocationSummary
from folium.plugins import MarkerCluster


def haversine(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Calculate the distance in meters between two geographic points"""
    R = 6371000  # Earth radius in meters
    phi1 = radians(lat1)
    phi2 = radians(lat2)
    delta_phi = radians(lat2 - lat1)
    delta_lambda = radians(lon1 - lon2)  # Note: lon1 - lon2 for E-W direction
    
    a = sin(delta_phi/2)**2 + cos(phi1)*cos(phi2)*sin(delta_lambda/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    return R * c

def detect_duplicates(location_data: list[tuple[LocationSummary, str, str]]) -> dict[str, list[tuple[LocationSummary, str, str]]]:
    """Detect duplicates based on proximity and attributes"""
    # Spatial indexing grid (50m threshold)
    GRID_SIZE = 0.00045  # Approx 50 meters in degrees
    grid = defaultdict(list)
    
    # First pass: Create spatial grid index
    for idx, (loc, pid, pname) in enumerate(location_data):
        if loc.point_y_wgs84_web and loc.point_x_wgs84_web:
            grid_key = (round(loc.point_y_wgs84_web / GRID_SIZE), 
                       round(loc.point_x_wgs84_web / GRID_SIZE))
            grid[grid_key].append(idx)

    # Second pass: Check neighbors in adjacent grid cells
    duplicates = defaultdict(list)
    checked_pairs = set()
    
    for idx, (loc, pid, pname) in enumerate(location_data):
        if not (loc.point_y_wgs84_web and loc.point_x_wgs84_web):
            continue
            
        base_lat = loc.point_y_wgs84_web
        base_lon = loc.point_x_wgs84_web
        base_grid = (round(base_lat / GRID_SIZE), round(base_lon / GRID_SIZE))
        
        # Check current and adjacent grids
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                neighbor_grid = (base_grid[0] + dx, base_grid[1] + dy)
                for neighbor_idx in grid.get(neighbor_grid, []):
                    if neighbor_idx == idx or (neighbor_idx, idx) in checked_pairs:
                        continue
                        
                    # Get neighbor location
                    nloc, npid, npname = location_data[neighbor_idx]
                    if not (nloc.point_y_wgs84_web and nloc.point_x_wgs84_web):
                        continue
                        
                    # Calculate distance
                    distance = haversine(base_lat, base_lon,
                                        nloc.point_y_wgs84_web, nloc.point_x_wgs84_web)
                    
                    if distance <= 50:
                        # Determine duplicate type
                        same_name = loc.name == nloc.name
                        # methods is a list, comparing methods added name
                        loc_method_names = sorted([method.name for method in loc.methods or []])
                        nloc_method_names = sorted([method.name for method in nloc.methods or []])
                        same_methods = loc_method_names == nloc_method_names
                        
                        if same_name and same_methods:
                            dtype = "III"
                        elif same_name:
                            dtype = "II"
                        else:
                            dtype = "I"
                        
                        # Add to duplicate groups
                        duplicates[dtype].append((idx, neighbor_idx))
                        checked_pairs.add((idx, neighbor_idx))
    
    return duplicates

def create_duplicate_layers(
    location_data: list[tuple[LocationSummary, str, str]],
    duplicates: dict[str, list[tuple[int, int]]]
) -> dict[str, MarkerCluster]:
    """
    Create Folium layers for duplicate locations.
    
    Args:
        location_data: List of tuples containing (LocationSummary, project_id, project_name).
        duplicates: Dictionary of duplicate pairs by type.
    
    Returns:
        A dictionary of Folium MarkerCluster layers for each duplicate type.
    """
    duplicate_layers = {
        "I": MarkerCluster(name="Type I Duplicates (Proximity)", show=False),
        "II": MarkerCluster(name="Type II Duplicates (+Name)", show=False),
        "III": MarkerCluster(name="Type III Duplicates (+Methods)", show=False)
    }

    # Track indices of all duplicates
    duplicate_indices = set()
    for dtype in duplicates.values():
        for pair in dtype:
            duplicate_indices.update(pair)

    # Add markers to appropriate layers
    for idx, (loc, pid, pname) in enumerate(location_data):
        if not (loc.point_y_wgs84_web and loc.point_x_wgs84_web):
            continue

        # Popup content
        popup_content = f"""
            <b>Project:</b> {pname}<br>
            <b>Location:</b> {loc.name}<br>
            <b>Methods:</b> {', '.join(method.name for method in loc.methods or [])}<br>
            <a href="https://app.fieldmanager.io/project/{pid}" target="_blank">View Project</a><br>
            <a href="https://app.fieldmanager.io/project/{pid}/locations/{loc.location_id}" target="_blank">View Location</a>
        """

        # Create marker
        marker = folium.Marker(
            location=[loc.point_y_wgs84_web, loc.point_x_wgs84_web],
            popup=folium.Popup(popup_content, max_width=300),
            icon=folium.Icon(color="red")
        )

        # Add to appropriate layer
        if idx in duplicate_indices:
            # Find highest duplicate type
            max_type = "I"
            for dtype in ["II", "III"]:
                if any(idx in pair for pair in duplicates.get(dtype, [])):
                    max_type = dtype
            duplicate_layers[max_type].add_child(marker)

    return duplicate_layers