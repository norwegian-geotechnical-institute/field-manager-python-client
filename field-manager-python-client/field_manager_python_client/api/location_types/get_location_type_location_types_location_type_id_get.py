from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    location_type_id: int,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/location_types/{location_type_id}",
    }

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
    location_type_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[HTTPValidationError]:
    """Get Location Type

     Location type will be deprecated.

    Use Project.standard_id instead.

    Args:
        location_type_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError]
    """

    kwargs = _get_kwargs(
        location_type_id=location_type_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    location_type_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[HTTPValidationError]:
    """Get Location Type

     Location type will be deprecated.

    Use Project.standard_id instead.

    Args:
        location_type_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError
    """

    return sync_detailed(
        location_type_id=location_type_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    location_type_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[HTTPValidationError]:
    """Get Location Type

     Location type will be deprecated.

    Use Project.standard_id instead.

    Args:
        location_type_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError]
    """

    kwargs = _get_kwargs(
        location_type_id=location_type_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    location_type_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[HTTPValidationError]:
    """Get Location Type

     Location type will be deprecated.

    Use Project.standard_id instead.

    Args:
        location_type_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError
    """

    return (
        await asyncio_detailed(
            location_type_id=location_type_id,
            client=client,
        )
    ).parsed
