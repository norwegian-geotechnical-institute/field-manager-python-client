from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.soil_type_enum import SoilTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="LocationLayerIntervalSegment")


@_attrs_define
class LocationLayerIntervalSegment:
    """
    Attributes:
        soil_unit_id (UUID):
        soil_unit_name (str):
        soil_type (SoilTypeEnum): Standardized soil type classifications
        start_depth (float):
        end_depth (float):
        color (None | str | Unset):
    """

    soil_unit_id: UUID
    soil_unit_name: str
    soil_type: SoilTypeEnum
    start_depth: float
    end_depth: float
    color: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        soil_unit_id = str(self.soil_unit_id)

        soil_unit_name = self.soil_unit_name

        soil_type = self.soil_type.value

        start_depth = self.start_depth

        end_depth = self.end_depth

        color: None | str | Unset
        if isinstance(self.color, Unset):
            color = UNSET
        else:
            color = self.color

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "soil_unit_id": soil_unit_id,
                "soil_unit_name": soil_unit_name,
                "soil_type": soil_type,
                "start_depth": start_depth,
                "end_depth": end_depth,
            }
        )
        if color is not UNSET:
            field_dict["color"] = color

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        soil_unit_id = UUID(d.pop("soil_unit_id"))

        soil_unit_name = d.pop("soil_unit_name")

        soil_type = SoilTypeEnum(d.pop("soil_type"))

        start_depth = d.pop("start_depth")

        end_depth = d.pop("end_depth")

        def _parse_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        color = _parse_color(d.pop("color", UNSET))

        location_layer_interval_segment = cls(
            soil_unit_id=soil_unit_id,
            soil_unit_name=soil_unit_name,
            soil_type=soil_type,
            start_depth=start_depth,
            end_depth=end_depth,
            color=color,
        )

        location_layer_interval_segment.additional_properties = d
        return location_layer_interval_segment

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
