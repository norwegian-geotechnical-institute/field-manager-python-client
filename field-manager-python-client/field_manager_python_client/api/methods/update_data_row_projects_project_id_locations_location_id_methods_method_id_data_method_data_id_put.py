from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.method_cpt_data import MethodCPTData
from ...models.method_cpt_data_update import MethodCPTDataUpdate
from ...models.method_dp_data import MethodDPData
from ...models.method_dt_data import MethodDTData
from ...models.method_dt_data_update import MethodDTDataUpdate
from ...models.method_pz_data import MethodPZData
from ...models.method_pz_data_update import MethodPZDataUpdate
from ...models.method_rcd_data import MethodRCDData
from ...models.method_rcd_data_update import MethodRCDDataUpdate
from ...models.method_rp_data import MethodRPData
from ...models.method_rp_data_update import MethodRPDataUpdate
from ...models.method_srs_data import MethodSRSData
from ...models.method_srs_data_update import MethodSRSDataUpdate
from ...models.method_ss_data import MethodSSData
from ...models.method_ss_data_update import MethodSSDataUpdate
from ...models.method_svt_data import MethodSVTData
from ...models.method_svt_data_update import MethodSVTDataUpdate
from ...models.method_tot_data import MethodTOTData
from ...models.method_tot_data_update import MethodTOTDataUpdate
from ...models.method_tr_data import MethodTRData
from ...models.method_tr_data_update import MethodTRDataUpdate
from ...models.method_wst_data import MethodWSTData
from ...models.method_wst_data_update import MethodWSTDataUpdate
from ...types import Response


