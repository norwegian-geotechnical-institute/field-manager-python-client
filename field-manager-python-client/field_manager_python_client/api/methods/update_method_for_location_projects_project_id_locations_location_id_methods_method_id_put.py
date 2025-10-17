from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.method_ad_update import MethodADUpdate
from ...models.method_cd_update import MethodCDUpdate
from ...models.method_cpt_update import MethodCPTUpdate
from ...models.method_def_update import MethodDEFUpdate
from ...models.method_dp_update import MethodDPUpdate
from ...models.method_dt_update import MethodDTUpdate
from ...models.method_esa_update import MethodESAUpdate
from ...models.method_inc_update import MethodINCUpdate
from ...models.method_iw_update import MethodIWUpdate
from ...models.method_other_update import MethodOTHERUpdate
from ...models.method_pt_update import MethodPTUpdate
from ...models.method_pz_update import MethodPZUpdate
from ...models.method_rcd_update import MethodRCDUpdate
from ...models.method_ro_update import MethodROUpdate
from ...models.method_rp_update import MethodRPUpdate
from ...models.method_rs_update import MethodRSUpdate
from ...models.method_rws_update import MethodRWSUpdate
from ...models.method_sa_update import MethodSAUpdate
from ...models.method_slb_update import MethodSLBUpdate
from ...models.method_spt_update import MethodSPTUpdate
from ...models.method_srs_update import MethodSRSUpdate
from ...models.method_ss_update import MethodSSUpdate
from ...models.method_sti_update import MethodSTIUpdate
from ...models.method_svt_update import MethodSVTUpdate
from ...models.method_tot_update import MethodTOTUpdate
from ...models.method_tp_update import MethodTPUpdate
from ...models.method_tr_update import MethodTRUpdate
from ...models.method_wst_update import MethodWSTUpdate
from ...types import Response


