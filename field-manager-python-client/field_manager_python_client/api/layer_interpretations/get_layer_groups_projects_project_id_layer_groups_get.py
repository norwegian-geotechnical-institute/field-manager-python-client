from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.layer_group import LayerGroup
from ...models.layer_group_with_soil_units import LayerGroupWithSoilUnits
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    *,
    include_soil_units: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["include_soil_units"] = include_soil_units

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/projects/{project_id}/layer-groups".format(
            project_id=quote(str(project_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | list[LayerGroup | LayerGroupWithSoilUnits] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:

            def _parse_response_200_item(data: object) -> LayerGroup | LayerGroupWithSoilUnits:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_200_item_type_0 = LayerGroup.from_dict(data)

                    return response_200_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_item_type_1 = LayerGroupWithSoilUnits.from_dict(data)

                return response_200_item_type_1

            response_200_item = _parse_response_200_item(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[HTTPValidationError | list[LayerGroup | LayerGroupWithSoilUnits]]:
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
    include_soil_units: bool | Unset = False,
) -> Response[HTTPValidationError | list[LayerGroup | LayerGroupWithSoilUnits]]:
    """Get Layer Groups

     Get all layer groups for a project.

    Args:
        project_id (str):
        include_soil_units (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[LayerGroup | LayerGroupWithSoilUnits]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        include_soil_units=include_soil_units,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient,
    include_soil_units: bool | Unset = False,
) -> HTTPValidationError | list[LayerGroup | LayerGroupWithSoilUnits] | None:
    """Get Layer Groups

     Get all layer groups for a project.

    Args:
        project_id (str):
        include_soil_units (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[LayerGroup | LayerGroupWithSoilUnits]
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        include_soil_units=include_soil_units,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient,
    include_soil_units: bool | Unset = False,
) -> Response[HTTPValidationError | list[LayerGroup | LayerGroupWithSoilUnits]]:
    """Get Layer Groups

     Get all layer groups for a project.

    Args:
        project_id (str):
        include_soil_units (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[LayerGroup | LayerGroupWithSoilUnits]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        include_soil_units=include_soil_units,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient,
    include_soil_units: bool | Unset = False,
) -> HTTPValidationError | list[LayerGroup | LayerGroupWithSoilUnits] | None:
    """Get Layer Groups

     Get all layer groups for a project.

    Args:
        project_id (str):
        include_soil_units (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[LayerGroup | LayerGroupWithSoilUnits]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            include_soil_units=include_soil_units,
        )
    ).parsed
