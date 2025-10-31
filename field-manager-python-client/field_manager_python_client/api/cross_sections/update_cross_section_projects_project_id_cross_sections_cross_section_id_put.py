from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cross_section import CrossSection
from ...models.cross_section_update import CrossSectionUpdate
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    project_id: str,
    cross_section_id: UUID,
    *,
    body: CrossSectionUpdate,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/projects/{project_id}/cross_sections/{cross_section_id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CrossSection | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = CrossSection.from_dict(response.json())

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
) -> Response[CrossSection | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    cross_section_id: UUID,
    *,
    client: AuthenticatedClient,
    body: CrossSectionUpdate,
) -> Response[CrossSection | HTTPValidationError]:
    """Update Cross Section

     Update a cross section.

    Args:
        project_id (str):
        cross_section_id (UUID):
        body (CrossSectionUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CrossSection | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        cross_section_id=cross_section_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    cross_section_id: UUID,
    *,
    client: AuthenticatedClient,
    body: CrossSectionUpdate,
) -> CrossSection | HTTPValidationError | None:
    """Update Cross Section

     Update a cross section.

    Args:
        project_id (str):
        cross_section_id (UUID):
        body (CrossSectionUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CrossSection | HTTPValidationError
    """

    return sync_detailed(
        project_id=project_id,
        cross_section_id=cross_section_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    cross_section_id: UUID,
    *,
    client: AuthenticatedClient,
    body: CrossSectionUpdate,
) -> Response[CrossSection | HTTPValidationError]:
    """Update Cross Section

     Update a cross section.

    Args:
        project_id (str):
        cross_section_id (UUID):
        body (CrossSectionUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CrossSection | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        cross_section_id=cross_section_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    cross_section_id: UUID,
    *,
    client: AuthenticatedClient,
    body: CrossSectionUpdate,
) -> CrossSection | HTTPValidationError | None:
    """Update Cross Section

     Update a cross section.

    Args:
        project_id (str):
        cross_section_id (UUID):
        body (CrossSectionUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CrossSection | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            cross_section_id=cross_section_id,
            client=client,
            body=body,
        )
    ).parsed
