from http import HTTPStatus
from typing import Any
from urllib.parse import quote
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
    body: list[
        MethodADCreate
        | MethodCDCreate
        | MethodCPTCreate
        | MethodDEFCreate
        | MethodDPCreate
        | MethodDTCreate
        | MethodESACreate
        | MethodINCCreate
        | MethodIWCreate
        | MethodOTHERCreate
        | MethodPTCreate
        | MethodPZCreate
        | MethodRCDCreate
        | MethodROCreate
        | MethodRPCreate
        | MethodRSCreate
        | MethodRWSCreate
        | MethodSACreate
        | MethodSLBCreate
        | MethodSPTCreate
        | MethodSRSCreate
        | MethodSSCreate
        | MethodSTICreate
        | MethodSVTCreate
        | MethodTOTCreate
        | MethodTPCreate
        | MethodTRCreate
        | MethodWSTCreate
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/projects/{project_id}/locations/{location_id}/methods/batch".format(
            project_id=quote(str(project_id), safe=""),
            location_id=quote(str(location_id), safe=""),
        ),
    }

    _kwargs["json"] = []
    for body_item_data in body:
        body_item: dict[str, Any]
        if isinstance(body_item_data, MethodADCreate):
            body_item = body_item_data.to_dict()
        elif isinstance(body_item_data, MethodCDCreate):
            body_item = body_item_data.to_dict()
        elif isinstance(body_item_data, MethodCPTCreate):
            body_item = body_item_data.to_dict()
        elif isinstance(body_item_data, MethodDPCreate):
            body_item = body_item_data.to_dict()
        elif isinstance(body_item_data, MethodDTCreate):
            body_item = body_item_data.to_dict()
        elif isinstance(body_item_data, MethodESACreate):
            body_item = body_item_data.to_dict()
        elif isinstance(body_item_data, MethodINCCreate):
            body_item = body_item_data.to_dict()
        elif isinstance(body_item_data, MethodIWCreate):
            body_item = body_item_data.to_dict()
        elif isinstance(body_item_data, MethodOTHERCreate):
            body_item = body_item_data.to_dict()
        elif isinstance(body_item_data, MethodPTCreate):
            body_item = body_item_data.to_dict()
        elif isinstance(body_item_data, MethodPZCreate):
            body_item = body_item_data.to_dict()
        elif isinstance(body_item_data, MethodRCDCreate):
            body_item = body_item_data.to_dict()
        elif isinstance(body_item_data, MethodROCreate):
            body_item = body_item_data.to_dict()
        elif isinstance(body_item_data, MethodRPCreate):
            body_item = body_item_data.to_dict()
        elif isinstance(body_item_data, MethodRSCreate):
            body_item = body_item_data.to_dict()
        elif isinstance(body_item_data, MethodRWSCreate):
            body_item = body_item_data.to_dict()
        elif isinstance(body_item_data, MethodSACreate):
            body_item = body_item_data.to_dict()
        elif isinstance(body_item_data, MethodSLBCreate):
            body_item = body_item_data.to_dict()
        elif isinstance(body_item_data, MethodSPTCreate):
            body_item = body_item_data.to_dict()
        elif isinstance(body_item_data, MethodDEFCreate):
            body_item = body_item_data.to_dict()
        elif isinstance(body_item_data, MethodSRSCreate):
            body_item = body_item_data.to_dict()
        elif isinstance(body_item_data, MethodSSCreate):
            body_item = body_item_data.to_dict()
        elif isinstance(body_item_data, MethodSTICreate):
            body_item = body_item_data.to_dict()
        elif isinstance(body_item_data, MethodSVTCreate):
            body_item = body_item_data.to_dict()
        elif isinstance(body_item_data, MethodTOTCreate):
            body_item = body_item_data.to_dict()
        elif isinstance(body_item_data, MethodTPCreate):
            body_item = body_item_data.to_dict()
        elif isinstance(body_item_data, MethodTRCreate):
            body_item = body_item_data.to_dict()
        else:
            body_item = body_item_data.to_dict()

        _kwargs["json"].append(body_item)

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    HTTPValidationError
    | list[
        MethodAD
        | MethodCD
        | MethodCPT
        | MethodDEF
        | MethodDP
        | MethodDT
        | MethodESA
        | MethodINC
        | MethodIW
        | MethodOTHER
        | MethodPT
        | MethodPZ
        | MethodRCD
        | MethodRO
        | MethodRP
        | MethodRS
        | MethodRWS
        | MethodSA
        | MethodSLB
        | MethodSPT
        | MethodSRS
        | MethodSS
        | MethodSTI
        | MethodSVT
        | MethodTOT
        | MethodTP
        | MethodTR
        | MethodWST
    ]
    | None
):
    if response.status_code == 201:
        response_201 = []
        _response_201 = response.json()
        for response_201_item_data in _response_201:

            def _parse_response_201_item(
                data: object,
            ) -> (
                MethodAD
                | MethodCD
                | MethodCPT
                | MethodDEF
                | MethodDP
                | MethodDT
                | MethodESA
                | MethodINC
                | MethodIW
                | MethodOTHER
                | MethodPT
                | MethodPZ
                | MethodRCD
                | MethodRO
                | MethodRP
                | MethodRS
                | MethodRWS
                | MethodSA
                | MethodSLB
                | MethodSPT
                | MethodSRS
                | MethodSS
                | MethodSTI
                | MethodSVT
                | MethodTOT
                | MethodTP
                | MethodTR
                | MethodWST
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_201_item_type_0 = MethodCPT.from_dict(data)

                    return response_201_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_201_item_type_1 = MethodTOT.from_dict(data)

                    return response_201_item_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_201_item_type_2 = MethodRP.from_dict(data)

                    return response_201_item_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_201_item_type_3 = MethodSA.from_dict(data)

                    return response_201_item_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_201_item_type_4 = MethodPZ.from_dict(data)

                    return response_201_item_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_201_item_type_5 = MethodSS.from_dict(data)

                    return response_201_item_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_201_item_type_6 = MethodRWS.from_dict(data)

                    return response_201_item_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_201_item_type_7 = MethodRCD.from_dict(data)

                    return response_201_item_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_201_item_type_8 = MethodRS.from_dict(data)

                    return response_201_item_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_201_item_type_9 = MethodSVT.from_dict(data)

                    return response_201_item_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_201_item_type_10 = MethodSPT.from_dict(data)

                    return response_201_item_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_201_item_type_11 = MethodCD.from_dict(data)

                    return response_201_item_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_201_item_type_12 = MethodTP.from_dict(data)

                    return response_201_item_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_201_item_type_13 = MethodPT.from_dict(data)

                    return response_201_item_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_201_item_type_14 = MethodESA.from_dict(data)

                    return response_201_item_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_201_item_type_15 = MethodTR.from_dict(data)

                    return response_201_item_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_201_item_type_16 = MethodAD.from_dict(data)

                    return response_201_item_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_201_item_type_17 = MethodRO.from_dict(data)

                    return response_201_item_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_201_item_type_18 = MethodINC.from_dict(data)

                    return response_201_item_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_201_item_type_19 = MethodDEF.from_dict(data)

                    return response_201_item_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_201_item_type_20 = MethodIW.from_dict(data)

                    return response_201_item_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_201_item_type_21 = MethodDT.from_dict(data)

                    return response_201_item_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_201_item_type_22 = MethodOTHER.from_dict(data)

                    return response_201_item_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_201_item_type_23 = MethodSRS.from_dict(data)

                    return response_201_item_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_201_item_type_24 = MethodDP.from_dict(data)

                    return response_201_item_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_201_item_type_25 = MethodWST.from_dict(data)

                    return response_201_item_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_201_item_type_26 = MethodSLB.from_dict(data)

                    return response_201_item_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_item_type_27 = MethodSTI.from_dict(data)

                return response_201_item_type_27

            response_201_item = _parse_response_201_item(response_201_item_data)

            response_201.append(response_201_item)

        return response_201

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    HTTPValidationError
    | list[
        MethodAD
        | MethodCD
        | MethodCPT
        | MethodDEF
        | MethodDP
        | MethodDT
        | MethodESA
        | MethodINC
        | MethodIW
        | MethodOTHER
        | MethodPT
        | MethodPZ
        | MethodRCD
        | MethodRO
        | MethodRP
        | MethodRS
        | MethodRWS
        | MethodSA
        | MethodSLB
        | MethodSPT
        | MethodSRS
        | MethodSS
        | MethodSTI
        | MethodSVT
        | MethodTOT
        | MethodTP
        | MethodTR
        | MethodWST
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
    body: list[
        MethodADCreate
        | MethodCDCreate
        | MethodCPTCreate
        | MethodDEFCreate
        | MethodDPCreate
        | MethodDTCreate
        | MethodESACreate
        | MethodINCCreate
        | MethodIWCreate
        | MethodOTHERCreate
        | MethodPTCreate
        | MethodPZCreate
        | MethodRCDCreate
        | MethodROCreate
        | MethodRPCreate
        | MethodRSCreate
        | MethodRWSCreate
        | MethodSACreate
        | MethodSLBCreate
        | MethodSPTCreate
        | MethodSRSCreate
        | MethodSSCreate
        | MethodSTICreate
        | MethodSVTCreate
        | MethodTOTCreate
        | MethodTPCreate
        | MethodTRCreate
        | MethodWSTCreate
    ],
) -> Response[
    HTTPValidationError
    | list[
        MethodAD
        | MethodCD
        | MethodCPT
        | MethodDEF
        | MethodDP
        | MethodDT
        | MethodESA
        | MethodINC
        | MethodIW
        | MethodOTHER
        | MethodPT
        | MethodPZ
        | MethodRCD
        | MethodRO
        | MethodRP
        | MethodRS
        | MethodRWS
        | MethodSA
        | MethodSLB
        | MethodSPT
        | MethodSRS
        | MethodSS
        | MethodSTI
        | MethodSVT
        | MethodTOT
        | MethodTP
        | MethodTR
        | MethodWST
    ]
]:
    """Add Methods To Location Batch

     Add multiple methods to one location in a single request.

    Args:
        project_id (str):
        location_id (UUID):
        body (list[MethodADCreate | MethodCDCreate | MethodCPTCreate | MethodDEFCreate |
            MethodDPCreate | MethodDTCreate | MethodESACreate | MethodINCCreate | MethodIWCreate |
            MethodOTHERCreate | MethodPTCreate | MethodPZCreate | MethodRCDCreate | MethodROCreate |
            MethodRPCreate | MethodRSCreate | MethodRWSCreate | MethodSACreate | MethodSLBCreate |
            MethodSPTCreate | MethodSRSCreate | MethodSSCreate | MethodSTICreate | MethodSVTCreate |
            MethodTOTCreate | MethodTPCreate | MethodTRCreate | MethodWSTCreate]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[MethodAD | MethodCD | MethodCPT | MethodDEF | MethodDP | MethodDT | MethodESA | MethodINC | MethodIW | MethodOTHER | MethodPT | MethodPZ | MethodRCD | MethodRO | MethodRP | MethodRS | MethodRWS | MethodSA | MethodSLB | MethodSPT | MethodSRS | MethodSS | MethodSTI | MethodSVT | MethodTOT | MethodTP | MethodTR | MethodWST]]
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
    body: list[
        MethodADCreate
        | MethodCDCreate
        | MethodCPTCreate
        | MethodDEFCreate
        | MethodDPCreate
        | MethodDTCreate
        | MethodESACreate
        | MethodINCCreate
        | MethodIWCreate
        | MethodOTHERCreate
        | MethodPTCreate
        | MethodPZCreate
        | MethodRCDCreate
        | MethodROCreate
        | MethodRPCreate
        | MethodRSCreate
        | MethodRWSCreate
        | MethodSACreate
        | MethodSLBCreate
        | MethodSPTCreate
        | MethodSRSCreate
        | MethodSSCreate
        | MethodSTICreate
        | MethodSVTCreate
        | MethodTOTCreate
        | MethodTPCreate
        | MethodTRCreate
        | MethodWSTCreate
    ],
) -> (
    HTTPValidationError
    | list[
        MethodAD
        | MethodCD
        | MethodCPT
        | MethodDEF
        | MethodDP
        | MethodDT
        | MethodESA
        | MethodINC
        | MethodIW
        | MethodOTHER
        | MethodPT
        | MethodPZ
        | MethodRCD
        | MethodRO
        | MethodRP
        | MethodRS
        | MethodRWS
        | MethodSA
        | MethodSLB
        | MethodSPT
        | MethodSRS
        | MethodSS
        | MethodSTI
        | MethodSVT
        | MethodTOT
        | MethodTP
        | MethodTR
        | MethodWST
    ]
    | None
):
    """Add Methods To Location Batch

     Add multiple methods to one location in a single request.

    Args:
        project_id (str):
        location_id (UUID):
        body (list[MethodADCreate | MethodCDCreate | MethodCPTCreate | MethodDEFCreate |
            MethodDPCreate | MethodDTCreate | MethodESACreate | MethodINCCreate | MethodIWCreate |
            MethodOTHERCreate | MethodPTCreate | MethodPZCreate | MethodRCDCreate | MethodROCreate |
            MethodRPCreate | MethodRSCreate | MethodRWSCreate | MethodSACreate | MethodSLBCreate |
            MethodSPTCreate | MethodSRSCreate | MethodSSCreate | MethodSTICreate | MethodSVTCreate |
            MethodTOTCreate | MethodTPCreate | MethodTRCreate | MethodWSTCreate]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[MethodAD | MethodCD | MethodCPT | MethodDEF | MethodDP | MethodDT | MethodESA | MethodINC | MethodIW | MethodOTHER | MethodPT | MethodPZ | MethodRCD | MethodRO | MethodRP | MethodRS | MethodRWS | MethodSA | MethodSLB | MethodSPT | MethodSRS | MethodSS | MethodSTI | MethodSVT | MethodTOT | MethodTP | MethodTR | MethodWST]
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
    body: list[
        MethodADCreate
        | MethodCDCreate
        | MethodCPTCreate
        | MethodDEFCreate
        | MethodDPCreate
        | MethodDTCreate
        | MethodESACreate
        | MethodINCCreate
        | MethodIWCreate
        | MethodOTHERCreate
        | MethodPTCreate
        | MethodPZCreate
        | MethodRCDCreate
        | MethodROCreate
        | MethodRPCreate
        | MethodRSCreate
        | MethodRWSCreate
        | MethodSACreate
        | MethodSLBCreate
        | MethodSPTCreate
        | MethodSRSCreate
        | MethodSSCreate
        | MethodSTICreate
        | MethodSVTCreate
        | MethodTOTCreate
        | MethodTPCreate
        | MethodTRCreate
        | MethodWSTCreate
    ],
) -> Response[
    HTTPValidationError
    | list[
        MethodAD
        | MethodCD
        | MethodCPT
        | MethodDEF
        | MethodDP
        | MethodDT
        | MethodESA
        | MethodINC
        | MethodIW
        | MethodOTHER
        | MethodPT
        | MethodPZ
        | MethodRCD
        | MethodRO
        | MethodRP
        | MethodRS
        | MethodRWS
        | MethodSA
        | MethodSLB
        | MethodSPT
        | MethodSRS
        | MethodSS
        | MethodSTI
        | MethodSVT
        | MethodTOT
        | MethodTP
        | MethodTR
        | MethodWST
    ]
]:
    """Add Methods To Location Batch

     Add multiple methods to one location in a single request.

    Args:
        project_id (str):
        location_id (UUID):
        body (list[MethodADCreate | MethodCDCreate | MethodCPTCreate | MethodDEFCreate |
            MethodDPCreate | MethodDTCreate | MethodESACreate | MethodINCCreate | MethodIWCreate |
            MethodOTHERCreate | MethodPTCreate | MethodPZCreate | MethodRCDCreate | MethodROCreate |
            MethodRPCreate | MethodRSCreate | MethodRWSCreate | MethodSACreate | MethodSLBCreate |
            MethodSPTCreate | MethodSRSCreate | MethodSSCreate | MethodSTICreate | MethodSVTCreate |
            MethodTOTCreate | MethodTPCreate | MethodTRCreate | MethodWSTCreate]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[MethodAD | MethodCD | MethodCPT | MethodDEF | MethodDP | MethodDT | MethodESA | MethodINC | MethodIW | MethodOTHER | MethodPT | MethodPZ | MethodRCD | MethodRO | MethodRP | MethodRS | MethodRWS | MethodSA | MethodSLB | MethodSPT | MethodSRS | MethodSS | MethodSTI | MethodSVT | MethodTOT | MethodTP | MethodTR | MethodWST]]
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
    body: list[
        MethodADCreate
        | MethodCDCreate
        | MethodCPTCreate
        | MethodDEFCreate
        | MethodDPCreate
        | MethodDTCreate
        | MethodESACreate
        | MethodINCCreate
        | MethodIWCreate
        | MethodOTHERCreate
        | MethodPTCreate
        | MethodPZCreate
        | MethodRCDCreate
        | MethodROCreate
        | MethodRPCreate
        | MethodRSCreate
        | MethodRWSCreate
        | MethodSACreate
        | MethodSLBCreate
        | MethodSPTCreate
        | MethodSRSCreate
        | MethodSSCreate
        | MethodSTICreate
        | MethodSVTCreate
        | MethodTOTCreate
        | MethodTPCreate
        | MethodTRCreate
        | MethodWSTCreate
    ],
) -> (
    HTTPValidationError
    | list[
        MethodAD
        | MethodCD
        | MethodCPT
        | MethodDEF
        | MethodDP
        | MethodDT
        | MethodESA
        | MethodINC
        | MethodIW
        | MethodOTHER
        | MethodPT
        | MethodPZ
        | MethodRCD
        | MethodRO
        | MethodRP
        | MethodRS
        | MethodRWS
        | MethodSA
        | MethodSLB
        | MethodSPT
        | MethodSRS
        | MethodSS
        | MethodSTI
        | MethodSVT
        | MethodTOT
        | MethodTP
        | MethodTR
        | MethodWST
    ]
    | None
):
    """Add Methods To Location Batch

     Add multiple methods to one location in a single request.

    Args:
        project_id (str):
        location_id (UUID):
        body (list[MethodADCreate | MethodCDCreate | MethodCPTCreate | MethodDEFCreate |
            MethodDPCreate | MethodDTCreate | MethodESACreate | MethodINCCreate | MethodIWCreate |
            MethodOTHERCreate | MethodPTCreate | MethodPZCreate | MethodRCDCreate | MethodROCreate |
            MethodRPCreate | MethodRSCreate | MethodRWSCreate | MethodSACreate | MethodSLBCreate |
            MethodSPTCreate | MethodSRSCreate | MethodSSCreate | MethodSTICreate | MethodSVTCreate |
            MethodTOTCreate | MethodTPCreate | MethodTRCreate | MethodWSTCreate]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[MethodAD | MethodCD | MethodCPT | MethodDEF | MethodDP | MethodDT | MethodESA | MethodINC | MethodIW | MethodOTHER | MethodPT | MethodPZ | MethodRCD | MethodRO | MethodRP | MethodRS | MethodRWS | MethodSA | MethodSLB | MethodSPT | MethodSRS | MethodSS | MethodSTI | MethodSVT | MethodTOT | MethodTP | MethodTR | MethodWST]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            location_id=location_id,
            client=client,
            body=body,
        )
    ).parsed
