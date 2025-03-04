from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.method_cpt_data import MethodCPTData
from ...models.method_dp_data import MethodDPData
from ...models.method_dt_data import MethodDTData
from ...models.method_pz_data import MethodPZData
from ...models.method_rcd_data import MethodRCDData
from ...models.method_rp_data import MethodRPData
from ...models.method_srs_data import MethodSRSData
from ...models.method_ss_data import MethodSSData
from ...models.method_svt_data import MethodSVTData
from ...models.method_tot_data import MethodTOTData
from ...models.method_tr_data import MethodTRData
from ...models.method_wst_data import MethodWSTData
from ...types import Response


def _get_kwargs(
    project_id: str,
    location_id: UUID,
    method_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/projects/{project_id}/locations/{location_id}/methods/{method_id}/data",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        HTTPValidationError,
        list[
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
                    response_200_item_type_0 = MethodCPTData.from_dict(data)

                    return response_200_item_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_200_item_type_1 = MethodDPData.from_dict(data)

                    return response_200_item_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_200_item_type_2 = MethodDTData.from_dict(data)

                    return response_200_item_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_200_item_type_3 = MethodPZData.from_dict(data)

                    return response_200_item_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_200_item_type_4 = MethodRCDData.from_dict(data)

                    return response_200_item_type_4
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_200_item_type_5 = MethodRPData.from_dict(data)

                    return response_200_item_type_5
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_200_item_type_6 = MethodSSData.from_dict(data)

                    return response_200_item_type_6
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_200_item_type_7 = MethodSRSData.from_dict(data)

                    return response_200_item_type_7
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_200_item_type_8 = MethodSVTData.from_dict(data)

                    return response_200_item_type_8
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_200_item_type_9 = MethodTOTData.from_dict(data)

                    return response_200_item_type_9
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_200_item_type_10 = MethodTRData.from_dict(data)

                    return response_200_item_type_10
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_item_type_11 = MethodWSTData.from_dict(data)

                return response_200_item_type_11

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
    method_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[
    Union[
        HTTPValidationError,
        list[
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
            ]
        ],
    ]
]:
    """Get Methods Data

     Get the method's data

    Args:
        project_id (str):
        location_id (UUID):
        method_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, list[Union['MethodCPTData', 'MethodDPData', 'MethodDTData', 'MethodPZData', 'MethodRCDData', 'MethodRPData', 'MethodSRSData', 'MethodSSData', 'MethodSVTData', 'MethodTOTData', 'MethodTRData', 'MethodWSTData']]]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        location_id=location_id,
        method_id=method_id,
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
) -> Optional[
    Union[
        HTTPValidationError,
        list[
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
            ]
        ],
    ]
]:
    """Get Methods Data

     Get the method's data

    Args:
        project_id (str):
        location_id (UUID):
        method_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, list[Union['MethodCPTData', 'MethodDPData', 'MethodDTData', 'MethodPZData', 'MethodRCDData', 'MethodRPData', 'MethodSRSData', 'MethodSSData', 'MethodSVTData', 'MethodTOTData', 'MethodTRData', 'MethodWSTData']]]
    """

    return sync_detailed(
        project_id=project_id,
        location_id=location_id,
        method_id=method_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    location_id: UUID,
    method_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[
    Union[
        HTTPValidationError,
        list[
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
            ]
        ],
    ]
]:
    """Get Methods Data

     Get the method's data

    Args:
        project_id (str):
        location_id (UUID):
        method_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, list[Union['MethodCPTData', 'MethodDPData', 'MethodDTData', 'MethodPZData', 'MethodRCDData', 'MethodRPData', 'MethodSRSData', 'MethodSSData', 'MethodSVTData', 'MethodTOTData', 'MethodTRData', 'MethodWSTData']]]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        location_id=location_id,
        method_id=method_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    location_id: UUID,
    method_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Optional[
    Union[
        HTTPValidationError,
        list[
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
            ]
        ],
    ]
]:
    """Get Methods Data

     Get the method's data

    Args:
        project_id (str):
        location_id (UUID):
        method_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, list[Union['MethodCPTData', 'MethodDPData', 'MethodDTData', 'MethodPZData', 'MethodRCDData', 'MethodRPData', 'MethodSRSData', 'MethodSSData', 'MethodSVTData', 'MethodTOTData', 'MethodTRData', 'MethodWSTData']]]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            location_id=location_id,
            method_id=method_id,
            client=client,
        )
    ).parsed
