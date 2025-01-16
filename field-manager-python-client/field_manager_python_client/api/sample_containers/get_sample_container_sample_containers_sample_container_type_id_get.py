from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.sample_container_type import SampleContainerType
from ...types import Response


def _get_kwargs(
    sample_container_type_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/sample_containers/{sample_container_type_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, SampleContainerType]]:
    if response.status_code == 200:
        response_200 = SampleContainerType.from_dict(response.json())

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
) -> Response[Union[HTTPValidationError, SampleContainerType]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    sample_container_type_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[HTTPValidationError, SampleContainerType]]:
    """Get Sample Container

    Args:
        sample_container_type_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, SampleContainerType]]
    """

    kwargs = _get_kwargs(
        sample_container_type_id=sample_container_type_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    sample_container_type_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[HTTPValidationError, SampleContainerType]]:
    """Get Sample Container

    Args:
        sample_container_type_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, SampleContainerType]
    """

    return sync_detailed(
        sample_container_type_id=sample_container_type_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    sample_container_type_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[HTTPValidationError, SampleContainerType]]:
    """Get Sample Container

    Args:
        sample_container_type_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, SampleContainerType]]
    """

    kwargs = _get_kwargs(
        sample_container_type_id=sample_container_type_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    sample_container_type_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[HTTPValidationError, SampleContainerType]]:
    """Get Sample Container

    Args:
        sample_container_type_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, SampleContainerType]
    """

    return (
        await asyncio_detailed(
            sample_container_type_id=sample_container_type_id,
            client=client,
        )
    ).parsed
