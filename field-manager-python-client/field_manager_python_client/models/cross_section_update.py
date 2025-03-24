from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.language import Language
from ..types import UNSET, Unset

T = TypeVar("T", bound="CrossSectionUpdate")


@_attrs_define
class CrossSectionUpdate:
    """
    Attributes:
        polyline_coordinates (Union[None, Unset, list[list[float]]]):
        width (Union[None, Unset, float]):
        vertical_scale (Union[None, Unset, str]):
        horizontal_scale (Union[None, Unset, str]):
        method_ids (Union[None, Unset, list[UUID]]):
        name (Union[None, Unset, str]):
        language (Union[Unset, Language]): ISO 639-2 language three-letter codes (set 2)
    """

    polyline_coordinates: Union[None, Unset, list[list[float]]] = UNSET
    width: Union[None, Unset, float] = UNSET
    vertical_scale: Union[None, Unset, str] = UNSET
    horizontal_scale: Union[None, Unset, str] = UNSET
    method_ids: Union[None, Unset, list[UUID]] = UNSET
    name: Union[None, Unset, str] = UNSET
    language: Union[Unset, Language] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        polyline_coordinates: Union[None, Unset, list[list[float]]]
        if isinstance(self.polyline_coordinates, Unset):
            polyline_coordinates = UNSET
        elif isinstance(self.polyline_coordinates, list):
            polyline_coordinates = []
            for polyline_coordinates_type_0_item_data in self.polyline_coordinates:
                polyline_coordinates_type_0_item = []
                for polyline_coordinates_type_0_item_item_data in polyline_coordinates_type_0_item_data:
                    polyline_coordinates_type_0_item_item: float
                    polyline_coordinates_type_0_item_item = polyline_coordinates_type_0_item_item_data
                    polyline_coordinates_type_0_item.append(polyline_coordinates_type_0_item_item)

                polyline_coordinates.append(polyline_coordinates_type_0_item)

        else:
            polyline_coordinates = self.polyline_coordinates

        width: Union[None, Unset, float]
        if isinstance(self.width, Unset):
            width = UNSET
        else:
            width = self.width

        vertical_scale: Union[None, Unset, str]
        if isinstance(self.vertical_scale, Unset):
            vertical_scale = UNSET
        else:
            vertical_scale = self.vertical_scale

        horizontal_scale: Union[None, Unset, str]
        if isinstance(self.horizontal_scale, Unset):
            horizontal_scale = UNSET
        else:
            horizontal_scale = self.horizontal_scale

        method_ids: Union[None, Unset, list[str]]
        if isinstance(self.method_ids, Unset):
            method_ids = UNSET
        elif isinstance(self.method_ids, list):
            method_ids = []
            for method_ids_type_0_item_data in self.method_ids:
                method_ids_type_0_item = str(method_ids_type_0_item_data)
                method_ids.append(method_ids_type_0_item)

        else:
            method_ids = self.method_ids

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        language: Union[Unset, str] = UNSET
        if not isinstance(self.language, Unset):
            language = self.language.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if polyline_coordinates is not UNSET:
            field_dict["polyline_coordinates"] = polyline_coordinates
        if width is not UNSET:
            field_dict["width"] = width
        if vertical_scale is not UNSET:
            field_dict["vertical_scale"] = vertical_scale
        if horizontal_scale is not UNSET:
            field_dict["horizontal_scale"] = horizontal_scale
        if method_ids is not UNSET:
            field_dict["method_ids"] = method_ids
        if name is not UNSET:
            field_dict["name"] = name
        if language is not UNSET:
            field_dict["language"] = language

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_polyline_coordinates(data: object) -> Union[None, Unset, list[list[float]]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                polyline_coordinates_type_0 = []
                _polyline_coordinates_type_0 = data
                for polyline_coordinates_type_0_item_data in _polyline_coordinates_type_0:
                    polyline_coordinates_type_0_item = []
                    _polyline_coordinates_type_0_item = polyline_coordinates_type_0_item_data
                    for polyline_coordinates_type_0_item_item_data in _polyline_coordinates_type_0_item:

                        def _parse_polyline_coordinates_type_0_item_item(data: object) -> float:
                            return cast(float, data)

                        polyline_coordinates_type_0_item_item = _parse_polyline_coordinates_type_0_item_item(
                            polyline_coordinates_type_0_item_item_data
                        )

                        polyline_coordinates_type_0_item.append(polyline_coordinates_type_0_item_item)

                    polyline_coordinates_type_0.append(polyline_coordinates_type_0_item)

                return polyline_coordinates_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[list[float]]], data)

        polyline_coordinates = _parse_polyline_coordinates(d.pop("polyline_coordinates", UNSET))

        def _parse_width(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        width = _parse_width(d.pop("width", UNSET))

        def _parse_vertical_scale(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        vertical_scale = _parse_vertical_scale(d.pop("vertical_scale", UNSET))

        def _parse_horizontal_scale(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        horizontal_scale = _parse_horizontal_scale(d.pop("horizontal_scale", UNSET))

        def _parse_method_ids(data: object) -> Union[None, Unset, list[UUID]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                method_ids_type_0 = []
                _method_ids_type_0 = data
                for method_ids_type_0_item_data in _method_ids_type_0:
                    method_ids_type_0_item = UUID(method_ids_type_0_item_data)

                    method_ids_type_0.append(method_ids_type_0_item)

                return method_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[UUID]], data)

        method_ids = _parse_method_ids(d.pop("method_ids", UNSET))

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        _language = d.pop("language", UNSET)
        language: Union[Unset, Language]
        if isinstance(_language, Unset):
            language = UNSET
        else:
            language = Language(_language)

        cross_section_update = cls(
            polyline_coordinates=polyline_coordinates,
            width=width,
            vertical_scale=vertical_scale,
            horizontal_scale=horizontal_scale,
            method_ids=method_ids,
            name=name,
            language=language,
        )

        cross_section_update.additional_properties = d
        return cross_section_update

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