def _get_kwargs(
    project_id: str,
    location_id: UUID,
    method_id: UUID,
    method_data_id: UUID,
    *,
    body: Union[
        "MethodCPTDataUpdate",
        "MethodDTDataUpdate",
        "MethodPZDataUpdate",
        "MethodRCDDataUpdate",
        "MethodRPDataUpdate",
        "MethodSRSDataUpdate",
        "MethodSSDataUpdate",
        "MethodSVTDataUpdate",
        "MethodTOTDataUpdate",
        "MethodTRDataUpdate",
        "MethodWSTDataUpdate",
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/projects/{project_id}/locations/{location_id}/methods/{method_id}/data/{method_data_id}",
    }

    _body: dict[str, Any]
    if isinstance(body, MethodCPTDataUpdate):
        _body = body.to_dict()
    elif isinstance(body, MethodDTDataUpdate):
        _body = body.to_dict()
    elif isinstance(body, MethodPZDataUpdate):
        _body = body.to_dict()
    elif isinstance(body, MethodRCDDataUpdate):
        _body = body.to_dict()
    elif isinstance(body, MethodRPDataUpdate):
        _body = body.to_dict()
    elif isinstance(body, MethodSRSDataUpdate):
        _body = body.to_dict()
    elif isinstance(body, MethodSSDataUpdate):
        _body = body.to_dict()
    elif isinstance(body, MethodSVTDataUpdate):
        _body = body.to_dict()
    elif isinstance(body, MethodTOTDataUpdate):
        _body = body.to_dict()
    elif isinstance(body, MethodTRDataUpdate):
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
            "MethodCPTData",
            "MethodDPData",
            "MethodDTData",
            "MethodPZData",
            "MethodRCDData",
            "MethodRPData",
            "MethodSRSData",
            "MethodSSData",
            "MethodSVTData",
            "MethodTOTData",
            "MethodTRData",
            "MethodWSTData",
        ],
    ]
]:
    if response.status_code == 200:

        def _parse_response_200(
            data: object,
        ) -> Union[
            "MethodCPTData",
            "MethodDPData",
            "MethodDTData",
            "MethodPZData",
            "MethodRCDData",
            "MethodRPData",
            "MethodSRSData",
            "MethodSSData",
            "MethodSVTData",
            "MethodTOTData",
            "MethodTRData",
            "MethodWSTData",
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = MethodCPTData.from_dict(data)

                return response_200_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_1 = MethodDPData.from_dict(data)

                return response_200_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_2 = MethodDTData.from_dict(data)

                return response_200_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_3 = MethodPZData.from_dict(data)

                return response_200_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_4 = MethodRCDData.from_dict(data)

                return response_200_type_4
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_5 = MethodRPData.from_dict(data)

                return response_200_type_5
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_6 = MethodSSData.from_dict(data)

                return response_200_type_6
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_7 = MethodSRSData.from_dict(data)

                return response_200_type_7
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_8 = MethodSVTData.from_dict(data)

                return response_200_type_8
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_9 = MethodTOTData.from_dict(data)

                return response_200_type_9
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_10 = MethodTRData.from_dict(data)

                return response_200_type_10
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_11 = MethodWSTData.from_dict(data)

            return response_200_type_11

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
            "MethodCPTData",
            "MethodDPData",
            "MethodDTData",
            "MethodPZData",
            "MethodRCDData",
            "MethodRPData",
            "MethodSRSData",
            "MethodSSData",
            "MethodSVTData",
            "MethodTOTData",
            "MethodTRData",
            "MethodWSTData",
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
    method_data_id: UUID,
    *,
    client: AuthenticatedClient,
    body: Union[
        "MethodCPTDataUpdate",
        "MethodDTDataUpdate",
        "MethodPZDataUpdate",
        "MethodRCDDataUpdate",
        "MethodRPDataUpdate",
        "MethodSRSDataUpdate",
        "MethodSSDataUpdate",
        "MethodSVTDataUpdate",
        "MethodTOTDataUpdate",
        "MethodTRDataUpdate",
        "MethodWSTDataUpdate",
    ],
) -> Response[
    Union[
        HTTPValidationError,
        Union[
            "MethodCPTData",
            "MethodDPData",
            "MethodDTData",
            "MethodPZData",
            "MethodRCDData",
            "MethodRPData",
            "MethodSRSData",
            "MethodSSData",
            "MethodSVTData",
            "MethodTOTData",
            "MethodTRData",
            "MethodWSTData",
        ],
    ]
]:
    """Update Data Row

     Update a method's single data line

    Args:
        project_id (str):
        location_id (UUID):
        method_id (UUID):
        method_data_id (UUID):
        body (Union['MethodCPTDataUpdate', 'MethodDTDataUpdate', 'MethodPZDataUpdate',
            'MethodRCDDataUpdate', 'MethodRPDataUpdate', 'MethodSRSDataUpdate', 'MethodSSDataUpdate',
            'MethodSVTDataUpdate', 'MethodTOTDataUpdate', 'MethodTRDataUpdate',
            'MethodWSTDataUpdate']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, Union['MethodCPTData', 'MethodDPData', 'MethodDTData', 'MethodPZData', 'MethodRCDData', 'MethodRPData', 'MethodSRSData', 'MethodSSData', 'MethodSVTData', 'MethodTOTData', 'MethodTRData', 'MethodWSTData']]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        location_id=location_id,
        method_id=method_id,
        method_data_id=method_data_id,
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
    method_data_id: UUID,
    *,
    client: AuthenticatedClient,
    body: Union[
        "MethodCPTDataUpdate",
        "MethodDTDataUpdate",
        "MethodPZDataUpdate",
        "MethodRCDDataUpdate",
        "MethodRPDataUpdate",
        "MethodSRSDataUpdate",
        "MethodSSDataUpdate",
        "MethodSVTDataUpdate",
        "MethodTOTDataUpdate",
        "MethodTRDataUpdate",
        "MethodWSTDataUpdate",
    ],
) -> Optional[
    Union[
        HTTPValidationError,
        Union[
            "MethodCPTData",
            "MethodDPData",
            "MethodDTData",
            "MethodPZData",
            "MethodRCDData",
            "MethodRPData",
            "MethodSRSData",
            "MethodSSData",
            "MethodSVTData",
            "MethodTOTData",
            "MethodTRData",
            "MethodWSTData",
        ],
    ]
]:
    """Update Data Row

     Update a method's single data line

    Args:
        project_id (str):
        location_id (UUID):
        method_id (UUID):
        method_data_id (UUID):
        body (Union['MethodCPTDataUpdate', 'MethodDTDataUpdate', 'MethodPZDataUpdate',
            'MethodRCDDataUpdate', 'MethodRPDataUpdate', 'MethodSRSDataUpdate', 'MethodSSDataUpdate',
            'MethodSVTDataUpdate', 'MethodTOTDataUpdate', 'MethodTRDataUpdate',
            'MethodWSTDataUpdate']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, Union['MethodCPTData', 'MethodDPData', 'MethodDTData', 'MethodPZData', 'MethodRCDData', 'MethodRPData', 'MethodSRSData', 'MethodSSData', 'MethodSVTData', 'MethodTOTData', 'MethodTRData', 'MethodWSTData']]
    """

    return sync_detailed(
        project_id=project_id,
        location_id=location_id,
        method_id=method_id,
        method_data_id=method_data_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    location_id: UUID,
    method_id: UUID,
    method_data_id: UUID,
    *,
    client: AuthenticatedClient,
    body: Union[
        "MethodCPTDataUpdate",
        "MethodDTDataUpdate",
        "MethodPZDataUpdate",
        "MethodRCDDataUpdate",
        "MethodRPDataUpdate",
        "MethodSRSDataUpdate",
        "MethodSSDataUpdate",
        "MethodSVTDataUpdate",
        "MethodTOTDataUpdate",
        "MethodTRDataUpdate",
        "MethodWSTDataUpdate",
    ],
) -> Response[
    Union[
        HTTPValidationError,
        Union[
            "MethodCPTData",
            "MethodDPData",
            "MethodDTData",
            "MethodPZData",
            "MethodRCDData",
            "MethodRPData",
            "MethodSRSData",
            "MethodSSData",
            "MethodSVTData",
            "MethodTOTData",
            "MethodTRData",
            "MethodWSTData",
        ],
    ]
]:
    """Update Data Row

     Update a method's single data line

    Args:
        project_id (str):
        location_id (UUID):
        method_id (UUID):
        method_data_id (UUID):
        body (Union['MethodCPTDataUpdate', 'MethodDTDataUpdate', 'MethodPZDataUpdate',
            'MethodRCDDataUpdate', 'MethodRPDataUpdate', 'MethodSRSDataUpdate', 'MethodSSDataUpdate',
            'MethodSVTDataUpdate', 'MethodTOTDataUpdate', 'MethodTRDataUpdate',
            'MethodWSTDataUpdate']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, Union['MethodCPTData', 'MethodDPData', 'MethodDTData', 'MethodPZData', 'MethodRCDData', 'MethodRPData', 'MethodSRSData', 'MethodSSData', 'MethodSVTData', 'MethodTOTData', 'MethodTRData', 'MethodWSTData']]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        location_id=location_id,
        method_id=method_id,
        method_data_id=method_data_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    location_id: UUID,
    method_id: UUID,
    method_data_id: UUID,
    *,
    client: AuthenticatedClient,
    body: Union[
        "MethodCPTDataUpdate",
        "MethodDTDataUpdate",
        "MethodPZDataUpdate",
        "MethodRCDDataUpdate",
        "MethodRPDataUpdate",
        "MethodSRSDataUpdate",
        "MethodSSDataUpdate",
        "MethodSVTDataUpdate",
        "MethodTOTDataUpdate",
        "MethodTRDataUpdate",
        "MethodWSTDataUpdate",
    ],
) -> Optional[
    Union[
        HTTPValidationError,
        Union[
            "MethodCPTData",
            "MethodDPData",
            "MethodDTData",
            "MethodPZData",
            "MethodRCDData",
            "MethodRPData",
            "MethodSRSData",
            "MethodSSData",
            "MethodSVTData",
            "MethodTOTData",
            "MethodTRData",
            "MethodWSTData",
        ],
    ]
]:
    """Update Data Row

     Update a method's single data line

    Args:
        project_id (str):
        location_id (UUID):
        method_id (UUID):
        method_data_id (UUID):
        body (Union['MethodCPTDataUpdate', 'MethodDTDataUpdate', 'MethodPZDataUpdate',
            'MethodRCDDataUpdate', 'MethodRPDataUpdate', 'MethodSRSDataUpdate', 'MethodSSDataUpdate',
            'MethodSVTDataUpdate', 'MethodTOTDataUpdate', 'MethodTRDataUpdate',
            'MethodWSTDataUpdate']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, Union['MethodCPTData', 'MethodDPData', 'MethodDTData', 'MethodPZData', 'MethodRCDData', 'MethodRPData', 'MethodSRSData', 'MethodSSData', 'MethodSVTData', 'MethodTOTData', 'MethodTRData', 'MethodWSTData']]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            location_id=location_id,
            method_id=method_id,
            method_data_id=method_data_id,
            client=client,
            body=body,
        )
    ).parsed
