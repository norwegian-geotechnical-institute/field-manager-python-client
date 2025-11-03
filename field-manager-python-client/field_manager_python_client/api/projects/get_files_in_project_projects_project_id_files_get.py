from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.file import File
from ...models.file_extended import FileExtended
from ...models.file_type import FileType
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    *,
    file_types: list[FileType] | Unset = UNSET,
    extended_result: bool | Unset = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_file_types: list[str] | Unset = UNSET
    if not isinstance(file_types, Unset):
        json_file_types = []
        for file_types_item_data in file_types:
            file_types_item = file_types_item_data.value
            json_file_types.append(file_types_item)

    params["file_types"] = json_file_types

    params["extended_result"] = extended_result

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/projects/{project_id}/files",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | list[File | FileExtended] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:

            def _parse_response_200_item(data: object) -> File | FileExtended:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_200_item_type_0 = FileExtended.from_dict(data)

                    return response_200_item_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_item_type_1 = File.from_dict(data)

                return response_200_item_type_1

            response_200_item = _parse_response_200_item(response_200_item_data)

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
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[HTTPValidationError | list[File | FileExtended]]:
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
    file_types: list[FileType] | Unset = UNSET,
    extended_result: bool | Unset = False,
) -> Response[HTTPValidationError | list[File | FileExtended]]:
    """Get Files In Project

     Get all database file objects in a project by project_id and possible filtered by file type.

    Args:
        project_id (str):
        file_types (list[FileType] | Unset):
        extended_result (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[File | FileExtended]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        file_types=file_types,
        extended_result=extended_result,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient,
    file_types: list[FileType] | Unset = UNSET,
    extended_result: bool | Unset = False,
) -> HTTPValidationError | list[File | FileExtended] | None:
    """Get Files In Project

     Get all database file objects in a project by project_id and possible filtered by file type.

    Args:
        project_id (str):
        file_types (list[FileType] | Unset):
        extended_result (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[File | FileExtended]
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        file_types=file_types,
        extended_result=extended_result,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient,
    file_types: list[FileType] | Unset = UNSET,
    extended_result: bool | Unset = False,
) -> Response[HTTPValidationError | list[File | FileExtended]]:
    """Get Files In Project

     Get all database file objects in a project by project_id and possible filtered by file type.

    Args:
        project_id (str):
        file_types (list[FileType] | Unset):
        extended_result (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[File | FileExtended]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        file_types=file_types,
        extended_result=extended_result,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient,
    file_types: list[FileType] | Unset = UNSET,
    extended_result: bool | Unset = False,
) -> HTTPValidationError | list[File | FileExtended] | None:
    """Get Files In Project

     Get all database file objects in a project by project_id and possible filtered by file type.

    Args:
        project_id (str):
        file_types (list[FileType] | Unset):
        extended_result (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[File | FileExtended]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            file_types=file_types,
            extended_result=extended_result,
        )
    ).parsed
