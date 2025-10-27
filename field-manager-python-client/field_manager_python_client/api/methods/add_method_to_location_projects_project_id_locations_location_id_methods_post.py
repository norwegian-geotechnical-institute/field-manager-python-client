from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.method_ad_create import MethodADCreate
from ...models.method_cd_create import MethodCDCreate
from ...models.method_cpt_create import MethodCPTCreate
from ...models.method_def_create import MethodDEFCreate
from ...models.method_dp_create import MethodDPCreate
from ...models.method_dt_create import MethodDTCreate
from ...models.method_esa_create import MethodESACreate
from ...models.method_inc_create import MethodINCCreate
from ...models.method_iw_create import MethodIWCreate
from ...models.method_other_create import MethodOTHERCreate
from ...models.method_pt_create import MethodPTCreate
from ...models.method_pz_create import MethodPZCreate
from ...models.method_rcd_create import MethodRCDCreate
from ...models.method_ro_create import MethodROCreate
from ...models.method_rp_create import MethodRPCreate
from ...models.method_rs_create import MethodRSCreate
from ...models.method_rws_create import MethodRWSCreate
from ...models.method_sa_create import MethodSACreate
from ...models.method_slb_create import MethodSLBCreate
from ...models.method_spt_create import MethodSPTCreate
from ...models.method_srs_create import MethodSRSCreate
from ...models.method_ss_create import MethodSSCreate
from ...models.method_sti_create import MethodSTICreate
from ...models.method_svt_create import MethodSVTCreate
from ...models.method_tot_create import MethodTOTCreate
from ...models.method_tp_create import MethodTPCreate
from ...models.method_tr_create import MethodTRCreate
from ...models.method_wst_create import MethodWSTCreate
from ...types import Response


