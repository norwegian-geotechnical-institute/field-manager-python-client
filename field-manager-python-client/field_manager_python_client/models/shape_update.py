from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.shape_color import ShapeColor
from ..types import UNSET, Unset

T = TypeVar("T", bound="ShapeUpdate")


@_attrs_define
class ShapeUpdate:
    """
    Attributes:
        name (Union[None, Unset, str]):
        line_thickness (Union[None, Unset, int]):
        color (Union[None, ShapeColor, Unset]):
    """

    name: Union[None, Unset, str] = UNSET
    line_thickness: Union[None, Unset, int] = UNSET
    color: Union[None, ShapeColor, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        line_thickness: Union[None, Unset, int]
        if isinstance(self.line_thickness, Unset):
            line_thickness = UNSET
        else:
            line_thickness = self.line_thickness

        color: Union[None, Unset, str]
        if isinstance(self.color, Unset):
            color = UNSET
        elif isinstance(self.color, ShapeColor):
            color = self.color.value
        else:
            color = self.color

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if line_thickness is not UNSET:
            field_dict["line_thickness"] = line_thickness
        if color is not UNSET:
            field_dict["color"] = color

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_line_thickness(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        line_thickness = _parse_line_thickness(d.pop("line_thickness", UNSET))

        def _parse_color(data: object) -> Union[None, ShapeColor, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                color_type_0 = ShapeColor(data)

                return color_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, ShapeColor, Unset], data)

        color = _parse_color(d.pop("color", UNSET))

        shape_update = cls(
            name=name,
            line_thickness=line_thickness,
            color=color,
        )

        shape_update.additional_properties = d
        return shape_update

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
