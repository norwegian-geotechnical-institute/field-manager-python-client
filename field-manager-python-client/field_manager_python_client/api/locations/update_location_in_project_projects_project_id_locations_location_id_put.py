from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.location import Location
from ...models.location_update import LocationUpdate
from ...types import Response


def _get_kwargs(
    project_id: str,
    location_id: UUID,
    *,
    body: LocationUpdate,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/projects/{project_id}/locations/{location_id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | Location | None:
    if response.status_code == 200:
        response_200 = Location.from_dict(response.json())

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
) -> Response[HTTPValidationError | Location]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    location_id: UUID,
    *,
    client: AuthenticatedClient,
    body: LocationUpdate,
) -> Response[HTTPValidationError | Location]:
    """Update Location In Project

     Updates location

    Args:
        project_id (str):
        location_id (UUID):
        body (LocationUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | Location]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        location_id=location_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    location_id: UUID,
    *,
    client: AuthenticatedClient,
    body: LocationUpdate,
) -> HTTPValidationError | Location | None:
    """Update Location In Project

     Updates location

    Args:
        project_id (str):
        location_id (UUID):
        body (LocationUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | Location
    """

    return sync_detailed(
        project_id=project_id,
        location_id=location_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    location_id: UUID,
    *,
    client: AuthenticatedClient,
    body: LocationUpdate,
) -> Response[HTTPValidationError | Location]:
    """Update Location In Project

     Updates location

    Args:
        project_id (str):
        location_id (UUID):
        body (LocationUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | Location]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        location_id=location_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    location_id: UUID,
    *,
    client: AuthenticatedClient,
    body: LocationUpdate,
) -> HTTPValidationError | Location | None:
    """Update Location In Project

     Updates location

    Args:
        project_id (str):
        location_id (UUID):
        body (LocationUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | Location
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            location_id=location_id,
            client=client,
            body=body,
        )
    ).parsed
