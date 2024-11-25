from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.file import File
from ...models.file_extended import FileExtended
from ...models.file_type import FileType
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Unset
from typing import cast
from typing import cast, List
from typing import cast, Union
from typing import Dict
from typing import Union



def _get_kwargs(
    project_id: str,
    *,
    file_types: Union[Unset, List[FileType]] = UNSET,
    extended_result: Union[Unset, bool] = False,

) -> Dict[str, Any]:
    

    

    params: Dict[str, Any] = {}

    json_file_types: Union[Unset, List[str]] = UNSET
    if not isinstance(file_types, Unset):
        json_file_types = []
        for file_types_item_data in file_types:
            file_types_item = file_types_item_data.value
            json_file_types.append(file_types_item)


    params["file_types"] = json_file_types

    params["extended_result"] = extended_result


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/projects/{project_id}/files".format(project_id=project_id,),
        "params": params,
    }


    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[HTTPValidationError, List[Union['File', 'FileExtended']]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            def _parse_response_200_item(data: object) -> Union['File', 'FileExtended']:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_200_item_type_0 = FileExtended.from_dict(data)



                    return response_200_item_type_0
                except: # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_item_type_1 = File.from_dict(data)



                return response_200_item_type_1

            response_200_item = _parse_response_200_item(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[HTTPValidationError, List[Union['File', 'FileExtended']]]]:
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
    file_types: Union[Unset, List[FileType]] = UNSET,
    extended_result: Union[Unset, bool] = False,

) -> Response[Union[HTTPValidationError, List[Union['File', 'FileExtended']]]]:
    """ Get Files In Project

     Get all database file objects in a project by project_id and possible filtered by file type.

    Args:
        project_id (str):
        file_types (Union[Unset, List[FileType]]):
        extended_result (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, List[Union['File', 'FileExtended']]]]
     """


    kwargs = _get_kwargs(
        project_id=project_id,
file_types=file_types,
extended_result=extended_result,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    project_id: str,
    *,
    client: AuthenticatedClient,
    file_types: Union[Unset, List[FileType]] = UNSET,
    extended_result: Union[Unset, bool] = False,

) -> Optional[Union[HTTPValidationError, List[Union['File', 'FileExtended']]]]:
    """ Get Files In Project

     Get all database file objects in a project by project_id and possible filtered by file type.

    Args:
        project_id (str):
        file_types (Union[Unset, List[FileType]]):
        extended_result (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, List[Union['File', 'FileExtended']]]
     """


    return sync_detailed(
        project_id=project_id,
client=client,
file_types=file_types,
extended_result=extended_result,

    ).parsed

async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient,
    file_types: Union[Unset, List[FileType]] = UNSET,
    extended_result: Union[Unset, bool] = False,

) -> Response[Union[HTTPValidationError, List[Union['File', 'FileExtended']]]]:
    """ Get Files In Project

     Get all database file objects in a project by project_id and possible filtered by file type.

    Args:
        project_id (str):
        file_types (Union[Unset, List[FileType]]):
        extended_result (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, List[Union['File', 'FileExtended']]]]
     """


    kwargs = _get_kwargs(
        project_id=project_id,
file_types=file_types,
extended_result=extended_result,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient,
    file_types: Union[Unset, List[FileType]] = UNSET,
    extended_result: Union[Unset, bool] = False,

) -> Optional[Union[HTTPValidationError, List[Union['File', 'FileExtended']]]]:
    """ Get Files In Project

     Get all database file objects in a project by project_id and possible filtered by file type.

    Args:
        project_id (str):
        file_types (Union[Unset, List[FileType]]):
        extended_result (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, List[Union['File', 'FileExtended']]]
     """


    return (await asyncio_detailed(
        project_id=project_id,
client=client,
file_types=file_types,
extended_result=extended_result,

    )).parsed
