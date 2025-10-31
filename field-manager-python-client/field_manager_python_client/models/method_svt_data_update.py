from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MethodSVTDataUpdate")


@_attrs_define
class MethodSVTDataUpdate:
    """
    Attributes:
        method_type_id (Literal[10] | Unset):  Default: 10.
        depth_top (float | None | str | Unset): Depth (m).
        maximum_measurement_torque (float | None | str | Unset): Maximum measurement torque (Nm).
        maximum_measurement_torque_remoulded (float | None | str | Unset): Maximum measurement torque (Nm).
        shear_strength (float | None | str | Unset): Shear strength (kPa). SGF code AS.
        shear_strength_remoulded (float | None | str | Unset): Shear strength (kPa).
        sensitivity (float | None | str | Unset): Sensitivity (unitless). SGF code SV.
        remarks (None | str | Unset):
    """

    method_type_id: Literal[10] | Unset = 10
    depth_top: float | None | str | Unset = UNSET
    maximum_measurement_torque: float | None | str | Unset = UNSET
    maximum_measurement_torque_remoulded: float | None | str | Unset = UNSET
    shear_strength: float | None | str | Unset = UNSET
    shear_strength_remoulded: float | None | str | Unset = UNSET
    sensitivity: float | None | str | Unset = UNSET
    remarks: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        method_type_id = self.method_type_id

        depth_top: float | None | str | Unset
        if isinstance(self.depth_top, Unset):
            depth_top = UNSET
        else:
            depth_top = self.depth_top

        maximum_measurement_torque: float | None | str | Unset
        if isinstance(self.maximum_measurement_torque, Unset):
            maximum_measurement_torque = UNSET
        else:
            maximum_measurement_torque = self.maximum_measurement_torque

        maximum_measurement_torque_remoulded: float | None | str | Unset
        if isinstance(self.maximum_measurement_torque_remoulded, Unset):
            maximum_measurement_torque_remoulded = UNSET
        else:
            maximum_measurement_torque_remoulded = self.maximum_measurement_torque_remoulded

        shear_strength: float | None | str | Unset
        if isinstance(self.shear_strength, Unset):
            shear_strength = UNSET
        else:
            shear_strength = self.shear_strength

        shear_strength_remoulded: float | None | str | Unset
        if isinstance(self.shear_strength_remoulded, Unset):
            shear_strength_remoulded = UNSET
        else:
            shear_strength_remoulded = self.shear_strength_remoulded

        sensitivity: float | None | str | Unset
        if isinstance(self.sensitivity, Unset):
            sensitivity = UNSET
        else:
            sensitivity = self.sensitivity

        remarks: None | str | Unset
        if isinstance(self.remarks, Unset):
            remarks = UNSET
        else:
            remarks = self.remarks

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if method_type_id is not UNSET:
            field_dict["method_type_id"] = method_type_id
        if depth_top is not UNSET:
            field_dict["depth_top"] = depth_top
        if maximum_measurement_torque is not UNSET:
            field_dict["maximum_measurement_torque"] = maximum_measurement_torque
        if maximum_measurement_torque_remoulded is not UNSET:
            field_dict["maximum_measurement_torque_remoulded"] = maximum_measurement_torque_remoulded
        if shear_strength is not UNSET:
            field_dict["shear_strength"] = shear_strength
        if shear_strength_remoulded is not UNSET:
            field_dict["shear_strength_remoulded"] = shear_strength_remoulded
        if sensitivity is not UNSET:
            field_dict["sensitivity"] = sensitivity
        if remarks is not UNSET:
            field_dict["remarks"] = remarks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        method_type_id = cast(Literal[10] | Unset, d.pop("method_type_id", UNSET))
        if method_type_id != 10 and not isinstance(method_type_id, Unset):
            raise ValueError(f"method_type_id must match const 10, got '{method_type_id}'")

        def _parse_depth_top(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        depth_top = _parse_depth_top(d.pop("depth_top", UNSET))

        def _parse_maximum_measurement_torque(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        maximum_measurement_torque = _parse_maximum_measurement_torque(d.pop("maximum_measurement_torque", UNSET))

        def _parse_maximum_measurement_torque_remoulded(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        maximum_measurement_torque_remoulded = _parse_maximum_measurement_torque_remoulded(
            d.pop("maximum_measurement_torque_remoulded", UNSET)
        )

        def _parse_shear_strength(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        shear_strength = _parse_shear_strength(d.pop("shear_strength", UNSET))

        def _parse_shear_strength_remoulded(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        shear_strength_remoulded = _parse_shear_strength_remoulded(d.pop("shear_strength_remoulded", UNSET))

        def _parse_sensitivity(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        sensitivity = _parse_sensitivity(d.pop("sensitivity", UNSET))

        def _parse_remarks(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remarks = _parse_remarks(d.pop("remarks", UNSET))

        method_svt_data_update = cls(
            method_type_id=method_type_id,
            depth_top=depth_top,
            maximum_measurement_torque=maximum_measurement_torque,
            maximum_measurement_torque_remoulded=maximum_measurement_torque_remoulded,
            shear_strength=shear_strength,
            shear_strength_remoulded=shear_strength_remoulded,
            sensitivity=sensitivity,
            remarks=remarks,
        )

        method_svt_data_update.additional_properties = d
        return method_svt_data_update

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
