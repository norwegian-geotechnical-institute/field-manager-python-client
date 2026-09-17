#!/usr/bin/env python3
"""
Example: Get Piezometer Data

This example shows how to:
1. Connect to the Field Manager API
2. Select a project, either from FIELD_MANAGER_PROJECT_ID or the first accessible project
3. Find locations with piezometer (PZ) methods
4. Fetch and print piezometer data rows for each method

Optional .env values:
    FIELD_MANAGER_ENVIRONMENT=prod
    FIELD_MANAGER_PROJECT_ID=<project id>
    FIELD_MANAGER_LOCATION_LIMIT=100
    FIELD_MANAGER_METHOD_LIMIT=100
    FIELD_MANAGER_DATA_PREVIEW_LIMIT=5

Run this example from the examples directory:
    python examples/ex_get_piezometer_data.py
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any

from dotenv import load_dotenv

from field_manager_python_client import (
    get_prod_device_code_client,
    get_test_device_code_client,
)
from field_manager_python_client.api.locations import (
    get_locations_in_project_projects_project_id_locations_get,
)
from field_manager_python_client.api.methods import (
    get_methods_data_projects_project_id_locations_location_id_methods_method_id_data_get,
    get_methods_for_location_of_type_projects_project_id_locations_location_id_methods_type_method_type_name_get,
)
from field_manager_python_client.api.organizations import (
    get_organization_projects_organizations_organization_id_projects_get,
    get_organizations_organizations_get,
)
from field_manager_python_client.models.http_validation_error import HTTPValidationError
from field_manager_python_client.models.location import Location
from field_manager_python_client.models.method_pz import MethodPZ
from field_manager_python_client.models.method_pz_data import MethodPZData
from field_manager_python_client.models.method_type_enum import MethodTypeEnum
from field_manager_python_client.models.method_type_enum_str import MethodTypeEnumStr
from field_manager_python_client.models.project import Project
from field_manager_python_client.types import Unset

# Method type id 5 is PZ in Field Manager.
PZ_METHOD_TYPE_ID = MethodTypeEnum.VALUE_5
get_piezometer_methods_for_location = get_methods_for_location_of_type_projects_project_id_locations_location_id_methods_type_method_type_name_get
get_method_data = get_methods_data_projects_project_id_locations_location_id_methods_method_id_data_get

ENV_FILE = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(ENV_FILE)
load_dotenv()

FIELD_MANAGER_ENVIRONMENT = os.getenv("FIELD_MANAGER_ENVIRONMENT", "test")
FIELD_MANAGER_PROJECT_ID = os.getenv("FIELD_MANAGER_PROJECT_ID")
LOCATION_LIMIT = int(os.getenv("FIELD_MANAGER_LOCATION_LIMIT", "10"))
METHOD_LIMIT = int(os.getenv("FIELD_MANAGER_METHOD_LIMIT", "10"))
DATA_PREVIEW_LIMIT = int(os.getenv("FIELD_MANAGER_DATA_PREVIEW_LIMIT", "5"))


def _get_client(environment: str):
    environment = environment.lower()
    if environment == "prod":
        return get_prod_device_code_client()
    if environment == "test":
        return get_test_device_code_client()
    raise ValueError("FIELD_MANAGER_ENVIRONMENT must be either 'prod' or 'test'")


def _format_value(value: Any) -> str:
    if value is None or isinstance(value, Unset):
        return "-"
    return str(value)


def _format_row(row: MethodPZData) -> str:
    return (
        f"{_format_value(row.date)} | "
        f"reading={_format_value(row.reading_type)} | "
        f"pore_pressure={_format_value(row.pore_pressure)} | "
        f"calculated_pore_pressure={_format_value(row.calculated_pore_pressure)} | "
        f"head={_format_value(row.calculated_piezometric_head)} | "
        f"potential_level={_format_value(row.calculated_piezometric_potential_level)} | "
        f"temperature={_format_value(row.temperature)}"
    )


def _select_first_accessible_project(client) -> Project | None:
    organizations = get_organizations_organizations_get.sync(client=client)

    if organizations is None:
        print("Organizations request returned no data.")
        return None

    if isinstance(organizations, HTTPValidationError):
        print(f"Organizations request failed: {organizations}")
        return None

    for organization in organizations:
        projects = (
            get_organization_projects_organizations_organization_id_projects_get.sync(
                client=client,
                organization_id=organization.organization_id,
                limit=100,
            )
        )

        if projects is None or isinstance(projects, HTTPValidationError):
            continue

        if projects:
            return projects[0]

    return None


def _get_locations_with_piezometers(client, project_id: str) -> list[Location]:
    locations = get_locations_in_project_projects_project_id_locations_get.sync(
        client=client,
        project_id=project_id,
        limit=LOCATION_LIMIT,
        method_types=[PZ_METHOD_TYPE_ID],
    )

    if locations is None:
        print("Locations request returned no data.")
        return []

    if isinstance(locations, HTTPValidationError):
        print(f"Locations request failed: {locations}")
        return []

    return locations


def _get_piezometer_methods(
    client,
    project_id: str,
    location: Location,
) -> list[MethodPZ]:
    methods = get_piezometer_methods_for_location.sync(
        client=client,
        project_id=project_id,
        location_id=location.location_id,
        method_type_name=MethodTypeEnumStr.PZ,
        limit=METHOD_LIMIT,
    )

    if methods is None:
        print(f"  Methods request returned no data for {location.name}.")
        return []

    if isinstance(methods, HTTPValidationError):
        print(f"  Methods request failed for {location.name}: {methods}")
        return []

    return [method for method in methods if isinstance(method, MethodPZ)]


def _get_piezometer_data(
    client,
    project_id: str,
    location: Location,
    method: MethodPZ,
) -> list[MethodPZData]:
    rows = get_method_data.sync(
        client=client,
        project_id=project_id,
        location_id=location.location_id,
        method_id=method.method_id,
    )

    if rows is None:
        print(f"    Data request returned no rows for method {method.name}.")
        return []

    if isinstance(rows, HTTPValidationError):
        print(f"    Data request failed for method {method.name}: {rows}")
        return []

    return [row for row in rows if isinstance(row, MethodPZData)]


def main() -> None:
    print("Getting piezometer data")
    print()
    print(f"Using environment: {FIELD_MANAGER_ENVIRONMENT}")

    client = _get_client(FIELD_MANAGER_ENVIRONMENT)

    with client as authenticated_client:
        project_id = FIELD_MANAGER_PROJECT_ID
        project_name = "configured project"

        if not project_id:
            project = _select_first_accessible_project(authenticated_client)
            if project is None:
                print("No accessible projects found.")
                return
            project_id = str(project.project_id)
            project_name = project.name

        print(f"Using project: {project_name} ({project_id})")
        print()

        locations = _get_locations_with_piezometers(authenticated_client, project_id)
        if not locations:
            print("No locations with piezometer methods found.")
            return

        print(f"Found {len(locations)} location(s) with piezometer methods.")

        total_methods = 0
        total_rows = 0

        for location in locations:
            print()
            print(f"Location: {location.name} ({location.location_id})")

            methods = _get_piezometer_methods(
                authenticated_client,
                project_id,
                location,
            )
            total_methods += len(methods)

            if not methods:
                print("  No PZ methods found.")
                continue

            for method in methods:
                method_type = _format_value(method.piezometer_type)
                transformation = _format_value(method.transformation_type)
                print(f"  Method: {method.name} ({method.method_id})")
                print(f"    Type: {method_type}, transformation: {transformation}")

                rows = _get_piezometer_data(
                    authenticated_client,
                    project_id,
                    location,
                    method,
                )
                total_rows += len(rows)

                if not rows:
                    print("    No piezometer data rows found.")
                    continue

                print(f"    Rows: {len(rows)}")
                print(f"    First {min(len(rows), DATA_PREVIEW_LIMIT)} row(s):")
                for row in rows[:DATA_PREVIEW_LIMIT]:
                    print(f"      - {_format_row(row)}")

                if len(rows) > DATA_PREVIEW_LIMIT:
                    print(f"      ... and {len(rows) - DATA_PREVIEW_LIMIT} more row(s)")

        print()
        print(f"Summary: {total_methods} PZ method(s), {total_rows} data row(s)")


if __name__ == "__main__":
    main()
