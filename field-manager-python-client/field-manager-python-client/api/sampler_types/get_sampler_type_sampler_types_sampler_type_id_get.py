from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.sampler_type import SamplerType
from typing import cast
from typing import Dict



def _get_kwargs(
    sampler_type_id: int,

) -> Dict[str, Any]:
    

    

    

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/sampler_types/{sampler_type_id}".format(sampler_type_id=sampler_type_id,),
    }


    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[HTTPValidationError, SamplerType]]:
    if response.status_code == 200:
        response_200 = SamplerType.from_dict(response.json())



        return response_200
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[HTTPValidationError, SamplerType]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    sampler_type_id: int,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[Union[HTTPValidationError, SamplerType]]:
    """ Get Sampler Type

    Args:
        sampler_type_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, SamplerType]]
     """


    kwargs = _get_kwargs(
        sampler_type_id=sampler_type_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    sampler_type_id: int,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Optional[Union[HTTPValidationError, SamplerType]]:
    """ Get Sampler Type

    Args:
        sampler_type_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, SamplerType]
     """


    return sync_detailed(
        sampler_type_id=sampler_type_id,
client=client,

    ).parsed

async def asyncio_detailed(
    sampler_type_id: int,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[Union[HTTPValidationError, SamplerType]]:
    """ Get Sampler Type

    Args:
        sampler_type_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, SamplerType]]
     """


    kwargs = _get_kwargs(
        sampler_type_id=sampler_type_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    sampler_type_id: int,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Optional[Union[HTTPValidationError, SamplerType]]:
    """ Get Sampler Type

    Args:
        sampler_type_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, SamplerType]
     """


    return (await asyncio_detailed(
        sampler_type_id=sampler_type_id,
client=client,

    )).parsed
