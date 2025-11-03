from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.shape import Shape
from ...types import Response


def _get_kwargs(
    project_id: str,
    shape_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/projects/{project_id}/shapes/{shape_id}",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | Shape | None:
    if response.status_code == 200:
        response_200 = Shape.from_dict(response.json())

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
) -> Response[HTTPValidationError | Shape]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    shape_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPValidationError | Shape]:
    """Get Shape

     Get shape by shape_id

    Args:
        project_id (str):
        shape_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | Shape]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        shape_id=shape_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    shape_id: UUID,
    *,
    client: AuthenticatedClient,
) -> HTTPValidationError | Shape | None:
    """Get Shape

     Get shape by shape_id

    Args:
        project_id (str):
        shape_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | Shape
    """

    return sync_detailed(
        project_id=project_id,
        shape_id=shape_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    shape_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPValidationError | Shape]:
    """Get Shape

     Get shape by shape_id

    Args:
        project_id (str):
        shape_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | Shape]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        shape_id=shape_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    shape_id: UUID,
    *,
    client: AuthenticatedClient,
) -> HTTPValidationError | Shape | None:
    """Get Shape

     Get shape by shape_id

    Args:
        project_id (str):
        shape_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | Shape
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            shape_id=shape_id,
            client=client,
        )
    ).parsed
