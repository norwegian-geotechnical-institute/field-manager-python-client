"""
Example: List Organizations and Projects

This example shows how to:
1. Connect to the Field Manager API
2. List all organizations you have access to
3. Show project counts for each organization
4. List projects for the first organization with projects
5. Handle API response errors gracefully

Run this example:
    python ex_list_organizations_and_projects.py
"""

from field_manager_python_client import get_prod_client
from field_manager_python_client.models import Organization, Project
from field_manager_python_client.api.organizations import (
    get_organizations_organizations_get,
    get_organization_organizations_organization_id_get,
    get_organization_projects_organizations_organization_id_projects_get,
)
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
DEFAULT_EMAIL = os.getenv("DEFAULT_EMAIL", "your.email@example.com")


def main():
    print("🏢 Getting organizations and projects...")
    print()

    # Use default email directly (non-interactive mode)
    email = DEFAULT_EMAIL
    print(f"Using email: {email}")

    # Connect to production environment
    client = get_prod_client(email=email)

    with client as client:
        # Get all organizations
        organizations: list[Organization] = get_organizations_organizations_get.sync(
            client=client
        )

        print(f"📋 Found {len(organizations)} organization(s):")
        print()

        for index, org in enumerate(organizations):
            # Get detailed organization info
            org_details: Organization = (
                get_organization_organizations_organization_id_get.sync(
                    client=client, organization_id=org.organization_id
                )
            )

            print(f"{index + 1}. {org.name}")
            
            # Check if org_details is not None before accessing attributes
            if org_details and hasattr(org_details, 'number_of_projects'):
                print(f"   📊 Projects: {org_details.number_of_projects}")
                
                # Show projects for the first organization
                if index == 0 and org_details.number_of_projects > 0:
                    print("   📁 Projects in this organization:")

                    projects: list[Project] = (
                        get_organization_projects_organizations_organization_id_projects_get.sync(
                            client=client, organization_id=org.organization_id
                        )
                    )

                    for project in projects[:5]:  # Show first 5 projects
                        print(f"      • {project.name}")

                    if len(projects) > 5:
                        print(f"      ... and {len(projects) - 5} more projects")
            else:
                print("   📊 Projects: Unable to retrieve count")

            print()

        print("✅ Done!")


if __name__ == "__main__":
    main()
