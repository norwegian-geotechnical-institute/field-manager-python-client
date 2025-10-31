from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.file import File
from ...models.file_type import FileType
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: str,
    *,
    file_types: list[FileType] | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_file_types: list[str] | Unset = UNSET
    if not isinstance(file_types, Unset):
        json_file_types = []
        for file_types_item_data in file_types:
            file_types_item = file_types_item_data.value
            json_file_types.append(file_types_item)

    params["file_types"] = json_file_types

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/organizations/{organization_id}/files",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | list[File] | None:
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
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[HTTPValidationError | list[File]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organization_id: str,
    *,
    client: AuthenticatedClient,
    file_types: list[FileType] | Unset = UNSET,
) -> Response[HTTPValidationError | list[File]]:
    """Get Files In Organization

     Get all database file objects that are directly attached to the specified organization with
    organization_id and
    possible filtered by file types.

    Please note that you will not get files that is only attached to an underlying Project, Location or
    Method in
    the Organization.

    Args:
        organization_id (str):
        file_types (list[FileType] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[File]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        file_types=file_types,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: str,
    *,
    client: AuthenticatedClient,
    file_types: list[FileType] | Unset = UNSET,
) -> HTTPValidationError | list[File] | None:
    """Get Files In Organization

     Get all database file objects that are directly attached to the specified organization with
    organization_id and
    possible filtered by file types.

    Please note that you will not get files that is only attached to an underlying Project, Location or
    Method in
    the Organization.

    Args:
        organization_id (str):
        file_types (list[FileType] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[File]
    """

    return sync_detailed(
        organization_id=organization_id,
        client=client,
        file_types=file_types,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    *,
    client: AuthenticatedClient,
    file_types: list[FileType] | Unset = UNSET,
) -> Response[HTTPValidationError | list[File]]:
    """Get Files In Organization

     Get all database file objects that are directly attached to the specified organization with
    organization_id and
    possible filtered by file types.

    Please note that you will not get files that is only attached to an underlying Project, Location or
    Method in
    the Organization.

    Args:
        organization_id (str):
        file_types (list[FileType] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[File]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        file_types=file_types,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: str,
    *,
    client: AuthenticatedClient,
    file_types: list[FileType] | Unset = UNSET,
) -> HTTPValidationError | list[File] | None:
    """Get Files In Organization

     Get all database file objects that are directly attached to the specified organization with
    organization_id and
    possible filtered by file types.

    Please note that you will not get files that is only attached to an underlying Project, Location or
    Method in
    the Organization.

    Args:
        organization_id (str):
        file_types (list[FileType] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[File]
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            client=client,
            file_types=file_types,
        )
    ).parsed
