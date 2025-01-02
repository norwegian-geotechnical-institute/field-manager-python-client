from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.map_layout_version import MapLayoutVersion
from ...models.map_layout_version_update import MapLayoutVersionUpdate
from ...types import Response


def _get_kwargs(
    project_id: str,
    map_layout_id: UUID,
    map_layout_version_id: UUID,
    *,
    body: MapLayoutVersionUpdate,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/projects/{project_id}/map_layouts/{map_layout_id}/versions/{map_layout_version_id}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, MapLayoutVersion]]:
    if response.status_code == 200:
        response_200 = MapLayoutVersion.from_dict(response.json())

        return response_200
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[HTTPValidationError, MapLayoutVersion]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    map_layout_id: UUID,
    map_layout_version_id: UUID,
    *,
    client: AuthenticatedClient,
    body: MapLayoutVersionUpdate,
) -> Response[Union[HTTPValidationError, MapLayoutVersion]]:
    """Update Map Layout Version

     Update map layout version by project_id, map_layout_id and map_layout_version_id.

    Args:
        project_id (str):
        map_layout_id (UUID):
        map_layout_version_id (UUID):
        body (MapLayoutVersionUpdate): Map Layout Version Update. The map_layout_version_id in the
            url will override the map_layout_version_id in the body.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, MapLayoutVersion]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        map_layout_id=map_layout_id,
        map_layout_version_id=map_layout_version_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    map_layout_id: UUID,
    map_layout_version_id: UUID,
    *,
    client: AuthenticatedClient,
    body: MapLayoutVersionUpdate,
) -> Optional[Union[HTTPValidationError, MapLayoutVersion]]:
    """Update Map Layout Version

     Update map layout version by project_id, map_layout_id and map_layout_version_id.

    Args:
        project_id (str):
        map_layout_id (UUID):
        map_layout_version_id (UUID):
        body (MapLayoutVersionUpdate): Map Layout Version Update. The map_layout_version_id in the
            url will override the map_layout_version_id in the body.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, MapLayoutVersion]
    """

    return sync_detailed(
        project_id=project_id,
        map_layout_id=map_layout_id,
        map_layout_version_id=map_layout_version_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    map_layout_id: UUID,
    map_layout_version_id: UUID,
    *,
    client: AuthenticatedClient,
    body: MapLayoutVersionUpdate,
) -> Response[Union[HTTPValidationError, MapLayoutVersion]]:
    """Update Map Layout Version

     Update map layout version by project_id, map_layout_id and map_layout_version_id.

    Args:
        project_id (str):
        map_layout_id (UUID):
        map_layout_version_id (UUID):
        body (MapLayoutVersionUpdate): Map Layout Version Update. The map_layout_version_id in the
            url will override the map_layout_version_id in the body.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, MapLayoutVersion]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        map_layout_id=map_layout_id,
        map_layout_version_id=map_layout_version_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    map_layout_id: UUID,
    map_layout_version_id: UUID,
    *,
    client: AuthenticatedClient,
    body: MapLayoutVersionUpdate,
) -> Optional[Union[HTTPValidationError, MapLayoutVersion]]:
    """Update Map Layout Version

     Update map layout version by project_id, map_layout_id and map_layout_version_id.

    Args:
        project_id (str):
        map_layout_id (UUID):
        map_layout_version_id (UUID):
        body (MapLayoutVersionUpdate): Map Layout Version Update. The map_layout_version_id in the
            url will override the map_layout_version_id in the body.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, MapLayoutVersion]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            map_layout_id=map_layout_id,
            map_layout_version_id=map_layout_version_id,
            client=client,
            body=body,
        )
    ).parsed
