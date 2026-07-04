from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_upload_file_to_project_projects_project_id_upload_post import (
    BodyUploadFileToProjectProjectsProjectIdUploadPost,
)
from ...models.file import File
from ...models.file_type import FileType
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    *,
    body: BodyUploadFileToProjectProjectsProjectIdUploadPost,
    file_type: FileType | None | Unset = UNSET,
    layer_file: bool | Unset = False,
    srid: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_file_type: None | str | Unset
    if isinstance(file_type, Unset):
        json_file_type = UNSET
    elif isinstance(file_type, FileType):
        json_file_type = file_type.value
    else:
        json_file_type = file_type
    params["file_type"] = json_file_type

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
        "url": "/projects/{project_id}/upload".format(
            project_id=quote(str(project_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["files"] = body.to_multipart()

    headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> File | HTTPValidationError | None:
    if response.status_code == 201:
        response_201 = File.from_dict(response.json())

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
) -> Response[File | HTTPValidationError]:
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
    file_type: FileType | None | Unset = UNSET,
    layer_file: bool | Unset = False,
    srid: None | str | Unset = UNSET,
) -> Response[File | HTTPValidationError]:
    """Upload File To Project

     Upload a file to project. If file_type is LAYER, then the file is converted to GeoJSON and used for
    showing extra
    layers in a project. If file_type is omitted, images are detected automatically and other files are
    attached as
    general project files. The deprecated layer_file query parameter is still supported for backwards
    compatibility.

    For layer files, only two types are supported: .dxf files with POINT, LINE and / or POLYLINE and
    .zip files
    containing shape (.shp) files.

    Args:
        project_id (str):
        file_type (FileType | None | Unset):
        layer_file (bool | Unset):  Default: False.
        srid (None | str | Unset):
        body (BodyUploadFileToProjectProjectsProjectIdUploadPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[File | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
        file_type=file_type,
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
    file_type: FileType | None | Unset = UNSET,
    layer_file: bool | Unset = False,
    srid: None | str | Unset = UNSET,
) -> File | HTTPValidationError | None:
    """Upload File To Project

     Upload a file to project. If file_type is LAYER, then the file is converted to GeoJSON and used for
    showing extra
    layers in a project. If file_type is omitted, images are detected automatically and other files are
    attached as
    general project files. The deprecated layer_file query parameter is still supported for backwards
    compatibility.

    For layer files, only two types are supported: .dxf files with POINT, LINE and / or POLYLINE and
    .zip files
    containing shape (.shp) files.

    Args:
        project_id (str):
        file_type (FileType | None | Unset):
        layer_file (bool | Unset):  Default: False.
        srid (None | str | Unset):
        body (BodyUploadFileToProjectProjectsProjectIdUploadPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        File | HTTPValidationError
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        body=body,
        file_type=file_type,
        layer_file=layer_file,
        srid=srid,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient,
    body: BodyUploadFileToProjectProjectsProjectIdUploadPost,
    file_type: FileType | None | Unset = UNSET,
    layer_file: bool | Unset = False,
    srid: None | str | Unset = UNSET,
) -> Response[File | HTTPValidationError]:
    """Upload File To Project

     Upload a file to project. If file_type is LAYER, then the file is converted to GeoJSON and used for
    showing extra
    layers in a project. If file_type is omitted, images are detected automatically and other files are
    attached as
    general project files. The deprecated layer_file query parameter is still supported for backwards
    compatibility.

    For layer files, only two types are supported: .dxf files with POINT, LINE and / or POLYLINE and
    .zip files
    containing shape (.shp) files.

    Args:
        project_id (str):
        file_type (FileType | None | Unset):
        layer_file (bool | Unset):  Default: False.
        srid (None | str | Unset):
        body (BodyUploadFileToProjectProjectsProjectIdUploadPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[File | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
        file_type=file_type,
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
    file_type: FileType | None | Unset = UNSET,
    layer_file: bool | Unset = False,
    srid: None | str | Unset = UNSET,
) -> File | HTTPValidationError | None:
    """Upload File To Project

     Upload a file to project. If file_type is LAYER, then the file is converted to GeoJSON and used for
    showing extra
    layers in a project. If file_type is omitted, images are detected automatically and other files are
    attached as
    general project files. The deprecated layer_file query parameter is still supported for backwards
    compatibility.

    For layer files, only two types are supported: .dxf files with POINT, LINE and / or POLYLINE and
    .zip files
    containing shape (.shp) files.

    Args:
        project_id (str):
        file_type (FileType | None | Unset):
        layer_file (bool | Unset):  Default: False.
        srid (None | str | Unset):
        body (BodyUploadFileToProjectProjectsProjectIdUploadPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        File | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            body=body,
            file_type=file_type,
            layer_file=layer_file,
            srid=srid,
        )
    ).parsed
