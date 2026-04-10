from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.soil_unit import SoilUnit
from ...models.soil_unit_create import SoilUnitCreate
from ...types import Response


def _get_kwargs(
    project_id: str,
    layer_group_id: UUID,
    *,
    body: SoilUnitCreate,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/projects/{project_id}/layer-groups/{layer_group_id}/soil-units".format(
            project_id=quote(str(project_id), safe=""),
            layer_group_id=quote(str(layer_group_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | SoilUnit | None:
    if response.status_code == 201:
        response_201 = SoilUnit.from_dict(response.json())

        return response_201

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[HTTPValidationError | SoilUnit]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    layer_group_id: UUID,
    *,
    client: AuthenticatedClient,
    body: SoilUnitCreate,
) -> Response[HTTPValidationError | SoilUnit]:
    """Create Soil Unit

     Create a soil unit in a layer group.

    Args:
        project_id (str):
        layer_group_id (UUID):
        body (SoilUnitCreate): Schema for creating a new soil unit.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SoilUnit]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        layer_group_id=layer_group_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    layer_group_id: UUID,
    *,
    client: AuthenticatedClient,
    body: SoilUnitCreate,
) -> HTTPValidationError | SoilUnit | None:
    """Create Soil Unit

     Create a soil unit in a layer group.

    Args:
        project_id (str):
        layer_group_id (UUID):
        body (SoilUnitCreate): Schema for creating a new soil unit.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SoilUnit
    """

    return sync_detailed(
        project_id=project_id,
        layer_group_id=layer_group_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    layer_group_id: UUID,
    *,
    client: AuthenticatedClient,
    body: SoilUnitCreate,
) -> Response[HTTPValidationError | SoilUnit]:
    """Create Soil Unit

     Create a soil unit in a layer group.

    Args:
        project_id (str):
        layer_group_id (UUID):
        body (SoilUnitCreate): Schema for creating a new soil unit.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SoilUnit]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        layer_group_id=layer_group_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    layer_group_id: UUID,
    *,
    client: AuthenticatedClient,
    body: SoilUnitCreate,
) -> HTTPValidationError | SoilUnit | None:
    """Create Soil Unit

     Create a soil unit in a layer group.

    Args:
        project_id (str):
        layer_group_id (UUID):
        body (SoilUnitCreate): Schema for creating a new soil unit.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SoilUnit
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            layer_group_id=layer_group_id,
            client=client,
            body=body,
        )
    ).parsed
