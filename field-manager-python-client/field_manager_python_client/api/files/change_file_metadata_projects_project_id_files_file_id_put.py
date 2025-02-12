from http import HTTPStatus
from typing import Any, Dict, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.file import File
from ...models.file_update import FileUpdate
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    project_id: str,
    file_id: UUID,
    *,
    body: FileUpdate,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/projects/{project_id}/files/{file_id}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[File, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = File.from_dict(response.json())

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
) -> Response[Union[File, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    file_id: UUID,
    *,
    client: AuthenticatedClient,
    body: FileUpdate,
) -> Response[Union[File, HTTPValidationError]]:
    """Change File Metadata

     Update the file metadata by project_id and file_id

    Args:
        project_id (str):
        file_id (UUID):
        body (FileUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[File, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        file_id=file_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    file_id: UUID,
    *,
    client: AuthenticatedClient,
    body: FileUpdate,
) -> Optional[Union[File, HTTPValidationError]]:
    """Change File Metadata

     Update the file metadata by project_id and file_id

    Args:
        project_id (str):
        file_id (UUID):
        body (FileUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[File, HTTPValidationError]
    """

    return sync_detailed(
        project_id=project_id,
        file_id=file_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    file_id: UUID,
    *,
    client: AuthenticatedClient,
    body: FileUpdate,
) -> Response[Union[File, HTTPValidationError]]:
    """Change File Metadata

     Update the file metadata by project_id and file_id

    Args:
        project_id (str):
        file_id (UUID):
        body (FileUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[File, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        file_id=file_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    file_id: UUID,
    *,
    client: AuthenticatedClient,
    body: FileUpdate,
) -> Optional[Union[File, HTTPValidationError]]:
    """Change File Metadata

     Update the file metadata by project_id and file_id

    Args:
        project_id (str):
        file_id (UUID):
        body (FileUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[File, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            file_id=file_id,
            client=client,
            body=body,
        )
    ).parsed
