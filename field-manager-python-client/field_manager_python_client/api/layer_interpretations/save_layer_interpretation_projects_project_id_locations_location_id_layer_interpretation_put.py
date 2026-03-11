from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.save_layer_interpretation_request import SaveLayerInterpretationRequest
from ...models.save_layer_interpretation_response import SaveLayerInterpretationResponse
from ...types import Response


def _get_kwargs(
    project_id: str,
    location_id: UUID,
    *,
    body: SaveLayerInterpretationRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/projects/{project_id}/locations/{location_id}/layer-interpretation".format(
            project_id=quote(str(project_id), safe=""),
            location_id=quote(str(location_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | SaveLayerInterpretationResponse | None:
    if response.status_code == 200:
        response_200 = SaveLayerInterpretationResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | SaveLayerInterpretationResponse]:
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
    body: SaveLayerInterpretationRequest,
) -> Response[HTTPValidationError | SaveLayerInterpretationResponse]:
    """Save Layer Interpretation

     Save layer interpretation for a location.
    Replaces all existing intervals.

    Args:
        project_id (str):
        location_id (UUID):
        body (SaveLayerInterpretationRequest): Request schema for saving layer interpretation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SaveLayerInterpretationResponse]
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
    body: SaveLayerInterpretationRequest,
) -> HTTPValidationError | SaveLayerInterpretationResponse | None:
    """Save Layer Interpretation

     Save layer interpretation for a location.
    Replaces all existing intervals.

    Args:
        project_id (str):
        location_id (UUID):
        body (SaveLayerInterpretationRequest): Request schema for saving layer interpretation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SaveLayerInterpretationResponse
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
    body: SaveLayerInterpretationRequest,
) -> Response[HTTPValidationError | SaveLayerInterpretationResponse]:
    """Save Layer Interpretation

     Save layer interpretation for a location.
    Replaces all existing intervals.

    Args:
        project_id (str):
        location_id (UUID):
        body (SaveLayerInterpretationRequest): Request schema for saving layer interpretation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SaveLayerInterpretationResponse]
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
    body: SaveLayerInterpretationRequest,
) -> HTTPValidationError | SaveLayerInterpretationResponse | None:
    """Save Layer Interpretation

     Save layer interpretation for a location.
    Replaces all existing intervals.

    Args:
        project_id (str):
        location_id (UUID):
        body (SaveLayerInterpretationRequest): Request schema for saving layer interpretation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SaveLayerInterpretationResponse
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            location_id=location_id,
            client=client,
            body=body,
        )
    ).parsed
