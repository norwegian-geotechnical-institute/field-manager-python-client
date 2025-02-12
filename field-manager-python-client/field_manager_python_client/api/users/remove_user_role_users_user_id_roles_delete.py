from http import HTTPStatus
from typing import Any, Dict, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response


def _get_kwargs(
    user_id: UUID,
    *,
    role_name: str,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["role_name"] = role_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "delete",
        "url": f"/users/{user_id}/roles",
        "params": params,
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
    user_id: UUID,
    *,
    client: AuthenticatedClient,
    role_name: str,
) -> Response[HTTPValidationError]:
    r"""Remove User Role

     Delete a user's role

    You need to be either an application administrator, organization administrator or a project
    administrator in the
    same project as the role is attached to.

    The role_name parameter is the string representation of the role. The format is \"admin--\"

    Args:
        user_id (UUID):
        role_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        role_name=role_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: UUID,
    *,
    client: AuthenticatedClient,
    role_name: str,
) -> Optional[HTTPValidationError]:
    r"""Remove User Role

     Delete a user's role

    You need to be either an application administrator, organization administrator or a project
    administrator in the
    same project as the role is attached to.

    The role_name parameter is the string representation of the role. The format is \"admin--\"

    Args:
        user_id (UUID):
        role_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        role_name=role_name,
    ).parsed


async def asyncio_detailed(
    user_id: UUID,
    *,
    client: AuthenticatedClient,
    role_name: str,
) -> Response[HTTPValidationError]:
    r"""Remove User Role

     Delete a user's role

    You need to be either an application administrator, organization administrator or a project
    administrator in the
    same project as the role is attached to.

    The role_name parameter is the string representation of the role. The format is \"admin--\"

    Args:
        user_id (UUID):
        role_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        role_name=role_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: UUID,
    *,
    client: AuthenticatedClient,
    role_name: str,
) -> Optional[HTTPValidationError]:
    r"""Remove User Role

     Delete a user's role

    You need to be either an application administrator, organization administrator or a project
    administrator in the
    same project as the role is attached to.

    The role_name parameter is the string representation of the role. The format is \"admin--\"

    Args:
        user_id (UUID):
        role_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            role_name=role_name,
        )
    ).parsed
