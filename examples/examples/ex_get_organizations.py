"""
This example demonstrates how to interact with an API using a Python client to retrieve
and display information about organizations and their associated projects.

1. Setup: Imports necessary models (Organization, Project) and API functions for fetching
   organizations and their projects.
2. Client Initialization: Sets up and uses an API client.
3. Fetch and List Organizations:
   - Retrieves a list of organizations and iterates through each organization to print its name
     and number of projects.
4. Detailed Fetch for First Organization:
   - For the first organization, fetches and displays its projects by iterating through them
     and printing each project name.

This approach allows the user to:
- List all organizations.
- Display the number of projects for each organization.
- List project names for the first organization in a detailed format.
"""

# Import models
from field_manager_python_client.models import Organization, Project

# Import API functions for organizations
from field_manager_python_client.api.organizations import (
    get_organizations_organizations_get,
    get_organization_organizations_organization_id_get,
    get_organization_projects_organizations_organization_id_projects_get,
)

# Import client setup
from examples.examples.setup_auto_fetch_token import client


with client as client:
    my_orgs: list[Organization] = get_organizations_organizations_get.sync(
        client=client
    )
    for index, org in enumerate(my_orgs):
        # For each organization, print the name, then fetch the organization by ID
        org_id = org.organization_id
        # Fetch each organization by ID
        my_org: Organization = get_organization_organizations_organization_id_get.sync(
            client=client, organization_id=org_id
        )
        print(org.name, "has", my_org.number_of_projects, "projects.")

        # Fetch the projects for the first organization
        if index == 0:
            first_org_projects: list[Project] = (
                get_organization_projects_organizations_organization_id_projects_get.sync(
                    client=client, organization_id=org_id
                )
            )
            print("    ", org.name, "has the following projects:")
            for project in first_org_projects:
                print("        ", project.name)
