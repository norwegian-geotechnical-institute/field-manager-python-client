from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="MethodCPTDataCreate")


@_attrs_define
class MethodCPTDataCreate:
    """
    Attributes:
        depth (float | str): Depth (m). SGF code D.
        method_data_id (None | Unset | UUID):
        method_id (None | Unset | UUID):
        method_type_id (Literal[1] | Unset):  Default: 1.
        created_at (datetime.datetime | None | Unset):
        updated_at (datetime.datetime | None | Unset):
        penetration_rate (float | None | str | Unset):
        penetration_force (float | None | str | Unset):
        fs (float | None | str | Unset):
        comment_code (int | None | Unset):
        conductivity (float | None | str | Unset):
        zero_value_resistance (float | None | str | Unset):
        zero_value_friction (float | None | str | Unset):
        zero_value_pressure (float | None | str | Unset):
        temperature (float | None | str | Unset):
        qc (float | None | str | Unset):
        remarks (None | str | Unset):
        tilt (float | None | str | Unset):
        u2 (float | None | str | Unset):
    """

    depth: float | str
    method_data_id: None | Unset | UUID = UNSET
    method_id: None | Unset | UUID = UNSET
    method_type_id: Literal[1] | Unset = 1
    created_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    penetration_rate: float | None | str | Unset = UNSET
    penetration_force: float | None | str | Unset = UNSET
    fs: float | None | str | Unset = UNSET
    comment_code: int | None | Unset = UNSET
    conductivity: float | None | str | Unset = UNSET
    zero_value_resistance: float | None | str | Unset = UNSET
    zero_value_friction: float | None | str | Unset = UNSET
    zero_value_pressure: float | None | str | Unset = UNSET
    temperature: float | None | str | Unset = UNSET
    qc: float | None | str | Unset = UNSET
    remarks: None | str | Unset = UNSET
    tilt: float | None | str | Unset = UNSET
    u2: float | None | str | Unset = UNSET
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

        fs: float | None | str | Unset
        if isinstance(self.fs, Unset):
            fs = UNSET
        else:
            fs = self.fs

        comment_code: int | None | Unset
        if isinstance(self.comment_code, Unset):
            comment_code = UNSET
        else:
            comment_code = self.comment_code

        conductivity: float | None | str | Unset
        if isinstance(self.conductivity, Unset):
            conductivity = UNSET
        else:
            conductivity = self.conductivity

        zero_value_resistance: float | None | str | Unset
        if isinstance(self.zero_value_resistance, Unset):
            zero_value_resistance = UNSET
        else:
            zero_value_resistance = self.zero_value_resistance

        zero_value_friction: float | None | str | Unset
        if isinstance(self.zero_value_friction, Unset):
            zero_value_friction = UNSET
        else:
            zero_value_friction = self.zero_value_friction

        zero_value_pressure: float | None | str | Unset
        if isinstance(self.zero_value_pressure, Unset):
            zero_value_pressure = UNSET
        else:
            zero_value_pressure = self.zero_value_pressure

        temperature: float | None | str | Unset
        if isinstance(self.temperature, Unset):
            temperature = UNSET
        else:
            temperature = self.temperature

        qc: float | None | str | Unset
        if isinstance(self.qc, Unset):
            qc = UNSET
        else:
            qc = self.qc

        remarks: None | str | Unset
        if isinstance(self.remarks, Unset):
            remarks = UNSET
        else:
            remarks = self.remarks

        tilt: float | None | str | Unset
        if isinstance(self.tilt, Unset):
            tilt = UNSET
        else:
            tilt = self.tilt

        u2: float | None | str | Unset
        if isinstance(self.u2, Unset):
            u2 = UNSET
        else:
            u2 = self.u2

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
        if fs is not UNSET:
            field_dict["fs"] = fs
        if comment_code is not UNSET:
            field_dict["comment_code"] = comment_code
        if conductivity is not UNSET:
            field_dict["conductivity"] = conductivity
        if zero_value_resistance is not UNSET:
            field_dict["zero_value_resistance"] = zero_value_resistance
        if zero_value_friction is not UNSET:
            field_dict["zero_value_friction"] = zero_value_friction
        if zero_value_pressure is not UNSET:
            field_dict["zero_value_pressure"] = zero_value_pressure
        if temperature is not UNSET:
            field_dict["temperature"] = temperature
        if qc is not UNSET:
            field_dict["qc"] = qc
        if remarks is not UNSET:
            field_dict["remarks"] = remarks
        if tilt is not UNSET:
            field_dict["tilt"] = tilt
        if u2 is not UNSET:
            field_dict["u2"] = u2

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

        method_type_id = cast(Literal[1] | Unset, d.pop("method_type_id", UNSET))
        if method_type_id != 1 and not isinstance(method_type_id, Unset):
            raise ValueError(f"method_type_id must match const 1, got '{method_type_id}'")

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

        def _parse_fs(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        fs = _parse_fs(d.pop("fs", UNSET))

        def _parse_comment_code(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        comment_code = _parse_comment_code(d.pop("comment_code", UNSET))

        def _parse_conductivity(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        conductivity = _parse_conductivity(d.pop("conductivity", UNSET))

        def _parse_zero_value_resistance(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        zero_value_resistance = _parse_zero_value_resistance(d.pop("zero_value_resistance", UNSET))

        def _parse_zero_value_friction(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        zero_value_friction = _parse_zero_value_friction(d.pop("zero_value_friction", UNSET))

        def _parse_zero_value_pressure(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        zero_value_pressure = _parse_zero_value_pressure(d.pop("zero_value_pressure", UNSET))

        def _parse_temperature(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        temperature = _parse_temperature(d.pop("temperature", UNSET))

        def _parse_qc(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        qc = _parse_qc(d.pop("qc", UNSET))

        def _parse_remarks(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remarks = _parse_remarks(d.pop("remarks", UNSET))

        def _parse_tilt(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        tilt = _parse_tilt(d.pop("tilt", UNSET))

        def _parse_u2(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        u2 = _parse_u2(d.pop("u2", UNSET))

        method_cpt_data_create = cls(
            depth=depth,
            method_data_id=method_data_id,
            method_id=method_id,
            method_type_id=method_type_id,
            created_at=created_at,
            updated_at=updated_at,
            penetration_rate=penetration_rate,
            penetration_force=penetration_force,
            fs=fs,
            comment_code=comment_code,
            conductivity=conductivity,
            zero_value_resistance=zero_value_resistance,
            zero_value_friction=zero_value_friction,
            zero_value_pressure=zero_value_pressure,
            temperature=temperature,
            qc=qc,
            remarks=remarks,
            tilt=tilt,
            u2=u2,
        )

        method_cpt_data_create.additional_properties = d
        return method_cpt_data_create

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
