from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.nadag_sync_status_details import NadagSyncStatusDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    *,
    limit: int | Unset = 100,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/projects/{project_id}/nadag_sync/status/details".format(
            project_id=quote(str(project_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | NadagSyncStatusDetails | None:
    if response.status_code == 200:
        response_200 = NadagSyncStatusDetails.from_dict(response.json())

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
) -> Response[HTTPValidationError | NadagSyncStatusDetails]:
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
    limit: int | Unset = 100,
) -> Response[HTTPValidationError | NadagSyncStatusDetails]:
    """Get Nadag Sync Status Details

     Get detailed NADAG sync candidates, blockers, and a capped list of the latest failed sync rows for a
    project.

    Args:
        project_id (str):
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | NadagSyncStatusDetails]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 100,
) -> HTTPValidationError | NadagSyncStatusDetails | None:
    """Get Nadag Sync Status Details

     Get detailed NADAG sync candidates, blockers, and a capped list of the latest failed sync rows for a
    project.

    Args:
        project_id (str):
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | NadagSyncStatusDetails
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 100,
) -> Response[HTTPValidationError | NadagSyncStatusDetails]:
    """Get Nadag Sync Status Details

     Get detailed NADAG sync candidates, blockers, and a capped list of the latest failed sync rows for a
    project.

    Args:
        project_id (str):
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | NadagSyncStatusDetails]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 100,
) -> HTTPValidationError | NadagSyncStatusDetails | None:
    """Get Nadag Sync Status Details

     Get detailed NADAG sync candidates, blockers, and a capped list of the latest failed sync rows for a
    project.

    Args:
        project_id (str):
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | NadagSyncStatusDetails
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            limit=limit,
        )
    ).parsed
