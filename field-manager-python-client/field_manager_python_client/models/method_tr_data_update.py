from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MethodTRDataUpdate")


@_attrs_define
class MethodTRDataUpdate:
    """
    Attributes:
        method_type_id (Literal[16] | Unset):  Default: 16.
        depth (float | None | str | Unset): Depth (m). SGF code D.
        penetration_rate (float | None | str | Unset): Penetration rate (mm/s)
        penetration_force (float | None | str | Unset): Penetration force (kN)
        rotation_rate (float | None | str | Unset): Rotation rate (rpm)
        rod_friction (float | None | str | Unset): Rod friction (kN)
        increased_rotation_rate (bool | None | Unset): Increased rotation rate
    """

    method_type_id: Literal[16] | Unset = 16
    depth: float | None | str | Unset = UNSET
    penetration_rate: float | None | str | Unset = UNSET
    penetration_force: float | None | str | Unset = UNSET
    rotation_rate: float | None | str | Unset = UNSET
    rod_friction: float | None | str | Unset = UNSET
    increased_rotation_rate: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        method_type_id = self.method_type_id

        depth: float | None | str | Unset
        if isinstance(self.depth, Unset):
            depth = UNSET
        else:
            depth = self.depth

        penetration_rate: float | None | str | Unset
        if isinstance(self.penetration_rate, Unset):
            penetration_rate = UNSET
        else:
            penetration_rate = self.penetration_rate

        penetration_force: float | None | str | Unset
        if isinstance(self.penetration_force, Unset):
            penetration_force = UNSET
        else:
            penetration_force = self.penetration_force

        rotation_rate: float | None | str | Unset
        if isinstance(self.rotation_rate, Unset):
            rotation_rate = UNSET
        else:
            rotation_rate = self.rotation_rate

        rod_friction: float | None | str | Unset
        if isinstance(self.rod_friction, Unset):
            rod_friction = UNSET
        else:
            rod_friction = self.rod_friction

        increased_rotation_rate: bool | None | Unset
        if isinstance(self.increased_rotation_rate, Unset):
            increased_rotation_rate = UNSET
        else:
            increased_rotation_rate = self.increased_rotation_rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if method_type_id is not UNSET:
            field_dict["method_type_id"] = method_type_id
        if depth is not UNSET:
            field_dict["depth"] = depth
        if penetration_rate is not UNSET:
            field_dict["penetration_rate"] = penetration_rate
        if penetration_force is not UNSET:
            field_dict["penetration_force"] = penetration_force
        if rotation_rate is not UNSET:
            field_dict["rotation_rate"] = rotation_rate
        if rod_friction is not UNSET:
            field_dict["rod_friction"] = rod_friction
        if increased_rotation_rate is not UNSET:
            field_dict["increased_rotation_rate"] = increased_rotation_rate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        method_type_id = cast(Literal[16] | Unset, d.pop("method_type_id", UNSET))
        if method_type_id != 16 and not isinstance(method_type_id, Unset):
            raise ValueError(f"method_type_id must match const 16, got '{method_type_id}'")

        def _parse_depth(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        depth = _parse_depth(d.pop("depth", UNSET))

        def _parse_penetration_rate(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        penetration_rate = _parse_penetration_rate(d.pop("penetration_rate", UNSET))

        def _parse_penetration_force(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        penetration_force = _parse_penetration_force(d.pop("penetration_force", UNSET))

        def _parse_rotation_rate(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        rotation_rate = _parse_rotation_rate(d.pop("rotation_rate", UNSET))

        def _parse_rod_friction(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        rod_friction = _parse_rod_friction(d.pop("rod_friction", UNSET))

        def _parse_increased_rotation_rate(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        increased_rotation_rate = _parse_increased_rotation_rate(d.pop("increased_rotation_rate", UNSET))

        method_tr_data_update = cls(
            method_type_id=method_type_id,
            depth=depth,
            penetration_rate=penetration_rate,
            penetration_force=penetration_force,
            rotation_rate=rotation_rate,
            rod_friction=rod_friction,
            increased_rotation_rate=increased_rotation_rate,
        )

        method_tr_data_update.additional_properties = d
        return method_tr_data_update

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
