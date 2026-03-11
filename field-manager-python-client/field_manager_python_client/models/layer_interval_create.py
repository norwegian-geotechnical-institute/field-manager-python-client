from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LayerIntervalCreate")


@_attrs_define
class LayerIntervalCreate:
    """Schema for creating a new layer interval.

    Attributes:
        soil_unit_id (UUID):
        start_depth (float):
        end_depth (float):
    """

    soil_unit_id: UUID
    start_depth: float
    end_depth: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        soil_unit_id = str(self.soil_unit_id)

        start_depth = self.start_depth

        end_depth = self.end_depth

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "soil_unit_id": soil_unit_id,
                "start_depth": start_depth,
                "end_depth": end_depth,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        soil_unit_id = UUID(d.pop("soil_unit_id"))

        start_depth = d.pop("start_depth")

        end_depth = d.pop("end_depth")

        layer_interval_create = cls(
            soil_unit_id=soil_unit_id,
            start_depth=start_depth,
            end_depth=end_depth,
        )

        layer_interval_create.additional_properties = d
        return layer_interval_create

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
