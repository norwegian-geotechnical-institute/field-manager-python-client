from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.standard_type import StandardType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.method_type import MethodType
    from ..models.sampling_technique import SamplingTechnique


T = TypeVar("T", bound="Standard")


@_attrs_define
class Standard:
    """
    Attributes:
        standard_id (StandardType):
        name (str):
        description (str):
        sort_order (int):
        method_types (list[MethodType] | Unset):
        sampling_techniques (list[SamplingTechnique] | Unset):
    """

    standard_id: StandardType
    name: str
    description: str
    sort_order: int
    method_types: list[MethodType] | Unset = UNSET
    sampling_techniques: list[SamplingTechnique] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        standard_id = self.standard_id.value

        name = self.name

        description = self.description

        sort_order = self.sort_order

        method_types: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.method_types, Unset):
            method_types = []
            for method_types_item_data in self.method_types:
                method_types_item = method_types_item_data.to_dict()
                method_types.append(method_types_item)

        sampling_techniques: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sampling_techniques, Unset):
            sampling_techniques = []
            for sampling_techniques_item_data in self.sampling_techniques:
                sampling_techniques_item = sampling_techniques_item_data.to_dict()
                sampling_techniques.append(sampling_techniques_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "standard_id": standard_id,
                "name": name,
                "description": description,
                "sort_order": sort_order,
            }
        )
        if method_types is not UNSET:
            field_dict["method_types"] = method_types
        if sampling_techniques is not UNSET:
            field_dict["sampling_techniques"] = sampling_techniques

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.method_type import MethodType
        from ..models.sampling_technique import SamplingTechnique

        d = dict(src_dict)
        standard_id = StandardType(d.pop("standard_id"))

        name = d.pop("name")

        description = d.pop("description")

        sort_order = d.pop("sort_order")

        _method_types = d.pop("method_types", UNSET)
        method_types: list[MethodType] | Unset = UNSET
        if _method_types is not UNSET:
            method_types = []
            for method_types_item_data in _method_types:
                method_types_item = MethodType.from_dict(method_types_item_data)

                method_types.append(method_types_item)

        _sampling_techniques = d.pop("sampling_techniques", UNSET)
        sampling_techniques: list[SamplingTechnique] | Unset = UNSET
        if _sampling_techniques is not UNSET:
            sampling_techniques = []
            for sampling_techniques_item_data in _sampling_techniques:
                sampling_techniques_item = SamplingTechnique.from_dict(sampling_techniques_item_data)

                sampling_techniques.append(sampling_techniques_item)

        standard = cls(
            standard_id=standard_id,
            name=name,
            description=description,
            sort_order=sort_order,
            method_types=method_types,
            sampling_techniques=sampling_techniques,
        )

        standard.additional_properties = d
        return standard

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
