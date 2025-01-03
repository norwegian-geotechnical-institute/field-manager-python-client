from http import HTTPStatus
from typing import Any, Optional, Union, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    project_id: str,
    *,
    body: list[UUID],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/projects/{project_id}/files",
    }

    _body = []
    for body_item_data in body:
        body_item = str(body_item_data)
        _body.append(body_item)

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError]]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, HTTPValidationError]]:
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
    body: list[UUID],
) -> Response[Union[Any, HTTPValidationError]]:
    """Delete Files

     Batch delete project files.

    Having a request body in a DELETE method is not supported by every client library.
    If you have trouble using this endpoint, you may want to use the endpoint
    `DELETE /projects/{project_id}/files/{file_id}` instead.

    Args:
        project_id (str):
        body (list[UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient,
    body: list[UUID],
) -> Optional[Union[Any, HTTPValidationError]]:
    """Delete Files

     Batch delete project files.

    Having a request body in a DELETE method is not supported by every client library.
    If you have trouble using this endpoint, you may want to use the endpoint
    `DELETE /projects/{project_id}/files/{file_id}` instead.

    Args:
        project_id (str):
        body (list[UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient,
    body: list[UUID],
) -> Response[Union[Any, HTTPValidationError]]:
    """Delete Files

     Batch delete project files.

    Having a request body in a DELETE method is not supported by every client library.
    If you have trouble using this endpoint, you may want to use the endpoint
    `DELETE /projects/{project_id}/files/{file_id}` instead.

    Args:
        project_id (str):
        body (list[UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient,
    body: list[UUID],
) -> Optional[Union[Any, HTTPValidationError]]:
    """Delete Files

     Batch delete project files.

    Having a request body in a DELETE method is not supported by every client library.
    If you have trouble using this endpoint, you may want to use the endpoint
    `DELETE /projects/{project_id}/files/{file_id}` instead.

    Args:
        project_id (str):
        body (list[UUID]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            body=body,
        )
    ).parsed
