from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.method_export_type import MethodExportType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    location_id: UUID,
    *,
    export_type: MethodExportType,
    swap_x_y: Union[Unset, bool] = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_export_type = export_type.value
    params["export_type"] = json_export_type

    params["swap_x_y"] = swap_x_y

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/projects/{project_id}/locations/{location_id}/export",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = response.json()
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
) -> Response[Union[Any, HTTPValidationError]]:
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
    export_type: MethodExportType,
    swap_x_y: Union[Unset, bool] = False,
) -> Response[Union[Any, HTTPValidationError]]:
    """Export

     Endpoint for exporting specified location data.

    Supported **export_type** (MethodExportType):

    - **SND**: Download SND file.
               For now only CPT, RP, SS and TOT methods are supported.
               You will get a single SND file containing all methods for this location.

    Args:
        project_id (str):
        location_id (UUID):
        export_type (MethodExportType):
        swap_x_y (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        location_id=location_id,
        export_type=export_type,
        swap_x_y=swap_x_y,
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
    export_type: MethodExportType,
    swap_x_y: Union[Unset, bool] = False,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Export

     Endpoint for exporting specified location data.

    Supported **export_type** (MethodExportType):

    - **SND**: Download SND file.
               For now only CPT, RP, SS and TOT methods are supported.
               You will get a single SND file containing all methods for this location.

    Args:
        project_id (str):
        location_id (UUID):
        export_type (MethodExportType):
        swap_x_y (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return sync_detailed(
        project_id=project_id,
        location_id=location_id,
        client=client,
        export_type=export_type,
        swap_x_y=swap_x_y,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    location_id: UUID,
    *,
    client: AuthenticatedClient,
    export_type: MethodExportType,
    swap_x_y: Union[Unset, bool] = False,
) -> Response[Union[Any, HTTPValidationError]]:
    """Export

     Endpoint for exporting specified location data.

    Supported **export_type** (MethodExportType):

    - **SND**: Download SND file.
               For now only CPT, RP, SS and TOT methods are supported.
               You will get a single SND file containing all methods for this location.

    Args:
        project_id (str):
        location_id (UUID):
        export_type (MethodExportType):
        swap_x_y (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        location_id=location_id,
        export_type=export_type,
        swap_x_y=swap_x_y,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    location_id: UUID,
    *,
    client: AuthenticatedClient,
    export_type: MethodExportType,
    swap_x_y: Union[Unset, bool] = False,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Export

     Endpoint for exporting specified location data.

    Supported **export_type** (MethodExportType):

    - **SND**: Download SND file.
               For now only CPT, RP, SS and TOT methods are supported.
               You will get a single SND file containing all methods for this location.

    Args:
        project_id (str):
        location_id (UUID):
        export_type (MethodExportType):
        swap_x_y (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            location_id=location_id,
            client=client,
            export_type=export_type,
            swap_x_y=swap_x_y,
        )
    ).parsed
