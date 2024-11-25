from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.http_validation_error import HTTPValidationError
from ...models.piezometer_model import PiezometerModel
from ...models.piezometer_model_update import PiezometerModelUpdate
from typing import cast
from typing import Dict
from uuid import UUID



def _get_kwargs(
    project_id: str,
    model_id: UUID,
    *,
    body: PiezometerModelUpdate,

) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}


    

    

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": "/projects/{project_id}/piezometers/models/{model_id}".format(project_id=project_id,model_id=model_id,),
    }

    _body = body.to_dict()


    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[HTTPValidationError, PiezometerModel]]:
    if response.status_code == 200:
        response_200 = PiezometerModel.from_dict(response.json())



        return response_200
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())



        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[HTTPValidationError, PiezometerModel]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    model_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PiezometerModelUpdate,

) -> Response[Union[HTTPValidationError, PiezometerModel]]:
    """ Update Piezometer Model

     Update piezometer model

    Args:
        project_id (str):
        model_id (UUID):
        body (PiezometerModelUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, PiezometerModel]]
     """


    kwargs = _get_kwargs(
        project_id=project_id,
model_id=model_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    project_id: str,
    model_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PiezometerModelUpdate,

) -> Optional[Union[HTTPValidationError, PiezometerModel]]:
    """ Update Piezometer Model

     Update piezometer model

    Args:
        project_id (str):
        model_id (UUID):
        body (PiezometerModelUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, PiezometerModel]
     """


    return sync_detailed(
        project_id=project_id,
model_id=model_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    project_id: str,
    model_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PiezometerModelUpdate,

) -> Response[Union[HTTPValidationError, PiezometerModel]]:
    """ Update Piezometer Model

     Update piezometer model

    Args:
        project_id (str):
        model_id (UUID):
        body (PiezometerModelUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, PiezometerModel]]
     """


    kwargs = _get_kwargs(
        project_id=project_id,
model_id=model_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    project_id: str,
    model_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PiezometerModelUpdate,

) -> Optional[Union[HTTPValidationError, PiezometerModel]]:
    """ Update Piezometer Model

     Update piezometer model

    Args:
        project_id (str):
        model_id (UUID):
        body (PiezometerModelUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, PiezometerModel]
     """


    return (await asyncio_detailed(
        project_id=project_id,
model_id=model_id,
client=client,
body=body,

    )).parsed
