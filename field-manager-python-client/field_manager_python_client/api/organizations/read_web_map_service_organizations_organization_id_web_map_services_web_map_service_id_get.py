from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.web_map_service import WebMapService
from ...types import Response


def _get_kwargs(
    organization_id: str,
    web_map_service_id: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/organizations/{organization_id}/web_map_services/{web_map_service_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, WebMapService]]:
    if response.status_code == 200:
        response_200 = WebMapService.from_dict(response.json())

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
) -> Response[Union[HTTPValidationError, WebMapService]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organization_id: str,
    web_map_service_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Union[HTTPValidationError, WebMapService]]:
    """Get a Web Map Service by ID

     Get a Web Map Service by organization_id and web_map_service_id.

    Args:
        organization_id (str):
        web_map_service_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, WebMapService]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        web_map_service_id=web_map_service_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: str,
    web_map_service_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[HTTPValidationError, WebMapService]]:
    """Get a Web Map Service by ID

     Get a Web Map Service by organization_id and web_map_service_id.

    Args:
        organization_id (str):
        web_map_service_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, WebMapService]
    """

    return sync_detailed(
        organization_id=organization_id,
        web_map_service_id=web_map_service_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    web_map_service_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Union[HTTPValidationError, WebMapService]]:
    """Get a Web Map Service by ID

     Get a Web Map Service by organization_id and web_map_service_id.

    Args:
        organization_id (str):
        web_map_service_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, WebMapService]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        web_map_service_id=web_map_service_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: str,
    web_map_service_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[HTTPValidationError, WebMapService]]:
    """Get a Web Map Service by ID

     Get a Web Map Service by organization_id and web_map_service_id.

    Args:
        organization_id (str):
        web_map_service_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, WebMapService]
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            web_map_service_id=web_map_service_id,
            client=client,
        )
    ).parsed
