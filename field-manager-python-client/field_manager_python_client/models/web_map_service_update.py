from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.standard_type import StandardType
from ..models.web_map_service_type import WebMapServiceType
from ..types import UNSET, Unset

T = TypeVar("T", bound="WebMapServiceUpdate")


@_attrs_define
class WebMapServiceUpdate:
    """
    Attributes:
        name (Union[None, Unset, str]):
        url (Union[None, Unset, str]):
        service_type (Union[None, Unset, WebMapServiceType]):
        available_standard_ids (Union[None, Unset, list[StandardType]]):
        description (Union[None, Unset, str]):
    """

    name: Union[None, Unset, str] = UNSET
    url: Union[None, Unset, str] = UNSET
    service_type: Union[None, Unset, WebMapServiceType] = UNSET
    available_standard_ids: Union[None, Unset, list[StandardType]] = UNSET
    description: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        url: Union[None, Unset, str]
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        service_type: Union[None, Unset, str]
        if isinstance(self.service_type, Unset):
            service_type = UNSET
        elif isinstance(self.service_type, WebMapServiceType):
            service_type = self.service_type.value
        else:
            service_type = self.service_type

        available_standard_ids: Union[None, Unset, list[str]]
        if isinstance(self.available_standard_ids, Unset):
            available_standard_ids = UNSET
        elif isinstance(self.available_standard_ids, list):
            available_standard_ids = []
            for available_standard_ids_type_0_item_data in self.available_standard_ids:
                available_standard_ids_type_0_item = available_standard_ids_type_0_item_data.value
                available_standard_ids.append(available_standard_ids_type_0_item)

        else:
            available_standard_ids = self.available_standard_ids

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if url is not UNSET:
            field_dict["url"] = url
        if service_type is not UNSET:
            field_dict["service_type"] = service_type
        if available_standard_ids is not UNSET:
            field_dict["available_standard_ids"] = available_standard_ids
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_service_type(data: object) -> Union[None, Unset, WebMapServiceType]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                service_type_type_0 = WebMapServiceType(data)

                return service_type_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, WebMapServiceType], data)

        service_type = _parse_service_type(d.pop("service_type", UNSET))

        def _parse_available_standard_ids(data: object) -> Union[None, Unset, list[StandardType]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                available_standard_ids_type_0 = []
                _available_standard_ids_type_0 = data
                for available_standard_ids_type_0_item_data in _available_standard_ids_type_0:
                    available_standard_ids_type_0_item = StandardType(available_standard_ids_type_0_item_data)

                    available_standard_ids_type_0.append(available_standard_ids_type_0_item)

                return available_standard_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[StandardType]], data)

        available_standard_ids = _parse_available_standard_ids(d.pop("available_standard_ids", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        web_map_service_update = cls(
            name=name,
            url=url,
            service_type=service_type,
            available_standard_ids=available_standard_ids,
            description=description,
        )

        web_map_service_update.additional_properties = d
        return web_map_service_update

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
