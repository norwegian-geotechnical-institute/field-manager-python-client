from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="MethodCPTData")


@_attrs_define
class MethodCPTData:
    """
    Attributes:
        method_data_id (UUID):
        method_id (UUID):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        depth (float): Depth (m). SGF code D.
        method_type_id (Literal[1] | Unset):  Default: 1.
        penetration_rate (float | None | Unset): Penetration rate (mm/s). SGF code B.
        penetration_force (float | None | Unset): Penetration force (kN). SGF code A.
        fs (float | None | Unset): Friction (kPa). SGF code FS/F.
        comment_code (int | None | Unset): Comment code. Two digit value.
        conductivity (float | None | Unset): Conductivity (S/m). SGF code M.
        zero_value_resistance (float | None | Unset): Zero value resistance (MPa). SGF code NA.
        zero_value_friction (float | None | Unset): Zero value friction (kPa). SGF code NB.
        zero_value_pressure (float | None | Unset): Zero value pressure (kPa). SGF code NC.
        temperature (float | None | Unset): Temperature (degree C). SGF code O.
        qc (float | None | Unset): Resistance (MPa). SGF code QC.
        remarks (None | str | Unset): Remarks. SGF code T
        tilt (float | None | Unset): Inclination (degree). SGF code TA.
        u2 (float | None | Unset): Shoulder pressure (kPa). SGF code U.
    """

    method_data_id: UUID
    method_id: UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    depth: float
    method_type_id: Literal[1] | Unset = 1
    penetration_rate: float | None | Unset = UNSET
    penetration_force: float | None | Unset = UNSET
    fs: float | None | Unset = UNSET
    comment_code: int | None | Unset = UNSET
    conductivity: float | None | Unset = UNSET
    zero_value_resistance: float | None | Unset = UNSET
    zero_value_friction: float | None | Unset = UNSET
    zero_value_pressure: float | None | Unset = UNSET
    temperature: float | None | Unset = UNSET
    qc: float | None | Unset = UNSET
    remarks: None | str | Unset = UNSET
    tilt: float | None | Unset = UNSET
    u2: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        method_data_id = str(self.method_data_id)

        method_id = str(self.method_id)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        depth = self.depth

        method_type_id = self.method_type_id

        penetration_rate: float | None | Unset
        if isinstance(self.penetration_rate, Unset):
            penetration_rate = UNSET
        else:
            penetration_rate = self.penetration_rate

        penetration_force: float | None | Unset
        if isinstance(self.penetration_force, Unset):
            penetration_force = UNSET
        else:
            penetration_force = self.penetration_force

        fs: float | None | Unset
        if isinstance(self.fs, Unset):
            fs = UNSET
        else:
            fs = self.fs

        comment_code: int | None | Unset
        if isinstance(self.comment_code, Unset):
            comment_code = UNSET
        else:
            comment_code = self.comment_code

        conductivity: float | None | Unset
        if isinstance(self.conductivity, Unset):
            conductivity = UNSET
        else:
            conductivity = self.conductivity

        zero_value_resistance: float | None | Unset
        if isinstance(self.zero_value_resistance, Unset):
            zero_value_resistance = UNSET
        else:
            zero_value_resistance = self.zero_value_resistance

        zero_value_friction: float | None | Unset
        if isinstance(self.zero_value_friction, Unset):
            zero_value_friction = UNSET
        else:
            zero_value_friction = self.zero_value_friction

        zero_value_pressure: float | None | Unset
        if isinstance(self.zero_value_pressure, Unset):
            zero_value_pressure = UNSET
        else:
            zero_value_pressure = self.zero_value_pressure

        temperature: float | None | Unset
        if isinstance(self.temperature, Unset):
            temperature = UNSET
        else:
            temperature = self.temperature

        qc: float | None | Unset
        if isinstance(self.qc, Unset):
            qc = UNSET
        else:
            qc = self.qc

        remarks: None | str | Unset
        if isinstance(self.remarks, Unset):
            remarks = UNSET
        else:
            remarks = self.remarks

        tilt: float | None | Unset
        if isinstance(self.tilt, Unset):
            tilt = UNSET
        else:
            tilt = self.tilt

        u2: float | None | Unset
        if isinstance(self.u2, Unset):
            u2 = UNSET
        else:
            u2 = self.u2

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "method_data_id": method_data_id,
                "method_id": method_id,
                "created_at": created_at,
                "updated_at": updated_at,
                "depth": depth,
            }
        )
        if method_type_id is not UNSET:
            field_dict["method_type_id"] = method_type_id
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
        method_data_id = UUID(d.pop("method_data_id"))

        method_id = UUID(d.pop("method_id"))

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        depth = d.pop("depth")

        method_type_id = cast(Literal[1] | Unset, d.pop("method_type_id", UNSET))
        if method_type_id != 1 and not isinstance(method_type_id, Unset):
            raise ValueError(f"method_type_id must match const 1, got '{method_type_id}'")

        def _parse_penetration_rate(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        penetration_rate = _parse_penetration_rate(d.pop("penetration_rate", UNSET))

        def _parse_penetration_force(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        penetration_force = _parse_penetration_force(d.pop("penetration_force", UNSET))

        def _parse_fs(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        fs = _parse_fs(d.pop("fs", UNSET))

        def _parse_comment_code(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        comment_code = _parse_comment_code(d.pop("comment_code", UNSET))

        def _parse_conductivity(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        conductivity = _parse_conductivity(d.pop("conductivity", UNSET))

        def _parse_zero_value_resistance(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        zero_value_resistance = _parse_zero_value_resistance(d.pop("zero_value_resistance", UNSET))

        def _parse_zero_value_friction(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        zero_value_friction = _parse_zero_value_friction(d.pop("zero_value_friction", UNSET))

        def _parse_zero_value_pressure(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        zero_value_pressure = _parse_zero_value_pressure(d.pop("zero_value_pressure", UNSET))

        def _parse_temperature(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        temperature = _parse_temperature(d.pop("temperature", UNSET))

        def _parse_qc(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        qc = _parse_qc(d.pop("qc", UNSET))

        def _parse_remarks(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remarks = _parse_remarks(d.pop("remarks", UNSET))

        def _parse_tilt(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        tilt = _parse_tilt(d.pop("tilt", UNSET))

        def _parse_u2(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        u2 = _parse_u2(d.pop("u2", UNSET))

        method_cpt_data = cls(
            method_data_id=method_data_id,
            method_id=method_id,
            created_at=created_at,
            updated_at=updated_at,
            depth=depth,
            method_type_id=method_type_id,
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

        method_cpt_data.additional_properties = d
        return method_cpt_data

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
