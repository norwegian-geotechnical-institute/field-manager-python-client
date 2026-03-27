from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.layer_interval_with_soil_unit import LayerIntervalWithSoilUnit


T = TypeVar("T", bound="SaveLayerInterpretationResponse")


@_attrs_define
class SaveLayerInterpretationResponse:
    """Response schema for saving layer interpretation.

    Attributes:
        layer_group_location_association_id (UUID):
        layer_group_id (UUID):
        layer_group_name (str):
        intervals (list[LayerIntervalWithSoilUnit]):
    """

    layer_group_location_association_id: UUID
    layer_group_id: UUID
    layer_group_name: str
    intervals: list[LayerIntervalWithSoilUnit]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        layer_group_location_association_id = str(self.layer_group_location_association_id)

        layer_group_id = str(self.layer_group_id)

        layer_group_name = self.layer_group_name

        intervals = []
        for intervals_item_data in self.intervals:
            intervals_item = intervals_item_data.to_dict()
            intervals.append(intervals_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "layer_group_location_association_id": layer_group_location_association_id,
                "layer_group_id": layer_group_id,
                "layer_group_name": layer_group_name,
                "intervals": intervals,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.layer_interval_with_soil_unit import LayerIntervalWithSoilUnit

        d = dict(src_dict)
        layer_group_location_association_id = UUID(d.pop("layer_group_location_association_id"))

        layer_group_id = UUID(d.pop("layer_group_id"))

        layer_group_name = d.pop("layer_group_name")

        intervals = []
        _intervals = d.pop("intervals")
        for intervals_item_data in _intervals:
            intervals_item = LayerIntervalWithSoilUnit.from_dict(intervals_item_data)

            intervals.append(intervals_item)

        save_layer_interpretation_response = cls(
            layer_group_location_association_id=layer_group_location_association_id,
            layer_group_id=layer_group_id,
            layer_group_name=layer_group_name,
            intervals=intervals,
        )

        save_layer_interpretation_response.additional_properties = d
        return save_layer_interpretation_response

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
