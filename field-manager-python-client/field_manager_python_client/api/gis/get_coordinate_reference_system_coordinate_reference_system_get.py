from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.crs_info import CRSInfo
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    srid: int | None | Unset = UNSET,
    name: None | str | Unset = UNSET,
    vertical: bool | None | Unset = False,
    skip: int | Unset = 0,
    limit: int | Unset = 100,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_srid: int | None | Unset
    if isinstance(srid, Unset):
        json_srid = UNSET
    else:
        json_srid = srid
    params["srid"] = json_srid

    json_name: None | str | Unset
    if isinstance(name, Unset):
        json_name = UNSET
    else:
        json_name = name
    params["name"] = json_name

    json_vertical: bool | None | Unset
    if isinstance(vertical, Unset):
        json_vertical = UNSET
    else:
        json_vertical = vertical
    params["vertical"] = json_vertical

    params["skip"] = skip

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/coordinate_reference_system",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | list[CRSInfo] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = CRSInfo.from_dict(response_200_item_data)

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
) -> Response[HTTPValidationError | list[CRSInfo]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    srid: int | None | Unset = UNSET,
    name: None | str | Unset = UNSET,
    vertical: bool | None | Unset = False,
    skip: int | Unset = 0,
    limit: int | Unset = 100,
) -> Response[HTTPValidationError | list[CRSInfo]]:
    """Get Coordinate Reference System

     Special endpoint for getting information about a Coordinate Reference System (CRS) by its SRID or
    name.

    Either `srid` or `name` must be provided, but not both.

    Submitting a srid will do an exact match, while submitting a name will do a partial match.

    The `vertical` parameter specify if you are searching for vertical coordinate reference systems or
    not.

    Results can be paginated using the `skip` and `limit` query parameters.

    Args:
        srid (int | None | Unset): The SRID (EPSG code) of the coordinate reference system to look
            up
        name (None | str | Unset): The name (or part of the name) of the coordinate reference
            system to look up
        vertical (bool | None | Unset): Whether to search for vertical coordinate reference
            systems Default: False.
        skip (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[CRSInfo]]
    """

    kwargs = _get_kwargs(
        srid=srid,
        name=name,
        vertical=vertical,
        skip=skip,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    srid: int | None | Unset = UNSET,
    name: None | str | Unset = UNSET,
    vertical: bool | None | Unset = False,
    skip: int | Unset = 0,
    limit: int | Unset = 100,
) -> HTTPValidationError | list[CRSInfo] | None:
    """Get Coordinate Reference System

     Special endpoint for getting information about a Coordinate Reference System (CRS) by its SRID or
    name.

    Either `srid` or `name` must be provided, but not both.

    Submitting a srid will do an exact match, while submitting a name will do a partial match.

    The `vertical` parameter specify if you are searching for vertical coordinate reference systems or
    not.

    Results can be paginated using the `skip` and `limit` query parameters.

    Args:
        srid (int | None | Unset): The SRID (EPSG code) of the coordinate reference system to look
            up
        name (None | str | Unset): The name (or part of the name) of the coordinate reference
            system to look up
        vertical (bool | None | Unset): Whether to search for vertical coordinate reference
            systems Default: False.
        skip (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[CRSInfo]
    """

    return sync_detailed(
        client=client,
        srid=srid,
        name=name,
        vertical=vertical,
        skip=skip,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    srid: int | None | Unset = UNSET,
    name: None | str | Unset = UNSET,
    vertical: bool | None | Unset = False,
    skip: int | Unset = 0,
    limit: int | Unset = 100,
) -> Response[HTTPValidationError | list[CRSInfo]]:
    """Get Coordinate Reference System

     Special endpoint for getting information about a Coordinate Reference System (CRS) by its SRID or
    name.

    Either `srid` or `name` must be provided, but not both.

    Submitting a srid will do an exact match, while submitting a name will do a partial match.

    The `vertical` parameter specify if you are searching for vertical coordinate reference systems or
    not.

    Results can be paginated using the `skip` and `limit` query parameters.

    Args:
        srid (int | None | Unset): The SRID (EPSG code) of the coordinate reference system to look
            up
        name (None | str | Unset): The name (or part of the name) of the coordinate reference
            system to look up
        vertical (bool | None | Unset): Whether to search for vertical coordinate reference
            systems Default: False.
        skip (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[CRSInfo]]
    """

    kwargs = _get_kwargs(
        srid=srid,
        name=name,
        vertical=vertical,
        skip=skip,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    srid: int | None | Unset = UNSET,
    name: None | str | Unset = UNSET,
    vertical: bool | None | Unset = False,
    skip: int | Unset = 0,
    limit: int | Unset = 100,
) -> HTTPValidationError | list[CRSInfo] | None:
    """Get Coordinate Reference System

     Special endpoint for getting information about a Coordinate Reference System (CRS) by its SRID or
    name.

    Either `srid` or `name` must be provided, but not both.

    Submitting a srid will do an exact match, while submitting a name will do a partial match.

    The `vertical` parameter specify if you are searching for vertical coordinate reference systems or
    not.

    Results can be paginated using the `skip` and `limit` query parameters.

    Args:
        srid (int | None | Unset): The SRID (EPSG code) of the coordinate reference system to look
            up
        name (None | str | Unset): The name (or part of the name) of the coordinate reference
            system to look up
        vertical (bool | None | Unset): Whether to search for vertical coordinate reference
            systems Default: False.
        skip (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[CRSInfo]
    """

    return (
        await asyncio_detailed(
            client=client,
            srid=srid,
            name=name,
            vertical=vertical,
            skip=skip,
            limit=limit,
        )
    ).parsed
