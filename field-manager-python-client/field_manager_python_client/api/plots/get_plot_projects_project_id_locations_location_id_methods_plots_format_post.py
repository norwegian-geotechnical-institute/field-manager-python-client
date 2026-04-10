from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.method_plot_format import MethodPlotFormat
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    location_id: UUID,
    format_: MethodPlotFormat,
    *,
    body: list[UUID],
    cross_section: bool | Unset = False,
    show_depth: bool | Unset = False,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["cross_section"] = cross_section

    params["show_depth"] = show_depth

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/projects/{project_id}/locations/{location_id}/methods/plots/{format_}".format(
            project_id=quote(str(project_id), safe=""),
            location_id=quote(str(location_id), safe=""),
            format_=quote(str(format_), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = []
    for body_item_data in body:
        body_item = str(body_item_data)
        _kwargs["json"].append(body_item)

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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
    format_: MethodPlotFormat,
    *,
    client: AuthenticatedClient,
    body: list[UUID],
    cross_section: bool | Unset = False,
    show_depth: bool | Unset = False,
) -> Response[Any | HTTPValidationError]:
    """Get Plot

     Get the plot for a given method (methods for Samples and offshore CPTUs) within a given location
    within a given project.

    Args:
        project_id (str):
        location_id (UUID):
        format_ (MethodPlotFormat):
        cross_section (bool | Unset):  Default: False.
        show_depth (bool | Unset):  Default: False.
        body (list[UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        location_id=location_id,
        format_=format_,
        body=body,
        cross_section=cross_section,
        show_depth=show_depth,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    location_id: UUID,
    format_: MethodPlotFormat,
    *,
    client: AuthenticatedClient,
    body: list[UUID],
    cross_section: bool | Unset = False,
    show_depth: bool | Unset = False,
) -> Any | HTTPValidationError | None:
    """Get Plot

     Get the plot for a given method (methods for Samples and offshore CPTUs) within a given location
    within a given project.

    Args:
        project_id (str):
        location_id (UUID):
        format_ (MethodPlotFormat):
        cross_section (bool | Unset):  Default: False.
        show_depth (bool | Unset):  Default: False.
        body (list[UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return sync_detailed(
        project_id=project_id,
        location_id=location_id,
        format_=format_,
        client=client,
        body=body,
        cross_section=cross_section,
        show_depth=show_depth,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    location_id: UUID,
    format_: MethodPlotFormat,
    *,
    client: AuthenticatedClient,
    body: list[UUID],
    cross_section: bool | Unset = False,
    show_depth: bool | Unset = False,
) -> Response[Any | HTTPValidationError]:
    """Get Plot

     Get the plot for a given method (methods for Samples and offshore CPTUs) within a given location
    within a given project.

    Args:
        project_id (str):
        location_id (UUID):
        format_ (MethodPlotFormat):
        cross_section (bool | Unset):  Default: False.
        show_depth (bool | Unset):  Default: False.
        body (list[UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        location_id=location_id,
        format_=format_,
        body=body,
        cross_section=cross_section,
        show_depth=show_depth,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    location_id: UUID,
    format_: MethodPlotFormat,
    *,
    client: AuthenticatedClient,
    body: list[UUID],
    cross_section: bool | Unset = False,
    show_depth: bool | Unset = False,
) -> Any | HTTPValidationError | None:
    """Get Plot

     Get the plot for a given method (methods for Samples and offshore CPTUs) within a given location
    within a given project.

    Args:
        project_id (str):
        location_id (UUID):
        format_ (MethodPlotFormat):
        cross_section (bool | Unset):  Default: False.
        show_depth (bool | Unset):  Default: False.
        body (list[UUID]):

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
            format_=format_,
            client=client,
            body=body,
            cross_section=cross_section,
            show_depth=show_depth,
        )
    ).parsed
