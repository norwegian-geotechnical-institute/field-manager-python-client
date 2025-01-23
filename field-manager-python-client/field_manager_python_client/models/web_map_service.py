from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.standard_type import StandardType
from ..models.web_map_service_type import WebMapServiceType
from ..types import UNSET, Unset

T = TypeVar("T", bound="WebMapService")


@_attrs_define
class WebMapService:
    """
    Attributes:
        web_map_service_id (UUID):
        name (str):
        url (str):
        service_type (WebMapServiceType):
        organization_id (Union[None, UUID]): The ID for the organization that owns this web map service. If null, it is
            global.
        is_application_layer (bool): True if this web map service is global for the application. Output only.
        available_standard_ids (Union[Unset, list[StandardType]]):
        description (Union[None, Unset, str]):
    """

    web_map_service_id: UUID
    name: str
    url: str
    service_type: WebMapServiceType
    organization_id: Union[None, UUID]
    is_application_layer: bool
    available_standard_ids: Union[Unset, list[StandardType]] = UNSET
    description: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        web_map_service_id = str(self.web_map_service_id)

        name = self.name

        url = self.url

        service_type = self.service_type.value

        organization_id: Union[None, str]
        if isinstance(self.organization_id, UUID):
            organization_id = str(self.organization_id)
        else:
            organization_id = self.organization_id

        is_application_layer = self.is_application_layer

        available_standard_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.available_standard_ids, Unset):
            available_standard_ids = []
            for available_standard_ids_item_data in self.available_standard_ids:
                available_standard_ids_item = available_standard_ids_item_data.value
                available_standard_ids.append(available_standard_ids_item)

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "web_map_service_id": web_map_service_id,
                "name": name,
                "url": url,
                "service_type": service_type,
                "organization_id": organization_id,
                "is_application_layer": is_application_layer,
            }
        )
        if available_standard_ids is not UNSET:
            field_dict["available_standard_ids"] = available_standard_ids
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        web_map_service_id = UUID(d.pop("web_map_service_id"))

        name = d.pop("name")

        url = d.pop("url")

        service_type = WebMapServiceType(d.pop("service_type"))

        def _parse_organization_id(data: object) -> Union[None, UUID]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                organization_id_type_0 = UUID(data)

                return organization_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID], data)

        organization_id = _parse_organization_id(d.pop("organization_id"))

        is_application_layer = d.pop("is_application_layer")

        available_standard_ids = []
        _available_standard_ids = d.pop("available_standard_ids", UNSET)
        for available_standard_ids_item_data in _available_standard_ids or []:
            available_standard_ids_item = StandardType(available_standard_ids_item_data)

            available_standard_ids.append(available_standard_ids_item)

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        web_map_service = cls(
            web_map_service_id=web_map_service_id,
            name=name,
            url=url,
            service_type=service_type,
            organization_id=organization_id,
            is_application_layer=is_application_layer,
            available_standard_ids=available_standard_ids,
            description=description,
        )

        web_map_service.additional_properties = d
        return web_map_service

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
