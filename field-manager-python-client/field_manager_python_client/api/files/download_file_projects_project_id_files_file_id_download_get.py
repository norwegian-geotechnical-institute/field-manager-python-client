from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.image_size import ImageSize
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    file_id: UUID,
    *,
    size: Union[ImageSize, None, Unset] = ImageSize.ORIGINAL,
    geojson: Union[None, Unset, bool] = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_size: Union[None, Unset, str]
    if isinstance(size, Unset):
        json_size = UNSET
    elif isinstance(size, ImageSize):
        json_size = size.value
    else:
        json_size = size
    params["size"] = json_size

    json_geojson: Union[None, Unset, bool]
    if isinstance(geojson, Unset):
        json_geojson = UNSET
    else:
        json_geojson = geojson
    params["geojson"] = json_geojson

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/projects/{project_id}/files/{file_id}/download",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError]]:
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
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, HTTPValidationError]]:
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
    size: Union[ImageSize, None, Unset] = ImageSize.ORIGINAL,
    geojson: Union[None, Unset, bool] = False,
) -> Response[Union[Any, HTTPValidationError]]:
    """Download File

     Download the file blob content by project_id and file_id

    Args:
        project_id (str):
        file_id (UUID):
        size (Union[ImageSize, None, Unset]):  Default: ImageSize.ORIGINAL.
        geojson (Union[None, Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        file_id=file_id,
        size=size,
        geojson=geojson,
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
    size: Union[ImageSize, None, Unset] = ImageSize.ORIGINAL,
    geojson: Union[None, Unset, bool] = False,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Download File

     Download the file blob content by project_id and file_id

    Args:
        project_id (str):
        file_id (UUID):
        size (Union[ImageSize, None, Unset]):  Default: ImageSize.ORIGINAL.
        geojson (Union[None, Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return sync_detailed(
        project_id=project_id,
        file_id=file_id,
        client=client,
        size=size,
        geojson=geojson,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    file_id: UUID,
    *,
    client: AuthenticatedClient,
    size: Union[ImageSize, None, Unset] = ImageSize.ORIGINAL,
    geojson: Union[None, Unset, bool] = False,
) -> Response[Union[Any, HTTPValidationError]]:
    """Download File

     Download the file blob content by project_id and file_id

    Args:
        project_id (str):
        file_id (UUID):
        size (Union[ImageSize, None, Unset]):  Default: ImageSize.ORIGINAL.
        geojson (Union[None, Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        file_id=file_id,
        size=size,
        geojson=geojson,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    file_id: UUID,
    *,
    client: AuthenticatedClient,
    size: Union[ImageSize, None, Unset] = ImageSize.ORIGINAL,
    geojson: Union[None, Unset, bool] = False,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Download File

     Download the file blob content by project_id and file_id

    Args:
        project_id (str):
        file_id (UUID):
        size (Union[ImageSize, None, Unset]):  Default: ImageSize.ORIGINAL.
        geojson (Union[None, Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            file_id=file_id,
            client=client,
            size=size,
            geojson=geojson,
        )
    ).parsed
