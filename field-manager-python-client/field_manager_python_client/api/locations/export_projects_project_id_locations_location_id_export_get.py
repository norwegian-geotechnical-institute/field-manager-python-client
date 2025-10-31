from http import HTTPStatus
from typing import Any
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
    swap_x_y: bool | Unset = False,
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
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | None:
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
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | HTTPValidationError]:
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
    swap_x_y: bool | Unset = False,
) -> Response[Any | HTTPValidationError]:
    """Export

     Endpoint for exporting specified location data.

    Supported **export_type** (MethodExportType):

    - **SND**: Download SND, PRV, GRV files for all methods in a location in a zip file.

    Args:
        project_id (str):
        location_id (UUID):
        export_type (MethodExportType):
        swap_x_y (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
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
    swap_x_y: bool | Unset = False,
) -> Any | HTTPValidationError | None:
    """Export

     Endpoint for exporting specified location data.

    Supported **export_type** (MethodExportType):

    - **SND**: Download SND, PRV, GRV files for all methods in a location in a zip file.

    Args:
        project_id (str):
        location_id (UUID):
        export_type (MethodExportType):
        swap_x_y (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
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
    swap_x_y: bool | Unset = False,
) -> Response[Any | HTTPValidationError]:
    """Export

     Endpoint for exporting specified location data.

    Supported **export_type** (MethodExportType):

    - **SND**: Download SND, PRV, GRV files for all methods in a location in a zip file.

    Args:
        project_id (str):
        location_id (UUID):
        export_type (MethodExportType):
        swap_x_y (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
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
    swap_x_y: bool | Unset = False,
) -> Any | HTTPValidationError | None:
    """Export

     Endpoint for exporting specified location data.

    Supported **export_type** (MethodExportType):

    - **SND**: Download SND, PRV, GRV files for all methods in a location in a zip file.

    Args:
        project_id (str):
        location_id (UUID):
        export_type (MethodExportType):
        swap_x_y (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
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
