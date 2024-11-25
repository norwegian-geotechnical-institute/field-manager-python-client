from typing import Any, Dict, List, Type, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CrossSectionCreate")


@_attrs_define
class CrossSectionCreate:
    """
    Attributes:
        polyline_coordinates (List[List[float]]):
        width (float):
        vertical_scale (str):
        horizontal_scale (str):
        method_ids (List[UUID]):
        name (str):
    """

    polyline_coordinates: List[List[float]]
    width: float
    vertical_scale: str
    horizontal_scale: str
    method_ids: List[UUID]
    name: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        polyline_coordinates = []
        for polyline_coordinates_item_data in self.polyline_coordinates:
            polyline_coordinates_item = []
            for polyline_coordinates_item_item_data in polyline_coordinates_item_data:
                polyline_coordinates_item_item: float
                polyline_coordinates_item_item = polyline_coordinates_item_item_data
                polyline_coordinates_item.append(polyline_coordinates_item_item)

            polyline_coordinates.append(polyline_coordinates_item)

        width = self.width

        vertical_scale = self.vertical_scale

        horizontal_scale = self.horizontal_scale

        method_ids = []
        for method_ids_item_data in self.method_ids:
            method_ids_item = str(method_ids_item_data)
            method_ids.append(method_ids_item)

        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "polyline_coordinates": polyline_coordinates,
                "width": width,
                "vertical_scale": vertical_scale,
                "horizontal_scale": horizontal_scale,
                "method_ids": method_ids,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        polyline_coordinates = []
        _polyline_coordinates = d.pop("polyline_coordinates")
        for polyline_coordinates_item_data in _polyline_coordinates:
            polyline_coordinates_item = []
            _polyline_coordinates_item = polyline_coordinates_item_data
            for polyline_coordinates_item_item_data in _polyline_coordinates_item:

                def _parse_polyline_coordinates_item_item(data: object) -> float:
                    return cast(float, data)

                polyline_coordinates_item_item = _parse_polyline_coordinates_item_item(
                    polyline_coordinates_item_item_data
                )

                polyline_coordinates_item.append(polyline_coordinates_item_item)

            polyline_coordinates.append(polyline_coordinates_item)

        width = d.pop("width")

        vertical_scale = d.pop("vertical_scale")

        horizontal_scale = d.pop("horizontal_scale")

        method_ids = []
        _method_ids = d.pop("method_ids")
        for method_ids_item_data in _method_ids:
            method_ids_item = UUID(method_ids_item_data)

            method_ids.append(method_ids_item)

        name = d.pop("name")

        cross_section_create = cls(
            polyline_coordinates=polyline_coordinates,
            width=width,
            vertical_scale=vertical_scale,
            horizontal_scale=horizontal_scale,
            method_ids=method_ids,
            name=name,
        )

        cross_section_create.additional_properties = d
        return cross_section_create

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
