from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    *,
    file_ids: list[UUID] | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_file_ids: list[str] | Unset = UNSET
    if not isinstance(file_ids, Unset):
        json_file_ids = []
        for file_ids_item_data in file_ids:
            file_ids_item = str(file_ids_item_data)
            json_file_ids.append(file_ids_item)

    params["file_ids"] = json_file_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/projects/{project_id}/export/files",
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
    *,
    client: AuthenticatedClient,
    file_ids: list[UUID] | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Export Files

     Export specified project files in one zip file.

    Not limited to files only attached to the project, but also files attached to
    locations and methods in the specified project.

    Args:
        project_id (str):
        file_ids (list[UUID] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        file_ids=file_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient,
    file_ids: list[UUID] | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Export Files

     Export specified project files in one zip file.

    Not limited to files only attached to the project, but also files attached to
    locations and methods in the specified project.

    Args:
        project_id (str):
        file_ids (list[UUID] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        file_ids=file_ids,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient,
    file_ids: list[UUID] | Unset = UNSET,
) -> Response[Any | HTTPValidationError]:
    """Export Files

     Export specified project files in one zip file.

    Not limited to files only attached to the project, but also files attached to
    locations and methods in the specified project.

    Args:
        project_id (str):
        file_ids (list[UUID] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        file_ids=file_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient,
    file_ids: list[UUID] | Unset = UNSET,
) -> Any | HTTPValidationError | None:
    """Export Files

     Export specified project files in one zip file.

    Not limited to files only attached to the project, but also files attached to
    locations and methods in the specified project.

    Args:
        project_id (str):
        file_ids (list[UUID] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            file_ids=file_ids,
        )
    ).parsed
