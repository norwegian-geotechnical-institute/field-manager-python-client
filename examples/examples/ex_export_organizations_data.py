"""
Example demonstrating how to save API data to files in the output directory.

This example shows:
1. Using the new integrated authentication system
2. Fetching organization data from the API
3. Saving results to various file formats in the output/ directory
4. Proper error handling and logging
"""

import json
import csv
from pathlib import Path
from datetime import datetime

# Import models
from field_manager_python_client.models import Organization

# Import API functions
from field_manager_python_client.api.organizations import (
    get_organizations_organizations_get,
    get_organization_organizations_organization_id_get,
)

# New authentication system
from field_manager_python_client import get_prod_device_code_client


def setup_output_directory():
    """Create output directory if it doesn't exist."""
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    return output_dir


def save_organizations_json(organizations: list[Organization], output_dir: Path):
    """Save organizations data to JSON file."""
    filename = (
        output_dir / f"organizations_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    )

    # Convert to serializable format
    data = []
    for org in organizations:
        data.append(
            {
                "organization_id": str(org.organization_id),
                "name": org.name,
                "created_at": org.created_at.isoformat() if org.created_at else None,
                "updated_at": org.updated_at.isoformat() if org.updated_at else None,
            }
        )

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"✅ Saved organizations to JSON: {filename}")
    return filename


def save_organizations_csv(organizations: list[Organization], output_dir: Path):
    """Save organizations data to CSV file."""
    filename = (
        output_dir / f"organizations_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    )

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        # Write header
        writer.writerow(["Organization ID", "Name", "Created At", "Updated At"])

        # Write data
        for org in organizations:
            writer.writerow(
                [
                    str(org.organization_id),
                    org.name,
                    org.created_at.isoformat() if org.created_at else "",
                    org.updated_at.isoformat() if org.updated_at else "",
                ]
            )

    print(f"✅ Saved organizations to CSV: {filename}")
    return filename


def save_detailed_organizations_report(
    organizations: list[Organization], client, output_dir: Path
):
    """Save detailed organizations report with project counts."""
    filename = (
        output_dir
        / f"organizations_detailed_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    )

    detailed_data = []

    for org in organizations:
        try:
            # Get detailed organization info
            detailed_org = get_organization_organizations_organization_id_get.sync(
                client=client, organization_id=org.organization_id
            )

            detailed_data.append(
                {
                    "organization_id": str(org.organization_id),
                    "name": org.name,
                    "created_at": org.created_at.isoformat()
                    if org.created_at
                    else None,
                    "updated_at": org.updated_at.isoformat()
                    if org.updated_at
                    else None,
                    "number_of_projects": detailed_org.number_of_projects,
                    "status": "active"
                    if detailed_org.number_of_projects > 0
                    else "inactive",
                }
            )

        except Exception as e:
            print(f"⚠️  Warning: Could not fetch details for {org.name}: {e}")
            detailed_data.append(
                {
                    "organization_id": str(org.organization_id),
                    "name": org.name,
                    "created_at": org.created_at.isoformat()
                    if org.created_at
                    else None,
                    "updated_at": org.updated_at.isoformat()
                    if org.updated_at
                    else None,
                    "number_of_projects": None,
                    "status": "unknown",
                    "error": str(e),
                }
            )

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(detailed_data, f, indent=2, ensure_ascii=False)

    print(f"✅ Saved detailed organizations report: {filename}")
    return filename


def create_summary_report(organizations: list[Organization], output_dir: Path):
    """Create a summary report of the organizations."""
    filename = (
        output_dir
        / f"organizations_summary_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    )

    with open(filename, "w", encoding="utf-8") as f:
        f.write("FIELD MANAGER ORGANIZATIONS SUMMARY\n")
        f.write("=" * 50 + "\n\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Total Organizations: {len(organizations)}\n\n")

        f.write("ORGANIZATIONS LIST:\n")
        f.write("-" * 30 + "\n")

        for i, org in enumerate(organizations, 1):
            f.write(f"{i:2d}. {org.name}\n")
            f.write(f"    ID: {org.organization_id}\n")
            if org.created_at:
                f.write(f"    Created: {org.created_at.strftime('%Y-%m-%d')}\n")
            f.write("\n")

    print(f"✅ Saved summary report: {filename}")
    return filename


def main():
    """Main function demonstrating file output capabilities."""

    print("=== Organizations Data Export Example ===\n")

    try:
        # Setup output directory
        output_dir = setup_output_directory()
        print(f"📁 Output directory: {output_dir.absolute()}\n")

        # Authenticate with test environment
        # Replace with your actual email address
        client = get_prod_device_code_client()
        print("✅ Authentication successful!\n")

        # Fetch organizations
        print("🔄 Fetching organizations...")
        with client as client:
            organizations: list[Organization] = (
                get_organizations_organizations_get.sync(client=client)
            )

        print(f"✅ Found {len(organizations)} organizations\n")

        if not organizations:
            print("⚠️  No organizations found. Nothing to export.")
            return

        # Save to different formats
        print("💾 Saving data to files...")

        # Save to JSON
        json_file = save_organizations_json(organizations, output_dir)

        # Save to CSV
        csv_file = save_organizations_csv(organizations, output_dir)

        # Save detailed report
        detailed_file = save_detailed_organizations_report(
            organizations, client, output_dir
        )

        # Create summary report
        summary_file = create_summary_report(organizations, output_dir)

        print("\n🎉 Export completed successfully!")
        print("📄 Files created:")
        print(f"   - JSON: {json_file.name}")
        print(f"   - CSV: {csv_file.name}")
        print(f"   - Detailed: {detailed_file.name}")
        print(f"   - Summary: {summary_file.name}")
        print(f"\n📁 All files saved to: {output_dir.absolute()}")

    except Exception as e:
        print(f"❌ Error occurred: {e}")
        print("\nTroubleshooting tips:")
        print(
            "1. Make sure you have python-keycloak installed: pip install python-keycloak"
        )
        print("2. Replace 'your.email@example.com' with your actual email address")
        print("3. Check your internet connection")
        print("4. Verify you have access to the test environment")
        print("5. Make sure the output/ directory is writable")


if __name__ == "__main__":
    main()
