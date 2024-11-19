from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bff_project_summary import BFFProjectSummary
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    skip: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 100,
    tags: Union[Unset, List[str]] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["skip"] = skip

    params["limit"] = limit

    json_tags: Union[Unset, List[str]] = UNSET
    if not isinstance(tags, Unset):
        json_tags = tags

    params["tags"] = json_tags

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/project_summaries",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, List["BFFProjectSummary"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = BFFProjectSummary.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[Union[HTTPValidationError, List["BFFProjectSummary"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    skip: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 100,
    tags: Union[Unset, List[str]] = UNSET,
) -> Response[Union[HTTPValidationError, List["BFFProjectSummary"]]]:
    """Get Project Summaries

     This is a very heavy and specialized endpoint, only returning exactly what is needed for displaying
    information
    in the landing page (Projects with geometry boundary and some special).

    Args:
        skip (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 100.
        tags (Union[Unset, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, List['BFFProjectSummary']]]
    """

    kwargs = _get_kwargs(
        skip=skip,
        limit=limit,
        tags=tags,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    skip: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 100,
    tags: Union[Unset, List[str]] = UNSET,
) -> Optional[Union[HTTPValidationError, List["BFFProjectSummary"]]]:
    """Get Project Summaries

     This is a very heavy and specialized endpoint, only returning exactly what is needed for displaying
    information
    in the landing page (Projects with geometry boundary and some special).

    Args:
        skip (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 100.
        tags (Union[Unset, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, List['BFFProjectSummary']]
    """

    return sync_detailed(
        client=client,
        skip=skip,
        limit=limit,
        tags=tags,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    skip: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 100,
    tags: Union[Unset, List[str]] = UNSET,
) -> Response[Union[HTTPValidationError, List["BFFProjectSummary"]]]:
    """Get Project Summaries

     This is a very heavy and specialized endpoint, only returning exactly what is needed for displaying
    information
    in the landing page (Projects with geometry boundary and some special).

    Args:
        skip (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 100.
        tags (Union[Unset, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, List['BFFProjectSummary']]]
    """

    kwargs = _get_kwargs(
        skip=skip,
        limit=limit,
        tags=tags,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    skip: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 100,
    tags: Union[Unset, List[str]] = UNSET,
) -> Optional[Union[HTTPValidationError, List["BFFProjectSummary"]]]:
    """Get Project Summaries

     This is a very heavy and specialized endpoint, only returning exactly what is needed for displaying
    information
    in the landing page (Projects with geometry boundary and some special).

    Args:
        skip (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 100.
        tags (Union[Unset, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, List['BFFProjectSummary']]
    """

    return (
        await asyncio_detailed(
            client=client,
            skip=skip,
            limit=limit,
            tags=tags,
        )
    ).parsed
