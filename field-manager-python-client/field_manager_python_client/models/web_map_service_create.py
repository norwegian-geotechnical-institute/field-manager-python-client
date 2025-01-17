from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.standard_type import StandardType
from ..models.web_map_service_type import WebMapServiceType
from ..types import UNSET, Unset

T = TypeVar("T", bound="WebMapServiceCreate")


@_attrs_define
class WebMapServiceCreate:
    """
    Attributes:
        name (str):
        url (str):
        service_type (WebMapServiceType):
        available_standard_ids (Union[Unset, list[StandardType]]):
        description (Union[None, Unset, str]):
    """

    name: str
    url: str
    service_type: WebMapServiceType
    available_standard_ids: Union[Unset, list[StandardType]] = UNSET
    description: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        url = self.url

        service_type = self.service_type.value

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
                "name": name,
                "url": url,
                "service_type": service_type,
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
        name = d.pop("name")

        url = d.pop("url")

        service_type = WebMapServiceType(d.pop("service_type"))

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

        web_map_service_create = cls(
            name=name,
            url=url,
            service_type=service_type,
            available_standard_ids=available_standard_ids,
            description=description,
        )

        web_map_service_create.additional_properties = d
        return web_map_service_create

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
