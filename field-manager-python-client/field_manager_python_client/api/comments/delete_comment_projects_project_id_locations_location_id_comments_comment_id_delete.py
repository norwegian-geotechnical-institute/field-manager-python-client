from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.comment import Comment
from ...models.http_validation_error import HTTPValidationError
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
        "method": "delete",
        "url": f"/projects/{project_id}/locations/{location_id}/comments/{comment_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Comment, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = Comment.from_dict(response.json())

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
) -> Response[Union[Comment, HTTPValidationError]]:
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
) -> Response[Union[Comment, HTTPValidationError]]:
    """Delete Comment

     Soft delete comment by setting is_deleted true
    Only the comment creator and project admins are allowed to delete comments

    Args:
        project_id (str):
        location_id (UUID):
        comment_id (UUID):
        method_id (Union[None, UUID, Unset]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Comment, HTTPValidationError]]
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
) -> Optional[Union[Comment, HTTPValidationError]]:
    """Delete Comment

     Soft delete comment by setting is_deleted true
    Only the comment creator and project admins are allowed to delete comments

    Args:
        project_id (str):
        location_id (UUID):
        comment_id (UUID):
        method_id (Union[None, UUID, Unset]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Comment, HTTPValidationError]
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
) -> Response[Union[Comment, HTTPValidationError]]:
    """Delete Comment

     Soft delete comment by setting is_deleted true
    Only the comment creator and project admins are allowed to delete comments

    Args:
        project_id (str):
        location_id (UUID):
        comment_id (UUID):
        method_id (Union[None, UUID, Unset]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Comment, HTTPValidationError]]
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
) -> Optional[Union[Comment, HTTPValidationError]]:
    """Delete Comment

     Soft delete comment by setting is_deleted true
    Only the comment creator and project admins are allowed to delete comments

    Args:
        project_id (str):
        location_id (UUID):
        comment_id (UUID):
        method_id (Union[None, UUID, Unset]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Comment, HTTPValidationError]
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
