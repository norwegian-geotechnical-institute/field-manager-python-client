"""
Example: Get Project Information by ID

This example shows how to:
1. Connect to the Field Manager API
2. Get detailed information about a specific project
3. Display project details

Run this example:
    python examples/ex_get_project_info_by_id.py
"""

from field_manager_python_client import get_prod_client
from field_manager_python_client.api.projects import get_project_projects_project_id_get
from field_manager_python_client.api.organizations import (
    get_organizations_organizations_get,
)
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
DEFAULT_EMAIL = os.getenv("DEFAULT_EMAIL", "your.email@example.com")


def main():
    print("📁 Getting project information...")
    print()

    # Use default email directly (non-interactive mode)
    email = DEFAULT_EMAIL
    print(f"Using email: {email}")

    # Connect to production environment
    client = get_prod_client(email=email)

    with client as client:
        # Show available projects first
        print("📋 Available projects:")
        organizations = get_organizations_organizations_get.sync(client=client)

        all_projects = []
        for org in organizations:
            from field_manager_python_client.api.organizations import (
                get_organization_projects_organizations_organization_id_projects_get,
            )

            projects = get_organization_projects_organizations_organization_id_projects_get.sync(
                client=client, organization_id=org.organization_id
            )
            if projects:
                for project in projects:
                    all_projects.append((project, org.name))

        if not all_projects:
            print("❌ No projects found")
            return

        for i, (project, org_name) in enumerate(all_projects[:10]):  # Show first 10
            print(
                f"{i + 1}. {project.name} (ID: {project.project_id}) - {org_name}"
            )

        if len(all_projects) > 10:
            print(f"... and {len(all_projects) - 10} more projects")

        # Use first project for demonstration
        if all_projects:
            project_id = all_projects[0][0].project_id
            print(f"\nUsing first project ID for demonstration: {project_id}")

            try:
                # Get project information
                project_info = get_project_projects_project_id_get.sync(
                    client=client, project_id=project_id
                )

                print()
                print("📁 Project Information:")
                print(f"   Name: {project_info.name}")
                print(f"   ID: {project_info.project_id}")
                print(f"   Description: {project_info.description or 'No description'}")
                print(f"   Created: {project_info.created_at}")
                if hasattr(project_info, 'status'):
                    print(f"   Status: {project_info.status or 'Unknown'}")
                else:
                    print("   Status: Not available")
                print()
                print("✅ Done!")

            except Exception as e:
                print(f"❌ Error getting project info: {e}")
                print("Make sure the project ID is correct and you have access to it.")


if __name__ == "__main__":
    main()
