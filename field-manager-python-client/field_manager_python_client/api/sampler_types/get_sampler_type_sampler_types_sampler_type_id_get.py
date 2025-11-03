from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.sampler_type import SamplerType
from ...types import Response


def _get_kwargs(
    sampler_type_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/sampler_types/{sampler_type_id}",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | SamplerType | None:
    if response.status_code == 200:
        response_200 = SamplerType.from_dict(response.json())

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
) -> Response[HTTPValidationError | SamplerType]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    sampler_type_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[HTTPValidationError | SamplerType]:
    """Get Sampler Type

    Args:
        sampler_type_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SamplerType]
    """

    kwargs = _get_kwargs(
        sampler_type_id=sampler_type_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    sampler_type_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> HTTPValidationError | SamplerType | None:
    """Get Sampler Type

    Args:
        sampler_type_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SamplerType
    """

    return sync_detailed(
        sampler_type_id=sampler_type_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    sampler_type_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[HTTPValidationError | SamplerType]:
    """Get Sampler Type

    Args:
        sampler_type_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | SamplerType]
    """

    kwargs = _get_kwargs(
        sampler_type_id=sampler_type_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    sampler_type_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> HTTPValidationError | SamplerType | None:
    """Get Sampler Type

    Args:
        sampler_type_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | SamplerType
    """

    return (
        await asyncio_detailed(
            sampler_type_id=sampler_type_id,
            client=client,
        )
    ).parsed
