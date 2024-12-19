from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SampleContainerType")


@_attrs_define
class SampleContainerType:
    """
    Attributes:
        sample_container_type_id (int):
        name (str):
        description (str):
        sort_order (int):
    """

    sample_container_type_id: int
    name: str
    description: str
    sort_order: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sample_container_type_id = self.sample_container_type_id

        name = self.name

        description = self.description

        sort_order = self.sort_order

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sample_container_type_id": sample_container_type_id,
                "name": name,
                "description": description,
                "sort_order": sort_order,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        sample_container_type_id = d.pop("sample_container_type_id")

        name = d.pop("name")

        description = d.pop("description")

        sort_order = d.pop("sort_order")

        sample_container_type = cls(
            sample_container_type_id=sample_container_type_id,
            name=name,
            description=description,
            sort_order=sort_order,
        )

        sample_container_type.additional_properties = d
        return sample_container_type

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
