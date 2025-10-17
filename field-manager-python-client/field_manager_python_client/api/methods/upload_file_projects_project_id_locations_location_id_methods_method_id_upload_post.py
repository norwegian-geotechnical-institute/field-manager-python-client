from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_upload_file_projects_project_id_locations_location_id_methods_method_id_upload_post import (
    BodyUploadFileProjectsProjectIdLocationsLocationIdMethodsMethodIdUploadPost,
)
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    project_id: str,
    location_id: UUID,
    method_id: UUID,
    *,
    body: BodyUploadFileProjectsProjectIdLocationsLocationIdMethodsMethodIdUploadPost,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/projects/{project_id}/locations/{location_id}/methods/{method_id}/upload",
    }

    _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[HTTPValidationError]:
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    location_id: UUID,
    method_id: UUID,
    *,
    client: AuthenticatedClient,
    body: BodyUploadFileProjectsProjectIdLocationsLocationIdMethodsMethodIdUploadPost,
) -> Response[HTTPValidationError]:
    r"""Upload File

     Upload method file.

    This endpoint will only allow that the passed in file contains one method.

    Multi-method or multi-stroke files should be uploaded to the location endpoint.

    If the file uploaded does not have a recognized method file extension, it is uploaded as a
    \"general file\" and not parsed.

    Args:
        project_id (str):
        location_id (UUID):
        method_id (UUID):
        body (BodyUploadFileProjectsProjectIdLocationsLocationIdMethodsMethodIdUploadPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        location_id=location_id,
        method_id=method_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    location_id: UUID,
    method_id: UUID,
    *,
    client: AuthenticatedClient,
    body: BodyUploadFileProjectsProjectIdLocationsLocationIdMethodsMethodIdUploadPost,
) -> Optional[HTTPValidationError]:
    r"""Upload File

     Upload method file.

    This endpoint will only allow that the passed in file contains one method.

    Multi-method or multi-stroke files should be uploaded to the location endpoint.

    If the file uploaded does not have a recognized method file extension, it is uploaded as a
    \"general file\" and not parsed.

    Args:
        project_id (str):
        location_id (UUID):
        method_id (UUID):
        body (BodyUploadFileProjectsProjectIdLocationsLocationIdMethodsMethodIdUploadPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError
    """

    return sync_detailed(
        project_id=project_id,
        location_id=location_id,
        method_id=method_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    location_id: UUID,
    method_id: UUID,
    *,
    client: AuthenticatedClient,
    body: BodyUploadFileProjectsProjectIdLocationsLocationIdMethodsMethodIdUploadPost,
) -> Response[HTTPValidationError]:
    r"""Upload File

     Upload method file.

    This endpoint will only allow that the passed in file contains one method.

    Multi-method or multi-stroke files should be uploaded to the location endpoint.

    If the file uploaded does not have a recognized method file extension, it is uploaded as a
    \"general file\" and not parsed.

    Args:
        project_id (str):
        location_id (UUID):
        method_id (UUID):
        body (BodyUploadFileProjectsProjectIdLocationsLocationIdMethodsMethodIdUploadPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        location_id=location_id,
        method_id=method_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    location_id: UUID,
    method_id: UUID,
    *,
    client: AuthenticatedClient,
    body: BodyUploadFileProjectsProjectIdLocationsLocationIdMethodsMethodIdUploadPost,
) -> Optional[HTTPValidationError]:
    r"""Upload File

     Upload method file.

    This endpoint will only allow that the passed in file contains one method.

    Multi-method or multi-stroke files should be uploaded to the location endpoint.

    If the file uploaded does not have a recognized method file extension, it is uploaded as a
    \"general file\" and not parsed.

    Args:
        project_id (str):
        location_id (UUID):
        method_id (UUID):
        body (BodyUploadFileProjectsProjectIdLocationsLocationIdMethodsMethodIdUploadPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            location_id=location_id,
            method_id=method_id,
            client=client,
            body=body,
        )
    ).parsed
