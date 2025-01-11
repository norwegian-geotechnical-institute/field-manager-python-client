from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_cross_section_plot_projects_project_id_cross_sections_cross_section_id_format_get_format import (
    GetCrossSectionPlotProjectsProjectIdCrossSectionsCrossSectionIdFormatGetFormat,
)
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    project_id: str,
    cross_section_id: UUID,
    format_: GetCrossSectionPlotProjectsProjectIdCrossSectionsCrossSectionIdFormatGetFormat,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/projects/{project_id}/cross_sections/{cross_section_id}/{format_}",
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
    cross_section_id: UUID,
    format_: GetCrossSectionPlotProjectsProjectIdCrossSectionsCrossSectionIdFormatGetFormat,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, HTTPValidationError]]:
    """Get Cross Section Plot

     Get the dxf-plots for a given cross section within a given project.

    Args:
        project_id (str):
        cross_section_id (UUID):
        format_ (GetCrossSectionPlotProjectsProjectIdCrossSectionsCrossSectionIdFormatGetFormat):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        cross_section_id=cross_section_id,
        format_=format_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    cross_section_id: UUID,
    format_: GetCrossSectionPlotProjectsProjectIdCrossSectionsCrossSectionIdFormatGetFormat,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Get Cross Section Plot

     Get the dxf-plots for a given cross section within a given project.

    Args:
        project_id (str):
        cross_section_id (UUID):
        format_ (GetCrossSectionPlotProjectsProjectIdCrossSectionsCrossSectionIdFormatGetFormat):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return sync_detailed(
        project_id=project_id,
        cross_section_id=cross_section_id,
        format_=format_,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    cross_section_id: UUID,
    format_: GetCrossSectionPlotProjectsProjectIdCrossSectionsCrossSectionIdFormatGetFormat,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, HTTPValidationError]]:
    """Get Cross Section Plot

     Get the dxf-plots for a given cross section within a given project.

    Args:
        project_id (str):
        cross_section_id (UUID):
        format_ (GetCrossSectionPlotProjectsProjectIdCrossSectionsCrossSectionIdFormatGetFormat):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        cross_section_id=cross_section_id,
        format_=format_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    cross_section_id: UUID,
    format_: GetCrossSectionPlotProjectsProjectIdCrossSectionsCrossSectionIdFormatGetFormat,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Get Cross Section Plot

     Get the dxf-plots for a given cross section within a given project.

    Args:
        project_id (str):
        cross_section_id (UUID):
        format_ (GetCrossSectionPlotProjectsProjectIdCrossSectionsCrossSectionIdFormatGetFormat):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            cross_section_id=cross_section_id,
            format_=format_,
            client=client,
        )
    ).parsed
