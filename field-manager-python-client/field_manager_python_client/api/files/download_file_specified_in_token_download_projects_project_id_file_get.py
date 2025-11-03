from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.image_size import ImageSize
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: UUID,
    *,
    token: str,
    size: ImageSize | None | Unset = ImageSize.ORIGINAL,
    geojson: bool | None | Unset = False,
    as_attachment: bool | None | Unset = True,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["token"] = token

    json_size: None | str | Unset
    if isinstance(size, Unset):
        json_size = UNSET
    elif isinstance(size, ImageSize):
        json_size = size.value
    else:
        json_size = size
    params["size"] = json_size

    json_geojson: bool | None | Unset
    if isinstance(geojson, Unset):
        json_geojson = UNSET
    else:
        json_geojson = geojson
    params["geojson"] = json_geojson

    json_as_attachment: bool | None | Unset
    if isinstance(as_attachment, Unset):
        json_as_attachment = UNSET
    else:
        json_as_attachment = as_attachment
    params["as_attachment"] = json_as_attachment

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/download/projects/{project_id}/file",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | None:
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
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    token: str,
    size: ImageSize | None | Unset = ImageSize.ORIGINAL,
    geojson: bool | None | Unset = False,
    as_attachment: bool | None | Unset = True,
) -> Response[Any | HTTPValidationError]:
    """Download File Specified In Token

     Download the file specified in the token

    Args:
        project_id (UUID):
        token (str):
        size (ImageSize | None | Unset):  Default: ImageSize.ORIGINAL.
        geojson (bool | None | Unset):  Default: False.
        as_attachment (bool | None | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        token=token,
        size=size,
        geojson=geojson,
        as_attachment=as_attachment,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    token: str,
    size: ImageSize | None | Unset = ImageSize.ORIGINAL,
    geojson: bool | None | Unset = False,
    as_attachment: bool | None | Unset = True,
) -> Any | HTTPValidationError | None:
    """Download File Specified In Token

     Download the file specified in the token

    Args:
        project_id (UUID):
        token (str):
        size (ImageSize | None | Unset):  Default: ImageSize.ORIGINAL.
        geojson (bool | None | Unset):  Default: False.
        as_attachment (bool | None | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        token=token,
        size=size,
        geojson=geojson,
        as_attachment=as_attachment,
    ).parsed


async def asyncio_detailed(
    project_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    token: str,
    size: ImageSize | None | Unset = ImageSize.ORIGINAL,
    geojson: bool | None | Unset = False,
    as_attachment: bool | None | Unset = True,
) -> Response[Any | HTTPValidationError]:
    """Download File Specified In Token

     Download the file specified in the token

    Args:
        project_id (UUID):
        token (str):
        size (ImageSize | None | Unset):  Default: ImageSize.ORIGINAL.
        geojson (bool | None | Unset):  Default: False.
        as_attachment (bool | None | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        token=token,
        size=size,
        geojson=geojson,
        as_attachment=as_attachment,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    token: str,
    size: ImageSize | None | Unset = ImageSize.ORIGINAL,
    geojson: bool | None | Unset = False,
    as_attachment: bool | None | Unset = True,
) -> Any | HTTPValidationError | None:
    """Download File Specified In Token

     Download the file specified in the token

    Args:
        project_id (UUID):
        token (str):
        size (ImageSize | None | Unset):  Default: ImageSize.ORIGINAL.
        geojson (bool | None | Unset):  Default: False.
        as_attachment (bool | None | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            token=token,
            size=size,
            geojson=geojson,
            as_attachment=as_attachment,
        )
    ).parsed
