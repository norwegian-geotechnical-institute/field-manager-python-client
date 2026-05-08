from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.location_layer_export_interval import LocationLayerExportInterval


T = TypeVar("T", bound="LocationLayerExportResult")


@_attrs_define
class LocationLayerExportResult:
    """
    Attributes:
        project_external_id (str):
        location_name (str):
        layer_group_name (str):
        intervals (list[LocationLayerExportInterval]):
        coordinate_x (float | None | Unset):
        coordinate_y (float | None | Unset):
        coordinate_z (float | None | Unset):
    """

    project_external_id: str
    location_name: str
    layer_group_name: str
    intervals: list[LocationLayerExportInterval]
    coordinate_x: float | None | Unset = UNSET
    coordinate_y: float | None | Unset = UNSET
    coordinate_z: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_external_id = self.project_external_id

        location_name = self.location_name

        layer_group_name = self.layer_group_name

        intervals = []
        for intervals_item_data in self.intervals:
            intervals_item = intervals_item_data.to_dict()
            intervals.append(intervals_item)

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "project_external_id": project_external_id,
                "location_name": location_name,
                "layer_group_name": layer_group_name,
                "intervals": intervals,
            }
        )
        if coordinate_x is not UNSET:
            field_dict["coordinate_x"] = coordinate_x
        if coordinate_y is not UNSET:
            field_dict["coordinate_y"] = coordinate_y
        if coordinate_z is not UNSET:
            field_dict["coordinate_z"] = coordinate_z

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.location_layer_export_interval import LocationLayerExportInterval

        d = dict(src_dict)
        project_external_id = d.pop("project_external_id")

        location_name = d.pop("location_name")

        layer_group_name = d.pop("layer_group_name")

        intervals = []
        _intervals = d.pop("intervals")
        for intervals_item_data in _intervals:
            intervals_item = LocationLayerExportInterval.from_dict(intervals_item_data)

            intervals.append(intervals_item)

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

        location_layer_export_result = cls(
            project_external_id=project_external_id,
            location_name=location_name,
            layer_group_name=layer_group_name,
            intervals=intervals,
            coordinate_x=coordinate_x,
            coordinate_y=coordinate_y,
            coordinate_z=coordinate_z,
        )

        location_layer_export_result.additional_properties = d
        return location_layer_export_result

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
