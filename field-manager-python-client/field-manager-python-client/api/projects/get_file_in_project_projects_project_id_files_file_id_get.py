from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.file import File
from ...models.http_validation_error import HTTPValidationError
from typing import cast
from typing import Dict
from uuid import UUID



def _get_kwargs(
    project_id: str,
    file_id: UUID,

) -> Dict[str, Any]:
    

    

    

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/projects/{project_id}/files/{file_id}".format(project_id=project_id,file_id=file_id,),
    }


    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[File, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = File.from_dict(response.json())



        return response_200
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[File, HTTPValidationError]]:
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

) -> Response[Union[File, HTTPValidationError]]:
    """ Get File In Project

     Return a database file object with the given file_id in specified project.

    Args:
        project_id (str):
        file_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[File, HTTPValidationError]]
     """


    kwargs = _get_kwargs(
        project_id=project_id,
file_id=file_id,

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

) -> Optional[Union[File, HTTPValidationError]]:
    """ Get File In Project

     Return a database file object with the given file_id in specified project.

    Args:
        project_id (str):
        file_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[File, HTTPValidationError]
     """


    return sync_detailed(
        project_id=project_id,
file_id=file_id,
client=client,

    ).parsed

async def asyncio_detailed(
    project_id: str,
    file_id: UUID,
    *,
    client: AuthenticatedClient,

) -> Response[Union[File, HTTPValidationError]]:
    """ Get File In Project

     Return a database file object with the given file_id in specified project.

    Args:
        project_id (str):
        file_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[File, HTTPValidationError]]
     """


    kwargs = _get_kwargs(
        project_id=project_id,
file_id=file_id,

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

) -> Optional[Union[File, HTTPValidationError]]:
    """ Get File In Project

     Return a database file object with the given file_id in specified project.

    Args:
        project_id (str):
        file_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[File, HTTPValidationError]
     """


    return (await asyncio_detailed(
        project_id=project_id,
file_id=file_id,
client=client,

    )).parsed