def _get_kwargs(
    project_id: str,
    location_id: UUID,
    *,
    body: Union[
        "MethodADCreate",
        "MethodCDCreate",
        "MethodCPTCreate",
        "MethodDEFCreate",
        "MethodDPCreate",
        "MethodDTCreate",
        "MethodESACreate",
        "MethodINCCreate",
        "MethodIWCreate",
        "MethodOTHERCreate",
        "MethodPTCreate",
        "MethodPZCreate",
        "MethodRCDCreate",
        "MethodROCreate",
        "MethodRPCreate",
        "MethodRSCreate",
        "MethodRWSCreate",
        "MethodSACreate",
        "MethodSLBCreate",
        "MethodSPTCreate",
        "MethodSRSCreate",
        "MethodSSCreate",
        "MethodSTICreate",
        "MethodSVTCreate",
        "MethodTOTCreate",
        "MethodTPCreate",
        "MethodTRCreate",
        "MethodWSTCreate",
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/projects/{project_id}/locations/{location_id}/methods",
    }

    _kwargs["json"]: dict[str, Any]
    if isinstance(body, MethodADCreate):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MethodCDCreate):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MethodCPTCreate):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MethodDPCreate):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MethodDTCreate):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MethodESACreate):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MethodINCCreate):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MethodIWCreate):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MethodOTHERCreate):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MethodPTCreate):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MethodPZCreate):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MethodRCDCreate):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MethodROCreate):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MethodRPCreate):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MethodRSCreate):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MethodRWSCreate):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MethodSACreate):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MethodSLBCreate):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MethodSPTCreate):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MethodDEFCreate):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MethodSRSCreate):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MethodSSCreate):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MethodSTICreate):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MethodSVTCreate):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MethodTOTCreate):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MethodTPCreate):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MethodTRCreate):
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
    *,
    client: AuthenticatedClient,
    body: Union[
        "MethodADCreate",
        "MethodCDCreate",
        "MethodCPTCreate",
        "MethodDEFCreate",
        "MethodDPCreate",
        "MethodDTCreate",
        "MethodESACreate",
        "MethodINCCreate",
        "MethodIWCreate",
        "MethodOTHERCreate",
        "MethodPTCreate",
        "MethodPZCreate",
        "MethodRCDCreate",
        "MethodROCreate",
        "MethodRPCreate",
        "MethodRSCreate",
        "MethodRWSCreate",
        "MethodSACreate",
        "MethodSLBCreate",
        "MethodSPTCreate",
        "MethodSRSCreate",
        "MethodSSCreate",
        "MethodSTICreate",
        "MethodSVTCreate",
        "MethodTOTCreate",
        "MethodTPCreate",
        "MethodTRCreate",
        "MethodWSTCreate",
    ],
) -> Response[HTTPValidationError]:
    """Add Method To Location

     Add method to location

    Args:
        project_id (str):
        location_id (UUID):
        body (Union['MethodADCreate', 'MethodCDCreate', 'MethodCPTCreate', 'MethodDEFCreate',
            'MethodDPCreate', 'MethodDTCreate', 'MethodESACreate', 'MethodINCCreate',
            'MethodIWCreate', 'MethodOTHERCreate', 'MethodPTCreate', 'MethodPZCreate',
            'MethodRCDCreate', 'MethodROCreate', 'MethodRPCreate', 'MethodRSCreate',
            'MethodRWSCreate', 'MethodSACreate', 'MethodSLBCreate', 'MethodSPTCreate',
            'MethodSRSCreate', 'MethodSSCreate', 'MethodSTICreate', 'MethodSVTCreate',
            'MethodTOTCreate', 'MethodTPCreate', 'MethodTRCreate', 'MethodWSTCreate']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        location_id=location_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    location_id: UUID,
    *,
    client: AuthenticatedClient,
    body: Union[
        "MethodADCreate",
        "MethodCDCreate",
        "MethodCPTCreate",
        "MethodDEFCreate",
        "MethodDPCreate",
        "MethodDTCreate",
        "MethodESACreate",
        "MethodINCCreate",
        "MethodIWCreate",
        "MethodOTHERCreate",
        "MethodPTCreate",
        "MethodPZCreate",
        "MethodRCDCreate",
        "MethodROCreate",
        "MethodRPCreate",
        "MethodRSCreate",
        "MethodRWSCreate",
        "MethodSACreate",
        "MethodSLBCreate",
        "MethodSPTCreate",
        "MethodSRSCreate",
        "MethodSSCreate",
        "MethodSTICreate",
        "MethodSVTCreate",
        "MethodTOTCreate",
        "MethodTPCreate",
        "MethodTRCreate",
        "MethodWSTCreate",
    ],
) -> Optional[HTTPValidationError]:
    """Add Method To Location

     Add method to location

    Args:
        project_id (str):
        location_id (UUID):
        body (Union['MethodADCreate', 'MethodCDCreate', 'MethodCPTCreate', 'MethodDEFCreate',
            'MethodDPCreate', 'MethodDTCreate', 'MethodESACreate', 'MethodINCCreate',
            'MethodIWCreate', 'MethodOTHERCreate', 'MethodPTCreate', 'MethodPZCreate',
            'MethodRCDCreate', 'MethodROCreate', 'MethodRPCreate', 'MethodRSCreate',
            'MethodRWSCreate', 'MethodSACreate', 'MethodSLBCreate', 'MethodSPTCreate',
            'MethodSRSCreate', 'MethodSSCreate', 'MethodSTICreate', 'MethodSVTCreate',
            'MethodTOTCreate', 'MethodTPCreate', 'MethodTRCreate', 'MethodWSTCreate']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError
    """

    return sync_detailed(
        project_id=project_id,
        location_id=location_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    location_id: UUID,
    *,
    client: AuthenticatedClient,
    body: Union[
        "MethodADCreate",
        "MethodCDCreate",
        "MethodCPTCreate",
        "MethodDEFCreate",
        "MethodDPCreate",
        "MethodDTCreate",
        "MethodESACreate",
        "MethodINCCreate",
        "MethodIWCreate",
        "MethodOTHERCreate",
        "MethodPTCreate",
        "MethodPZCreate",
        "MethodRCDCreate",
        "MethodROCreate",
        "MethodRPCreate",
        "MethodRSCreate",
        "MethodRWSCreate",
        "MethodSACreate",
        "MethodSLBCreate",
        "MethodSPTCreate",
        "MethodSRSCreate",
        "MethodSSCreate",
        "MethodSTICreate",
        "MethodSVTCreate",
        "MethodTOTCreate",
        "MethodTPCreate",
        "MethodTRCreate",
        "MethodWSTCreate",
    ],
) -> Response[HTTPValidationError]:
    """Add Method To Location

     Add method to location

    Args:
        project_id (str):
        location_id (UUID):
        body (Union['MethodADCreate', 'MethodCDCreate', 'MethodCPTCreate', 'MethodDEFCreate',
            'MethodDPCreate', 'MethodDTCreate', 'MethodESACreate', 'MethodINCCreate',
            'MethodIWCreate', 'MethodOTHERCreate', 'MethodPTCreate', 'MethodPZCreate',
            'MethodRCDCreate', 'MethodROCreate', 'MethodRPCreate', 'MethodRSCreate',
            'MethodRWSCreate', 'MethodSACreate', 'MethodSLBCreate', 'MethodSPTCreate',
            'MethodSRSCreate', 'MethodSSCreate', 'MethodSTICreate', 'MethodSVTCreate',
            'MethodTOTCreate', 'MethodTPCreate', 'MethodTRCreate', 'MethodWSTCreate']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        location_id=location_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    location_id: UUID,
    *,
    client: AuthenticatedClient,
    body: Union[
        "MethodADCreate",
        "MethodCDCreate",
        "MethodCPTCreate",
        "MethodDEFCreate",
        "MethodDPCreate",
        "MethodDTCreate",
        "MethodESACreate",
        "MethodINCCreate",
        "MethodIWCreate",
        "MethodOTHERCreate",
        "MethodPTCreate",
        "MethodPZCreate",
        "MethodRCDCreate",
        "MethodROCreate",
        "MethodRPCreate",
        "MethodRSCreate",
        "MethodRWSCreate",
        "MethodSACreate",
        "MethodSLBCreate",
        "MethodSPTCreate",
        "MethodSRSCreate",
        "MethodSSCreate",
        "MethodSTICreate",
        "MethodSVTCreate",
        "MethodTOTCreate",
        "MethodTPCreate",
        "MethodTRCreate",
        "MethodWSTCreate",
    ],
) -> Optional[HTTPValidationError]:
    """Add Method To Location

     Add method to location

    Args:
        project_id (str):
        location_id (UUID):
        body (Union['MethodADCreate', 'MethodCDCreate', 'MethodCPTCreate', 'MethodDEFCreate',
            'MethodDPCreate', 'MethodDTCreate', 'MethodESACreate', 'MethodINCCreate',
            'MethodIWCreate', 'MethodOTHERCreate', 'MethodPTCreate', 'MethodPZCreate',
            'MethodRCDCreate', 'MethodROCreate', 'MethodRPCreate', 'MethodRSCreate',
            'MethodRWSCreate', 'MethodSACreate', 'MethodSLBCreate', 'MethodSPTCreate',
            'MethodSRSCreate', 'MethodSSCreate', 'MethodSTICreate', 'MethodSVTCreate',
            'MethodTOTCreate', 'MethodTPCreate', 'MethodTRCreate', 'MethodWSTCreate']):

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
            client=client,
            body=body,
        )
    ).parsed
