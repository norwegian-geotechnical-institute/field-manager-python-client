from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.project import Project
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    linked_project_id: UUID,
    *,
    linked_project_prefix: None | str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_linked_project_prefix: None | str | Unset
    if isinstance(linked_project_prefix, Unset):
        json_linked_project_prefix = UNSET
    else:
        json_linked_project_prefix = linked_project_prefix
    params["linked_project_prefix"] = json_linked_project_prefix

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/projects/{project_id}/linked_projects/{linked_project_id}".format(
            project_id=quote(str(project_id), safe=""),
            linked_project_id=quote(str(linked_project_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | Project | None:
    if response.status_code == 200:
        response_200 = Project.from_dict(response.json())

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
) -> Response[HTTPValidationError | Project]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    linked_project_id: UUID,
    *,
    client: AuthenticatedClient,
    linked_project_prefix: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | Project]:
    """Link Linked Project

     Link a project with `project_id` to another project with `linked_project_id`.

    Optionally add a linked project prefix usually including a separator character at the end of the
    string.

    Args:
        project_id (str):
        linked_project_id (UUID):
        linked_project_prefix (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | Project]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        linked_project_id=linked_project_id,
        linked_project_prefix=linked_project_prefix,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    linked_project_id: UUID,
    *,
    client: AuthenticatedClient,
    linked_project_prefix: None | str | Unset = UNSET,
) -> HTTPValidationError | Project | None:
    """Link Linked Project

     Link a project with `project_id` to another project with `linked_project_id`.

    Optionally add a linked project prefix usually including a separator character at the end of the
    string.

    Args:
        project_id (str):
        linked_project_id (UUID):
        linked_project_prefix (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | Project
    """

    return sync_detailed(
        project_id=project_id,
        linked_project_id=linked_project_id,
        client=client,
        linked_project_prefix=linked_project_prefix,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    linked_project_id: UUID,
    *,
    client: AuthenticatedClient,
    linked_project_prefix: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | Project]:
    """Link Linked Project

     Link a project with `project_id` to another project with `linked_project_id`.

    Optionally add a linked project prefix usually including a separator character at the end of the
    string.

    Args:
        project_id (str):
        linked_project_id (UUID):
        linked_project_prefix (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | Project]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        linked_project_id=linked_project_id,
        linked_project_prefix=linked_project_prefix,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    linked_project_id: UUID,
    *,
    client: AuthenticatedClient,
    linked_project_prefix: None | str | Unset = UNSET,
) -> HTTPValidationError | Project | None:
    """Link Linked Project

     Link a project with `project_id` to another project with `linked_project_id`.

    Optionally add a linked project prefix usually including a separator character at the end of the
    string.

    Args:
        project_id (str):
        linked_project_id (UUID):
        linked_project_prefix (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | Project
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            linked_project_id=linked_project_id,
            client=client,
            linked_project_prefix=linked_project_prefix,
        )
    ).parsed
