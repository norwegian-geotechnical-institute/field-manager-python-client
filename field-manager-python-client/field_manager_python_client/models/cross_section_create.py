from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.language import Language
from ..types import UNSET, Unset

T = TypeVar("T", bound="CrossSectionCreate")


@_attrs_define
class CrossSectionCreate:
    """
    Attributes:
        polyline_coordinates (list[list[float]]):
        width (float):
        vertical_scale (str):
        horizontal_scale (str):
        method_ids (list[UUID]):
        name (str):
        language (Union[Unset, Language]): ISO 639-2 language three-letter codes (set 2)
    """

    polyline_coordinates: list[list[float]]
    width: float
    vertical_scale: str
    horizontal_scale: str
    method_ids: list[UUID]
    name: str
    language: Union[Unset, Language] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        language: Union[Unset, str] = UNSET
        if not isinstance(self.language, Unset):
            language = self.language.value

        field_dict: dict[str, Any] = {}
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
        if language is not UNSET:
            field_dict["language"] = language

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
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

        _language = d.pop("language", UNSET)
        language: Union[Unset, Language]
        if isinstance(_language, Unset):
            language = UNSET
        else:
            language = Language(_language)

        cross_section_create = cls(
            polyline_coordinates=polyline_coordinates,
            width=width,
            vertical_scale=vertical_scale,
            horizontal_scale=horizontal_scale,
            method_ids=method_ids,
            name=name,
            language=language,
        )

        cross_section_create.additional_properties = d
        return cross_section_create

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
