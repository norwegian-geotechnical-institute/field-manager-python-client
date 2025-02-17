from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.like import Like
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    location_id: UUID,
    comment_id: UUID,
    *,
    method_id: Union[None, UUID, Unset] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_method_id: Union[None, Unset, str]
    if isinstance(method_id, Unset):
        json_method_id = UNSET
    elif isinstance(method_id, UUID):
        json_method_id = str(method_id)
    else:
        json_method_id = method_id
    params["method_id"] = json_method_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/projects/{project_id}/locations/{location_id}/comments/{comment_id}/likes",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, Like]]:
    if response.status_code == 201:
        response_201 = Like.from_dict(response.json())

        return response_201
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[HTTPValidationError, Like]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    location_id: UUID,
    comment_id: UUID,
    *,
    client: AuthenticatedClient,
    method_id: Union[None, UUID, Unset] = UNSET,
) -> Response[Union[HTTPValidationError, Like]]:
    """Like Comment

     Like a comment

    Args:
        project_id (str):
        location_id (UUID):
        comment_id (UUID):
        method_id (Union[None, UUID, Unset]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, Like]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        location_id=location_id,
        comment_id=comment_id,
        method_id=method_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    location_id: UUID,
    comment_id: UUID,
    *,
    client: AuthenticatedClient,
    method_id: Union[None, UUID, Unset] = UNSET,
) -> Optional[Union[HTTPValidationError, Like]]:
    """Like Comment

     Like a comment

    Args:
        project_id (str):
        location_id (UUID):
        comment_id (UUID):
        method_id (Union[None, UUID, Unset]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, Like]
    """

    return sync_detailed(
        project_id=project_id,
        location_id=location_id,
        comment_id=comment_id,
        client=client,
        method_id=method_id,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    location_id: UUID,
    comment_id: UUID,
    *,
    client: AuthenticatedClient,
    method_id: Union[None, UUID, Unset] = UNSET,
) -> Response[Union[HTTPValidationError, Like]]:
    """Like Comment

     Like a comment

    Args:
        project_id (str):
        location_id (UUID):
        comment_id (UUID):
        method_id (Union[None, UUID, Unset]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, Like]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        location_id=location_id,
        comment_id=comment_id,
        method_id=method_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    location_id: UUID,
    comment_id: UUID,
    *,
    client: AuthenticatedClient,
    method_id: Union[None, UUID, Unset] = UNSET,
) -> Optional[Union[HTTPValidationError, Like]]:
    """Like Comment

     Like a comment

    Args:
        project_id (str):
        location_id (UUID):
        comment_id (UUID):
        method_id (Union[None, UUID, Unset]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, Like]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            location_id=location_id,
            comment_id=comment_id,
            client=client,
            method_id=method_id,
        )
    ).parsed
