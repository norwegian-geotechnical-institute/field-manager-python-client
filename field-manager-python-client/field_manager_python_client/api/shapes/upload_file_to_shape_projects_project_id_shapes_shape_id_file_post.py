from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_upload_file_to_shape_projects_project_id_shapes_shape_id_file_post import (
    BodyUploadFileToShapeProjectsProjectIdShapesShapeIdFilePost,
)
from ...models.file import File
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    project_id: str,
    shape_id: UUID,
    *,
    body: BodyUploadFileToShapeProjectsProjectIdShapesShapeIdFilePost,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/projects/{project_id}/shapes/{shape_id}/file",
    }

    _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[File, HTTPValidationError]]:
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
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[File, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    shape_id: UUID,
    *,
    client: AuthenticatedClient,
    body: BodyUploadFileToShapeProjectsProjectIdShapesShapeIdFilePost,
) -> Response[Union[File, HTTPValidationError]]:
    """Upload File To Shape

     Upload file and associate it with a shape or sub_shape
    To associate it with a shape, leave feature_index empty or set it to None.
    To associate it with a sub_shape, provide the feature_index of the sub_shape in the geojson file.

    Args:
        project_id (str):
        shape_id (UUID):
        body (BodyUploadFileToShapeProjectsProjectIdShapesShapeIdFilePost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[File, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        shape_id=shape_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    shape_id: UUID,
    *,
    client: AuthenticatedClient,
    body: BodyUploadFileToShapeProjectsProjectIdShapesShapeIdFilePost,
) -> Optional[Union[File, HTTPValidationError]]:
    """Upload File To Shape

     Upload file and associate it with a shape or sub_shape
    To associate it with a shape, leave feature_index empty or set it to None.
    To associate it with a sub_shape, provide the feature_index of the sub_shape in the geojson file.

    Args:
        project_id (str):
        shape_id (UUID):
        body (BodyUploadFileToShapeProjectsProjectIdShapesShapeIdFilePost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[File, HTTPValidationError]
    """

    return sync_detailed(
        project_id=project_id,
        shape_id=shape_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    shape_id: UUID,
    *,
    client: AuthenticatedClient,
    body: BodyUploadFileToShapeProjectsProjectIdShapesShapeIdFilePost,
) -> Response[Union[File, HTTPValidationError]]:
    """Upload File To Shape

     Upload file and associate it with a shape or sub_shape
    To associate it with a shape, leave feature_index empty or set it to None.
    To associate it with a sub_shape, provide the feature_index of the sub_shape in the geojson file.

    Args:
        project_id (str):
        shape_id (UUID):
        body (BodyUploadFileToShapeProjectsProjectIdShapesShapeIdFilePost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[File, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        shape_id=shape_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    shape_id: UUID,
    *,
    client: AuthenticatedClient,
    body: BodyUploadFileToShapeProjectsProjectIdShapesShapeIdFilePost,
) -> Optional[Union[File, HTTPValidationError]]:
    """Upload File To Shape

     Upload file and associate it with a shape or sub_shape
    To associate it with a shape, leave feature_index empty or set it to None.
    To associate it with a sub_shape, provide the feature_index of the sub_shape in the geojson file.

    Args:
        project_id (str):
        shape_id (UUID):
        body (BodyUploadFileToShapeProjectsProjectIdShapesShapeIdFilePost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[File, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            shape_id=shape_id,
            client=client,
            body=body,
        )
    ).parsed
