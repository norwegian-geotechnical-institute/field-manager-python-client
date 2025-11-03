from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_upload_file_to_project_projects_project_id_upload_post import (
    BodyUploadFileToProjectProjectsProjectIdUploadPost,
)
from ...models.http_validation_error import HTTPValidationError
from ...models.project import Project
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    *,
    body: BodyUploadFileToProjectProjectsProjectIdUploadPost,
    layer_file: bool | Unset = False,
    srid: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["layer_file"] = layer_file

    json_srid: None | str | Unset
    if isinstance(srid, Unset):
        json_srid = UNSET
    else:
        json_srid = srid
    params["srid"] = json_srid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/projects/{project_id}/upload",
        "params": params,
    }

    _kwargs["files"] = body.to_multipart()

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
    project_id: str,
    *,
    client: AuthenticatedClient,
    body: BodyUploadFileToProjectProjectsProjectIdUploadPost,
    layer_file: bool | Unset = False,
    srid: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | Project]:
    """Upload File To Project

     Upload a data file to project. If layer_file is passed as True, then the file is converted to
    GeoJSON and used for
    showing extra layers in a project. Otherwise, the file is not parsed, but only attached to the
    project.

    For layer files, only two types are supported: .dxf files with POINT, LINE and / or POLYLINE and
    .zip files
    containing shape (.shp) files.

    Args:
        project_id (str):
        layer_file (bool | Unset):  Default: False.
        srid (None | str | Unset):
        body (BodyUploadFileToProjectProjectsProjectIdUploadPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | Project]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
        layer_file=layer_file,
        srid=srid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient,
    body: BodyUploadFileToProjectProjectsProjectIdUploadPost,
    layer_file: bool | Unset = False,
    srid: None | str | Unset = UNSET,
) -> HTTPValidationError | Project | None:
    """Upload File To Project

     Upload a data file to project. If layer_file is passed as True, then the file is converted to
    GeoJSON and used for
    showing extra layers in a project. Otherwise, the file is not parsed, but only attached to the
    project.

    For layer files, only two types are supported: .dxf files with POINT, LINE and / or POLYLINE and
    .zip files
    containing shape (.shp) files.

    Args:
        project_id (str):
        layer_file (bool | Unset):  Default: False.
        srid (None | str | Unset):
        body (BodyUploadFileToProjectProjectsProjectIdUploadPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | Project
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        body=body,
        layer_file=layer_file,
        srid=srid,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient,
    body: BodyUploadFileToProjectProjectsProjectIdUploadPost,
    layer_file: bool | Unset = False,
    srid: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | Project]:
    """Upload File To Project

     Upload a data file to project. If layer_file is passed as True, then the file is converted to
    GeoJSON and used for
    showing extra layers in a project. Otherwise, the file is not parsed, but only attached to the
    project.

    For layer files, only two types are supported: .dxf files with POINT, LINE and / or POLYLINE and
    .zip files
    containing shape (.shp) files.

    Args:
        project_id (str):
        layer_file (bool | Unset):  Default: False.
        srid (None | str | Unset):
        body (BodyUploadFileToProjectProjectsProjectIdUploadPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | Project]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
        layer_file=layer_file,
        srid=srid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient,
    body: BodyUploadFileToProjectProjectsProjectIdUploadPost,
    layer_file: bool | Unset = False,
    srid: None | str | Unset = UNSET,
) -> HTTPValidationError | Project | None:
    """Upload File To Project

     Upload a data file to project. If layer_file is passed as True, then the file is converted to
    GeoJSON and used for
    showing extra layers in a project. Otherwise, the file is not parsed, but only attached to the
    project.

    For layer files, only two types are supported: .dxf files with POINT, LINE and / or POLYLINE and
    .zip files
    containing shape (.shp) files.

    Args:
        project_id (str):
        layer_file (bool | Unset):  Default: False.
        srid (None | str | Unset):
        body (BodyUploadFileToProjectProjectsProjectIdUploadPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | Project
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            body=body,
            layer_file=layer_file,
            srid=srid,
        )
    ).parsed
