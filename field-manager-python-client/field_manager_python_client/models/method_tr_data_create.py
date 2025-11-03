from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="MethodTRDataCreate")


@_attrs_define
class MethodTRDataCreate:
    """
    Attributes:
        depth (float | str): Depth (m)
        method_data_id (None | Unset | UUID):
        method_id (None | Unset | UUID):
        method_type_id (Literal[16] | Unset):  Default: 16.
        created_at (datetime.datetime | None | Unset):
        updated_at (datetime.datetime | None | Unset):
        penetration_rate (float | None | str | Unset): Penetration rate (mm/s)
        penetration_force (float | None | str | Unset): Penetration force (kN)
        rotation_rate (float | None | str | Unset): Rotation rate (rpm)
        rod_friction (float | None | str | Unset): Rod friction (kN)
        increased_rotation_rate (bool | Unset): Increased rotation rate
    """

    depth: float | str
    method_data_id: None | Unset | UUID = UNSET
    method_id: None | Unset | UUID = UNSET
    method_type_id: Literal[16] | Unset = 16
    created_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    penetration_rate: float | None | str | Unset = UNSET
    penetration_force: float | None | str | Unset = UNSET
    rotation_rate: float | None | str | Unset = UNSET
    rod_friction: float | None | str | Unset = UNSET
    increased_rotation_rate: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        depth: float | str
        depth = self.depth

        method_data_id: None | str | Unset
        if isinstance(self.method_data_id, Unset):
            method_data_id = UNSET
        elif isinstance(self.method_data_id, UUID):
            method_data_id = str(self.method_data_id)
        else:
            method_data_id = self.method_data_id

        method_id: None | str | Unset
        if isinstance(self.method_id, Unset):
            method_id = UNSET
        elif isinstance(self.method_id, UUID):
            method_id = str(self.method_id)
        else:
            method_id = self.method_id

        method_type_id = self.method_type_id

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

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

        increased_rotation_rate = self.increased_rotation_rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "depth": depth,
            }
        )
        if method_data_id is not UNSET:
            field_dict["method_data_id"] = method_data_id
        if method_id is not UNSET:
            field_dict["method_id"] = method_id
        if method_type_id is not UNSET:
            field_dict["method_type_id"] = method_type_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
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

        def _parse_depth(data: object) -> float | str:
            return cast(float | str, data)

        depth = _parse_depth(d.pop("depth"))

        def _parse_method_data_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                method_data_id_type_0 = UUID(data)

                return method_data_id_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | UUID, data)

        method_data_id = _parse_method_data_id(d.pop("method_data_id", UNSET))

        def _parse_method_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                method_id_type_0 = UUID(data)

                return method_id_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | UUID, data)

        method_id = _parse_method_id(d.pop("method_id", UNSET))

        method_type_id = cast(Literal[16] | Unset, d.pop("method_type_id", UNSET))
        if method_type_id != 16 and not isinstance(method_type_id, Unset):
            raise ValueError(f"method_type_id must match const 16, got '{method_type_id}'")

        def _parse_created_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = isoparse(data)

                return created_at_type_0
            except:  # noqa: E722
                pass
            return cast(datetime.datetime | None | Unset, data)

        created_at = _parse_created_at(d.pop("created_at", UNSET))

        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = isoparse(data)

                return updated_at_type_0
            except:  # noqa: E722
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))

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

        increased_rotation_rate = d.pop("increased_rotation_rate", UNSET)

        method_tr_data_create = cls(
            depth=depth,
            method_data_id=method_data_id,
            method_id=method_id,
            method_type_id=method_type_id,
            created_at=created_at,
            updated_at=updated_at,
            penetration_rate=penetration_rate,
            penetration_force=penetration_force,
            rotation_rate=rotation_rate,
            rod_friction=rod_friction,
            increased_rotation_rate=increased_rotation_rate,
        )

        method_tr_data_create.additional_properties = d
        return method_tr_data_create

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
