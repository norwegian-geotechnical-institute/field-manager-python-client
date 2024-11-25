from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.location import Location
from typing import cast
from typing import Dict



def _get_kwargs(
    project_id: str,
    name: str,

) -> Dict[str, Any]:
    

    

    

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/projects/{project_id}/locations/get_by_name/{name}".format(project_id=project_id,name=name,),
    }


    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[HTTPValidationError, Location]]:
    if response.status_code == 200:
        response_200 = Location.from_dict(response.json())



        return response_200
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[HTTPValidationError, Location]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    name: str,
    *,
    client: AuthenticatedClient,

) -> Response[Union[HTTPValidationError, Location]]:
    """ Get Location In Project By Name

     Return a specific location

    Args:
        project_id (str):
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, Location]]
     """


    kwargs = _get_kwargs(
        project_id=project_id,
name=name,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    project_id: str,
    name: str,
    *,
    client: AuthenticatedClient,

) -> Optional[Union[HTTPValidationError, Location]]:
    """ Get Location In Project By Name

     Return a specific location

    Args:
        project_id (str):
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, Location]
     """


    return sync_detailed(
        project_id=project_id,
name=name,
client=client,

    ).parsed

async def asyncio_detailed(
    project_id: str,
    name: str,
    *,
    client: AuthenticatedClient,

) -> Response[Union[HTTPValidationError, Location]]:
    """ Get Location In Project By Name

     Return a specific location

    Args:
        project_id (str):
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, Location]]
     """


    kwargs = _get_kwargs(
        project_id=project_id,
name=name,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    project_id: str,
    name: str,
    *,
    client: AuthenticatedClient,

) -> Optional[Union[HTTPValidationError, Location]]:
    """ Get Location In Project By Name

     Return a specific location

    Args:
        project_id (str):
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, Location]
     """


    return (await asyncio_detailed(
        project_id=project_id,
name=name,
client=client,

    )).parsed
