from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.project import Project
from ...models.project_update import ProjectUpdate
from ...types import Response


def _get_kwargs(
    project_id: str,
    *,
    body: ProjectUpdate,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/projects/{project_id}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, Project]]:
    if response.status_code == 200:
        response_200 = Project.from_dict(response.json())

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
) -> Response[Union[HTTPValidationError, Project]]:
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
    body: ProjectUpdate,
) -> Response[Union[HTTPValidationError, Project]]:
    """Update Project

     Update a project with passed project_in.

    If srid is changed, then all location values are transformed from the old srid to the new srid.
    The location should not move on the map.

    Args:
        project_id (str):
        body (ProjectUpdate):  Example: {'external_id': '2020193232', 'height_reference':
            'NN2000', 'name': 'Project Name', 'srid': 3857}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, Project]]
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
    body: ProjectUpdate,
) -> Optional[Union[HTTPValidationError, Project]]:
    """Update Project

     Update a project with passed project_in.

    If srid is changed, then all location values are transformed from the old srid to the new srid.
    The location should not move on the map.

    Args:
        project_id (str):
        body (ProjectUpdate):  Example: {'external_id': '2020193232', 'height_reference':
            'NN2000', 'name': 'Project Name', 'srid': 3857}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, Project]
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
    body: ProjectUpdate,
) -> Response[Union[HTTPValidationError, Project]]:
    """Update Project

     Update a project with passed project_in.

    If srid is changed, then all location values are transformed from the old srid to the new srid.
    The location should not move on the map.

    Args:
        project_id (str):
        body (ProjectUpdate):  Example: {'external_id': '2020193232', 'height_reference':
            'NN2000', 'name': 'Project Name', 'srid': 3857}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, Project]]
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
    body: ProjectUpdate,
) -> Optional[Union[HTTPValidationError, Project]]:
    """Update Project

     Update a project with passed project_in.

    If srid is changed, then all location values are transformed from the old srid to the new srid.
    The location should not move on the map.

    Args:
        project_id (str):
        body (ProjectUpdate):  Example: {'external_id': '2020193232', 'height_reference':
            'NN2000', 'name': 'Project Name', 'srid': 3857}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, Project]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            body=body,
        )
    ).parsed
