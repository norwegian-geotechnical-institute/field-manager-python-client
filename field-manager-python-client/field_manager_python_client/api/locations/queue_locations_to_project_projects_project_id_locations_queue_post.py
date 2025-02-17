from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.body_queue_locations_to_project_projects_project_id_locations_queue_post import (
    BodyQueueLocationsToProjectProjectsProjectIdLocationsQueuePost,
)
from ...models.file import File
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    *,
    body: BodyQueueLocationsToProjectProjectsProjectIdLocationsQueuePost,
    srid: Union[None, Unset, int] = UNSET,
    swap_x_y: Union[None, Unset, bool] = False,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_srid: Union[None, Unset, int]
    if isinstance(srid, Unset):
        json_srid = UNSET
    else:
        json_srid = srid
    params["srid"] = json_srid

    json_swap_x_y: Union[None, Unset, bool]
    if isinstance(swap_x_y, Unset):
        json_swap_x_y = UNSET
    else:
        json_swap_x_y = swap_x_y
    params["swap_x_y"] = json_swap_x_y

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/projects/{project_id}/locations/queue",
        "params": params,
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
    project_id: str,
    *,
    client: AuthenticatedClient,
    body: BodyQueueLocationsToProjectProjectsProjectIdLocationsQueuePost,
    srid: Union[None, Unset, int] = UNSET,
    swap_x_y: Union[None, Unset, bool] = False,
) -> Response[Union[File, HTTPValidationError]]:
    """Queue Locations To Project

     Upload location file and add to queue for parsing.

    Supported file extensions: .ags, .csv, .gvr, .kof, .snd, .xlsx, .xls and image files.


    Parsing of the file is done asynchronously, so the response can be returned before parsing is done.

    You may check the status of the parsing by using the endpoints specified here:
    https://app.fieldmanager.io/developer/file-director

    Args:
        project_id (str):
        srid (Union[None, Unset, int]):
        swap_x_y (Union[None, Unset, bool]):  Default: False.
        body (BodyQueueLocationsToProjectProjectsProjectIdLocationsQueuePost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[File, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
        srid=srid,
        swap_x_y=swap_x_y,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient,
    body: BodyQueueLocationsToProjectProjectsProjectIdLocationsQueuePost,
    srid: Union[None, Unset, int] = UNSET,
    swap_x_y: Union[None, Unset, bool] = False,
) -> Optional[Union[File, HTTPValidationError]]:
    """Queue Locations To Project

     Upload location file and add to queue for parsing.

    Supported file extensions: .ags, .csv, .gvr, .kof, .snd, .xlsx, .xls and image files.


    Parsing of the file is done asynchronously, so the response can be returned before parsing is done.

    You may check the status of the parsing by using the endpoints specified here:
    https://app.fieldmanager.io/developer/file-director

    Args:
        project_id (str):
        srid (Union[None, Unset, int]):
        swap_x_y (Union[None, Unset, bool]):  Default: False.
        body (BodyQueueLocationsToProjectProjectsProjectIdLocationsQueuePost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[File, HTTPValidationError]
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        body=body,
        srid=srid,
        swap_x_y=swap_x_y,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient,
    body: BodyQueueLocationsToProjectProjectsProjectIdLocationsQueuePost,
    srid: Union[None, Unset, int] = UNSET,
    swap_x_y: Union[None, Unset, bool] = False,
) -> Response[Union[File, HTTPValidationError]]:
    """Queue Locations To Project

     Upload location file and add to queue for parsing.

    Supported file extensions: .ags, .csv, .gvr, .kof, .snd, .xlsx, .xls and image files.


    Parsing of the file is done asynchronously, so the response can be returned before parsing is done.

    You may check the status of the parsing by using the endpoints specified here:
    https://app.fieldmanager.io/developer/file-director

    Args:
        project_id (str):
        srid (Union[None, Unset, int]):
        swap_x_y (Union[None, Unset, bool]):  Default: False.
        body (BodyQueueLocationsToProjectProjectsProjectIdLocationsQueuePost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[File, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
        srid=srid,
        swap_x_y=swap_x_y,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient,
    body: BodyQueueLocationsToProjectProjectsProjectIdLocationsQueuePost,
    srid: Union[None, Unset, int] = UNSET,
    swap_x_y: Union[None, Unset, bool] = False,
) -> Optional[Union[File, HTTPValidationError]]:
    """Queue Locations To Project

     Upload location file and add to queue for parsing.

    Supported file extensions: .ags, .csv, .gvr, .kof, .snd, .xlsx, .xls and image files.


    Parsing of the file is done asynchronously, so the response can be returned before parsing is done.

    You may check the status of the parsing by using the endpoints specified here:
    https://app.fieldmanager.io/developer/file-director

    Args:
        project_id (str):
        srid (Union[None, Unset, int]):
        swap_x_y (Union[None, Unset, bool]):  Default: False.
        body (BodyQueueLocationsToProjectProjectsProjectIdLocationsQueuePost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[File, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            body=body,
            srid=srid,
            swap_x_y=swap_x_y,
        )
    ).parsed
