from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.shape_color import ShapeColor
from ..types import UNSET, Unset

T = TypeVar("T", bound="ShapeUpdate")


@_attrs_define
class ShapeUpdate:
    """
    Attributes:
        name (None | str | Unset):
        line_thickness (int | None | Unset):
        color (None | ShapeColor | Unset):
    """

    name: None | str | Unset = UNSET
    line_thickness: int | None | Unset = UNSET
    color: None | ShapeColor | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        line_thickness: int | None | Unset
        if isinstance(self.line_thickness, Unset):
            line_thickness = UNSET
        else:
            line_thickness = self.line_thickness

        color: None | str | Unset
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

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_line_thickness(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        line_thickness = _parse_line_thickness(d.pop("line_thickness", UNSET))

        def _parse_color(data: object) -> None | ShapeColor | Unset:
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
            return cast(None | ShapeColor | Unset, data)

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
