from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.location_layer_intervals_response import LocationLayerIntervalsResponse
from ...types import Response


def _get_kwargs(
    project_id: str,
    layer_group_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/projects/{project_id}/layer-groups/{layer_group_id}/location-layer-intervals".format(
            project_id=quote(str(project_id), safe=""),
            layer_group_id=quote(str(layer_group_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | LocationLayerIntervalsResponse | None:
    if response.status_code == 200:
        response_200 = LocationLayerIntervalsResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | LocationLayerIntervalsResponse]:
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
) -> Response[HTTPValidationError | LocationLayerIntervalsResponse]:
    """Get Location Layer Intervals

     Get all layer intervals for locations in a project and layer group.

    Returns map-ready location coordinates with ordered intervals and soil unit metadata.

    Args:
        project_id (str):
        layer_group_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | LocationLayerIntervalsResponse]
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
) -> HTTPValidationError | LocationLayerIntervalsResponse | None:
    """Get Location Layer Intervals

     Get all layer intervals for locations in a project and layer group.

    Returns map-ready location coordinates with ordered intervals and soil unit metadata.

    Args:
        project_id (str):
        layer_group_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | LocationLayerIntervalsResponse
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
) -> Response[HTTPValidationError | LocationLayerIntervalsResponse]:
    """Get Location Layer Intervals

     Get all layer intervals for locations in a project and layer group.

    Returns map-ready location coordinates with ordered intervals and soil unit metadata.

    Args:
        project_id (str):
        layer_group_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | LocationLayerIntervalsResponse]
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
) -> HTTPValidationError | LocationLayerIntervalsResponse | None:
    """Get Location Layer Intervals

     Get all layer intervals for locations in a project and layer group.

    Returns map-ready location coordinates with ordered intervals and soil unit metadata.

    Args:
        project_id (str):
        layer_group_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | LocationLayerIntervalsResponse
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            layer_group_id=layer_group_id,
            client=client,
        )
    ).parsed
