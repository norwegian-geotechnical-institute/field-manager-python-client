from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SamplingTechnique")


@_attrs_define
class SamplingTechnique:
    """
    Attributes:
        sampling_technique_id (int):
        name (str):
        description (str):
        sort_order (int):
        is_disturbed (bool):
    """

    sampling_technique_id: int
    name: str
    description: str
    sort_order: int
    is_disturbed: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sampling_technique_id = self.sampling_technique_id

        name = self.name

        description = self.description

        sort_order = self.sort_order

        is_disturbed = self.is_disturbed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sampling_technique_id": sampling_technique_id,
                "name": name,
                "description": description,
                "sort_order": sort_order,
                "is_disturbed": is_disturbed,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        sampling_technique_id = d.pop("sampling_technique_id")

        name = d.pop("name")

        description = d.pop("description")

        sort_order = d.pop("sort_order")

        is_disturbed = d.pop("is_disturbed")

        sampling_technique = cls(
            sampling_technique_id=sampling_technique_id,
            name=name,
            description=description,
            sort_order=sort_order,
            is_disturbed=is_disturbed,
        )

        sampling_technique.additional_properties = d
        return sampling_technique

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
