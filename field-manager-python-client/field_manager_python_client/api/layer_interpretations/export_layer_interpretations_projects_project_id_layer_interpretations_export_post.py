from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.location_layer_export_request import LocationLayerExportRequest
from ...models.location_layer_export_result import LocationLayerExportResult
from ...models.location_layer_filter_export_result import LocationLayerFilterExportResult
from ...types import Response


def _get_kwargs(
    project_id: str,
    *,
    body: LocationLayerExportRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/projects/{project_id}/layer-interpretations/export".format(
            project_id=quote(str(project_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | list[LocationLayerExportResult] | list[LocationLayerFilterExportResult] | None:
    if response.status_code == 200:

        def _parse_response_200(
            data: object,
        ) -> list[LocationLayerExportResult] | list[LocationLayerFilterExportResult]:
            try:
                if not isinstance(data, list):
                    raise TypeError()
                response_200_type_0 = []
                _response_200_type_0 = data
                for response_200_type_0_item_data in _response_200_type_0:
                    response_200_type_0_item = LocationLayerExportResult.from_dict(response_200_type_0_item_data)

                    response_200_type_0.append(response_200_type_0_item)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, list):
                raise TypeError()
            response_200_type_1 = []
            _response_200_type_1 = data
            for response_200_type_1_item_data in _response_200_type_1:
                response_200_type_1_item = LocationLayerFilterExportResult.from_dict(response_200_type_1_item_data)

                response_200_type_1.append(response_200_type_1_item)

            return response_200_type_1

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
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[HTTPValidationError | list[LocationLayerExportResult] | list[LocationLayerFilterExportResult]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient,
    body: LocationLayerExportRequest,
) -> Response[HTTPValidationError | list[LocationLayerExportResult] | list[LocationLayerFilterExportResult]]:
    """Export Layer Interpretations

     Export interpreted layer data as JSON or files.

    Without filters the export contains full interval data. When soil unit or
    exclude filters are provided, the export switches to one flat row per
    matched location using the existing filter priority logic.

    Args:
        project_id (str):
        body (LocationLayerExportRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[LocationLayerExportResult] | list[LocationLayerFilterExportResult]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient,
    body: LocationLayerExportRequest,
) -> HTTPValidationError | list[LocationLayerExportResult] | list[LocationLayerFilterExportResult] | None:
    """Export Layer Interpretations

     Export interpreted layer data as JSON or files.

    Without filters the export contains full interval data. When soil unit or
    exclude filters are provided, the export switches to one flat row per
    matched location using the existing filter priority logic.

    Args:
        project_id (str):
        body (LocationLayerExportRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[LocationLayerExportResult] | list[LocationLayerFilterExportResult]
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient,
    body: LocationLayerExportRequest,
) -> Response[HTTPValidationError | list[LocationLayerExportResult] | list[LocationLayerFilterExportResult]]:
    """Export Layer Interpretations

     Export interpreted layer data as JSON or files.

    Without filters the export contains full interval data. When soil unit or
    exclude filters are provided, the export switches to one flat row per
    matched location using the existing filter priority logic.

    Args:
        project_id (str):
        body (LocationLayerExportRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[LocationLayerExportResult] | list[LocationLayerFilterExportResult]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient,
    body: LocationLayerExportRequest,
) -> HTTPValidationError | list[LocationLayerExportResult] | list[LocationLayerFilterExportResult] | None:
    """Export Layer Interpretations

     Export interpreted layer data as JSON or files.

    Without filters the export contains full interval data. When soil unit or
    exclude filters are provided, the export switches to one flat row per
    matched location using the existing filter priority logic.

    Args:
        project_id (str):
        body (LocationLayerExportRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[LocationLayerExportResult] | list[LocationLayerFilterExportResult]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            body=body,
        )
    ).parsed
