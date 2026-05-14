from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.layer_group_with_soil_units import LayerGroupWithSoilUnits
from ...types import Response


def _get_kwargs(
    project_id: str,
    layer_group_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/projects/{project_id}/layer-groups/{layer_group_id}/set-default".format(
            project_id=quote(str(project_id), safe=""),
            layer_group_id=quote(str(layer_group_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | LayerGroupWithSoilUnits | None:
    if response.status_code == 200:
        response_200 = LayerGroupWithSoilUnits.from_dict(response.json())

        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[HTTPValidationError | LayerGroupWithSoilUnits]:
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
) -> Response[HTTPValidationError | LayerGroupWithSoilUnits]:
    """Set Default Layer Group

     Set the project default layer group.

    Args:
        project_id (str):
        layer_group_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | LayerGroupWithSoilUnits]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        layer_group_id=layer_group_id,
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
) -> HTTPValidationError | LayerGroupWithSoilUnits | None:
    """Set Default Layer Group

     Set the project default layer group.

    Args:
        project_id (str):
        layer_group_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | LayerGroupWithSoilUnits
    """

    return sync_detailed(
        project_id=project_id,
        layer_group_id=layer_group_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    layer_group_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPValidationError | LayerGroupWithSoilUnits]:
    """Set Default Layer Group

     Set the project default layer group.

    Args:
        project_id (str):
        layer_group_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | LayerGroupWithSoilUnits]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        layer_group_id=layer_group_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    layer_group_id: UUID,
    *,
    client: AuthenticatedClient,
) -> HTTPValidationError | LayerGroupWithSoilUnits | None:
    """Set Default Layer Group

     Set the project default layer group.

    Args:
        project_id (str):
        layer_group_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | LayerGroupWithSoilUnits
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            layer_group_id=layer_group_id,
            client=client,
        )
    ).parsed
