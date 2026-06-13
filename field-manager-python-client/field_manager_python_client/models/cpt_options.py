from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.scaling_mode import ScalingMode
from ..models.standard_type import StandardType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CPTOptions")


@_attrs_define
class CPTOptions:
    """
    Attributes:
        scaling_mode (ScalingMode | Unset):
        percentile (float | Unset):  Default: 0.975.
        standard (StandardType | Unset):
    """

    scaling_mode: ScalingMode | Unset = UNSET
    percentile: float | Unset = 0.975
    standard: StandardType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        scaling_mode: str | Unset = UNSET
        if not isinstance(self.scaling_mode, Unset):
            scaling_mode = self.scaling_mode.value

        percentile = self.percentile

        standard: str | Unset = UNSET
        if not isinstance(self.standard, Unset):
            standard = self.standard.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if scaling_mode is not UNSET:
            field_dict["scaling_mode"] = scaling_mode
        if percentile is not UNSET:
            field_dict["percentile"] = percentile
        if standard is not UNSET:
            field_dict["standard"] = standard

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _scaling_mode = d.pop("scaling_mode", UNSET)
        scaling_mode: ScalingMode | Unset
        if isinstance(_scaling_mode, Unset):
            scaling_mode = UNSET
        else:
            scaling_mode = ScalingMode(_scaling_mode)

        percentile = d.pop("percentile", UNSET)

        _standard = d.pop("standard", UNSET)
        standard: StandardType | Unset
        if isinstance(_standard, Unset):
            standard = UNSET
        else:
            standard = StandardType(_standard)

        cpt_options = cls(
            scaling_mode=scaling_mode,
            percentile=percentile,
            standard=standard,
        )

        cpt_options.additional_properties = d
        return cpt_options

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
