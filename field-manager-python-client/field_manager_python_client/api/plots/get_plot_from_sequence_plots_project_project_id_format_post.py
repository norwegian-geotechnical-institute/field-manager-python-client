from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.plot_format import PlotFormat
from ...models.plot_sequence import PlotSequence
from ...types import Response


def _get_kwargs(
    project_id: str,
    format_: PlotFormat,
    *,
    body: PlotSequence,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/plots/project/{project_id}/{format_}",
    }

    _kwargs["json"] = body.to_dict()

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
    format_: PlotFormat,
    *,
    client: AuthenticatedClient,
    body: PlotSequence,
) -> Response[Any | HTTPValidationError]:
    """Get Plot From Sequence

     Get the plots sequence from any location within a given project.

    Args:
        project_id (str):
        format_ (PlotFormat):
        body (PlotSequence):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
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
    body: PlotSequence,
) -> Any | HTTPValidationError | None:
    """Get Plot From Sequence

     Get the plots sequence from any location within a given project.

    Args:
        project_id (str):
        format_ (PlotFormat):
        body (PlotSequence):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
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
    body: PlotSequence,
) -> Response[Any | HTTPValidationError]:
    """Get Plot From Sequence

     Get the plots sequence from any location within a given project.

    Args:
        project_id (str):
        format_ (PlotFormat):
        body (PlotSequence):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
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
    body: PlotSequence,
) -> Any | HTTPValidationError | None:
    """Get Plot From Sequence

     Get the plots sequence from any location within a given project.

    Args:
        project_id (str):
        format_ (PlotFormat):
        body (PlotSequence):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            format_=format_,
            client=client,
            body=body,
        )
    ).parsed
