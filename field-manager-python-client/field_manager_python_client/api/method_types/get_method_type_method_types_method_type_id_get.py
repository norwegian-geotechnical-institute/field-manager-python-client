from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.method_type import MethodType
from ...types import Response


def _get_kwargs(
    method_type_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/method_types/{method_type_id}",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | MethodType | None:
    if response.status_code == 200:
        response_200 = MethodType.from_dict(response.json())

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
) -> Response[HTTPValidationError | MethodType]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    method_type_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[HTTPValidationError | MethodType]:
    """Get Method Type

     Get a method type by ID.

    Please note that this endpoint will look at the Accept-Language header in the request
    to determine the language for the response data.

    Args:
        method_type_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | MethodType]
    """

    kwargs = _get_kwargs(
        method_type_id=method_type_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    method_type_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> HTTPValidationError | MethodType | None:
    """Get Method Type

     Get a method type by ID.

    Please note that this endpoint will look at the Accept-Language header in the request
    to determine the language for the response data.

    Args:
        method_type_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | MethodType
    """

    return sync_detailed(
        method_type_id=method_type_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    method_type_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[HTTPValidationError | MethodType]:
    """Get Method Type

     Get a method type by ID.

    Please note that this endpoint will look at the Accept-Language header in the request
    to determine the language for the response data.

    Args:
        method_type_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | MethodType]
    """

    kwargs = _get_kwargs(
        method_type_id=method_type_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    method_type_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> HTTPValidationError | MethodType | None:
    """Get Method Type

     Get a method type by ID.

    Please note that this endpoint will look at the Accept-Language header in the request
    to determine the language for the response data.

    Args:
        method_type_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | MethodType
    """

    return (
        await asyncio_detailed(
            method_type_id=method_type_id,
            client=client,
        )
    ).parsed
