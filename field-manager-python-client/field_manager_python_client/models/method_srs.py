from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.method_status_enum import MethodStatusEnum
from ..models.sounding_class import SoundingClass
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file import File


T = TypeVar("T", bound="MethodSRS")


@_attrs_define
class MethodSRS:
    """SRS method
    Soil-Rock Sounding (Swedish Jord-bergsondering)

        Attributes:
            method_id (UUID):
            name (str):
            location_id (UUID):
            method_status_id (MethodStatusEnum): (
                PLANNED=1,
                READY=2,
                CONDUCTED=3,
                VOIDED=4,
                APPROVED=5,
                )
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
            remarks (None | str | Unset):
            method_type_id (Literal[24] | Unset):  Default: 24.
            created_by (None | str | Unset):
            updated_by (None | str | Unset):
            conducted_at (datetime.datetime | None | Unset):
            conducted_by (None | str | Unset):
            files (list[File] | Unset):
            self_ (None | str | Unset):
            sounding_class (None | SoundingClass | Unset):
            serial_number (None | str | Unset):
            calibration_date (datetime.datetime | None | Unset):
            conversion_factor (float | None | Unset):
            depth_top (float | None | Unset):
            depth_base (float | None | Unset):
            stopcode (int | None | Unset):
            depth_in_soil (float | None | Unset):
            depth_in_rock (float | None | Unset):
            bedrock_elevation (float | None | Unset):
    """

    method_id: UUID
    name: str
    location_id: UUID
    method_status_id: MethodStatusEnum
    created_at: datetime.datetime
    updated_at: datetime.datetime
    remarks: None | str | Unset = UNSET
    method_type_id: Literal[24] | Unset = 24
    created_by: None | str | Unset = UNSET
    updated_by: None | str | Unset = UNSET
    conducted_at: datetime.datetime | None | Unset = UNSET
    conducted_by: None | str | Unset = UNSET
    files: list[File] | Unset = UNSET
    self_: None | str | Unset = UNSET
    sounding_class: None | SoundingClass | Unset = UNSET
    serial_number: None | str | Unset = UNSET
    calibration_date: datetime.datetime | None | Unset = UNSET
    conversion_factor: float | None | Unset = UNSET
    depth_top: float | None | Unset = UNSET
    depth_base: float | None | Unset = UNSET
    stopcode: int | None | Unset = UNSET
    depth_in_soil: float | None | Unset = UNSET
    depth_in_rock: float | None | Unset = UNSET
    bedrock_elevation: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        method_id = str(self.method_id)

        name = self.name

        location_id = str(self.location_id)

        method_status_id = self.method_status_id.value

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        remarks: None | str | Unset
        if isinstance(self.remarks, Unset):
            remarks = UNSET
        else:
            remarks = self.remarks

        method_type_id = self.method_type_id

        created_by: None | str | Unset
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        else:
            created_by = self.created_by

        updated_by: None | str | Unset
        if isinstance(self.updated_by, Unset):
            updated_by = UNSET
        else:
            updated_by = self.updated_by

        conducted_at: None | str | Unset
        if isinstance(self.conducted_at, Unset):
            conducted_at = UNSET
        elif isinstance(self.conducted_at, datetime.datetime):
            conducted_at = self.conducted_at.isoformat()
        else:
            conducted_at = self.conducted_at

        conducted_by: None | str | Unset
        if isinstance(self.conducted_by, Unset):
            conducted_by = UNSET
        else:
            conducted_by = self.conducted_by

        files: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = []
            for files_item_data in self.files:
                files_item = files_item_data.to_dict()
                files.append(files_item)

        self_: None | str | Unset
        if isinstance(self.self_, Unset):
            self_ = UNSET
        else:
            self_ = self.self_

        sounding_class: None | str | Unset
        if isinstance(self.sounding_class, Unset):
            sounding_class = UNSET
        elif isinstance(self.sounding_class, SoundingClass):
            sounding_class = self.sounding_class.value
        else:
            sounding_class = self.sounding_class

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

        conversion_factor: float | None | Unset
        if isinstance(self.conversion_factor, Unset):
            conversion_factor = UNSET
        else:
            conversion_factor = self.conversion_factor

        depth_top: float | None | Unset
        if isinstance(self.depth_top, Unset):
            depth_top = UNSET
        else:
            depth_top = self.depth_top

        depth_base: float | None | Unset
        if isinstance(self.depth_base, Unset):
            depth_base = UNSET
        else:
            depth_base = self.depth_base

        stopcode: int | None | Unset
        if isinstance(self.stopcode, Unset):
            stopcode = UNSET
        else:
            stopcode = self.stopcode

        depth_in_soil: float | None | Unset
        if isinstance(self.depth_in_soil, Unset):
            depth_in_soil = UNSET
        else:
            depth_in_soil = self.depth_in_soil

        depth_in_rock: float | None | Unset
        if isinstance(self.depth_in_rock, Unset):
            depth_in_rock = UNSET
        else:
            depth_in_rock = self.depth_in_rock

        bedrock_elevation: float | None | Unset
        if isinstance(self.bedrock_elevation, Unset):
            bedrock_elevation = UNSET
        else:
            bedrock_elevation = self.bedrock_elevation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "method_id": method_id,
                "name": name,
                "location_id": location_id,
                "method_status_id": method_status_id,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if remarks is not UNSET:
            field_dict["remarks"] = remarks
        if method_type_id is not UNSET:
            field_dict["method_type_id"] = method_type_id
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if updated_by is not UNSET:
            field_dict["updated_by"] = updated_by
        if conducted_at is not UNSET:
            field_dict["conducted_at"] = conducted_at
        if conducted_by is not UNSET:
            field_dict["conducted_by"] = conducted_by
        if files is not UNSET:
            field_dict["files"] = files
        if self_ is not UNSET:
            field_dict["self"] = self_
        if sounding_class is not UNSET:
            field_dict["sounding_class"] = sounding_class
        if serial_number is not UNSET:
            field_dict["serial_number"] = serial_number
        if calibration_date is not UNSET:
            field_dict["calibration_date"] = calibration_date
        if conversion_factor is not UNSET:
            field_dict["conversion_factor"] = conversion_factor
        if depth_top is not UNSET:
            field_dict["depth_top"] = depth_top
        if depth_base is not UNSET:
            field_dict["depth_base"] = depth_base
        if stopcode is not UNSET:
            field_dict["stopcode"] = stopcode
        if depth_in_soil is not UNSET:
            field_dict["depth_in_soil"] = depth_in_soil
        if depth_in_rock is not UNSET:
            field_dict["depth_in_rock"] = depth_in_rock
        if bedrock_elevation is not UNSET:
            field_dict["bedrock_elevation"] = bedrock_elevation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file import File

        d = dict(src_dict)
        method_id = UUID(d.pop("method_id"))

        name = d.pop("name")

        location_id = UUID(d.pop("location_id"))

        method_status_id = MethodStatusEnum(d.pop("method_status_id"))

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        def _parse_remarks(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remarks = _parse_remarks(d.pop("remarks", UNSET))

        method_type_id = cast(Literal[24] | Unset, d.pop("method_type_id", UNSET))
        if method_type_id != 24 and not isinstance(method_type_id, Unset):
            raise ValueError(f"method_type_id must match const 24, got '{method_type_id}'")

        def _parse_created_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_by = _parse_created_by(d.pop("created_by", UNSET))

        def _parse_updated_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        updated_by = _parse_updated_by(d.pop("updated_by", UNSET))

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

        def _parse_conducted_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        conducted_by = _parse_conducted_by(d.pop("conducted_by", UNSET))

        files = []
        _files = d.pop("files", UNSET)
        for files_item_data in _files or []:
            files_item = File.from_dict(files_item_data)

            files.append(files_item)

        def _parse_self_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        self_ = _parse_self_(d.pop("self", UNSET))

        def _parse_sounding_class(data: object) -> None | SoundingClass | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sounding_class_type_0 = SoundingClass(data)

                return sounding_class_type_0
            except:  # noqa: E722
                pass
            return cast(None | SoundingClass | Unset, data)

        sounding_class = _parse_sounding_class(d.pop("sounding_class", UNSET))

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

        def _parse_conversion_factor(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        conversion_factor = _parse_conversion_factor(d.pop("conversion_factor", UNSET))

        def _parse_depth_top(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        depth_top = _parse_depth_top(d.pop("depth_top", UNSET))

        def _parse_depth_base(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        depth_base = _parse_depth_base(d.pop("depth_base", UNSET))

        def _parse_stopcode(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        stopcode = _parse_stopcode(d.pop("stopcode", UNSET))

        def _parse_depth_in_soil(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        depth_in_soil = _parse_depth_in_soil(d.pop("depth_in_soil", UNSET))

        def _parse_depth_in_rock(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        depth_in_rock = _parse_depth_in_rock(d.pop("depth_in_rock", UNSET))

        def _parse_bedrock_elevation(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        bedrock_elevation = _parse_bedrock_elevation(d.pop("bedrock_elevation", UNSET))

        method_srs = cls(
            method_id=method_id,
            name=name,
            location_id=location_id,
            method_status_id=method_status_id,
            created_at=created_at,
            updated_at=updated_at,
            remarks=remarks,
            method_type_id=method_type_id,
            created_by=created_by,
            updated_by=updated_by,
            conducted_at=conducted_at,
            conducted_by=conducted_by,
            files=files,
            self_=self_,
            sounding_class=sounding_class,
            serial_number=serial_number,
            calibration_date=calibration_date,
            conversion_factor=conversion_factor,
            depth_top=depth_top,
            depth_base=depth_base,
            stopcode=stopcode,
            depth_in_soil=depth_in_soil,
            depth_in_rock=depth_in_rock,
            bedrock_elevation=bedrock_elevation,
        )

        method_srs.additional_properties = d
        return method_srs

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
