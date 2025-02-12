from http import HTTPStatus
from typing import Any, Dict, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cross_section import CrossSection
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    project_id: str,
    cross_section_id: UUID,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/projects/{project_id}/cross_sections/{cross_section_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CrossSection, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = CrossSection.from_dict(response.json())

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
) -> Response[Union[CrossSection, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    cross_section_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Union[CrossSection, HTTPValidationError]]:
    """Get Cross Section

     Get a cross section.

    Args:
        project_id (str):
        cross_section_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CrossSection, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        cross_section_id=cross_section_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    cross_section_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[CrossSection, HTTPValidationError]]:
    """Get Cross Section

     Get a cross section.

    Args:
        project_id (str):
        cross_section_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CrossSection, HTTPValidationError]
    """

    return sync_detailed(
        project_id=project_id,
        cross_section_id=cross_section_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    cross_section_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Response[Union[CrossSection, HTTPValidationError]]:
    """Get Cross Section

     Get a cross section.

    Args:
        project_id (str):
        cross_section_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CrossSection, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        cross_section_id=cross_section_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    cross_section_id: UUID,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[CrossSection, HTTPValidationError]]:
    """Get Cross Section

     Get a cross section.

    Args:
        project_id (str):
        cross_section_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CrossSection, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            cross_section_id=cross_section_id,
            client=client,
        )
    ).parsed
