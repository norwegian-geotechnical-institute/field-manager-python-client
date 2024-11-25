from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.location_gis import LocationGis
from ...types import UNSET, Unset
from typing import cast
from typing import cast, List
from typing import Dict
from typing import Union



def _get_kwargs(
    project_id: str,
    *,
    skip: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 100,

) -> Dict[str, Any]:
    

    

    params: Dict[str, Any] = {}

    params["skip"] = skip

    params["limit"] = limit


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/projects/{project_id}/gis/onshore".format(project_id=project_id,),
        "params": params,
    }


    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[HTTPValidationError, List['LocationGis']]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = LocationGis.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[HTTPValidationError, List['LocationGis']]]:
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
    skip: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 100,

) -> Response[Union[HTTPValidationError, List['LocationGis']]]:
    """ Get Locations In Project

     Special endpoint for getting a project's locations flattened with limited aggregated method data.
    One row per
    location.

    Args:
        project_id (str):
        skip (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, List['LocationGis']]]
     """


    kwargs = _get_kwargs(
        project_id=project_id,
skip=skip,
limit=limit,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    project_id: str,
    *,
    client: AuthenticatedClient,
    skip: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 100,

) -> Optional[Union[HTTPValidationError, List['LocationGis']]]:
    """ Get Locations In Project

     Special endpoint for getting a project's locations flattened with limited aggregated method data.
    One row per
    location.

    Args:
        project_id (str):
        skip (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, List['LocationGis']]
     """


    return sync_detailed(
        project_id=project_id,
client=client,
skip=skip,
limit=limit,

    ).parsed

async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient,
    skip: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 100,

) -> Response[Union[HTTPValidationError, List['LocationGis']]]:
    """ Get Locations In Project

     Special endpoint for getting a project's locations flattened with limited aggregated method data.
    One row per
    location.

    Args:
        project_id (str):
        skip (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, List['LocationGis']]]
     """


    kwargs = _get_kwargs(
        project_id=project_id,
skip=skip,
limit=limit,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient,
    skip: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 100,

) -> Optional[Union[HTTPValidationError, List['LocationGis']]]:
    """ Get Locations In Project

     Special endpoint for getting a project's locations flattened with limited aggregated method data.
    One row per
    location.

    Args:
        project_id (str):
        skip (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, List['LocationGis']]
     """


    return (await asyncio_detailed(
        project_id=project_id,
client=client,
skip=skip,
limit=limit,

    )).parsed
