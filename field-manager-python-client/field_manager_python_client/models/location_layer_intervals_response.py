from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.location_layer_intervals_result import LocationLayerIntervalsResult


T = TypeVar("T", bound="LocationLayerIntervalsResponse")


@_attrs_define
class LocationLayerIntervalsResponse:
    """
    Attributes:
        layer_group_id (UUID):
        locations (list[LocationLayerIntervalsResult]):
    """

    layer_group_id: UUID
    locations: list[LocationLayerIntervalsResult]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        layer_group_id = str(self.layer_group_id)

        locations = []
        for locations_item_data in self.locations:
            locations_item = locations_item_data.to_dict()
            locations.append(locations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "layer_group_id": layer_group_id,
                "locations": locations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.location_layer_intervals_result import LocationLayerIntervalsResult

        d = dict(src_dict)
        layer_group_id = UUID(d.pop("layer_group_id"))

        locations = []
        _locations = d.pop("locations")
        for locations_item_data in _locations:
            locations_item = LocationLayerIntervalsResult.from_dict(locations_item_data)

            locations.append(locations_item)

        location_layer_intervals_response = cls(
            layer_group_id=layer_group_id,
            locations=locations,
        )

        location_layer_intervals_response.additional_properties = d
        return location_layer_intervals_response

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