def _get_kwargs(
    project_id: str,
    location_id: UUID,
    method_id: UUID,
    *,
    body: Union[
        "MethodADUpdate",
        "MethodCDUpdate",
        "MethodCPTUpdate",
        "MethodDEFUpdate",
        "MethodDPUpdate",
        "MethodDTUpdate",
        "MethodESAUpdate",
        "MethodINCUpdate",
        "MethodIWUpdate",
        "MethodOTHERUpdate",
        "MethodPTUpdate",
        "MethodPZUpdate",
        "MethodRCDUpdate",
        "MethodROUpdate",
        "MethodRPUpdate",
        "MethodRSUpdate",
        "MethodRWSUpdate",
        "MethodSAUpdate",
        "MethodSLBUpdate",
        "MethodSPTUpdate",
        "MethodSRSUpdate",
        "MethodSSUpdate",
        "MethodSTIUpdate",
        "MethodSVTUpdate",
        "MethodTOTUpdate",
        "MethodTPUpdate",
        "MethodTRUpdate",
        "MethodWSTUpdate",
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/projects/{project_id}/locations/{location_id}/methods/{method_id}",
    }

    _kwargs["json"]: dict[str, Any]
    if isinstance(body, MethodCPTUpdate):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MethodTOTUpdate):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MethodRPUpdate):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MethodSAUpdate):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MethodPZUpdate):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MethodSSUpdate):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MethodRWSUpdate):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MethodRCDUpdate):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MethodRSUpdate):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MethodSVTUpdate):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MethodSPTUpdate):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MethodCDUpdate):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MethodTPUpdate):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MethodPTUpdate):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MethodESAUpdate):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MethodTRUpdate):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MethodADUpdate):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MethodROUpdate):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MethodINCUpdate):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MethodDEFUpdate):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MethodIWUpdate):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MethodDTUpdate):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MethodOTHERUpdate):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MethodSRSUpdate):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MethodDPUpdate):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MethodWSTUpdate):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, MethodSLBUpdate):
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
        "MethodADUpdate",
        "MethodCDUpdate",
        "MethodCPTUpdate",
        "MethodDEFUpdate",
        "MethodDPUpdate",
        "MethodDTUpdate",
        "MethodESAUpdate",
        "MethodINCUpdate",
        "MethodIWUpdate",
        "MethodOTHERUpdate",
        "MethodPTUpdate",
        "MethodPZUpdate",
        "MethodRCDUpdate",
        "MethodROUpdate",
        "MethodRPUpdate",
        "MethodRSUpdate",
        "MethodRWSUpdate",
        "MethodSAUpdate",
        "MethodSLBUpdate",
        "MethodSPTUpdate",
        "MethodSRSUpdate",
        "MethodSSUpdate",
        "MethodSTIUpdate",
        "MethodSVTUpdate",
        "MethodTOTUpdate",
        "MethodTPUpdate",
        "MethodTRUpdate",
        "MethodWSTUpdate",
    ],
) -> Response[HTTPValidationError]:
    """Update Method For Location

     Update method

    Args:
        project_id (str):
        location_id (UUID):
        method_id (UUID):
        body (Union['MethodADUpdate', 'MethodCDUpdate', 'MethodCPTUpdate', 'MethodDEFUpdate',
            'MethodDPUpdate', 'MethodDTUpdate', 'MethodESAUpdate', 'MethodINCUpdate',
            'MethodIWUpdate', 'MethodOTHERUpdate', 'MethodPTUpdate', 'MethodPZUpdate',
            'MethodRCDUpdate', 'MethodROUpdate', 'MethodRPUpdate', 'MethodRSUpdate',
            'MethodRWSUpdate', 'MethodSAUpdate', 'MethodSLBUpdate', 'MethodSPTUpdate',
            'MethodSRSUpdate', 'MethodSSUpdate', 'MethodSTIUpdate', 'MethodSVTUpdate',
            'MethodTOTUpdate', 'MethodTPUpdate', 'MethodTRUpdate', 'MethodWSTUpdate']):

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
        "MethodADUpdate",
        "MethodCDUpdate",
        "MethodCPTUpdate",
        "MethodDEFUpdate",
        "MethodDPUpdate",
        "MethodDTUpdate",
        "MethodESAUpdate",
        "MethodINCUpdate",
        "MethodIWUpdate",
        "MethodOTHERUpdate",
        "MethodPTUpdate",
        "MethodPZUpdate",
        "MethodRCDUpdate",
        "MethodROUpdate",
        "MethodRPUpdate",
        "MethodRSUpdate",
        "MethodRWSUpdate",
        "MethodSAUpdate",
        "MethodSLBUpdate",
        "MethodSPTUpdate",
        "MethodSRSUpdate",
        "MethodSSUpdate",
        "MethodSTIUpdate",
        "MethodSVTUpdate",
        "MethodTOTUpdate",
        "MethodTPUpdate",
        "MethodTRUpdate",
        "MethodWSTUpdate",
    ],
) -> Optional[HTTPValidationError]:
    """Update Method For Location

     Update method

    Args:
        project_id (str):
        location_id (UUID):
        method_id (UUID):
        body (Union['MethodADUpdate', 'MethodCDUpdate', 'MethodCPTUpdate', 'MethodDEFUpdate',
            'MethodDPUpdate', 'MethodDTUpdate', 'MethodESAUpdate', 'MethodINCUpdate',
            'MethodIWUpdate', 'MethodOTHERUpdate', 'MethodPTUpdate', 'MethodPZUpdate',
            'MethodRCDUpdate', 'MethodROUpdate', 'MethodRPUpdate', 'MethodRSUpdate',
            'MethodRWSUpdate', 'MethodSAUpdate', 'MethodSLBUpdate', 'MethodSPTUpdate',
            'MethodSRSUpdate', 'MethodSSUpdate', 'MethodSTIUpdate', 'MethodSVTUpdate',
            'MethodTOTUpdate', 'MethodTPUpdate', 'MethodTRUpdate', 'MethodWSTUpdate']):

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
        "MethodADUpdate",
        "MethodCDUpdate",
        "MethodCPTUpdate",
        "MethodDEFUpdate",
        "MethodDPUpdate",
        "MethodDTUpdate",
        "MethodESAUpdate",
        "MethodINCUpdate",
        "MethodIWUpdate",
        "MethodOTHERUpdate",
        "MethodPTUpdate",
        "MethodPZUpdate",
        "MethodRCDUpdate",
        "MethodROUpdate",
        "MethodRPUpdate",
        "MethodRSUpdate",
        "MethodRWSUpdate",
        "MethodSAUpdate",
        "MethodSLBUpdate",
        "MethodSPTUpdate",
        "MethodSRSUpdate",
        "MethodSSUpdate",
        "MethodSTIUpdate",
        "MethodSVTUpdate",
        "MethodTOTUpdate",
        "MethodTPUpdate",
        "MethodTRUpdate",
        "MethodWSTUpdate",
    ],
) -> Response[HTTPValidationError]:
    """Update Method For Location

     Update method

    Args:
        project_id (str):
        location_id (UUID):
        method_id (UUID):
        body (Union['MethodADUpdate', 'MethodCDUpdate', 'MethodCPTUpdate', 'MethodDEFUpdate',
            'MethodDPUpdate', 'MethodDTUpdate', 'MethodESAUpdate', 'MethodINCUpdate',
            'MethodIWUpdate', 'MethodOTHERUpdate', 'MethodPTUpdate', 'MethodPZUpdate',
            'MethodRCDUpdate', 'MethodROUpdate', 'MethodRPUpdate', 'MethodRSUpdate',
            'MethodRWSUpdate', 'MethodSAUpdate', 'MethodSLBUpdate', 'MethodSPTUpdate',
            'MethodSRSUpdate', 'MethodSSUpdate', 'MethodSTIUpdate', 'MethodSVTUpdate',
            'MethodTOTUpdate', 'MethodTPUpdate', 'MethodTRUpdate', 'MethodWSTUpdate']):

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
        "MethodADUpdate",
        "MethodCDUpdate",
        "MethodCPTUpdate",
        "MethodDEFUpdate",
        "MethodDPUpdate",
        "MethodDTUpdate",
        "MethodESAUpdate",
        "MethodINCUpdate",
        "MethodIWUpdate",
        "MethodOTHERUpdate",
        "MethodPTUpdate",
        "MethodPZUpdate",
        "MethodRCDUpdate",
        "MethodROUpdate",
        "MethodRPUpdate",
        "MethodRSUpdate",
        "MethodRWSUpdate",
        "MethodSAUpdate",
        "MethodSLBUpdate",
        "MethodSPTUpdate",
        "MethodSRSUpdate",
        "MethodSSUpdate",
        "MethodSTIUpdate",
        "MethodSVTUpdate",
        "MethodTOTUpdate",
        "MethodTPUpdate",
        "MethodTRUpdate",
        "MethodWSTUpdate",
    ],
) -> Optional[HTTPValidationError]:
    """Update Method For Location

     Update method

    Args:
        project_id (str):
        location_id (UUID):
        method_id (UUID):
        body (Union['MethodADUpdate', 'MethodCDUpdate', 'MethodCPTUpdate', 'MethodDEFUpdate',
            'MethodDPUpdate', 'MethodDTUpdate', 'MethodESAUpdate', 'MethodINCUpdate',
            'MethodIWUpdate', 'MethodOTHERUpdate', 'MethodPTUpdate', 'MethodPZUpdate',
            'MethodRCDUpdate', 'MethodROUpdate', 'MethodRPUpdate', 'MethodRSUpdate',
            'MethodRWSUpdate', 'MethodSAUpdate', 'MethodSLBUpdate', 'MethodSPTUpdate',
            'MethodSRSUpdate', 'MethodSSUpdate', 'MethodSTIUpdate', 'MethodSVTUpdate',
            'MethodTOTUpdate', 'MethodTPUpdate', 'MethodTRUpdate', 'MethodWSTUpdate']):

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
