from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.method_ad import MethodAD
from ...models.method_ad_create import MethodADCreate
from ...models.method_cd import MethodCD
from ...models.method_cd_create import MethodCDCreate
from ...models.method_cpt import MethodCPT
from ...models.method_cpt_create import MethodCPTCreate
from ...models.method_def import MethodDEF
from ...models.method_def_create import MethodDEFCreate
from ...models.method_dp import MethodDP
from ...models.method_dp_create import MethodDPCreate
from ...models.method_dt import MethodDT
from ...models.method_dt_create import MethodDTCreate
from ...models.method_esa import MethodESA
from ...models.method_esa_create import MethodESACreate
from ...models.method_inc import MethodINC
from ...models.method_inc_create import MethodINCCreate
from ...models.method_iw import MethodIW
from ...models.method_iw_create import MethodIWCreate
from ...models.method_other import MethodOTHER
from ...models.method_other_create import MethodOTHERCreate
from ...models.method_pt import MethodPT
from ...models.method_pt_create import MethodPTCreate
from ...models.method_pz import MethodPZ
from ...models.method_pz_create import MethodPZCreate
from ...models.method_rcd import MethodRCD
from ...models.method_rcd_create import MethodRCDCreate
from ...models.method_ro import MethodRO
from ...models.method_ro_create import MethodROCreate
from ...models.method_rp import MethodRP
from ...models.method_rp_create import MethodRPCreate
from ...models.method_rs import MethodRS
from ...models.method_rs_create import MethodRSCreate
from ...models.method_rws import MethodRWS
from ...models.method_rws_create import MethodRWSCreate
from ...models.method_sa import MethodSA
from ...models.method_sa_create import MethodSACreate
from ...models.method_slb import MethodSLB
from ...models.method_slb_create import MethodSLBCreate
from ...models.method_spt import MethodSPT
from ...models.method_spt_create import MethodSPTCreate
from ...models.method_srs import MethodSRS
from ...models.method_srs_create import MethodSRSCreate
from ...models.method_ss import MethodSS
from ...models.method_ss_create import MethodSSCreate
from ...models.method_sti import MethodSTI
from ...models.method_sti_create import MethodSTICreate
from ...models.method_svt import MethodSVT
from ...models.method_svt_create import MethodSVTCreate
from ...models.method_tot import MethodTOT
from ...models.method_tot_create import MethodTOTCreate
from ...models.method_tp import MethodTP
from ...models.method_tp_create import MethodTPCreate
from ...models.method_tr import MethodTR
from ...models.method_tr_create import MethodTRCreate
from ...models.method_wst import MethodWST
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

    _body: dict[str, Any]
    if isinstance(body, MethodADCreate):
        _body = body.to_dict()
    elif isinstance(body, MethodCDCreate):
        _body = body.to_dict()
    elif isinstance(body, MethodCPTCreate):
        _body = body.to_dict()
    elif isinstance(body, MethodDPCreate):
        _body = body.to_dict()
    elif isinstance(body, MethodDTCreate):
        _body = body.to_dict()
    elif isinstance(body, MethodESACreate):
        _body = body.to_dict()
    elif isinstance(body, MethodINCCreate):
        _body = body.to_dict()
    elif isinstance(body, MethodIWCreate):
        _body = body.to_dict()
    elif isinstance(body, MethodOTHERCreate):
        _body = body.to_dict()
    elif isinstance(body, MethodPTCreate):
        _body = body.to_dict()
    elif isinstance(body, MethodPZCreate):
        _body = body.to_dict()
    elif isinstance(body, MethodRCDCreate):
        _body = body.to_dict()
    elif isinstance(body, MethodROCreate):
        _body = body.to_dict()
    elif isinstance(body, MethodRPCreate):
        _body = body.to_dict()
    elif isinstance(body, MethodRSCreate):
        _body = body.to_dict()
    elif isinstance(body, MethodRWSCreate):
        _body = body.to_dict()
    elif isinstance(body, MethodSACreate):
        _body = body.to_dict()
    elif isinstance(body, MethodSLBCreate):
        _body = body.to_dict()
    elif isinstance(body, MethodSPTCreate):
        _body = body.to_dict()
    elif isinstance(body, MethodDEFCreate):
        _body = body.to_dict()
    elif isinstance(body, MethodSRSCreate):
        _body = body.to_dict()
    elif isinstance(body, MethodSSCreate):
        _body = body.to_dict()
    elif isinstance(body, MethodSTICreate):
        _body = body.to_dict()
    elif isinstance(body, MethodSVTCreate):
        _body = body.to_dict()
    elif isinstance(body, MethodTOTCreate):
        _body = body.to_dict()
    elif isinstance(body, MethodTPCreate):
        _body = body.to_dict()
    elif isinstance(body, MethodTRCreate):
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
    if response.status_code == 201:

        def _parse_response_201(
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
                response_201_type_0 = MethodCPT.from_dict(data)

                return response_201_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_1 = MethodTOT.from_dict(data)

                return response_201_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_2 = MethodRP.from_dict(data)

                return response_201_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_3 = MethodSA.from_dict(data)

                return response_201_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_4 = MethodPZ.from_dict(data)

                return response_201_type_4
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_5 = MethodSS.from_dict(data)

                return response_201_type_5
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_6 = MethodRWS.from_dict(data)

                return response_201_type_6
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_7 = MethodRCD.from_dict(data)

                return response_201_type_7
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_8 = MethodRS.from_dict(data)

                return response_201_type_8
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_9 = MethodSVT.from_dict(data)

                return response_201_type_9
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_10 = MethodSPT.from_dict(data)

                return response_201_type_10
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_11 = MethodCD.from_dict(data)

                return response_201_type_11
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_12 = MethodTP.from_dict(data)

                return response_201_type_12
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_13 = MethodPT.from_dict(data)

                return response_201_type_13
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_14 = MethodESA.from_dict(data)

                return response_201_type_14
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_15 = MethodTR.from_dict(data)

                return response_201_type_15
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_16 = MethodAD.from_dict(data)

                return response_201_type_16
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_17 = MethodRO.from_dict(data)

                return response_201_type_17
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_18 = MethodINC.from_dict(data)

                return response_201_type_18
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_19 = MethodDEF.from_dict(data)

                return response_201_type_19
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_20 = MethodIW.from_dict(data)

                return response_201_type_20
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_21 = MethodDT.from_dict(data)

                return response_201_type_21
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_22 = MethodOTHER.from_dict(data)

                return response_201_type_22
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_23 = MethodSRS.from_dict(data)

                return response_201_type_23
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_24 = MethodDP.from_dict(data)

                return response_201_type_24
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_25 = MethodWST.from_dict(data)

                return response_201_type_25
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_26 = MethodSLB.from_dict(data)

                return response_201_type_26
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_201_type_27 = MethodSTI.from_dict(data)

            return response_201_type_27

        response_201 = _parse_response_201(response.json())

        return response_201
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
        Response[Union[HTTPValidationError, Union['MethodAD', 'MethodCD', 'MethodCPT', 'MethodDEF', 'MethodDP', 'MethodDT', 'MethodESA', 'MethodINC', 'MethodIW', 'MethodOTHER', 'MethodPT', 'MethodPZ', 'MethodRCD', 'MethodRO', 'MethodRP', 'MethodRS', 'MethodRWS', 'MethodSA', 'MethodSLB', 'MethodSPT', 'MethodSRS', 'MethodSS', 'MethodSTI', 'MethodSVT', 'MethodTOT', 'MethodTP', 'MethodTR', 'MethodWST']]]
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
        Union[HTTPValidationError, Union['MethodAD', 'MethodCD', 'MethodCPT', 'MethodDEF', 'MethodDP', 'MethodDT', 'MethodESA', 'MethodINC', 'MethodIW', 'MethodOTHER', 'MethodPT', 'MethodPZ', 'MethodRCD', 'MethodRO', 'MethodRP', 'MethodRS', 'MethodRWS', 'MethodSA', 'MethodSLB', 'MethodSPT', 'MethodSRS', 'MethodSS', 'MethodSTI', 'MethodSVT', 'MethodTOT', 'MethodTP', 'MethodTR', 'MethodWST']]
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
        Response[Union[HTTPValidationError, Union['MethodAD', 'MethodCD', 'MethodCPT', 'MethodDEF', 'MethodDP', 'MethodDT', 'MethodESA', 'MethodINC', 'MethodIW', 'MethodOTHER', 'MethodPT', 'MethodPZ', 'MethodRCD', 'MethodRO', 'MethodRP', 'MethodRS', 'MethodRWS', 'MethodSA', 'MethodSLB', 'MethodSPT', 'MethodSRS', 'MethodSS', 'MethodSTI', 'MethodSVT', 'MethodTOT', 'MethodTP', 'MethodTR', 'MethodWST']]]
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
        Union[HTTPValidationError, Union['MethodAD', 'MethodCD', 'MethodCPT', 'MethodDEF', 'MethodDP', 'MethodDT', 'MethodESA', 'MethodINC', 'MethodIW', 'MethodOTHER', 'MethodPT', 'MethodPZ', 'MethodRCD', 'MethodRO', 'MethodRP', 'MethodRS', 'MethodRWS', 'MethodSA', 'MethodSLB', 'MethodSPT', 'MethodSRS', 'MethodSS', 'MethodSTI', 'MethodSVT', 'MethodTOT', 'MethodTP', 'MethodTR', 'MethodWST']]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            location_id=location_id,
            client=client,
            body=body,
        )
    ).parsed
