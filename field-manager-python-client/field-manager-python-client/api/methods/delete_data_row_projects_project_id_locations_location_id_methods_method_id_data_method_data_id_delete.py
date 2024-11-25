from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from typing import cast
from typing import Dict
from uuid import UUID



def _get_kwargs(
    project_id: str,
    location_id: UUID,
    method_id: UUID,
    method_data_id: UUID,

) -> Dict[str, Any]:
    

    

    

    _kwargs: Dict[str, Any] = {
        "method": "delete",
        "url": "/projects/{project_id}/locations/{location_id}/methods/{method_id}/data/{method_data_id}".format(project_id=project_id,location_id=location_id,method_id=method_id,method_data_id=method_data_id,),
    }


    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, HTTPValidationError]]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    location_id: UUID,
    method_id: UUID,
    method_data_id: UUID,
    *,
    client: AuthenticatedClient,

) -> Response[Union[Any, HTTPValidationError]]:
    """ Delete Data Row

     Delete a data row

    Args:
        project_id (str):
        location_id (UUID):
        method_id (UUID):
        method_data_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
     """


    kwargs = _get_kwargs(
        project_id=project_id,
location_id=location_id,
method_id=method_id,
method_data_id=method_data_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    project_id: str,
    location_id: UUID,
    method_id: UUID,
    method_data_id: UUID,
    *,
    client: AuthenticatedClient,

) -> Optional[Union[Any, HTTPValidationError]]:
    """ Delete Data Row

     Delete a data row

    Args:
        project_id (str):
        location_id (UUID):
        method_id (UUID):
        method_data_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
     """


    return sync_detailed(
        project_id=project_id,
location_id=location_id,
method_id=method_id,
method_data_id=method_data_id,
client=client,

    ).parsed

async def asyncio_detailed(
    project_id: str,
    location_id: UUID,
    method_id: UUID,
    method_data_id: UUID,
    *,
    client: AuthenticatedClient,

) -> Response[Union[Any, HTTPValidationError]]:
    """ Delete Data Row

     Delete a data row

    Args:
        project_id (str):
        location_id (UUID):
        method_id (UUID):
        method_data_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
     """


    kwargs = _get_kwargs(
        project_id=project_id,
location_id=location_id,
method_id=method_id,
method_data_id=method_data_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    project_id: str,
    location_id: UUID,
    method_id: UUID,
    method_data_id: UUID,
    *,
    client: AuthenticatedClient,

) -> Optional[Union[Any, HTTPValidationError]]:
    """ Delete Data Row

     Delete a data row

    Args:
        project_id (str):
        location_id (UUID):
        method_id (UUID):
        method_data_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
     """


    return (await asyncio_detailed(
        project_id=project_id,
location_id=location_id,
method_id=method_id,
method_data_id=method_data_id,
client=client,

    )).parsed
