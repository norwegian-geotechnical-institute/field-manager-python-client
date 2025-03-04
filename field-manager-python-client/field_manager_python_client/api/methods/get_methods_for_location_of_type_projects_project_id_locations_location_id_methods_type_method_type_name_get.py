from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.method_ad import MethodAD
from ...models.method_cd import MethodCD
from ...models.method_cpt import MethodCPT
from ...models.method_def import MethodDEF
from ...models.method_dp import MethodDP
from ...models.method_dt import MethodDT
from ...models.method_esa import MethodESA
from ...models.method_inc import MethodINC
from ...models.method_iw import MethodIW
from ...models.method_other import MethodOTHER
from ...models.method_pt import MethodPT
from ...models.method_pz import MethodPZ
from ...models.method_rcd import MethodRCD
from ...models.method_ro import MethodRO
from ...models.method_rp import MethodRP
from ...models.method_rs import MethodRS
from ...models.method_rws import MethodRWS
from ...models.method_sa import MethodSA
from ...models.method_slb import MethodSLB
from ...models.method_spt import MethodSPT
from ...models.method_srs import MethodSRS
from ...models.method_ss import MethodSS
from ...models.method_sti import MethodSTI
from ...models.method_svt import MethodSVT
from ...models.method_tot import MethodTOT
from ...models.method_tp import MethodTP
from ...models.method_tr import MethodTR
from ...models.method_type_enum_str import MethodTypeEnumStr
from ...models.method_wst import MethodWST
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    location_id: UUID,
    method_type_name: MethodTypeEnumStr,
    *,
    skip: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 100,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["skip"] = skip

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/projects/{project_id}/locations/{location_id}/methods/type/{method_type_name}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        HTTPValidationError,
        list[
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
            ]
        ],
    ]
]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:

            def _parse_response_200_item(
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
                    response_200_item_type_0 = MethodCPT.from_dict(data)

                    return response_200_item_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_200_item_type_1 = MethodTOT.from_dict(data)

                    return response_200_item_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_200_item_type_2 = MethodRP.from_dict(data)

                    return response_200_item_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_200_item_type_3 = MethodSA.from_dict(data)

                    return response_200_item_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_200_item_type_4 = MethodPZ.from_dict(data)

                    return response_200_item_type_4
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_200_item_type_5 = MethodSS.from_dict(data)

                    return response_200_item_type_5
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_200_item_type_6 = MethodRWS.from_dict(data)

                    return response_200_item_type_6
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_200_item_type_7 = MethodRCD.from_dict(data)

                    return response_200_item_type_7
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_200_item_type_8 = MethodRS.from_dict(data)

                    return response_200_item_type_8
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_200_item_type_9 = MethodSVT.from_dict(data)

                    return response_200_item_type_9
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_200_item_type_10 = MethodSPT.from_dict(data)

                    return response_200_item_type_10
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_200_item_type_11 = MethodCD.from_dict(data)

                    return response_200_item_type_11
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_200_item_type_12 = MethodTP.from_dict(data)

                    return response_200_item_type_12
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_200_item_type_13 = MethodPT.from_dict(data)

                    return response_200_item_type_13
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_200_item_type_14 = MethodESA.from_dict(data)

                    return response_200_item_type_14
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_200_item_type_15 = MethodTR.from_dict(data)

                    return response_200_item_type_15
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_200_item_type_16 = MethodAD.from_dict(data)

                    return response_200_item_type_16
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_200_item_type_17 = MethodRO.from_dict(data)

                    return response_200_item_type_17
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_200_item_type_18 = MethodINC.from_dict(data)

                    return response_200_item_type_18
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_200_item_type_19 = MethodDEF.from_dict(data)

                    return response_200_item_type_19
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_200_item_type_20 = MethodIW.from_dict(data)

                    return response_200_item_type_20
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_200_item_type_21 = MethodDT.from_dict(data)

                    return response_200_item_type_21
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_200_item_type_22 = MethodOTHER.from_dict(data)

                    return response_200_item_type_22
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_200_item_type_23 = MethodSRS.from_dict(data)

                    return response_200_item_type_23
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_200_item_type_24 = MethodDP.from_dict(data)

                    return response_200_item_type_24
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_200_item_type_25 = MethodWST.from_dict(data)

                    return response_200_item_type_25
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_200_item_type_26 = MethodSLB.from_dict(data)

                    return response_200_item_type_26
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_item_type_27 = MethodSTI.from_dict(data)

                return response_200_item_type_27

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


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        HTTPValidationError,
        list[
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
            ]
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
    method_type_name: MethodTypeEnumStr,
    *,
    client: AuthenticatedClient,
    skip: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 100,
) -> Response[
    Union[
        HTTPValidationError,
        list[
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
            ]
        ],
    ]
]:
    """Get Methods For Location Of Type

     Get all methods of type `method_type_name` from location.

    Args:
        project_id (str):
        location_id (UUID):
        method_type_name (MethodTypeEnumStr):
        skip (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, list[Union['MethodAD', 'MethodCD', 'MethodCPT', 'MethodDEF', 'MethodDP', 'MethodDT', 'MethodESA', 'MethodINC', 'MethodIW', 'MethodOTHER', 'MethodPT', 'MethodPZ', 'MethodRCD', 'MethodRO', 'MethodRP', 'MethodRS', 'MethodRWS', 'MethodSA', 'MethodSLB', 'MethodSPT', 'MethodSRS', 'MethodSS', 'MethodSTI', 'MethodSVT', 'MethodTOT', 'MethodTP', 'MethodTR', 'MethodWST']]]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        location_id=location_id,
        method_type_name=method_type_name,
        skip=skip,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    location_id: UUID,
    method_type_name: MethodTypeEnumStr,
    *,
    client: AuthenticatedClient,
    skip: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 100,
) -> Optional[
    Union[
        HTTPValidationError,
        list[
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
            ]
        ],
    ]
]:
    """Get Methods For Location Of Type

     Get all methods of type `method_type_name` from location.

    Args:
        project_id (str):
        location_id (UUID):
        method_type_name (MethodTypeEnumStr):
        skip (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, list[Union['MethodAD', 'MethodCD', 'MethodCPT', 'MethodDEF', 'MethodDP', 'MethodDT', 'MethodESA', 'MethodINC', 'MethodIW', 'MethodOTHER', 'MethodPT', 'MethodPZ', 'MethodRCD', 'MethodRO', 'MethodRP', 'MethodRS', 'MethodRWS', 'MethodSA', 'MethodSLB', 'MethodSPT', 'MethodSRS', 'MethodSS', 'MethodSTI', 'MethodSVT', 'MethodTOT', 'MethodTP', 'MethodTR', 'MethodWST']]]
    """

    return sync_detailed(
        project_id=project_id,
        location_id=location_id,
        method_type_name=method_type_name,
        client=client,
        skip=skip,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    location_id: UUID,
    method_type_name: MethodTypeEnumStr,
    *,
    client: AuthenticatedClient,
    skip: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 100,
) -> Response[
    Union[
        HTTPValidationError,
        list[
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
            ]
        ],
    ]
]:
    """Get Methods For Location Of Type

     Get all methods of type `method_type_name` from location.

    Args:
        project_id (str):
        location_id (UUID):
        method_type_name (MethodTypeEnumStr):
        skip (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, list[Union['MethodAD', 'MethodCD', 'MethodCPT', 'MethodDEF', 'MethodDP', 'MethodDT', 'MethodESA', 'MethodINC', 'MethodIW', 'MethodOTHER', 'MethodPT', 'MethodPZ', 'MethodRCD', 'MethodRO', 'MethodRP', 'MethodRS', 'MethodRWS', 'MethodSA', 'MethodSLB', 'MethodSPT', 'MethodSRS', 'MethodSS', 'MethodSTI', 'MethodSVT', 'MethodTOT', 'MethodTP', 'MethodTR', 'MethodWST']]]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        location_id=location_id,
        method_type_name=method_type_name,
        skip=skip,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    location_id: UUID,
    method_type_name: MethodTypeEnumStr,
    *,
    client: AuthenticatedClient,
    skip: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 100,
) -> Optional[
    Union[
        HTTPValidationError,
        list[
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
            ]
        ],
    ]
]:
    """Get Methods For Location Of Type

     Get all methods of type `method_type_name` from location.

    Args:
        project_id (str):
        location_id (UUID):
        method_type_name (MethodTypeEnumStr):
        skip (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, list[Union['MethodAD', 'MethodCD', 'MethodCPT', 'MethodDEF', 'MethodDP', 'MethodDT', 'MethodESA', 'MethodINC', 'MethodIW', 'MethodOTHER', 'MethodPT', 'MethodPZ', 'MethodRCD', 'MethodRO', 'MethodRP', 'MethodRS', 'MethodRWS', 'MethodSA', 'MethodSLB', 'MethodSPT', 'MethodSRS', 'MethodSS', 'MethodSTI', 'MethodSVT', 'MethodTOT', 'MethodTP', 'MethodTR', 'MethodWST']]]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            location_id=location_id,
            method_type_name=method_type_name,
            client=client,
            skip=skip,
            limit=limit,
        )
    ).parsed
