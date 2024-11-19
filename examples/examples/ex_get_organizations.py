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
    my_orgs: list[Organization] =  get_organizations_organizations_get.sync(client=client)
    # Print the org names
    for org in my_orgs:
        print(org.name)
        # Get each organization by ID
        org_id = org.organization_id
        print(org_id)
        my_org: Organization = get_organization_organizations_organization_id_get.sync(client=client, organization_id=org_id)
        print(my_org.number_of_projects)
        
        # Get the projects for each organization
        # E2E Org ID: f548e6e1-2aa5-4c9f-9132-bfbf8d05a545
        e2e_org_id = "f548e6e1-2aa5-4c9f-9132-bfbf8d05a545"
        if str(org_id) == e2e_org_id:
            print("E2E Organization projects:")
            akerbp_projects: list[Project] = get_organization_projects_organizations_organization_id_projects_get.sync(client=client, organization_id=e2e_org_id)
            # print(akerbp_projects)
            for project in akerbp_projects:
                print(project.name)