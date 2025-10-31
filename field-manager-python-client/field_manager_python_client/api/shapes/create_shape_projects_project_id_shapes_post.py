from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_create_shape_projects_project_id_shapes_post import BodyCreateShapeProjectsProjectIdShapesPost
from ...models.http_validation_error import HTTPValidationError
from ...models.shape import Shape
from ...types import Response


def _get_kwargs(
    project_id: str,
    *,
    body: BodyCreateShapeProjectsProjectIdShapesPost,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/projects/{project_id}/shapes",
    }

    _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | Shape | None:
    if response.status_code == 201:
        response_201 = Shape.from_dict(response.json())

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
) -> Response[HTTPValidationError | Shape]:
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
    body: BodyCreateShapeProjectsProjectIdShapesPost,
) -> Response[HTTPValidationError | Shape]:
    """Create Shape

     Create a new shape
    file can be a DXF, SHP, or GeoJSON file, or a zip file containing one of these formats.

    Args:
        project_id (str):
        body (BodyCreateShapeProjectsProjectIdShapesPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | Shape]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient,
    body: BodyCreateShapeProjectsProjectIdShapesPost,
) -> HTTPValidationError | Shape | None:
    """Create Shape

     Create a new shape
    file can be a DXF, SHP, or GeoJSON file, or a zip file containing one of these formats.

    Args:
        project_id (str):
        body (BodyCreateShapeProjectsProjectIdShapesPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | Shape
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient,
    body: BodyCreateShapeProjectsProjectIdShapesPost,
) -> Response[HTTPValidationError | Shape]:
    """Create Shape

     Create a new shape
    file can be a DXF, SHP, or GeoJSON file, or a zip file containing one of these formats.

    Args:
        project_id (str):
        body (BodyCreateShapeProjectsProjectIdShapesPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | Shape]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient,
    body: BodyCreateShapeProjectsProjectIdShapesPost,
) -> HTTPValidationError | Shape | None:
    """Create Shape

     Create a new shape
    file can be a DXF, SHP, or GeoJSON file, or a zip file containing one of these formats.

    Args:
        project_id (str):
        body (BodyCreateShapeProjectsProjectIdShapesPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | Shape
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            body=body,
        )
    ).parsed
