from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_cross_section_plot_projects_project_id_cross_sections_cross_section_id_format_get_format import (
    GetCrossSectionPlotProjectsProjectIdCrossSectionsCrossSectionIdFormatGetFormat,
)
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    cross_section_id: UUID,
    format_: GetCrossSectionPlotProjectsProjectIdCrossSectionsCrossSectionIdFormatGetFormat,
    *,
    include_layer_interpretation: bool | Unset = False,
    layer_group_id: None | Unset | UUID = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["include_layer_interpretation"] = include_layer_interpretation

    json_layer_group_id: None | str | Unset
    if isinstance(layer_group_id, Unset):
        json_layer_group_id = UNSET
    elif isinstance(layer_group_id, UUID):
        json_layer_group_id = str(layer_group_id)
    else:
        json_layer_group_id = layer_group_id
    params["layer_group_id"] = json_layer_group_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/projects/{project_id}/cross_sections/{cross_section_id}/{format_}".format(
            project_id=quote(str(project_id), safe=""),
            cross_section_id=quote(str(cross_section_id), safe=""),
            format_=quote(str(format_), safe=""),
        ),
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
    cross_section_id: UUID,
    format_: GetCrossSectionPlotProjectsProjectIdCrossSectionsCrossSectionIdFormatGetFormat,
    *,
    client: AuthenticatedClient,
    include_layer_interpretation: bool | Unset = False,
    layer_group_id: None | Unset | UUID = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Get Cross Section Plot

     Get the dxf-plots for a given cross section within a given project.

    Args:
        project_id (str):
        cross_section_id (UUID):
        format_ (GetCrossSectionPlotProjectsProjectIdCrossSectionsCrossSectionIdFormatGetFormat):
        include_layer_interpretation (bool | Unset):  Default: False.
        layer_group_id (None | Unset | UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        cross_section_id=cross_section_id,
        format_=format_,
        include_layer_interpretation=include_layer_interpretation,
        layer_group_id=layer_group_id,
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
    include_layer_interpretation: bool | Unset = False,
    layer_group_id: None | Unset | UUID = UNSET,
) -> Any | HTTPValidationError | None:
    """Get Cross Section Plot

     Get the dxf-plots for a given cross section within a given project.

    Args:
        project_id (str):
        cross_section_id (UUID):
        format_ (GetCrossSectionPlotProjectsProjectIdCrossSectionsCrossSectionIdFormatGetFormat):
        include_layer_interpretation (bool | Unset):  Default: False.
        layer_group_id (None | Unset | UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return sync_detailed(
        project_id=project_id,
        cross_section_id=cross_section_id,
        format_=format_,
        client=client,
        include_layer_interpretation=include_layer_interpretation,
        layer_group_id=layer_group_id,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    cross_section_id: UUID,
    format_: GetCrossSectionPlotProjectsProjectIdCrossSectionsCrossSectionIdFormatGetFormat,
    *,
    client: AuthenticatedClient,
    include_layer_interpretation: bool | Unset = False,
    layer_group_id: None | Unset | UUID = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Get Cross Section Plot

     Get the dxf-plots for a given cross section within a given project.

    Args:
        project_id (str):
        cross_section_id (UUID):
        format_ (GetCrossSectionPlotProjectsProjectIdCrossSectionsCrossSectionIdFormatGetFormat):
        include_layer_interpretation (bool | Unset):  Default: False.
        layer_group_id (None | Unset | UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        cross_section_id=cross_section_id,
        format_=format_,
        include_layer_interpretation=include_layer_interpretation,
        layer_group_id=layer_group_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    cross_section_id: UUID,
    format_: GetCrossSectionPlotProjectsProjectIdCrossSectionsCrossSectionIdFormatGetFormat,
    *,
    client: AuthenticatedClient,
    include_layer_interpretation: bool | Unset = False,
    layer_group_id: None | Unset | UUID = UNSET,
) -> Any | HTTPValidationError | None:
    """Get Cross Section Plot

     Get the dxf-plots for a given cross section within a given project.

    Args:
        project_id (str):
        cross_section_id (UUID):
        format_ (GetCrossSectionPlotProjectsProjectIdCrossSectionsCrossSectionIdFormatGetFormat):
        include_layer_interpretation (bool | Unset):  Default: False.
        layer_group_id (None | Unset | UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            cross_section_id=cross_section_id,
            format_=format_,
            client=client,
            include_layer_interpretation=include_layer_interpretation,
            layer_group_id=layer_group_id,
        )
    ).parsed
