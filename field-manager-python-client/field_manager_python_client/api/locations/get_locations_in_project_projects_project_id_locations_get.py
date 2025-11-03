from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.location import Location
from ...models.method_type_enum import MethodTypeEnum
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    *,
    skip: int | Unset = 0,
    limit: int | Unset = 100,
    deleted: bool | Unset = False,
    tags: list[str] | Unset = UNSET,
    method_types: list[MethodTypeEnum] | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["skip"] = skip

    params["limit"] = limit

    params["deleted"] = deleted

    json_tags: list[str] | Unset = UNSET
    if not isinstance(tags, Unset):
        json_tags = tags

    params["tags"] = json_tags

    json_method_types: list[int] | Unset = UNSET
    if not isinstance(method_types, Unset):
        json_method_types = []
        for method_types_item_data in method_types:
            method_types_item = method_types_item_data.value
            json_method_types.append(method_types_item)

    params["method_types"] = json_method_types

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/projects/{project_id}/locations",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | list[Location] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Location.from_dict(response_200_item_data)

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
) -> Response[HTTPValidationError | list[Location]]:
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
    skip: int | Unset = 0,
    limit: int | Unset = 100,
    deleted: bool | Unset = False,
    tags: list[str] | Unset = UNSET,
    method_types: list[MethodTypeEnum] | Unset = UNSET,
) -> Response[HTTPValidationError | list[Location]]:
    """Get Locations In Project

     Return all locations in project.

    It is possible to filter on tags (only return locations with any of the passed tags).
    If no tags are specified, all locations are returned.

    If method_types are specified, only locations with methods of the specified types are returned.

    Args:
        project_id (str):
        skip (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 100.
        deleted (bool | Unset):  Default: False.
        tags (list[str] | Unset):
        method_types (list[MethodTypeEnum] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[Location]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        skip=skip,
        limit=limit,
        deleted=deleted,
        tags=tags,
        method_types=method_types,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient,
    skip: int | Unset = 0,
    limit: int | Unset = 100,
    deleted: bool | Unset = False,
    tags: list[str] | Unset = UNSET,
    method_types: list[MethodTypeEnum] | Unset = UNSET,
) -> HTTPValidationError | list[Location] | None:
    """Get Locations In Project

     Return all locations in project.

    It is possible to filter on tags (only return locations with any of the passed tags).
    If no tags are specified, all locations are returned.

    If method_types are specified, only locations with methods of the specified types are returned.

    Args:
        project_id (str):
        skip (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 100.
        deleted (bool | Unset):  Default: False.
        tags (list[str] | Unset):
        method_types (list[MethodTypeEnum] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[Location]
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        skip=skip,
        limit=limit,
        deleted=deleted,
        tags=tags,
        method_types=method_types,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient,
    skip: int | Unset = 0,
    limit: int | Unset = 100,
    deleted: bool | Unset = False,
    tags: list[str] | Unset = UNSET,
    method_types: list[MethodTypeEnum] | Unset = UNSET,
) -> Response[HTTPValidationError | list[Location]]:
    """Get Locations In Project

     Return all locations in project.

    It is possible to filter on tags (only return locations with any of the passed tags).
    If no tags are specified, all locations are returned.

    If method_types are specified, only locations with methods of the specified types are returned.

    Args:
        project_id (str):
        skip (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 100.
        deleted (bool | Unset):  Default: False.
        tags (list[str] | Unset):
        method_types (list[MethodTypeEnum] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[Location]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        skip=skip,
        limit=limit,
        deleted=deleted,
        tags=tags,
        method_types=method_types,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient,
    skip: int | Unset = 0,
    limit: int | Unset = 100,
    deleted: bool | Unset = False,
    tags: list[str] | Unset = UNSET,
    method_types: list[MethodTypeEnum] | Unset = UNSET,
) -> HTTPValidationError | list[Location] | None:
    """Get Locations In Project

     Return all locations in project.

    It is possible to filter on tags (only return locations with any of the passed tags).
    If no tags are specified, all locations are returned.

    If method_types are specified, only locations with methods of the specified types are returned.

    Args:
        project_id (str):
        skip (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 100.
        deleted (bool | Unset):  Default: False.
        tags (list[str] | Unset):
        method_types (list[MethodTypeEnum] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[Location]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            skip=skip,
            limit=limit,
            deleted=deleted,
            tags=tags,
            method_types=method_types,
        )
    ).parsed
