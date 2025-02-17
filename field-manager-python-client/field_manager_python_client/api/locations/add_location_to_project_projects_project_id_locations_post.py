from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.location import Location
from ...models.location_create import LocationCreate
from ...types import Response


def _get_kwargs(
    project_id: str,
    *,
    body: LocationCreate,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/projects/{project_id}/locations",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, Location]]:
    if response.status_code == 201:
        response_201 = Location.from_dict(response.json())

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
) -> Response[Union[HTTPValidationError, Location]]:
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
    body: LocationCreate,
) -> Response[Union[HTTPValidationError, Location]]:
    """Add Location To Project

     Add location to project.

    Args:
        project_id (str):
        body (LocationCreate):  Example: {'methods': [{'method_type_id': 1}, {'method_type_id':
            2}], 'name': 'Loc01', 'point_easting': 1194547, 'point_northing': 8388298, 'point_z': 0,
            'srid': 3857}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, Location]]
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
    body: LocationCreate,
) -> Optional[Union[HTTPValidationError, Location]]:
    """Add Location To Project

     Add location to project.

    Args:
        project_id (str):
        body (LocationCreate):  Example: {'methods': [{'method_type_id': 1}, {'method_type_id':
            2}], 'name': 'Loc01', 'point_easting': 1194547, 'point_northing': 8388298, 'point_z': 0,
            'srid': 3857}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, Location]
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
    body: LocationCreate,
) -> Response[Union[HTTPValidationError, Location]]:
    """Add Location To Project

     Add location to project.

    Args:
        project_id (str):
        body (LocationCreate):  Example: {'methods': [{'method_type_id': 1}, {'method_type_id':
            2}], 'name': 'Loc01', 'point_easting': 1194547, 'point_northing': 8388298, 'point_z': 0,
            'srid': 3857}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, Location]]
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
    body: LocationCreate,
) -> Optional[Union[HTTPValidationError, Location]]:
    """Add Location To Project

     Add location to project.

    Args:
        project_id (str):
        body (LocationCreate):  Example: {'methods': [{'method_type_id': 1}, {'method_type_id':
            2}], 'name': 'Loc01', 'point_easting': 1194547, 'point_northing': 8388298, 'point_z': 0,
            'srid': 3857}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, Location]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            body=body,
        )
    ).parsed
