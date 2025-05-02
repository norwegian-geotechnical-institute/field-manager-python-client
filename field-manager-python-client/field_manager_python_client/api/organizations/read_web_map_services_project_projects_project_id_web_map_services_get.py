from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.web_map_service import WebMapService
from ...models.web_map_service_level import WebMapServiceLevel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    *,
    levels: Union[Unset, list[WebMapServiceLevel]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_levels: Union[Unset, list[str]] = UNSET
    if not isinstance(levels, Unset):
        json_levels = []
        for levels_item_data in levels:
            levels_item = levels_item_data.value
            json_levels.append(levels_item)

    params["levels"] = json_levels

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/projects/{project_id}/web_map_services",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, list["WebMapService"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = WebMapService.from_dict(response_200_item_data)

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
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[HTTPValidationError, list["WebMapService"]]]:
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
    levels: Union[Unset, list[WebMapServiceLevel]] = UNSET,
) -> Response[Union[HTTPValidationError, list["WebMapService"]]]:
    """Get Web Map Services by Project ID

     Get Web Map Services by project_id.

    You may optionally filter on levels and specify which levels to include.
    Not specifying any levels will return all levels you have access to.

    Args:
        project_id (str):
        levels (Union[Unset, list[WebMapServiceLevel]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, list['WebMapService']]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        levels=levels,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient,
    levels: Union[Unset, list[WebMapServiceLevel]] = UNSET,
) -> Optional[Union[HTTPValidationError, list["WebMapService"]]]:
    """Get Web Map Services by Project ID

     Get Web Map Services by project_id.

    You may optionally filter on levels and specify which levels to include.
    Not specifying any levels will return all levels you have access to.

    Args:
        project_id (str):
        levels (Union[Unset, list[WebMapServiceLevel]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, list['WebMapService']]
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        levels=levels,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient,
    levels: Union[Unset, list[WebMapServiceLevel]] = UNSET,
) -> Response[Union[HTTPValidationError, list["WebMapService"]]]:
    """Get Web Map Services by Project ID

     Get Web Map Services by project_id.

    You may optionally filter on levels and specify which levels to include.
    Not specifying any levels will return all levels you have access to.

    Args:
        project_id (str):
        levels (Union[Unset, list[WebMapServiceLevel]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, list['WebMapService']]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        levels=levels,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient,
    levels: Union[Unset, list[WebMapServiceLevel]] = UNSET,
) -> Optional[Union[HTTPValidationError, list["WebMapService"]]]:
    """Get Web Map Services by Project ID

     Get Web Map Services by project_id.

    You may optionally filter on levels and specify which levels to include.
    Not specifying any levels will return all levels you have access to.

    Args:
        project_id (str):
        levels (Union[Unset, list[WebMapServiceLevel]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, list['WebMapService']]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            levels=levels,
        )
    ).parsed
