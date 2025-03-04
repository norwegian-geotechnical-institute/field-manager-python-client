from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.standard import Standard
from ...models.standard_type import StandardType
from ...types import Response


def _get_kwargs(
    standard_id: StandardType,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/standards/{standard_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, Standard]]:
    if response.status_code == 200:
        response_200 = Standard.from_dict(response.json())

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
) -> Response[Union[HTTPValidationError, Standard]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    standard_id: StandardType,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[HTTPValidationError, Standard]]:
    """Get Standard

    Args:
        standard_id (StandardType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, Standard]]
    """

    kwargs = _get_kwargs(
        standard_id=standard_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    standard_id: StandardType,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[HTTPValidationError, Standard]]:
    """Get Standard

    Args:
        standard_id (StandardType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, Standard]
    """

    return sync_detailed(
        standard_id=standard_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    standard_id: StandardType,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[HTTPValidationError, Standard]]:
    """Get Standard

    Args:
        standard_id (StandardType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, Standard]]
    """

    kwargs = _get_kwargs(
        standard_id=standard_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    standard_id: StandardType,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[HTTPValidationError, Standard]]:
    """Get Standard

    Args:
        standard_id (StandardType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, Standard]
    """

    return (
        await asyncio_detailed(
            standard_id=standard_id,
            client=client,
        )
    ).parsed
