from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.organization_min import OrganizationMin
from ...types import Response


def _get_kwargs(
    email_address: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/public/organizations/{email_address}",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | None | OrganizationMin | None:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> None | OrganizationMin:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = OrganizationMin.from_dict(data)

                return response_200_type_0
            except:  # noqa: E722
                pass
            return cast(None | OrganizationMin, data)

        response_200 = _parse_response_200(response.json())

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
) -> Response[HTTPValidationError | None | OrganizationMin]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    email_address: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[HTTPValidationError | None | OrganizationMin]:
    """Get Organization By Email Address

     Return a specific organization by email_address.

    Args:
        email_address (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | None | OrganizationMin]
    """

    kwargs = _get_kwargs(
        email_address=email_address,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    email_address: str,
    *,
    client: AuthenticatedClient | Client,
) -> HTTPValidationError | None | OrganizationMin | None:
    """Get Organization By Email Address

     Return a specific organization by email_address.

    Args:
        email_address (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | None | OrganizationMin
    """

    return sync_detailed(
        email_address=email_address,
        client=client,
    ).parsed


async def asyncio_detailed(
    email_address: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[HTTPValidationError | None | OrganizationMin]:
    """Get Organization By Email Address

     Return a specific organization by email_address.

    Args:
        email_address (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | None | OrganizationMin]
    """

    kwargs = _get_kwargs(
        email_address=email_address,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    email_address: str,
    *,
    client: AuthenticatedClient | Client,
) -> HTTPValidationError | None | OrganizationMin | None:
    """Get Organization By Email Address

     Return a specific organization by email_address.

    Args:
        email_address (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | None | OrganizationMin
    """

    return (
        await asyncio_detailed(
            email_address=email_address,
            client=client,
        )
    ).parsed
