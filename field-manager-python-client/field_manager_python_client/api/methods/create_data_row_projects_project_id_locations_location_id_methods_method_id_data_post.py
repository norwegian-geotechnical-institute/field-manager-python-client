from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.method_cpt_data_create import MethodCPTDataCreate
from ...models.method_dp_data_create import MethodDPDataCreate
from ...models.method_dt_data_create import MethodDTDataCreate
from ...models.method_pz_data_create import MethodPZDataCreate
from ...models.method_rcd_data_create import MethodRCDDataCreate
from ...models.method_rp_data_create import MethodRPDataCreate
from ...models.method_srs_data_create import MethodSRSDataCreate
from ...models.method_ss_data_create import MethodSSDataCreate
from ...models.method_svt_data_create import MethodSVTDataCreate
from ...models.method_tot_data_create import MethodTOTDataCreate
from ...models.method_tr_data_create import MethodTRDataCreate
from ...models.method_wst_data_create import MethodWSTDataCreate
from ...types import Response


def _get_kwargs(
    project_id: str,
    location_id: UUID,
    method_id: UUID,
    *,
    body: Union[
        "MethodCPTDataCreate",
        "MethodDPDataCreate",
        "MethodDTDataCreate",
        "MethodPZDataCreate",
        "MethodRCDDataCreate",
        "MethodRPDataCreate",
        "MethodSRSDataCreate",
        "MethodSSDataCreate",
        "MethodSVTDataCreate",
        "MethodTOTDataCreate",
        "MethodTRDataCreate",
        "MethodWSTDataCreate",
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/projects/{project_id}/locations/{location_id}/methods/{method_id}/data",
    }

    _kwargs["json"]: dict[str, Any]
    if isinstance(body, MethodCPTDataCreate):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MethodDPDataCreate):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MethodDTDataCreate):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MethodPZDataCreate):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MethodRCDDataCreate):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MethodRPDataCreate):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MethodSRSDataCreate):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MethodSSDataCreate):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MethodSVTDataCreate):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MethodTOTDataCreate):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MethodTRDataCreate):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[HTTPValidationError]:
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[HTTPValidationError]:
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
    *,
    client: AuthenticatedClient,
    body: Union[
        "MethodCPTDataCreate",
        "MethodDPDataCreate",
        "MethodDTDataCreate",
        "MethodPZDataCreate",
        "MethodRCDDataCreate",
        "MethodRPDataCreate",
        "MethodSRSDataCreate",
        "MethodSSDataCreate",
        "MethodSVTDataCreate",
        "MethodTOTDataCreate",
        "MethodTRDataCreate",
        "MethodWSTDataCreate",
    ],
) -> Response[HTTPValidationError]:
    """Create Data Row

     Create a new data row for a method

    Args:
        project_id (str):
        location_id (UUID):
        method_id (UUID):
        body (Union['MethodCPTDataCreate', 'MethodDPDataCreate', 'MethodDTDataCreate',
            'MethodPZDataCreate', 'MethodRCDDataCreate', 'MethodRPDataCreate', 'MethodSRSDataCreate',
            'MethodSSDataCreate', 'MethodSVTDataCreate', 'MethodTOTDataCreate', 'MethodTRDataCreate',
            'MethodWSTDataCreate']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        location_id=location_id,
        method_id=method_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    location_id: UUID,
    method_id: UUID,
    *,
    client: AuthenticatedClient,
    body: Union[
        "MethodCPTDataCreate",
        "MethodDPDataCreate",
        "MethodDTDataCreate",
        "MethodPZDataCreate",
        "MethodRCDDataCreate",
        "MethodRPDataCreate",
        "MethodSRSDataCreate",
        "MethodSSDataCreate",
        "MethodSVTDataCreate",
        "MethodTOTDataCreate",
        "MethodTRDataCreate",
        "MethodWSTDataCreate",
    ],
) -> Optional[HTTPValidationError]:
    """Create Data Row

     Create a new data row for a method

    Args:
        project_id (str):
        location_id (UUID):
        method_id (UUID):
        body (Union['MethodCPTDataCreate', 'MethodDPDataCreate', 'MethodDTDataCreate',
            'MethodPZDataCreate', 'MethodRCDDataCreate', 'MethodRPDataCreate', 'MethodSRSDataCreate',
            'MethodSSDataCreate', 'MethodSVTDataCreate', 'MethodTOTDataCreate', 'MethodTRDataCreate',
            'MethodWSTDataCreate']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError
    """

    return sync_detailed(
        project_id=project_id,
        location_id=location_id,
        method_id=method_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    location_id: UUID,
    method_id: UUID,
    *,
    client: AuthenticatedClient,
    body: Union[
        "MethodCPTDataCreate",
        "MethodDPDataCreate",
        "MethodDTDataCreate",
        "MethodPZDataCreate",
        "MethodRCDDataCreate",
        "MethodRPDataCreate",
        "MethodSRSDataCreate",
        "MethodSSDataCreate",
        "MethodSVTDataCreate",
        "MethodTOTDataCreate",
        "MethodTRDataCreate",
        "MethodWSTDataCreate",
    ],
) -> Response[HTTPValidationError]:
    """Create Data Row

     Create a new data row for a method

    Args:
        project_id (str):
        location_id (UUID):
        method_id (UUID):
        body (Union['MethodCPTDataCreate', 'MethodDPDataCreate', 'MethodDTDataCreate',
            'MethodPZDataCreate', 'MethodRCDDataCreate', 'MethodRPDataCreate', 'MethodSRSDataCreate',
            'MethodSSDataCreate', 'MethodSVTDataCreate', 'MethodTOTDataCreate', 'MethodTRDataCreate',
            'MethodWSTDataCreate']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        location_id=location_id,
        method_id=method_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    location_id: UUID,
    method_id: UUID,
    *,
    client: AuthenticatedClient,
    body: Union[
        "MethodCPTDataCreate",
        "MethodDPDataCreate",
        "MethodDTDataCreate",
        "MethodPZDataCreate",
        "MethodRCDDataCreate",
        "MethodRPDataCreate",
        "MethodSRSDataCreate",
        "MethodSSDataCreate",
        "MethodSVTDataCreate",
        "MethodTOTDataCreate",
        "MethodTRDataCreate",
        "MethodWSTDataCreate",
    ],
) -> Optional[HTTPValidationError]:
    """Create Data Row

     Create a new data row for a method

    Args:
        project_id (str):
        location_id (UUID):
        method_id (UUID):
        body (Union['MethodCPTDataCreate', 'MethodDPDataCreate', 'MethodDTDataCreate',
            'MethodPZDataCreate', 'MethodRCDDataCreate', 'MethodRPDataCreate', 'MethodSRSDataCreate',
            'MethodSSDataCreate', 'MethodSVTDataCreate', 'MethodTOTDataCreate', 'MethodTRDataCreate',
            'MethodWSTDataCreate']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            location_id=location_id,
            method_id=method_id,
            client=client,
            body=body,
        )
    ).parsed
