#!/usr/bin/env python3
"""
Access check for dedicated service-account authentication.

This example will:
1. Authenticate using a dedicated service account
2. List the organizations the service account can access
3. List how many projects are available in each organization
4. Show up to the first 10 projects per organization

Setup:
    cp .env.service-account.template .env.service-account
    # Edit .env.service-account with your dedicated client credentials

Run:
    python ex_service_account_access_check.py
"""

import os
import sys
from typing import Iterable

from dotenv import load_dotenv

from field_manager_python_client import get_service_account_client
from field_manager_python_client.api.organizations import (
    get_organization_projects_organizations_organization_id_projects_get,
    get_organizations_organizations_get,
)
from field_manager_python_client.models.http_validation_error import HTTPValidationError
from field_manager_python_client.models.project import Project

PROJECT_PREVIEW_LIMIT = 10


def _load_configuration() -> tuple[str, str, str]:
    env_file = os.path.join(os.path.dirname(__file__), ".env.service-account")
    load_dotenv(env_file)

    client_id = os.getenv("KEYCLOAK_CLIENT_ID")
    client_secret = os.getenv("KEYCLOAK_CLIENT_SECRET")
    environment = os.getenv("FIELD_MANAGER_ENVIRONMENT", "prod")

    if not client_id:
        raise ValueError(f"Missing KEYCLOAK_CLIENT_ID in {env_file}")
    if not client_secret:
        raise ValueError(f"Missing KEYCLOAK_CLIENT_SECRET in {env_file}")

    return client_id, client_secret, environment


def _format_project_names(projects: Iterable[Project]) -> list[str]:
    names: list[str] = []
    for project in projects:
        project_name = getattr(project, "name", None) or "<unnamed project>"
        project_id = getattr(project, "project_id", None) or "<unknown id>"
        names.append(f"- {project_name} ({project_id})")
    return names


def main() -> int:
    try:
        client_id, client_secret, environment = _load_configuration()
    except ValueError as exc:
        print(exc)
        return 1

    print(f"Checking dedicated service-account access against {environment!r}...")

    try:
        client = get_service_account_client(
            environment=environment,
            client_id=client_id,
            client_secret=client_secret,
        )

        with client as authenticated_client:
            organizations = get_organizations_organizations_get.sync(
                client=authenticated_client
            )

            if organizations is None:
                print(
                    "Authentication succeeded, but the organizations request returned no data."
                )
                return 2

            if isinstance(organizations, HTTPValidationError):
                print(
                    f"Authentication succeeded, but organizations lookup failed: {organizations}"
                )
                return 2

            print("Service-account authentication succeeded.")
            print(f"Organizations available: {len(organizations)}")

            if not organizations:
                print(
                    "The service account authenticated, but no organizations are available."
                )
                return 0

            for index, organization in enumerate(organizations, start=1):
                organization_name = (
                    getattr(organization, "name", None) or "<unnamed organization>"
                )
                organization_id = (
                    getattr(organization, "organization_id", None) or "<unknown id>"
                )

                projects = get_organization_projects_organizations_organization_id_projects_get.sync(
                    client=authenticated_client,
                    organization_id=organization_id,
                    limit=100,
                )

                if projects is None:
                    print()
                    print(f"{index}. {organization_name} ({organization_id})")
                    print("   Projects: request returned no data")
                    continue

                if isinstance(projects, HTTPValidationError):
                    print()
                    print(f"{index}. {organization_name} ({organization_id})")
                    print(
                        f"   Projects: request failed with validation error: {projects}"
                    )
                    continue

                project_count = len(projects)
                preview = projects[:PROJECT_PREVIEW_LIMIT]

                print()
                print(f"{index}. {organization_name} ({organization_id})")
                print(f"   Projects available: {project_count}")

                if not preview:
                    print("   No projects available in this organization.")
                    continue

                print(
                    f"   First {min(project_count, PROJECT_PREVIEW_LIMIT)} project(s):"
                )
                for line in _format_project_names(preview):
                    print(f"   {line}")

                if project_count > PROJECT_PREVIEW_LIMIT:
                    print(
                        f"   ... and {project_count - PROJECT_PREVIEW_LIMIT} more project(s)"
                    )

        return 0
    except Exception as exc:
        print(f"Service-account access check failed: {exc}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
