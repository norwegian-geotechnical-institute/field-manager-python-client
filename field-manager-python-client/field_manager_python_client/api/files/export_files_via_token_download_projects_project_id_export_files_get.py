from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: UUID,
    *,
    token: str,
    file_ids: Union[Unset, list[UUID]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["token"] = token

    json_file_ids: Union[Unset, list[str]] = UNSET
    if not isinstance(file_ids, Unset):
        json_file_ids = []
        for file_ids_item_data in file_ids:
            file_ids_item = str(file_ids_item_data)
            json_file_ids.append(file_ids_item)

    params["file_ids"] = json_file_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/download/projects/{project_id}/export/files",
        "params": params,
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
    project_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    token: str,
    file_ids: Union[Unset, list[UUID]] = UNSET,
) -> Response[Union[Any, HTTPValidationError]]:
    """Export Files Via Token

     Export specified project files in one zip file.

    Not limited to files only attached to the project, but also files attached to
    locations and methods in the specified project.

    Args:
        project_id (UUID):
        token (str):
        file_ids (Union[Unset, list[UUID]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        token=token,
        file_ids=file_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    token: str,
    file_ids: Union[Unset, list[UUID]] = UNSET,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Export Files Via Token

     Export specified project files in one zip file.

    Not limited to files only attached to the project, but also files attached to
    locations and methods in the specified project.

    Args:
        project_id (UUID):
        token (str):
        file_ids (Union[Unset, list[UUID]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        token=token,
        file_ids=file_ids,
    ).parsed


async def asyncio_detailed(
    project_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    token: str,
    file_ids: Union[Unset, list[UUID]] = UNSET,
) -> Response[Union[Any, HTTPValidationError]]:
    """Export Files Via Token

     Export specified project files in one zip file.

    Not limited to files only attached to the project, but also files attached to
    locations and methods in the specified project.

    Args:
        project_id (UUID):
        token (str):
        file_ids (Union[Unset, list[UUID]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        token=token,
        file_ids=file_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    token: str,
    file_ids: Union[Unset, list[UUID]] = UNSET,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Export Files Via Token

     Export specified project files in one zip file.

    Not limited to files only attached to the project, but also files attached to
    locations and methods in the specified project.

    Args:
        project_id (UUID):
        token (str):
        file_ids (Union[Unset, list[UUID]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            token=token,
            file_ids=file_ids,
        )
    ).parsed
