from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.user import User
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/users",
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[User] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = User.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[list[User]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[list[User]]:
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
        Response[list[User]]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> list[User] | None:
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
        list[User]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[list[User]]:
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
        Response[list[User]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> list[User] | None:
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
        list[User]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
