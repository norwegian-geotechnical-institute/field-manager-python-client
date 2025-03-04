from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.method_ad import MethodAD
from ...models.method_ad_update import MethodADUpdate
from ...models.method_cd import MethodCD
from ...models.method_cd_update import MethodCDUpdate
from ...models.method_cpt import MethodCPT
from ...models.method_cpt_update import MethodCPTUpdate
from ...models.method_def import MethodDEF
from ...models.method_def_update import MethodDEFUpdate
from ...models.method_dp import MethodDP
from ...models.method_dp_update import MethodDPUpdate
from ...models.method_dt import MethodDT
from ...models.method_dt_update import MethodDTUpdate
from ...models.method_esa import MethodESA
from ...models.method_esa_update import MethodESAUpdate
from ...models.method_inc import MethodINC
from ...models.method_inc_update import MethodINCUpdate
from ...models.method_iw import MethodIW
from ...models.method_iw_update import MethodIWUpdate
from ...models.method_other import MethodOTHER
from ...models.method_other_update import MethodOTHERUpdate
from ...models.method_pt import MethodPT
from ...models.method_pt_update import MethodPTUpdate
from ...models.method_pz import MethodPZ
from ...models.method_pz_update import MethodPZUpdate
from ...models.method_rcd import MethodRCD
from ...models.method_rcd_update import MethodRCDUpdate
from ...models.method_ro import MethodRO
from ...models.method_ro_update import MethodROUpdate
from ...models.method_rp import MethodRP
from ...models.method_rp_update import MethodRPUpdate
from ...models.method_rs import MethodRS
from ...models.method_rs_update import MethodRSUpdate
from ...models.method_rws import MethodRWS
from ...models.method_rws_update import MethodRWSUpdate
from ...models.method_sa import MethodSA
from ...models.method_sa_update import MethodSAUpdate
from ...models.method_slb import MethodSLB
from ...models.method_slb_update import MethodSLBUpdate
from ...models.method_spt import MethodSPT
from ...models.method_spt_update import MethodSPTUpdate
from ...models.method_srs import MethodSRS
from ...models.method_srs_update import MethodSRSUpdate
from ...models.method_ss import MethodSS
from ...models.method_ss_update import MethodSSUpdate
from ...models.method_sti import MethodSTI
from ...models.method_sti_update import MethodSTIUpdate
from ...models.method_svt import MethodSVT
from ...models.method_svt_update import MethodSVTUpdate
from ...models.method_tot import MethodTOT
from ...models.method_tot_update import MethodTOTUpdate
from ...models.method_tp import MethodTP
from ...models.method_tp_update import MethodTPUpdate
from ...models.method_tr import MethodTR
from ...models.method_tr_update import MethodTRUpdate
from ...models.method_wst import MethodWST
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

    _body: dict[str, Any]
    if isinstance(body, MethodCPTUpdate):
        _body = body.to_dict()
    elif isinstance(body, MethodTOTUpdate):
        _body = body.to_dict()
    elif isinstance(body, MethodRPUpdate):
        _body = body.to_dict()
    elif isinstance(body, MethodSAUpdate):
        _body = body.to_dict()
    elif isinstance(body, MethodPZUpdate):
        _body = body.to_dict()
    elif isinstance(body, MethodSSUpdate):
        _body = body.to_dict()
    elif isinstance(body, MethodRWSUpdate):
        _body = body.to_dict()
    elif isinstance(body, MethodRCDUpdate):
        _body = body.to_dict()
    elif isinstance(body, MethodRSUpdate):
        _body = body.to_dict()
    elif isinstance(body, MethodSVTUpdate):
        _body = body.to_dict()
    elif isinstance(body, MethodSPTUpdate):
        _body = body.to_dict()
    elif isinstance(body, MethodCDUpdate):
        _body = body.to_dict()
    elif isinstance(body, MethodTPUpdate):
        _body = body.to_dict()
    elif isinstance(body, MethodPTUpdate):
        _body = body.to_dict()
    elif isinstance(body, MethodESAUpdate):
        _body = body.to_dict()
    elif isinstance(body, MethodTRUpdate):
        _body = body.to_dict()
    elif isinstance(body, MethodADUpdate):
        _body = body.to_dict()
    elif isinstance(body, MethodROUpdate):
        _body = body.to_dict()
    elif isinstance(body, MethodINCUpdate):
        _body = body.to_dict()
    elif isinstance(body, MethodDEFUpdate):
        _body = body.to_dict()
    elif isinstance(body, MethodIWUpdate):
        _body = body.to_dict()
    elif isinstance(body, MethodDTUpdate):
        _body = body.to_dict()
    elif isinstance(body, MethodOTHERUpdate):
        _body = body.to_dict()
    elif isinstance(body, MethodSRSUpdate):
        _body = body.to_dict()
    elif isinstance(body, MethodDPUpdate):
        _body = body.to_dict()
    elif isinstance(body, MethodWSTUpdate):
        _body = body.to_dict()
    elif isinstance(body, MethodSLBUpdate):
        _body = body.to_dict()
    else:
        _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        HTTPValidationError,
        Union[
            "MethodAD",
            "MethodCD",
            "MethodCPT",
            "MethodDEF",
            "MethodDP",
            "MethodDT",
            "MethodESA",
            "MethodINC",
            "MethodIW",
            "MethodOTHER",
            "MethodPT",
            "MethodPZ",
            "MethodRCD",
            "MethodRO",
            "MethodRP",
            "MethodRS",
            "MethodRWS",
            "MethodSA",
            "MethodSLB",
            "MethodSPT",
            "MethodSRS",
            "MethodSS",
            "MethodSTI",
            "MethodSVT",
            "MethodTOT",
            "MethodTP",
            "MethodTR",
            "MethodWST",
        ],
    ]
]:
    if response.status_code == 200:

        def _parse_response_200(
            data: object,
        ) -> Union[
            "MethodAD",
            "MethodCD",
            "MethodCPT",
            "MethodDEF",
            "MethodDP",
            "MethodDT",
            "MethodESA",
            "MethodINC",
            "MethodIW",
            "MethodOTHER",
            "MethodPT",
            "MethodPZ",
            "MethodRCD",
            "MethodRO",
            "MethodRP",
            "MethodRS",
            "MethodRWS",
            "MethodSA",
            "MethodSLB",
            "MethodSPT",
            "MethodSRS",
            "MethodSS",
            "MethodSTI",
            "MethodSVT",
            "MethodTOT",
            "MethodTP",
            "MethodTR",
            "MethodWST",
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = MethodCPT.from_dict(data)

                return response_200_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_1 = MethodTOT.from_dict(data)

                return response_200_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_2 = MethodRP.from_dict(data)

                return response_200_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_3 = MethodSA.from_dict(data)

                return response_200_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_4 = MethodPZ.from_dict(data)

                return response_200_type_4
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_5 = MethodSS.from_dict(data)

                return response_200_type_5
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_6 = MethodRWS.from_dict(data)

                return response_200_type_6
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_7 = MethodRCD.from_dict(data)

                return response_200_type_7
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_8 = MethodRS.from_dict(data)

                return response_200_type_8
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_9 = MethodSVT.from_dict(data)

                return response_200_type_9
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_10 = MethodSPT.from_dict(data)

                return response_200_type_10
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_11 = MethodCD.from_dict(data)

                return response_200_type_11
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_12 = MethodTP.from_dict(data)

                return response_200_type_12
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_13 = MethodPT.from_dict(data)

                return response_200_type_13
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_14 = MethodESA.from_dict(data)

                return response_200_type_14
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_15 = MethodTR.from_dict(data)

                return response_200_type_15
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_16 = MethodAD.from_dict(data)

                return response_200_type_16
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_17 = MethodRO.from_dict(data)

                return response_200_type_17
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_18 = MethodINC.from_dict(data)

                return response_200_type_18
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_19 = MethodDEF.from_dict(data)

                return response_200_type_19
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_20 = MethodIW.from_dict(data)

                return response_200_type_20
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_21 = MethodDT.from_dict(data)

                return response_200_type_21
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_22 = MethodOTHER.from_dict(data)

                return response_200_type_22
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_23 = MethodSRS.from_dict(data)

                return response_200_type_23
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_24 = MethodDP.from_dict(data)

                return response_200_type_24
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_25 = MethodWST.from_dict(data)

                return response_200_type_25
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_26 = MethodSLB.from_dict(data)

                return response_200_type_26
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_27 = MethodSTI.from_dict(data)

            return response_200_type_27

        response_200 = _parse_response_200(response.json())

        return response_200
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        HTTPValidationError,
        Union[
            "MethodAD",
            "MethodCD",
            "MethodCPT",
            "MethodDEF",
            "MethodDP",
            "MethodDT",
            "MethodESA",
            "MethodINC",
            "MethodIW",
            "MethodOTHER",
            "MethodPT",
            "MethodPZ",
            "MethodRCD",
            "MethodRO",
            "MethodRP",
            "MethodRS",
            "MethodRWS",
            "MethodSA",
            "MethodSLB",
            "MethodSPT",
            "MethodSRS",
            "MethodSS",
            "MethodSTI",
            "MethodSVT",
            "MethodTOT",
            "MethodTP",
            "MethodTR",
            "MethodWST",
        ],
    ]
]:
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
) -> Response[
    Union[
        HTTPValidationError,
        Union[
            "MethodAD",
            "MethodCD",
            "MethodCPT",
            "MethodDEF",
            "MethodDP",
            "MethodDT",
            "MethodESA",
            "MethodINC",
            "MethodIW",
            "MethodOTHER",
            "MethodPT",
            "MethodPZ",
            "MethodRCD",
            "MethodRO",
            "MethodRP",
            "MethodRS",
            "MethodRWS",
            "MethodSA",
            "MethodSLB",
            "MethodSPT",
            "MethodSRS",
            "MethodSS",
            "MethodSTI",
            "MethodSVT",
            "MethodTOT",
            "MethodTP",
            "MethodTR",
            "MethodWST",
        ],
    ]
]:
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
        Response[Union[HTTPValidationError, Union['MethodAD', 'MethodCD', 'MethodCPT', 'MethodDEF', 'MethodDP', 'MethodDT', 'MethodESA', 'MethodINC', 'MethodIW', 'MethodOTHER', 'MethodPT', 'MethodPZ', 'MethodRCD', 'MethodRO', 'MethodRP', 'MethodRS', 'MethodRWS', 'MethodSA', 'MethodSLB', 'MethodSPT', 'MethodSRS', 'MethodSS', 'MethodSTI', 'MethodSVT', 'MethodTOT', 'MethodTP', 'MethodTR', 'MethodWST']]]
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
) -> Optional[
    Union[
        HTTPValidationError,
        Union[
            "MethodAD",
            "MethodCD",
            "MethodCPT",
            "MethodDEF",
            "MethodDP",
            "MethodDT",
            "MethodESA",
            "MethodINC",
            "MethodIW",
            "MethodOTHER",
            "MethodPT",
            "MethodPZ",
            "MethodRCD",
            "MethodRO",
            "MethodRP",
            "MethodRS",
            "MethodRWS",
            "MethodSA",
            "MethodSLB",
            "MethodSPT",
            "MethodSRS",
            "MethodSS",
            "MethodSTI",
            "MethodSVT",
            "MethodTOT",
            "MethodTP",
            "MethodTR",
            "MethodWST",
        ],
    ]
]:
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
        Union[HTTPValidationError, Union['MethodAD', 'MethodCD', 'MethodCPT', 'MethodDEF', 'MethodDP', 'MethodDT', 'MethodESA', 'MethodINC', 'MethodIW', 'MethodOTHER', 'MethodPT', 'MethodPZ', 'MethodRCD', 'MethodRO', 'MethodRP', 'MethodRS', 'MethodRWS', 'MethodSA', 'MethodSLB', 'MethodSPT', 'MethodSRS', 'MethodSS', 'MethodSTI', 'MethodSVT', 'MethodTOT', 'MethodTP', 'MethodTR', 'MethodWST']]
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
) -> Response[
    Union[
        HTTPValidationError,
        Union[
            "MethodAD",
            "MethodCD",
            "MethodCPT",
            "MethodDEF",
            "MethodDP",
            "MethodDT",
            "MethodESA",
            "MethodINC",
            "MethodIW",
            "MethodOTHER",
            "MethodPT",
            "MethodPZ",
            "MethodRCD",
            "MethodRO",
            "MethodRP",
            "MethodRS",
            "MethodRWS",
            "MethodSA",
            "MethodSLB",
            "MethodSPT",
            "MethodSRS",
            "MethodSS",
            "MethodSTI",
            "MethodSVT",
            "MethodTOT",
            "MethodTP",
            "MethodTR",
            "MethodWST",
        ],
    ]
]:
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
        Response[Union[HTTPValidationError, Union['MethodAD', 'MethodCD', 'MethodCPT', 'MethodDEF', 'MethodDP', 'MethodDT', 'MethodESA', 'MethodINC', 'MethodIW', 'MethodOTHER', 'MethodPT', 'MethodPZ', 'MethodRCD', 'MethodRO', 'MethodRP', 'MethodRS', 'MethodRWS', 'MethodSA', 'MethodSLB', 'MethodSPT', 'MethodSRS', 'MethodSS', 'MethodSTI', 'MethodSVT', 'MethodTOT', 'MethodTP', 'MethodTR', 'MethodWST']]]
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
) -> Optional[
    Union[
        HTTPValidationError,
        Union[
            "MethodAD",
            "MethodCD",
            "MethodCPT",
            "MethodDEF",
            "MethodDP",
            "MethodDT",
            "MethodESA",
            "MethodINC",
            "MethodIW",
            "MethodOTHER",
            "MethodPT",
            "MethodPZ",
            "MethodRCD",
            "MethodRO",
            "MethodRP",
            "MethodRS",
            "MethodRWS",
            "MethodSA",
            "MethodSLB",
            "MethodSPT",
            "MethodSRS",
            "MethodSS",
            "MethodSTI",
            "MethodSVT",
            "MethodTOT",
            "MethodTP",
            "MethodTR",
            "MethodWST",
        ],
    ]
]:
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
        Union[HTTPValidationError, Union['MethodAD', 'MethodCD', 'MethodCPT', 'MethodDEF', 'MethodDP', 'MethodDT', 'MethodESA', 'MethodINC', 'MethodIW', 'MethodOTHER', 'MethodPT', 'MethodPZ', 'MethodRCD', 'MethodRO', 'MethodRP', 'MethodRS', 'MethodRWS', 'MethodSA', 'MethodSLB', 'MethodSPT', 'MethodSRS', 'MethodSS', 'MethodSTI', 'MethodSVT', 'MethodTOT', 'MethodTP', 'MethodTR', 'MethodWST']]
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
