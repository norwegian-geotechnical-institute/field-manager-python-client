from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_upload_locations_to_project_projects_project_id_locations_upload_post import (
    BodyUploadLocationsToProjectProjectsProjectIdLocationsUploadPost,
)
from ...models.http_validation_error import HTTPValidationError
from ...models.location import Location
from ...models.location_type_enum import LocationTypeEnum
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    *,
    body: BodyUploadLocationsToProjectProjectsProjectIdLocationsUploadPost,
    srid: Union[None, Unset, int] = UNSET,
    swap_x_y: Union[None, Unset, bool] = False,
    location_type_id: Union[Unset, LocationTypeEnum] = UNSET,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    params: Dict[str, Any] = {}

    json_srid: Union[None, Unset, int]
    if isinstance(srid, Unset):
        json_srid = UNSET
    else:
        json_srid = srid
    params["srid"] = json_srid

    json_swap_x_y: Union[None, Unset, bool]
    if isinstance(swap_x_y, Unset):
        json_swap_x_y = UNSET
    else:
        json_swap_x_y = swap_x_y
    params["swap_x_y"] = json_swap_x_y

    json_location_type_id: Union[Unset, int] = UNSET
    if not isinstance(location_type_id, Unset):
        json_location_type_id = location_type_id.value

    params["location_type_id"] = json_location_type_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/projects/{project_id}/locations/upload",
        "params": params,
    }

    _body = body.to_multipart()

    _kwargs["files"] = _body

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, List["Location"]]]:
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
) -> Response[Union[HTTPValidationError, List["Location"]]]:
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
    body: BodyUploadLocationsToProjectProjectsProjectIdLocationsUploadPost,
    srid: Union[None, Unset, int] = UNSET,
    swap_x_y: Union[None, Unset, bool] = False,
    location_type_id: Union[Unset, LocationTypeEnum] = UNSET,
) -> Response[Union[HTTPValidationError, List["Location"]]]:
    """Upload Locations To Project

     Upload locations from a file.

    Supported file extensions are: .ags, .csv, .gvr, .kof, .prv, .snd, .vb, .xlsx, .xls and image files.

    Please do not call this endpoint in parallel, since it is very resource intensive and will affect
    other users of
    the system.

    Args:
        project_id (str):
        srid (Union[None, Unset, int]):
        swap_x_y (Union[None, Unset, bool]):  Default: False.
        location_type_id (Union[Unset, LocationTypeEnum]): (
            ONSHORE=1,
            OFFSHORE=2,
            )
        body (BodyUploadLocationsToProjectProjectsProjectIdLocationsUploadPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, List['Location']]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
        srid=srid,
        swap_x_y=swap_x_y,
        location_type_id=location_type_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient,
    body: BodyUploadLocationsToProjectProjectsProjectIdLocationsUploadPost,
    srid: Union[None, Unset, int] = UNSET,
    swap_x_y: Union[None, Unset, bool] = False,
    location_type_id: Union[Unset, LocationTypeEnum] = UNSET,
) -> Optional[Union[HTTPValidationError, List["Location"]]]:
    """Upload Locations To Project

     Upload locations from a file.

    Supported file extensions are: .ags, .csv, .gvr, .kof, .prv, .snd, .vb, .xlsx, .xls and image files.

    Please do not call this endpoint in parallel, since it is very resource intensive and will affect
    other users of
    the system.

    Args:
        project_id (str):
        srid (Union[None, Unset, int]):
        swap_x_y (Union[None, Unset, bool]):  Default: False.
        location_type_id (Union[Unset, LocationTypeEnum]): (
            ONSHORE=1,
            OFFSHORE=2,
            )
        body (BodyUploadLocationsToProjectProjectsProjectIdLocationsUploadPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, List['Location']]
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        body=body,
        srid=srid,
        swap_x_y=swap_x_y,
        location_type_id=location_type_id,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient,
    body: BodyUploadLocationsToProjectProjectsProjectIdLocationsUploadPost,
    srid: Union[None, Unset, int] = UNSET,
    swap_x_y: Union[None, Unset, bool] = False,
    location_type_id: Union[Unset, LocationTypeEnum] = UNSET,
) -> Response[Union[HTTPValidationError, List["Location"]]]:
    """Upload Locations To Project

     Upload locations from a file.

    Supported file extensions are: .ags, .csv, .gvr, .kof, .prv, .snd, .vb, .xlsx, .xls and image files.

    Please do not call this endpoint in parallel, since it is very resource intensive and will affect
    other users of
    the system.

    Args:
        project_id (str):
        srid (Union[None, Unset, int]):
        swap_x_y (Union[None, Unset, bool]):  Default: False.
        location_type_id (Union[Unset, LocationTypeEnum]): (
            ONSHORE=1,
            OFFSHORE=2,
            )
        body (BodyUploadLocationsToProjectProjectsProjectIdLocationsUploadPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, List['Location']]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
        srid=srid,
        swap_x_y=swap_x_y,
        location_type_id=location_type_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient,
    body: BodyUploadLocationsToProjectProjectsProjectIdLocationsUploadPost,
    srid: Union[None, Unset, int] = UNSET,
    swap_x_y: Union[None, Unset, bool] = False,
    location_type_id: Union[Unset, LocationTypeEnum] = UNSET,
) -> Optional[Union[HTTPValidationError, List["Location"]]]:
    """Upload Locations To Project

     Upload locations from a file.

    Supported file extensions are: .ags, .csv, .gvr, .kof, .prv, .snd, .vb, .xlsx, .xls and image files.

    Please do not call this endpoint in parallel, since it is very resource intensive and will affect
    other users of
    the system.

    Args:
        project_id (str):
        srid (Union[None, Unset, int]):
        swap_x_y (Union[None, Unset, bool]):  Default: False.
        location_type_id (Union[Unset, LocationTypeEnum]): (
            ONSHORE=1,
            OFFSHORE=2,
            )
        body (BodyUploadLocationsToProjectProjectsProjectIdLocationsUploadPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, List['Location']]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            body=body,
            srid=srid,
            swap_x_y=swap_x_y,
            location_type_id=location_type_id,
        )
    ).parsed
