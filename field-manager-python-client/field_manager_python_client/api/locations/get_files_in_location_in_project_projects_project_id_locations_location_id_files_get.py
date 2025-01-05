from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.file import File
from ...models.file_type import FileType
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    location_id: UUID,
    *,
    file_type: Union[FileType, None, Unset] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_file_type: Union[None, Unset, str]
    if isinstance(file_type, Unset):
        json_file_type = UNSET
    elif isinstance(file_type, FileType):
        json_file_type = file_type.value
    else:
        json_file_type = file_type
    params["file_type"] = json_file_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/projects/{project_id}/locations/{location_id}/files",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, list["File"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = File.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[Union[HTTPValidationError, list["File"]]]:
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
    file_type: Union[FileType, None, Unset] = UNSET,
) -> Response[Union[HTTPValidationError, list["File"]]]:
    """Get Files In Location In Project

     Return database file objects for a specific location and optional file type

    Args:
        project_id (str):
        location_id (UUID):
        file_type (Union[FileType, None, Unset]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, list['File']]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        location_id=location_id,
        file_type=file_type,
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
    file_type: Union[FileType, None, Unset] = UNSET,
) -> Optional[Union[HTTPValidationError, list["File"]]]:
    """Get Files In Location In Project

     Return database file objects for a specific location and optional file type

    Args:
        project_id (str):
        location_id (UUID):
        file_type (Union[FileType, None, Unset]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, list['File']]
    """

    return sync_detailed(
        project_id=project_id,
        location_id=location_id,
        client=client,
        file_type=file_type,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    location_id: UUID,
    *,
    client: AuthenticatedClient,
    file_type: Union[FileType, None, Unset] = UNSET,
) -> Response[Union[HTTPValidationError, list["File"]]]:
    """Get Files In Location In Project

     Return database file objects for a specific location and optional file type

    Args:
        project_id (str):
        location_id (UUID):
        file_type (Union[FileType, None, Unset]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, list['File']]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        location_id=location_id,
        file_type=file_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    location_id: UUID,
    *,
    client: AuthenticatedClient,
    file_type: Union[FileType, None, Unset] = UNSET,
) -> Optional[Union[HTTPValidationError, list["File"]]]:
    """Get Files In Location In Project

     Return database file objects for a specific location and optional file type

    Args:
        project_id (str):
        location_id (UUID):
        file_type (Union[FileType, None, Unset]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, list['File']]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            location_id=location_id,
            client=client,
            file_type=file_type,
        )
    ).parsed
