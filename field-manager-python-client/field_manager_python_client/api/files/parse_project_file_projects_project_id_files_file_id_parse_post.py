from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.location import Location
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    file_id: UUID,
    *,
    srid: Union[None, Unset, int] = UNSET,
    swap_x_y: Union[Unset, bool] = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_srid: Union[None, Unset, int]
    if isinstance(srid, Unset):
        json_srid = UNSET
    else:
        json_srid = srid
    params["srid"] = json_srid

    params["swap_x_y"] = swap_x_y

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/projects/{project_id}/files/{file_id}/parse",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, list["Location"]]]:
    if response.status_code == 201:
        response_201 = []
        _response_201 = response.json()
        for response_201_item_data in _response_201:
            response_201_item = Location.from_dict(response_201_item_data)

            response_201.append(response_201_item)

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
) -> Response[Union[HTTPValidationError, list["Location"]]]:
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
    srid: Union[None, Unset, int] = UNSET,
    swap_x_y: Union[Unset, bool] = False,
) -> Response[Union[HTTPValidationError, list["Location"]]]:
    """Parse Project File

     Parse an already queued location file.

    Args:
        project_id (str):
        file_id (UUID):
        srid (Union[None, Unset, int]):
        swap_x_y (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, list['Location']]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        file_id=file_id,
        srid=srid,
        swap_x_y=swap_x_y,
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
    srid: Union[None, Unset, int] = UNSET,
    swap_x_y: Union[Unset, bool] = False,
) -> Optional[Union[HTTPValidationError, list["Location"]]]:
    """Parse Project File

     Parse an already queued location file.

    Args:
        project_id (str):
        file_id (UUID):
        srid (Union[None, Unset, int]):
        swap_x_y (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, list['Location']]
    """

    return sync_detailed(
        project_id=project_id,
        file_id=file_id,
        client=client,
        srid=srid,
        swap_x_y=swap_x_y,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    file_id: UUID,
    *,
    client: AuthenticatedClient,
    srid: Union[None, Unset, int] = UNSET,
    swap_x_y: Union[Unset, bool] = False,
) -> Response[Union[HTTPValidationError, list["Location"]]]:
    """Parse Project File

     Parse an already queued location file.

    Args:
        project_id (str):
        file_id (UUID):
        srid (Union[None, Unset, int]):
        swap_x_y (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, list['Location']]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        file_id=file_id,
        srid=srid,
        swap_x_y=swap_x_y,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    file_id: UUID,
    *,
    client: AuthenticatedClient,
    srid: Union[None, Unset, int] = UNSET,
    swap_x_y: Union[Unset, bool] = False,
) -> Optional[Union[HTTPValidationError, list["Location"]]]:
    """Parse Project File

     Parse an already queued location file.

    Args:
        project_id (str):
        file_id (UUID):
        srid (Union[None, Unset, int]):
        swap_x_y (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, list['Location']]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            file_id=file_id,
            client=client,
            srid=srid,
            swap_x_y=swap_x_y,
        )
    ).parsed
