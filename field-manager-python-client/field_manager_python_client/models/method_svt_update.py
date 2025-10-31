from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.method_status_enum import MethodStatusEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="MethodSVTUpdate")


@_attrs_define
class MethodSVTUpdate:
    """
    Attributes:
        method_id (None | Unset | UUID):
        name (None | str | Unset):
        remarks (None | str | Unset):
        method_status_id (MethodStatusEnum | None | Unset):
        updated_at (datetime.datetime | None | Unset):
        updated_by (None | str | Unset):
        conducted_by (None | str | Unset):
        conducted_at (datetime.datetime | None | Unset):
        method_type_id (Literal[10] | Unset):  Default: 10.
        vane_height (float | None | str | Unset): Height of the vane used (mm).
        vane_diameter (float | None | str | Unset): Diameter of the vane used (mm).
        serial_number (None | str | Unset): Serial number of the vane used.
        calibration_date (datetime.datetime | None | Unset): Date of calibration of the vane used.
        depth_top (float | None | str | Unset):
        depth_base (float | None | str | Unset):
    """

    method_id: None | Unset | UUID = UNSET
    name: None | str | Unset = UNSET
    remarks: None | str | Unset = UNSET
    method_status_id: MethodStatusEnum | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    updated_by: None | str | Unset = UNSET
    conducted_by: None | str | Unset = UNSET
    conducted_at: datetime.datetime | None | Unset = UNSET
    method_type_id: Literal[10] | Unset = 10
    vane_height: float | None | str | Unset = UNSET
    vane_diameter: float | None | str | Unset = UNSET
    serial_number: None | str | Unset = UNSET
    calibration_date: datetime.datetime | None | Unset = UNSET
    depth_top: float | None | str | Unset = UNSET
    depth_base: float | None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        method_id: None | str | Unset
        if isinstance(self.method_id, Unset):
            method_id = UNSET
        elif isinstance(self.method_id, UUID):
            method_id = str(self.method_id)
        else:
            method_id = self.method_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        remarks: None | str | Unset
        if isinstance(self.remarks, Unset):
            remarks = UNSET
        else:
            remarks = self.remarks

        method_status_id: int | None | Unset
        if isinstance(self.method_status_id, Unset):
            method_status_id = UNSET
        elif isinstance(self.method_status_id, MethodStatusEnum):
            method_status_id = self.method_status_id.value
        else:
            method_status_id = self.method_status_id

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        updated_by: None | str | Unset
        if isinstance(self.updated_by, Unset):
            updated_by = UNSET
        else:
            updated_by = self.updated_by

        conducted_by: None | str | Unset
        if isinstance(self.conducted_by, Unset):
            conducted_by = UNSET
        else:
            conducted_by = self.conducted_by

        conducted_at: None | str | Unset
        if isinstance(self.conducted_at, Unset):
            conducted_at = UNSET
        elif isinstance(self.conducted_at, datetime.datetime):
            conducted_at = self.conducted_at.isoformat()
        else:
            conducted_at = self.conducted_at

        method_type_id = self.method_type_id

        vane_height: float | None | str | Unset
        if isinstance(self.vane_height, Unset):
            vane_height = UNSET
        else:
            vane_height = self.vane_height

        vane_diameter: float | None | str | Unset
        if isinstance(self.vane_diameter, Unset):
            vane_diameter = UNSET
        else:
            vane_diameter = self.vane_diameter

        serial_number: None | str | Unset
        if isinstance(self.serial_number, Unset):
            serial_number = UNSET
        else:
            serial_number = self.serial_number

        calibration_date: None | str | Unset
        if isinstance(self.calibration_date, Unset):
            calibration_date = UNSET
        elif isinstance(self.calibration_date, datetime.datetime):
            calibration_date = self.calibration_date.isoformat()
        else:
            calibration_date = self.calibration_date

        depth_top: float | None | str | Unset
        if isinstance(self.depth_top, Unset):
            depth_top = UNSET
        else:
            depth_top = self.depth_top

        depth_base: float | None | str | Unset
        if isinstance(self.depth_base, Unset):
            depth_base = UNSET
        else:
            depth_base = self.depth_base

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if method_id is not UNSET:
            field_dict["method_id"] = method_id
        if name is not UNSET:
            field_dict["name"] = name
        if remarks is not UNSET:
            field_dict["remarks"] = remarks
        if method_status_id is not UNSET:
            field_dict["method_status_id"] = method_status_id
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if updated_by is not UNSET:
            field_dict["updated_by"] = updated_by
        if conducted_by is not UNSET:
            field_dict["conducted_by"] = conducted_by
        if conducted_at is not UNSET:
            field_dict["conducted_at"] = conducted_at
        if method_type_id is not UNSET:
            field_dict["method_type_id"] = method_type_id
        if vane_height is not UNSET:
            field_dict["vane_height"] = vane_height
        if vane_diameter is not UNSET:
            field_dict["vane_diameter"] = vane_diameter
        if serial_number is not UNSET:
            field_dict["serial_number"] = serial_number
        if calibration_date is not UNSET:
            field_dict["calibration_date"] = calibration_date
        if depth_top is not UNSET:
            field_dict["depth_top"] = depth_top
        if depth_base is not UNSET:
            field_dict["depth_base"] = depth_base

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

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

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_remarks(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remarks = _parse_remarks(d.pop("remarks", UNSET))

        def _parse_method_status_id(data: object) -> MethodStatusEnum | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, int):
                    raise TypeError()
                method_status_id_type_0 = MethodStatusEnum(data)

                return method_status_id_type_0
            except:  # noqa: E722
                pass
            return cast(MethodStatusEnum | None | Unset, data)

        method_status_id = _parse_method_status_id(d.pop("method_status_id", UNSET))

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

        def _parse_updated_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        updated_by = _parse_updated_by(d.pop("updated_by", UNSET))

        def _parse_conducted_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        conducted_by = _parse_conducted_by(d.pop("conducted_by", UNSET))

        def _parse_conducted_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                conducted_at_type_0 = isoparse(data)

                return conducted_at_type_0
            except:  # noqa: E722
                pass
            return cast(datetime.datetime | None | Unset, data)

        conducted_at = _parse_conducted_at(d.pop("conducted_at", UNSET))

        method_type_id = cast(Literal[10] | Unset, d.pop("method_type_id", UNSET))
        if method_type_id != 10 and not isinstance(method_type_id, Unset):
            raise ValueError(f"method_type_id must match const 10, got '{method_type_id}'")

        def _parse_vane_height(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        vane_height = _parse_vane_height(d.pop("vane_height", UNSET))

        def _parse_vane_diameter(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        vane_diameter = _parse_vane_diameter(d.pop("vane_diameter", UNSET))

        def _parse_serial_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        serial_number = _parse_serial_number(d.pop("serial_number", UNSET))

        def _parse_calibration_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                calibration_date_type_0 = isoparse(data)

                return calibration_date_type_0
            except:  # noqa: E722
                pass
            return cast(datetime.datetime | None | Unset, data)

        calibration_date = _parse_calibration_date(d.pop("calibration_date", UNSET))

        def _parse_depth_top(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        depth_top = _parse_depth_top(d.pop("depth_top", UNSET))

        def _parse_depth_base(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        depth_base = _parse_depth_base(d.pop("depth_base", UNSET))

        method_svt_update = cls(
            method_id=method_id,
            name=name,
            remarks=remarks,
            method_status_id=method_status_id,
            updated_at=updated_at,
            updated_by=updated_by,
            conducted_by=conducted_by,
            conducted_at=conducted_at,
            method_type_id=method_type_id,
            vane_height=vane_height,
            vane_diameter=vane_diameter,
            serial_number=serial_number,
            calibration_date=calibration_date,
            depth_top=depth_top,
            depth_base=depth_base,
        )

        method_svt_update.additional_properties = d
        return method_svt_update

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
