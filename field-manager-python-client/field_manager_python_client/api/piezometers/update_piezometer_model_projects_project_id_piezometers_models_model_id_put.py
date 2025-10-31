from http import HTTPStatus
from typing import Any, cast
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.piezometer_model import PiezometerModel
from ...models.piezometer_model_update import PiezometerModelUpdate
from ...types import Response


def _get_kwargs(
    project_id: str,
    model_id: UUID,
    *,
    body: PiezometerModelUpdate,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/projects/{project_id}/piezometers/models/{model_id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | None | PiezometerModel | None:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> None | PiezometerModel:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = PiezometerModel.from_dict(data)

                return response_200_type_0
            except:  # noqa: E722
                pass
            return cast(None | PiezometerModel, data)

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
) -> Response[HTTPValidationError | None | PiezometerModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    model_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PiezometerModelUpdate,
) -> Response[HTTPValidationError | None | PiezometerModel]:
    """Update Piezometer Model

     Update piezometer model

    Args:
        project_id (str):
        model_id (UUID):
        body (PiezometerModelUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | None | PiezometerModel]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        model_id=model_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    model_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PiezometerModelUpdate,
) -> HTTPValidationError | None | PiezometerModel | None:
    """Update Piezometer Model

     Update piezometer model

    Args:
        project_id (str):
        model_id (UUID):
        body (PiezometerModelUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | None | PiezometerModel
    """

    return sync_detailed(
        project_id=project_id,
        model_id=model_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    model_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PiezometerModelUpdate,
) -> Response[HTTPValidationError | None | PiezometerModel]:
    """Update Piezometer Model

     Update piezometer model

    Args:
        project_id (str):
        model_id (UUID):
        body (PiezometerModelUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | None | PiezometerModel]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        model_id=model_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    model_id: UUID,
    *,
    client: AuthenticatedClient,
    body: PiezometerModelUpdate,
) -> HTTPValidationError | None | PiezometerModel | None:
    """Update Piezometer Model

     Update piezometer model

    Args:
        project_id (str):
        model_id (UUID):
        body (PiezometerModelUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | None | PiezometerModel
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            model_id=model_id,
            client=client,
            body=body,
        )
    ).parsed
