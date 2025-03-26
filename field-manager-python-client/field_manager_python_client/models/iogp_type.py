from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.iogp_type_enum import IOGPTypeEnum

T = TypeVar("T", bound="IOGPType")


@_attrs_define
class IOGPType:
    """
    Attributes:
        iogp_type_id (IOGPTypeEnum): For offshore locations, an IOGP type is required
        name (str):
        description (str):
        sort_order (int):
    """

    iogp_type_id: IOGPTypeEnum
    name: str
    description: str
    sort_order: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        iogp_type_id = self.iogp_type_id.value

        name = self.name

        description = self.description

        sort_order = self.sort_order

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "iogp_type_id": iogp_type_id,
                "name": name,
                "description": description,
                "sort_order": sort_order,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        iogp_type_id = IOGPTypeEnum(d.pop("iogp_type_id"))

        name = d.pop("name")

        description = d.pop("description")

        sort_order = d.pop("sort_order")

        iogp_type = cls(
            iogp_type_id=iogp_type_id,
            name=name,
            description=description,
            sort_order=sort_order,
        )

        iogp_type.additional_properties = d
        return iogp_type

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
