from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.options import Options
from ...models.plot_format import PlotFormat
from ...models.plot_sequence import PlotSequence
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    format_: PlotFormat,
    *,
    body: None | Options | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/plots/project/{project_id}/plot_sequence/{format_}".format(
            project_id=quote(str(project_id), safe=""),
            format_=quote(str(format_), safe=""),
        ),
    }

    if isinstance(body, Options):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | PlotSequence | None:
    if response.status_code == 200:
        response_200 = PlotSequence.from_dict(response.json())

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
) -> Response[HTTPValidationError | PlotSequence]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    format_: PlotFormat,
    *,
    client: AuthenticatedClient,
    body: None | Options | Unset = UNSET,
) -> Response[HTTPValidationError | PlotSequence]:
    """Get Plot Sequence

     Get the plots sequence from any location within a given project.

    Args:
        project_id (str):
        format_ (PlotFormat):
        body (None | Options | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PlotSequence]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        format_=format_,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    format_: PlotFormat,
    *,
    client: AuthenticatedClient,
    body: None | Options | Unset = UNSET,
) -> HTTPValidationError | PlotSequence | None:
    """Get Plot Sequence

     Get the plots sequence from any location within a given project.

    Args:
        project_id (str):
        format_ (PlotFormat):
        body (None | Options | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PlotSequence
    """

    return sync_detailed(
        project_id=project_id,
        format_=format_,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    format_: PlotFormat,
    *,
    client: AuthenticatedClient,
    body: None | Options | Unset = UNSET,
) -> Response[HTTPValidationError | PlotSequence]:
    """Get Plot Sequence

     Get the plots sequence from any location within a given project.

    Args:
        project_id (str):
        format_ (PlotFormat):
        body (None | Options | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PlotSequence]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        format_=format_,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    format_: PlotFormat,
    *,
    client: AuthenticatedClient,
    body: None | Options | Unset = UNSET,
) -> HTTPValidationError | PlotSequence | None:
    """Get Plot Sequence

     Get the plots sequence from any location within a given project.

    Args:
        project_id (str):
        format_ (PlotFormat):
        body (None | Options | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PlotSequence
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            format_=format_,
            client=client,
            body=body,
        )
    ).parsed
