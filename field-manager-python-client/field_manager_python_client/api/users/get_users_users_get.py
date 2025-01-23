from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/users",
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """Get Users

     Return all users the caller has access to.

    Application admin will get all users in the system.

    Organization user (ADMIN/VIEWER) will get all users with a role in the caller's organizations or the
    caller's
    organizations' projects.

    Project user (ADMIN/EDITOR/VIEWER) will get all users with a role in the caller's projects. Not get
    users that have
    a role in the projects' organizations.

    This endpoint is potentially very slow, so consider using other endpoints like `GET
    /projects/{project_id}/users` or
    `GET /organization/{organization_id}/users` to restrict the search and result set.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """Get Users

     Return all users the caller has access to.

    Application admin will get all users in the system.

    Organization user (ADMIN/VIEWER) will get all users with a role in the caller's organizations or the
    caller's
    organizations' projects.

    Project user (ADMIN/EDITOR/VIEWER) will get all users with a role in the caller's projects. Not get
    users that have
    a role in the projects' organizations.

    This endpoint is potentially very slow, so consider using other endpoints like `GET
    /projects/{project_id}/users` or
    `GET /organization/{organization_id}/users` to restrict the search and result set.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
