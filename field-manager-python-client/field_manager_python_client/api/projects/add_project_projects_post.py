from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.project import Project
from ...models.project_create import ProjectCreate
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: ProjectCreate,
    set_manager_user: bool | None | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_set_manager_user: bool | None | Unset
    if isinstance(set_manager_user, Unset):
        json_set_manager_user = UNSET
    else:
        json_set_manager_user = set_manager_user
    params["set_manager_user"] = json_set_manager_user

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/projects",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | Project | None:
    if response.status_code == 201:
        response_201 = Project.from_dict(response.json())

        return response_201

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[HTTPValidationError | Project]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ProjectCreate,
    set_manager_user: bool | None | Unset = UNSET,
) -> Response[HTTPValidationError | Project]:
    """Add Project

     Add a project with passed project_in.

    If you pass in set_manager_user as:
    - True, then the calling user set as the project manager.
    - False, then the calling user is not set as the project manager.
    - None (default), the calling user is set as the project manager if the user is not an organization
    admin.

    Args:
        set_manager_user (bool | None | Unset):
        body (ProjectCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | Project]
    """

    kwargs = _get_kwargs(
        body=body,
        set_manager_user=set_manager_user,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: ProjectCreate,
    set_manager_user: bool | None | Unset = UNSET,
) -> HTTPValidationError | Project | None:
    """Add Project

     Add a project with passed project_in.

    If you pass in set_manager_user as:
    - True, then the calling user set as the project manager.
    - False, then the calling user is not set as the project manager.
    - None (default), the calling user is set as the project manager if the user is not an organization
    admin.

    Args:
        set_manager_user (bool | None | Unset):
        body (ProjectCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | Project
    """

    return sync_detailed(
        client=client,
        body=body,
        set_manager_user=set_manager_user,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ProjectCreate,
    set_manager_user: bool | None | Unset = UNSET,
) -> Response[HTTPValidationError | Project]:
    """Add Project

     Add a project with passed project_in.

    If you pass in set_manager_user as:
    - True, then the calling user set as the project manager.
    - False, then the calling user is not set as the project manager.
    - None (default), the calling user is set as the project manager if the user is not an organization
    admin.

    Args:
        set_manager_user (bool | None | Unset):
        body (ProjectCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | Project]
    """

    kwargs = _get_kwargs(
        body=body,
        set_manager_user=set_manager_user,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ProjectCreate,
    set_manager_user: bool | None | Unset = UNSET,
) -> HTTPValidationError | Project | None:
    """Add Project

     Add a project with passed project_in.

    If you pass in set_manager_user as:
    - True, then the calling user set as the project manager.
    - False, then the calling user is not set as the project manager.
    - None (default), the calling user is set as the project manager if the user is not an organization
    admin.

    Args:
        set_manager_user (bool | None | Unset):
        body (ProjectCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | Project
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            set_manager_user=set_manager_user,
        )
    ).parsed
