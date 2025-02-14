from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response


def _get_kwargs(
    organization_id: str,
    project_id: UUID,
    *,
    target_organization_id: UUID,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_target_organization_id = str(target_organization_id)
    params["target_organization_id"] = json_target_organization_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/organizations/{organization_id}/projects/{project_id}/move",
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
    organization_id: str,
    project_id: UUID,
    *,
    client: AuthenticatedClient,
    target_organization_id: UUID,
) -> Response[Union[Any, HTTPValidationError]]:
    """Move Organization Project

     Move a project from one organization to another. The calling user must be an admin in both
    organizations.

    Return 200 OK if successful move.

    Args:
        organization_id (str):
        project_id (UUID):
        target_organization_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        project_id=project_id,
        target_organization_id=target_organization_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: str,
    project_id: UUID,
    *,
    client: AuthenticatedClient,
    target_organization_id: UUID,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Move Organization Project

     Move a project from one organization to another. The calling user must be an admin in both
    organizations.

    Return 200 OK if successful move.

    Args:
        organization_id (str):
        project_id (UUID):
        target_organization_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return sync_detailed(
        organization_id=organization_id,
        project_id=project_id,
        client=client,
        target_organization_id=target_organization_id,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    project_id: UUID,
    *,
    client: AuthenticatedClient,
    target_organization_id: UUID,
) -> Response[Union[Any, HTTPValidationError]]:
    """Move Organization Project

     Move a project from one organization to another. The calling user must be an admin in both
    organizations.

    Return 200 OK if successful move.

    Args:
        organization_id (str):
        project_id (UUID):
        target_organization_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        project_id=project_id,
        target_organization_id=target_organization_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: str,
    project_id: UUID,
    *,
    client: AuthenticatedClient,
    target_organization_id: UUID,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Move Organization Project

     Move a project from one organization to another. The calling user must be an admin in both
    organizations.

    Return 200 OK if successful move.

    Args:
        organization_id (str):
        project_id (UUID):
        target_organization_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            project_id=project_id,
            client=client,
            target_organization_id=target_organization_id,
        )
    ).parsed
