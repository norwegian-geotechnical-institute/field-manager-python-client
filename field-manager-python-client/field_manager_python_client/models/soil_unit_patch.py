from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.hatch_style_enum import HatchStyleEnum
from ..models.soil_type_enum import SoilTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="SoilUnitPatch")


@_attrs_define
class SoilUnitPatch:
    """
    Attributes:
        name (None | str | Unset):
        soil_type (None | SoilTypeEnum | Unset):
        color (None | str | Unset):
        hatch_style (HatchStyleEnum | None | Unset):
    """

    name: None | str | Unset = UNSET
    soil_type: None | SoilTypeEnum | Unset = UNSET
    color: None | str | Unset = UNSET
    hatch_style: HatchStyleEnum | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

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

        hatch_style: None | str | Unset
        if isinstance(self.hatch_style, Unset):
            hatch_style = UNSET
        elif isinstance(self.hatch_style, HatchStyleEnum):
            hatch_style = self.hatch_style.value
        else:
            hatch_style = self.hatch_style

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if soil_type is not UNSET:
            field_dict["soil_type"] = soil_type
        if color is not UNSET:
            field_dict["color"] = color
        if hatch_style is not UNSET:
            field_dict["hatch_style"] = hatch_style

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

        def _parse_hatch_style(data: object) -> HatchStyleEnum | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                hatch_style_type_0 = HatchStyleEnum(data)

                return hatch_style_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HatchStyleEnum | None | Unset, data)

        hatch_style = _parse_hatch_style(d.pop("hatch_style", UNSET))

        soil_unit_patch = cls(
            name=name,
            soil_type=soil_type,
            color=color,
            hatch_style=hatch_style,
        )

        soil_unit_patch.additional_properties = d
        return soil_unit_patch

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
