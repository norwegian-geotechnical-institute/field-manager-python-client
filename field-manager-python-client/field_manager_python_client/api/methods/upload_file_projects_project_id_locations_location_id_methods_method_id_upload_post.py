from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_upload_file_projects_project_id_locations_location_id_methods_method_id_upload_post import (
    BodyUploadFileProjectsProjectIdLocationsLocationIdMethodsMethodIdUploadPost,
)
from ...models.http_validation_error import HTTPValidationError
from ...models.method_ad import MethodAD
from ...models.method_cd import MethodCD
from ...models.method_cpt import MethodCPT
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
from ...models.method_spt import MethodSPT
from ...models.method_sr import MethodSR
from ...models.method_srs import MethodSRS
from ...models.method_ss import MethodSS
from ...models.method_svt import MethodSVT
from ...models.method_tot import MethodTOT
from ...models.method_tp import MethodTP
from ...models.method_wst import MethodWST
from ...types import Response


def _get_kwargs(
    project_id: str,
    location_id: UUID,
    method_id: UUID,
    *,
    body: BodyUploadFileProjectsProjectIdLocationsLocationIdMethodsMethodIdUploadPost,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/projects/{project_id}/locations/{location_id}/methods/{method_id}/upload",
    }

    _body = body.to_multipart()

    _kwargs["files"] = _body

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
            "MethodSPT",
            "MethodSR",
            "MethodSRS",
            "MethodSS",
            "MethodSVT",
            "MethodTOT",
            "MethodTP",
            "MethodWST",
            None,
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
            "MethodSPT",
            "MethodSR",
            "MethodSRS",
            "MethodSS",
            "MethodSVT",
            "MethodTOT",
            "MethodTP",
            "MethodWST",
            None,
        ]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_0_type_0 = MethodCPT.from_dict(data)

                return response_201_type_0_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_0_type_1 = MethodTOT.from_dict(data)

                return response_201_type_0_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_0_type_2 = MethodRP.from_dict(data)

                return response_201_type_0_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_0_type_3 = MethodSA.from_dict(data)

                return response_201_type_0_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_0_type_4 = MethodPZ.from_dict(data)

                return response_201_type_0_type_4
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_0_type_5 = MethodSS.from_dict(data)

                return response_201_type_0_type_5
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_0_type_6 = MethodRWS.from_dict(data)

                return response_201_type_0_type_6
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_0_type_7 = MethodRCD.from_dict(data)

                return response_201_type_0_type_7
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_0_type_8 = MethodRS.from_dict(data)

                return response_201_type_0_type_8
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_0_type_9 = MethodSVT.from_dict(data)

                return response_201_type_0_type_9
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_0_type_10 = MethodSPT.from_dict(data)

                return response_201_type_0_type_10
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_0_type_11 = MethodCD.from_dict(data)

                return response_201_type_0_type_11
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_0_type_12 = MethodTP.from_dict(data)

                return response_201_type_0_type_12
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_0_type_13 = MethodPT.from_dict(data)

                return response_201_type_0_type_13
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_0_type_14 = MethodESA.from_dict(data)

                return response_201_type_0_type_14
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_0_type_15 = MethodAD.from_dict(data)

                return response_201_type_0_type_15
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_0_type_16 = MethodRO.from_dict(data)

                return response_201_type_0_type_16
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_0_type_17 = MethodINC.from_dict(data)

                return response_201_type_0_type_17
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_0_type_18 = MethodSR.from_dict(data)

                return response_201_type_0_type_18
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_0_type_19 = MethodIW.from_dict(data)

                return response_201_type_0_type_19
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_0_type_20 = MethodDT.from_dict(data)

                return response_201_type_0_type_20
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_0_type_21 = MethodOTHER.from_dict(data)

                return response_201_type_0_type_21
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_0_type_22 = MethodSRS.from_dict(data)

                return response_201_type_0_type_22
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_0_type_23 = MethodDP.from_dict(data)

                return response_201_type_0_type_23
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_0_type_24 = MethodWST.from_dict(data)

                return response_201_type_0_type_24
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    "MethodAD",
                    "MethodCD",
                    "MethodCPT",
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
                    "MethodSPT",
                    "MethodSR",
                    "MethodSRS",
                    "MethodSS",
                    "MethodSVT",
                    "MethodTOT",
                    "MethodTP",
                    "MethodWST",
                    None,
                ],
                data,
            )

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
            "MethodSPT",
            "MethodSR",
            "MethodSRS",
            "MethodSS",
            "MethodSVT",
            "MethodTOT",
            "MethodTP",
            "MethodWST",
            None,
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
    body: BodyUploadFileProjectsProjectIdLocationsLocationIdMethodsMethodIdUploadPost,
) -> Response[
    Union[
        HTTPValidationError,
        Union[
            "MethodAD",
            "MethodCD",
            "MethodCPT",
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
            "MethodSPT",
            "MethodSR",
            "MethodSRS",
            "MethodSS",
            "MethodSVT",
            "MethodTOT",
            "MethodTP",
            "MethodWST",
            None,
        ],
    ]
]:
    r"""Upload File

     Upload method file.

    This endpoint will only allow that the passed in file contains one method.

    Multi-method or multi-stroke files should be uploaded to the location endpoint.

    If the file uploaded does not have a recognized method file extension, it is uploaded as a
    \"general file\" and not parsed.

    Args:
        project_id (str):
        location_id (UUID):
        method_id (UUID):
        body (BodyUploadFileProjectsProjectIdLocationsLocationIdMethodsMethodIdUploadPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, Union['MethodAD', 'MethodCD', 'MethodCPT', 'MethodDP', 'MethodDT', 'MethodESA', 'MethodINC', 'MethodIW', 'MethodOTHER', 'MethodPT', 'MethodPZ', 'MethodRCD', 'MethodRO', 'MethodRP', 'MethodRS', 'MethodRWS', 'MethodSA', 'MethodSPT', 'MethodSR', 'MethodSRS', 'MethodSS', 'MethodSVT', 'MethodTOT', 'MethodTP', 'MethodWST', None]]]
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
    body: BodyUploadFileProjectsProjectIdLocationsLocationIdMethodsMethodIdUploadPost,
) -> Optional[
    Union[
        HTTPValidationError,
        Union[
            "MethodAD",
            "MethodCD",
            "MethodCPT",
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
            "MethodSPT",
            "MethodSR",
            "MethodSRS",
            "MethodSS",
            "MethodSVT",
            "MethodTOT",
            "MethodTP",
            "MethodWST",
            None,
        ],
    ]
]:
    r"""Upload File

     Upload method file.

    This endpoint will only allow that the passed in file contains one method.

    Multi-method or multi-stroke files should be uploaded to the location endpoint.

    If the file uploaded does not have a recognized method file extension, it is uploaded as a
    \"general file\" and not parsed.

    Args:
        project_id (str):
        location_id (UUID):
        method_id (UUID):
        body (BodyUploadFileProjectsProjectIdLocationsLocationIdMethodsMethodIdUploadPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, Union['MethodAD', 'MethodCD', 'MethodCPT', 'MethodDP', 'MethodDT', 'MethodESA', 'MethodINC', 'MethodIW', 'MethodOTHER', 'MethodPT', 'MethodPZ', 'MethodRCD', 'MethodRO', 'MethodRP', 'MethodRS', 'MethodRWS', 'MethodSA', 'MethodSPT', 'MethodSR', 'MethodSRS', 'MethodSS', 'MethodSVT', 'MethodTOT', 'MethodTP', 'MethodWST', None]]
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
    body: BodyUploadFileProjectsProjectIdLocationsLocationIdMethodsMethodIdUploadPost,
) -> Response[
    Union[
        HTTPValidationError,
        Union[
            "MethodAD",
            "MethodCD",
            "MethodCPT",
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
            "MethodSPT",
            "MethodSR",
            "MethodSRS",
            "MethodSS",
            "MethodSVT",
            "MethodTOT",
            "MethodTP",
            "MethodWST",
            None,
        ],
    ]
]:
    r"""Upload File

     Upload method file.

    This endpoint will only allow that the passed in file contains one method.

    Multi-method or multi-stroke files should be uploaded to the location endpoint.

    If the file uploaded does not have a recognized method file extension, it is uploaded as a
    \"general file\" and not parsed.

    Args:
        project_id (str):
        location_id (UUID):
        method_id (UUID):
        body (BodyUploadFileProjectsProjectIdLocationsLocationIdMethodsMethodIdUploadPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, Union['MethodAD', 'MethodCD', 'MethodCPT', 'MethodDP', 'MethodDT', 'MethodESA', 'MethodINC', 'MethodIW', 'MethodOTHER', 'MethodPT', 'MethodPZ', 'MethodRCD', 'MethodRO', 'MethodRP', 'MethodRS', 'MethodRWS', 'MethodSA', 'MethodSPT', 'MethodSR', 'MethodSRS', 'MethodSS', 'MethodSVT', 'MethodTOT', 'MethodTP', 'MethodWST', None]]]
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
    body: BodyUploadFileProjectsProjectIdLocationsLocationIdMethodsMethodIdUploadPost,
) -> Optional[
    Union[
        HTTPValidationError,
        Union[
            "MethodAD",
            "MethodCD",
            "MethodCPT",
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
            "MethodSPT",
            "MethodSR",
            "MethodSRS",
            "MethodSS",
            "MethodSVT",
            "MethodTOT",
            "MethodTP",
            "MethodWST",
            None,
        ],
    ]
]:
    r"""Upload File

     Upload method file.

    This endpoint will only allow that the passed in file contains one method.

    Multi-method or multi-stroke files should be uploaded to the location endpoint.

    If the file uploaded does not have a recognized method file extension, it is uploaded as a
    \"general file\" and not parsed.

    Args:
        project_id (str):
        location_id (UUID):
        method_id (UUID):
        body (BodyUploadFileProjectsProjectIdLocationsLocationIdMethodsMethodIdUploadPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, Union['MethodAD', 'MethodCD', 'MethodCPT', 'MethodDP', 'MethodDT', 'MethodESA', 'MethodINC', 'MethodIW', 'MethodOTHER', 'MethodPT', 'MethodPZ', 'MethodRCD', 'MethodRO', 'MethodRP', 'MethodRS', 'MethodRWS', 'MethodSA', 'MethodSPT', 'MethodSR', 'MethodSRS', 'MethodSS', 'MethodSVT', 'MethodTOT', 'MethodTP', 'MethodWST', None]]
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
