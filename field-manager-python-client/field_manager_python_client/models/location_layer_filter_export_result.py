from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.soil_type_enum import SoilTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="LocationLayerFilterExportResult")


@_attrs_define
class LocationLayerFilterExportResult:
    """
    Attributes:
        location_id (UUID):
        project_external_id (str):
        location_name (str):
        layer_group_name (str):
        coordinate_x (float | None | Unset):
        coordinate_y (float | None | Unset):
        coordinate_z (float | None | Unset):
        layer_name (None | str | Unset):
        soil_type (None | SoilTypeEnum | Unset):
        color (None | str | Unset):
        depth_in_soil (float | None | Unset):
    """

    location_id: UUID
    project_external_id: str
    location_name: str
    layer_group_name: str
    coordinate_x: float | None | Unset = UNSET
    coordinate_y: float | None | Unset = UNSET
    coordinate_z: float | None | Unset = UNSET
    layer_name: None | str | Unset = UNSET
    soil_type: None | SoilTypeEnum | Unset = UNSET
    color: None | str | Unset = UNSET
    depth_in_soil: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        location_id = str(self.location_id)

        project_external_id = self.project_external_id

        location_name = self.location_name

        layer_group_name = self.layer_group_name

        coordinate_x: float | None | Unset
        if isinstance(self.coordinate_x, Unset):
            coordinate_x = UNSET
        else:
            coordinate_x = self.coordinate_x

        coordinate_y: float | None | Unset
        if isinstance(self.coordinate_y, Unset):
            coordinate_y = UNSET
        else:
            coordinate_y = self.coordinate_y

        coordinate_z: float | None | Unset
        if isinstance(self.coordinate_z, Unset):
            coordinate_z = UNSET
        else:
            coordinate_z = self.coordinate_z

        layer_name: None | str | Unset
        if isinstance(self.layer_name, Unset):
            layer_name = UNSET
        else:
            layer_name = self.layer_name

        soil_type: None | str | Unset
        if isinstance(self.soil_type, Unset):
            soil_type = UNSET
        elif isinstance(self.soil_type, SoilTypeEnum):
            soil_type = self.soil_type.value
        else:
            soil_type = self.soil_type

        color: None | str | Unset
        if isinstance(self.color, Unset):
            color = UNSET
        else:
            color = self.color

        depth_in_soil: float | None | Unset
        if isinstance(self.depth_in_soil, Unset):
            depth_in_soil = UNSET
        else:
            depth_in_soil = self.depth_in_soil

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "location_id": location_id,
                "project_external_id": project_external_id,
                "location_name": location_name,
                "layer_group_name": layer_group_name,
            }
        )
        if coordinate_x is not UNSET:
            field_dict["coordinate_x"] = coordinate_x
        if coordinate_y is not UNSET:
            field_dict["coordinate_y"] = coordinate_y
        if coordinate_z is not UNSET:
            field_dict["coordinate_z"] = coordinate_z
        if layer_name is not UNSET:
            field_dict["layer_name"] = layer_name
        if soil_type is not UNSET:
            field_dict["soil_type"] = soil_type
        if color is not UNSET:
            field_dict["color"] = color
        if depth_in_soil is not UNSET:
            field_dict["depth_in_soil"] = depth_in_soil

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        location_id = UUID(d.pop("location_id"))

        project_external_id = d.pop("project_external_id")

        location_name = d.pop("location_name")

        layer_group_name = d.pop("layer_group_name")

        def _parse_coordinate_x(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        coordinate_x = _parse_coordinate_x(d.pop("coordinate_x", UNSET))

        def _parse_coordinate_y(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        coordinate_y = _parse_coordinate_y(d.pop("coordinate_y", UNSET))

        def _parse_coordinate_z(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        coordinate_z = _parse_coordinate_z(d.pop("coordinate_z", UNSET))

        def _parse_layer_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        layer_name = _parse_layer_name(d.pop("layer_name", UNSET))

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

        def _parse_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        color = _parse_color(d.pop("color", UNSET))

        def _parse_depth_in_soil(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        depth_in_soil = _parse_depth_in_soil(d.pop("depth_in_soil", UNSET))

        location_layer_filter_export_result = cls(
            location_id=location_id,
            project_external_id=project_external_id,
            location_name=location_name,
            layer_group_name=layer_group_name,
            coordinate_x=coordinate_x,
            coordinate_y=coordinate_y,
            coordinate_z=coordinate_z,
            layer_name=layer_name,
            soil_type=soil_type,
            color=color,
            depth_in_soil=depth_in_soil,
        )

        location_layer_filter_export_result.additional_properties = d
        return location_layer_filter_export_result

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
