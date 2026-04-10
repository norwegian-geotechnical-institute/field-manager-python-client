from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.soil_type_enum import SoilTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="LocationLayerFilterResult")


@_attrs_define
class LocationLayerFilterResult:
    """
    Attributes:
        location_id (UUID):
        point_x_wgs84_web (float | None | Unset):
        point_y_wgs84_web (float | None | Unset):
        point_x_wgs84_pseudo (float | None | Unset):
        point_y_wgs84_pseudo (float | None | Unset):
        color (None | str | Unset):
        soil_type (None | SoilTypeEnum | Unset):
        rule_label (None | str | Unset):
    """

    location_id: UUID
    point_x_wgs84_web: float | None | Unset = UNSET
    point_y_wgs84_web: float | None | Unset = UNSET
    point_x_wgs84_pseudo: float | None | Unset = UNSET
    point_y_wgs84_pseudo: float | None | Unset = UNSET
    color: None | str | Unset = UNSET
    soil_type: None | SoilTypeEnum | Unset = UNSET
    rule_label: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        location_id = str(self.location_id)

        point_x_wgs84_web: float | None | Unset
        if isinstance(self.point_x_wgs84_web, Unset):
            point_x_wgs84_web = UNSET
        else:
            point_x_wgs84_web = self.point_x_wgs84_web

        point_y_wgs84_web: float | None | Unset
        if isinstance(self.point_y_wgs84_web, Unset):
            point_y_wgs84_web = UNSET
        else:
            point_y_wgs84_web = self.point_y_wgs84_web

        point_x_wgs84_pseudo: float | None | Unset
        if isinstance(self.point_x_wgs84_pseudo, Unset):
            point_x_wgs84_pseudo = UNSET
        else:
            point_x_wgs84_pseudo = self.point_x_wgs84_pseudo

        point_y_wgs84_pseudo: float | None | Unset
        if isinstance(self.point_y_wgs84_pseudo, Unset):
            point_y_wgs84_pseudo = UNSET
        else:
            point_y_wgs84_pseudo = self.point_y_wgs84_pseudo

        color: None | str | Unset
        if isinstance(self.color, Unset):
            color = UNSET
        else:
            color = self.color

        soil_type: None | str | Unset
        if isinstance(self.soil_type, Unset):
            soil_type = UNSET
        elif isinstance(self.soil_type, SoilTypeEnum):
            soil_type = self.soil_type.value
        else:
            soil_type = self.soil_type

        rule_label: None | str | Unset
        if isinstance(self.rule_label, Unset):
            rule_label = UNSET
        else:
            rule_label = self.rule_label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "location_id": location_id,
            }
        )
        if point_x_wgs84_web is not UNSET:
            field_dict["point_x_wgs84_web"] = point_x_wgs84_web
        if point_y_wgs84_web is not UNSET:
            field_dict["point_y_wgs84_web"] = point_y_wgs84_web
        if point_x_wgs84_pseudo is not UNSET:
            field_dict["point_x_wgs84_pseudo"] = point_x_wgs84_pseudo
        if point_y_wgs84_pseudo is not UNSET:
            field_dict["point_y_wgs84_pseudo"] = point_y_wgs84_pseudo
        if color is not UNSET:
            field_dict["color"] = color
        if soil_type is not UNSET:
            field_dict["soil_type"] = soil_type
        if rule_label is not UNSET:
            field_dict["rule_label"] = rule_label

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        location_id = UUID(d.pop("location_id"))

        def _parse_point_x_wgs84_web(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        point_x_wgs84_web = _parse_point_x_wgs84_web(d.pop("point_x_wgs84_web", UNSET))

        def _parse_point_y_wgs84_web(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        point_y_wgs84_web = _parse_point_y_wgs84_web(d.pop("point_y_wgs84_web", UNSET))

        def _parse_point_x_wgs84_pseudo(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        point_x_wgs84_pseudo = _parse_point_x_wgs84_pseudo(d.pop("point_x_wgs84_pseudo", UNSET))

        def _parse_point_y_wgs84_pseudo(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        point_y_wgs84_pseudo = _parse_point_y_wgs84_pseudo(d.pop("point_y_wgs84_pseudo", UNSET))

        def _parse_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        color = _parse_color(d.pop("color", UNSET))

        def _parse_soil_type(data: object) -> None | SoilTypeEnum | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                soil_type_type_0 = SoilTypeEnum(data)

                return soil_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SoilTypeEnum | Unset, data)

        soil_type = _parse_soil_type(d.pop("soil_type", UNSET))

        def _parse_rule_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rule_label = _parse_rule_label(d.pop("rule_label", UNSET))

        location_layer_filter_result = cls(
            location_id=location_id,
            point_x_wgs84_web=point_x_wgs84_web,
            point_y_wgs84_web=point_y_wgs84_web,
            point_x_wgs84_pseudo=point_x_wgs84_pseudo,
            point_y_wgs84_pseudo=point_y_wgs84_pseudo,
            color=color,
            soil_type=soil_type,
            rule_label=rule_label,
        )

        location_layer_filter_result.additional_properties = d
        return location_layer_filter_result

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
