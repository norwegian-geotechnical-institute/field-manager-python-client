from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.project_location_method_types import ProjectLocationMethodTypes
from typing import cast
from typing import cast, List
from typing import Dict



def _get_kwargs(
    organization_id: str,

) -> Dict[str, Any]:
    

    

    

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/organizations/{organization_id}/projectlocationmethodtypes".format(organization_id=organization_id,),
    }


    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[HTTPValidationError, List['ProjectLocationMethodTypes']]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = ProjectLocationMethodTypes.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[HTTPValidationError, List['ProjectLocationMethodTypes']]]:
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

) -> Response[Union[HTTPValidationError, List['ProjectLocationMethodTypes']]]:
    """ Get Project Location Methodtypes Summary

     Gets a summary of all methodtypes for every location in every project for the given organization
    Used primarily for building elastic index for search in Geodata Explorer

    Args:
        organization_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, List['ProjectLocationMethodTypes']]]
     """


    kwargs = _get_kwargs(
        organization_id=organization_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    organization_id: str,
    *,
    client: AuthenticatedClient,

) -> Optional[Union[HTTPValidationError, List['ProjectLocationMethodTypes']]]:
    """ Get Project Location Methodtypes Summary

     Gets a summary of all methodtypes for every location in every project for the given organization
    Used primarily for building elastic index for search in Geodata Explorer

    Args:
        organization_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, List['ProjectLocationMethodTypes']]
     """


    return sync_detailed(
        organization_id=organization_id,
client=client,

    ).parsed

async def asyncio_detailed(
    organization_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Union[HTTPValidationError, List['ProjectLocationMethodTypes']]]:
    """ Get Project Location Methodtypes Summary

     Gets a summary of all methodtypes for every location in every project for the given organization
    Used primarily for building elastic index for search in Geodata Explorer

    Args:
        organization_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, List['ProjectLocationMethodTypes']]]
     """


    kwargs = _get_kwargs(
        organization_id=organization_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    organization_id: str,
    *,
    client: AuthenticatedClient,

) -> Optional[Union[HTTPValidationError, List['ProjectLocationMethodTypes']]]:
    """ Get Project Location Methodtypes Summary

     Gets a summary of all methodtypes for every location in every project for the given organization
    Used primarily for building elastic index for search in Geodata Explorer

    Args:
        organization_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, List['ProjectLocationMethodTypes']]
     """


    return (await asyncio_detailed(
        organization_id=organization_id,
client=client,

    )).parsed
