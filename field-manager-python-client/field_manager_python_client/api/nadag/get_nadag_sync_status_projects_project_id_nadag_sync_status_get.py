from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.nadag_sync_status import NadagSyncStatus
from ...types import Response


def _get_kwargs(
    project_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/projects/{project_id}/nadag_sync/status".format(
            project_id=quote(str(project_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | NadagSyncStatus | None:
    if response.status_code == 200:
        response_200 = NadagSyncStatus.from_dict(response.json())

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
) -> Response[HTTPValidationError | NadagSyncStatus]:
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
) -> Response[HTTPValidationError | NadagSyncStatus]:
    """Get Nadag Sync Status

     Get an overview of the project's NADAG sync status.

    Response fields:

    - `project_id`: The project this status belongs to.
    - `status`: The project-level NADAG sync state:
        - `NOT_REQUIRED`: The project is not required to sync because it is not NGF, the organization is
    exempt,
          or the project is exempt.
        - `SYNCED_WITH_ERRORS`: The latest sync command failed, or failed sync rows exist after the last
    successful
          sync command.
        - `SYNC_CANDIDATES_EXIST`: The project has never synced successfully, has newer
    project/report/location/method
          changes, or has blockers that must be inspected before sync.
        - `ALL_SYNCED_OK`: NADAG sync is required, current data is covered by successful syncs, and
    there are no newer
          failures, candidates, or blockers.
    - `required_to_sync`: `true` when the project is NGF and both organization and project NADAG sync
    flags are enabled.
    - `active_sync`: `true` when a `PENDING` or `IN_PROGRESS` sync command exists for the project.
      This can be `true` independently of `status`.
    - `has_blockers`: `true` when one or more project/report/location preflight problems exist.
    - `last_successful_sync_at`: `synced_at` for the newest successful project sync command, or `null`.
    - `latest_sync_status`: Status of the newest sync command by creation time, or `null` if no command
    exists.
    - `counts.reports`: Number of report files on the project.
    - `counts.report_candidates`: Report files not successfully synced, or changed since their
    successful file sync.
    - `counts.locations`: Syncable locations with position, height, and at least one approved NADAG-
    supported method.
    - `counts.location_candidates`: Syncable locations not successfully synced, or changed since their
    location sync.
    - `counts.methods`: Approved NADAG-supported methods on syncable locations.
    - `counts.method_candidates`: Approved NADAG-supported methods on syncable locations not covered by
    a successful
      location sync, or changed since that location sync.
    - `counts.blockers`: Number of preflight blockers, such as missing client/contractor/report or
    location coordinates.
    - `counts.failed_syncs`: Failed command/project/file/location sync rows after the last successful
    sync command.

    Args:
        project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | NadagSyncStatus]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient,
) -> HTTPValidationError | NadagSyncStatus | None:
    """Get Nadag Sync Status

     Get an overview of the project's NADAG sync status.

    Response fields:

    - `project_id`: The project this status belongs to.
    - `status`: The project-level NADAG sync state:
        - `NOT_REQUIRED`: The project is not required to sync because it is not NGF, the organization is
    exempt,
          or the project is exempt.
        - `SYNCED_WITH_ERRORS`: The latest sync command failed, or failed sync rows exist after the last
    successful
          sync command.
        - `SYNC_CANDIDATES_EXIST`: The project has never synced successfully, has newer
    project/report/location/method
          changes, or has blockers that must be inspected before sync.
        - `ALL_SYNCED_OK`: NADAG sync is required, current data is covered by successful syncs, and
    there are no newer
          failures, candidates, or blockers.
    - `required_to_sync`: `true` when the project is NGF and both organization and project NADAG sync
    flags are enabled.
    - `active_sync`: `true` when a `PENDING` or `IN_PROGRESS` sync command exists for the project.
      This can be `true` independently of `status`.
    - `has_blockers`: `true` when one or more project/report/location preflight problems exist.
    - `last_successful_sync_at`: `synced_at` for the newest successful project sync command, or `null`.
    - `latest_sync_status`: Status of the newest sync command by creation time, or `null` if no command
    exists.
    - `counts.reports`: Number of report files on the project.
    - `counts.report_candidates`: Report files not successfully synced, or changed since their
    successful file sync.
    - `counts.locations`: Syncable locations with position, height, and at least one approved NADAG-
    supported method.
    - `counts.location_candidates`: Syncable locations not successfully synced, or changed since their
    location sync.
    - `counts.methods`: Approved NADAG-supported methods on syncable locations.
    - `counts.method_candidates`: Approved NADAG-supported methods on syncable locations not covered by
    a successful
      location sync, or changed since that location sync.
    - `counts.blockers`: Number of preflight blockers, such as missing client/contractor/report or
    location coordinates.
    - `counts.failed_syncs`: Failed command/project/file/location sync rows after the last successful
    sync command.

    Args:
        project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | NadagSyncStatus
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[HTTPValidationError | NadagSyncStatus]:
    """Get Nadag Sync Status

     Get an overview of the project's NADAG sync status.

    Response fields:

    - `project_id`: The project this status belongs to.
    - `status`: The project-level NADAG sync state:
        - `NOT_REQUIRED`: The project is not required to sync because it is not NGF, the organization is
    exempt,
          or the project is exempt.
        - `SYNCED_WITH_ERRORS`: The latest sync command failed, or failed sync rows exist after the last
    successful
          sync command.
        - `SYNC_CANDIDATES_EXIST`: The project has never synced successfully, has newer
    project/report/location/method
          changes, or has blockers that must be inspected before sync.
        - `ALL_SYNCED_OK`: NADAG sync is required, current data is covered by successful syncs, and
    there are no newer
          failures, candidates, or blockers.
    - `required_to_sync`: `true` when the project is NGF and both organization and project NADAG sync
    flags are enabled.
    - `active_sync`: `true` when a `PENDING` or `IN_PROGRESS` sync command exists for the project.
      This can be `true` independently of `status`.
    - `has_blockers`: `true` when one or more project/report/location preflight problems exist.
    - `last_successful_sync_at`: `synced_at` for the newest successful project sync command, or `null`.
    - `latest_sync_status`: Status of the newest sync command by creation time, or `null` if no command
    exists.
    - `counts.reports`: Number of report files on the project.
    - `counts.report_candidates`: Report files not successfully synced, or changed since their
    successful file sync.
    - `counts.locations`: Syncable locations with position, height, and at least one approved NADAG-
    supported method.
    - `counts.location_candidates`: Syncable locations not successfully synced, or changed since their
    location sync.
    - `counts.methods`: Approved NADAG-supported methods on syncable locations.
    - `counts.method_candidates`: Approved NADAG-supported methods on syncable locations not covered by
    a successful
      location sync, or changed since that location sync.
    - `counts.blockers`: Number of preflight blockers, such as missing client/contractor/report or
    location coordinates.
    - `counts.failed_syncs`: Failed command/project/file/location sync rows after the last successful
    sync command.

    Args:
        project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | NadagSyncStatus]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient,
) -> HTTPValidationError | NadagSyncStatus | None:
    """Get Nadag Sync Status

     Get an overview of the project's NADAG sync status.

    Response fields:

    - `project_id`: The project this status belongs to.
    - `status`: The project-level NADAG sync state:
        - `NOT_REQUIRED`: The project is not required to sync because it is not NGF, the organization is
    exempt,
          or the project is exempt.
        - `SYNCED_WITH_ERRORS`: The latest sync command failed, or failed sync rows exist after the last
    successful
          sync command.
        - `SYNC_CANDIDATES_EXIST`: The project has never synced successfully, has newer
    project/report/location/method
          changes, or has blockers that must be inspected before sync.
        - `ALL_SYNCED_OK`: NADAG sync is required, current data is covered by successful syncs, and
    there are no newer
          failures, candidates, or blockers.
    - `required_to_sync`: `true` when the project is NGF and both organization and project NADAG sync
    flags are enabled.
    - `active_sync`: `true` when a `PENDING` or `IN_PROGRESS` sync command exists for the project.
      This can be `true` independently of `status`.
    - `has_blockers`: `true` when one or more project/report/location preflight problems exist.
    - `last_successful_sync_at`: `synced_at` for the newest successful project sync command, or `null`.
    - `latest_sync_status`: Status of the newest sync command by creation time, or `null` if no command
    exists.
    - `counts.reports`: Number of report files on the project.
    - `counts.report_candidates`: Report files not successfully synced, or changed since their
    successful file sync.
    - `counts.locations`: Syncable locations with position, height, and at least one approved NADAG-
    supported method.
    - `counts.location_candidates`: Syncable locations not successfully synced, or changed since their
    location sync.
    - `counts.methods`: Approved NADAG-supported methods on syncable locations.
    - `counts.method_candidates`: Approved NADAG-supported methods on syncable locations not covered by
    a successful
      location sync, or changed since that location sync.
    - `counts.blockers`: Number of preflight blockers, such as missing client/contractor/report or
    location coordinates.
    - `counts.failed_syncs`: Failed command/project/file/location sync rows after the last successful
    sync command.

    Args:
        project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | NadagSyncStatus
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
        )
    ).parsed
