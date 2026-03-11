from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.location_layer_filter_request import LocationLayerFilterRequest
from ...models.location_layer_filter_response import LocationLayerFilterResponse
from ...types import Response


def _get_kwargs(
    project_id: str,
    *,
    body: LocationLayerFilterRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/projects/{project_id}/location-layer-filters".format(
            project_id=quote(str(project_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | LocationLayerFilterResponse | None:
    if response.status_code == 200:
        response_200 = LocationLayerFilterResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | LocationLayerFilterResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient,
    body: LocationLayerFilterRequest,
) -> Response[HTTPValidationError | LocationLayerFilterResponse]:
    """Get Location Layer Filters

     Get locations matching soil unit or quick clay filters for a layer group.

    Returns locations with map coordinates and resolved rule/color for rendering.

    Args:
        project_id (str):
        body (LocationLayerFilterRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | LocationLayerFilterResponse]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient,
    body: LocationLayerFilterRequest,
) -> HTTPValidationError | LocationLayerFilterResponse | None:
    """Get Location Layer Filters

     Get locations matching soil unit or quick clay filters for a layer group.

    Returns locations with map coordinates and resolved rule/color for rendering.

    Args:
        project_id (str):
        body (LocationLayerFilterRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | LocationLayerFilterResponse
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient,
    body: LocationLayerFilterRequest,
) -> Response[HTTPValidationError | LocationLayerFilterResponse]:
    """Get Location Layer Filters

     Get locations matching soil unit or quick clay filters for a layer group.

    Returns locations with map coordinates and resolved rule/color for rendering.

    Args:
        project_id (str):
        body (LocationLayerFilterRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | LocationLayerFilterResponse]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient,
    body: LocationLayerFilterRequest,
) -> HTTPValidationError | LocationLayerFilterResponse | None:
    """Get Location Layer Filters

     Get locations matching soil unit or quick clay filters for a layer group.

    Returns locations with map coordinates and resolved rule/color for rendering.

    Args:
        project_id (str):
        body (LocationLayerFilterRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | LocationLayerFilterResponse
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            body=body,
        )
    ).parsed
