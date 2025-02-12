from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_upload_file_to_organization_organizations_organization_id_upload_post import (
    BodyUploadFileToOrganizationOrganizationsOrganizationIdUploadPost,
)
from ...models.file import File
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    organization_id: str,
    *,
    body: BodyUploadFileToOrganizationOrganizationsOrganizationIdUploadPost,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/organizations/{organization_id}/upload",
    }

    _body = body.to_multipart()

    _kwargs["files"] = _body

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[File, HTTPValidationError]]:
    if response.status_code == 201:
        response_201 = File.from_dict(response.json())

        return response_201
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[File, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organization_id: str,
    *,
    client: AuthenticatedClient,
    body: BodyUploadFileToOrganizationOrganizationsOrganizationIdUploadPost,
) -> Response[Union[File, HTTPValidationError]]:
    """Upload File To Organization

     Upload data file to organization. The file is not parsed, but only attached to the organization.

    Args:
        organization_id (str):
        body (BodyUploadFileToOrganizationOrganizationsOrganizationIdUploadPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[File, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: str,
    *,
    client: AuthenticatedClient,
    body: BodyUploadFileToOrganizationOrganizationsOrganizationIdUploadPost,
) -> Optional[Union[File, HTTPValidationError]]:
    """Upload File To Organization

     Upload data file to organization. The file is not parsed, but only attached to the organization.

    Args:
        organization_id (str):
        body (BodyUploadFileToOrganizationOrganizationsOrganizationIdUploadPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[File, HTTPValidationError]
    """

    return sync_detailed(
        organization_id=organization_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    *,
    client: AuthenticatedClient,
    body: BodyUploadFileToOrganizationOrganizationsOrganizationIdUploadPost,
) -> Response[Union[File, HTTPValidationError]]:
    """Upload File To Organization

     Upload data file to organization. The file is not parsed, but only attached to the organization.

    Args:
        organization_id (str):
        body (BodyUploadFileToOrganizationOrganizationsOrganizationIdUploadPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[File, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: str,
    *,
    client: AuthenticatedClient,
    body: BodyUploadFileToOrganizationOrganizationsOrganizationIdUploadPost,
) -> Optional[Union[File, HTTPValidationError]]:
    """Upload File To Organization

     Upload data file to organization. The file is not parsed, but only attached to the organization.

    Args:
        organization_id (str):
        body (BodyUploadFileToOrganizationOrganizationsOrganizationIdUploadPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[File, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            client=client,
            body=body,
        )
    ).parsed
