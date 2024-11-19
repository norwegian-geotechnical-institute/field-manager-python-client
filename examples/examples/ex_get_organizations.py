# Import models
from field_manager_data_api_client.models import Organization, Project

# Import API functions for organizations
from field_manager_data_api_client.api.organizations import (
    get_organizations_organizations_get,
    get_organization_organizations_organization_id_get,
    get_organization_projects_organizations_organization_id_projects_get,
)

# Import client setup
from setup import client


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
        print(org.name, "has ", my_org.number_of_projects, "projects.")

        # Fetch the projects for the first organization
        if index == 0:
            first_org_projects: list[Project] = (
                get_organization_projects_organizations_organization_id_projects_get.sync(
                    client=client, organization_id=org_id
                )
            )
            print("    ", org.name, " has the following projects: ")
            for project in first_org_projects:
                print("        ", project.name)
