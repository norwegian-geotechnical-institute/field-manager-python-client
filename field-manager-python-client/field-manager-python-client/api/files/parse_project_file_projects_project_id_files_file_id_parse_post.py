from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.location import Location
from ...models.location_type_enum import LocationTypeEnum
from ...types import UNSET, Unset
from typing import cast
from typing import cast, List
from typing import cast, Union
from typing import Dict
from typing import Union
from uuid import UUID



def _get_kwargs(
    project_id: str,
    file_id: UUID,
    *,
    srid: Union[None, Unset, int] = UNSET,
    swap_x_y: Union[Unset, bool] = False,
    location_type_id: Union[LocationTypeEnum, None, Unset] = LocationTypeEnum.VALUE_1,

) -> Dict[str, Any]:
    

    

    params: Dict[str, Any] = {}

    json_srid: Union[None, Unset, int]
    if isinstance(srid, Unset):
        json_srid = UNSET
    else:
        json_srid = srid
    params["srid"] = json_srid

    params["swap_x_y"] = swap_x_y

    json_location_type_id: Union[None, Unset, int]
    if isinstance(location_type_id, Unset):
        json_location_type_id = UNSET
    elif isinstance(location_type_id, LocationTypeEnum):
        json_location_type_id = location_type_id.value
    else:
        json_location_type_id = location_type_id
    params["location_type_id"] = json_location_type_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/projects/{project_id}/files/{file_id}/parse".format(project_id=project_id,file_id=file_id,),
        "params": params,
    }


    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[HTTPValidationError, List['Location']]]:
    if response.status_code == 201:
        response_201 = []
        _response_201 = response.json()
        for response_201_item_data in (_response_201):
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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[HTTPValidationError, List['Location']]]:
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
    location_type_id: Union[LocationTypeEnum, None, Unset] = LocationTypeEnum.VALUE_1,

) -> Response[Union[HTTPValidationError, List['Location']]]:
    """ Parse Project File

     Parse an already queued location file.

    Args:
        project_id (str):
        file_id (UUID):
        srid (Union[None, Unset, int]):
        swap_x_y (Union[Unset, bool]):  Default: False.
        location_type_id (Union[LocationTypeEnum, None, Unset]): Use Project.standard_id instead
            Default: LocationTypeEnum.VALUE_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, List['Location']]]
     """


    kwargs = _get_kwargs(
        project_id=project_id,
file_id=file_id,
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
    file_id: UUID,
    *,
    client: AuthenticatedClient,
    srid: Union[None, Unset, int] = UNSET,
    swap_x_y: Union[Unset, bool] = False,
    location_type_id: Union[LocationTypeEnum, None, Unset] = LocationTypeEnum.VALUE_1,

) -> Optional[Union[HTTPValidationError, List['Location']]]:
    """ Parse Project File

     Parse an already queued location file.

    Args:
        project_id (str):
        file_id (UUID):
        srid (Union[None, Unset, int]):
        swap_x_y (Union[Unset, bool]):  Default: False.
        location_type_id (Union[LocationTypeEnum, None, Unset]): Use Project.standard_id instead
            Default: LocationTypeEnum.VALUE_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, List['Location']]
     """


    return sync_detailed(
        project_id=project_id,
file_id=file_id,
client=client,
srid=srid,
swap_x_y=swap_x_y,
location_type_id=location_type_id,

    ).parsed

async def asyncio_detailed(
    project_id: str,
    file_id: UUID,
    *,
    client: AuthenticatedClient,
    srid: Union[None, Unset, int] = UNSET,
    swap_x_y: Union[Unset, bool] = False,
    location_type_id: Union[LocationTypeEnum, None, Unset] = LocationTypeEnum.VALUE_1,

) -> Response[Union[HTTPValidationError, List['Location']]]:
    """ Parse Project File

     Parse an already queued location file.

    Args:
        project_id (str):
        file_id (UUID):
        srid (Union[None, Unset, int]):
        swap_x_y (Union[Unset, bool]):  Default: False.
        location_type_id (Union[LocationTypeEnum, None, Unset]): Use Project.standard_id instead
            Default: LocationTypeEnum.VALUE_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, List['Location']]]
     """


    kwargs = _get_kwargs(
        project_id=project_id,
file_id=file_id,
srid=srid,
swap_x_y=swap_x_y,
location_type_id=location_type_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    project_id: str,
    file_id: UUID,
    *,
    client: AuthenticatedClient,
    srid: Union[None, Unset, int] = UNSET,
    swap_x_y: Union[Unset, bool] = False,
    location_type_id: Union[LocationTypeEnum, None, Unset] = LocationTypeEnum.VALUE_1,

) -> Optional[Union[HTTPValidationError, List['Location']]]:
    """ Parse Project File

     Parse an already queued location file.

    Args:
        project_id (str):
        file_id (UUID):
        srid (Union[None, Unset, int]):
        swap_x_y (Union[Unset, bool]):  Default: False.
        location_type_id (Union[LocationTypeEnum, None, Unset]): Use Project.standard_id instead
            Default: LocationTypeEnum.VALUE_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, List['Location']]
     """


    return (await asyncio_detailed(
        project_id=project_id,
file_id=file_id,
client=client,
srid=srid,
swap_x_y=swap_x_y,
location_type_id=location_type_id,

    )).parsed
