from field_manager_python_client.api.projects import get_project_projects_project_id_get
from examples.setup_auto_fetch_token import authenticate

client = authenticate()
project_id = "your-project-id"
project_info = get_project_projects_project_id_get.sync(
    client=client, project_id=project_id
)

print(f"Project Name: {project_info.name}")
