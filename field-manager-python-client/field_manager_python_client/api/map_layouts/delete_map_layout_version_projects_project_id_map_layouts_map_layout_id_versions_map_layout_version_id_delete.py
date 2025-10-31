from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    project_id: str,
    map_layout_id: UUID,
    map_layout_version_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/projects/{project_id}/map_layouts/{map_layout_id}/versions/{map_layout_version_id}",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = response.json()
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
) -> Response[Any | HTTPValidationError]:
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
) -> Response[Any | HTTPValidationError]:
    """Delete Map Layout Version

     Delete map layout version by project_id, map_layout_id and map_layout_version_id.

    Args:
        project_id (str):
        map_layout_id (UUID):
        map_layout_version_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        map_layout_id=map_layout_id,
        map_layout_version_id=map_layout_version_id,
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
) -> Any | HTTPValidationError | None:
    """Delete Map Layout Version

     Delete map layout version by project_id, map_layout_id and map_layout_version_id.

    Args:
        project_id (str):
        map_layout_id (UUID):
        map_layout_version_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return sync_detailed(
        project_id=project_id,
        map_layout_id=map_layout_id,
        map_layout_version_id=map_layout_version_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    map_layout_id: UUID,
    map_layout_version_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Any | HTTPValidationError]:
    """Delete Map Layout Version

     Delete map layout version by project_id, map_layout_id and map_layout_version_id.

    Args:
        project_id (str):
        map_layout_id (UUID):
        map_layout_version_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        map_layout_id=map_layout_id,
        map_layout_version_id=map_layout_version_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    map_layout_id: UUID,
    map_layout_version_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Any | HTTPValidationError | None:
    """Delete Map Layout Version

     Delete map layout version by project_id, map_layout_id and map_layout_version_id.

    Args:
        project_id (str):
        map_layout_id (UUID):
        map_layout_version_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            map_layout_id=map_layout_id,
            map_layout_version_id=map_layout_version_id,
            client=client,
        )
    ).parsed
