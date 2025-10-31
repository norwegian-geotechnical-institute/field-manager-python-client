from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.application_class_enum import ApplicationClassEnum
from ..models.method_status_enum import MethodStatusEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file import File


T = TypeVar("T", bound="MethodCPT")


@_attrs_define
class MethodCPT:
    """Structure for a cone penetration test method instance

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
        method_type_id (Literal[1] | Unset):  Default: 1.
        created_by (None | str | Unset):
        updated_by (None | str | Unset):
        conducted_at (datetime.datetime | None | Unset):
        conducted_by (None | str | Unset):
        files (list[File] | Unset):
        self_ (None | str | Unset):
        predrilling_depth (float | None | Unset):
        cone_reference (None | str | Unset):
        water_depth (float | None | Unset):
        cone_area_ratio (float | None | Unset):
        sleeve_area_ratio (float | None | Unset):
        application_class (ApplicationClassEnum | Unset): (
            ONE=1,
            TWO=2,
            THREE=3,
            FOUR=4,
            OUT_OF_BOUNDS=10,
            UNKNOWN=100,
            )
        application_class_depth (ApplicationClassEnum | Unset): (
            ONE=1,
            TWO=2,
            THREE=3,
            FOUR=4,
            OUT_OF_BOUNDS=10,
            UNKNOWN=100,
            )
        application_class_resistance (ApplicationClassEnum | Unset): (
            ONE=1,
            TWO=2,
            THREE=3,
            FOUR=4,
            OUT_OF_BOUNDS=10,
            UNKNOWN=100,
            )
        application_class_friction (ApplicationClassEnum | Unset): (
            ONE=1,
            TWO=2,
            THREE=3,
            FOUR=4,
            OUT_OF_BOUNDS=10,
            UNKNOWN=100,
            )
        application_class_pressure (ApplicationClassEnum | Unset): (
            ONE=1,
            TWO=2,
            THREE=3,
            FOUR=4,
            OUT_OF_BOUNDS=10,
            UNKNOWN=100,
            )
        depth_top (float | None | Unset):
        depth_base (float | None | Unset):
        stopcode (int | None | Unset):
    """

    method_id: UUID
    name: str
    location_id: UUID
    method_status_id: MethodStatusEnum
    created_at: datetime.datetime
    updated_at: datetime.datetime
    remarks: None | str | Unset = UNSET
    method_type_id: Literal[1] | Unset = 1
    created_by: None | str | Unset = UNSET
    updated_by: None | str | Unset = UNSET
    conducted_at: datetime.datetime | None | Unset = UNSET
    conducted_by: None | str | Unset = UNSET
    files: list[File] | Unset = UNSET
    self_: None | str | Unset = UNSET
    predrilling_depth: float | None | Unset = UNSET
    cone_reference: None | str | Unset = UNSET
    water_depth: float | None | Unset = UNSET
    cone_area_ratio: float | None | Unset = UNSET
    sleeve_area_ratio: float | None | Unset = UNSET
    application_class: ApplicationClassEnum | Unset = UNSET
    application_class_depth: ApplicationClassEnum | Unset = UNSET
    application_class_resistance: ApplicationClassEnum | Unset = UNSET
    application_class_friction: ApplicationClassEnum | Unset = UNSET
    application_class_pressure: ApplicationClassEnum | Unset = UNSET
    depth_top: float | None | Unset = UNSET
    depth_base: float | None | Unset = UNSET
    stopcode: int | None | Unset = UNSET
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

        predrilling_depth: float | None | Unset
        if isinstance(self.predrilling_depth, Unset):
            predrilling_depth = UNSET
        else:
            predrilling_depth = self.predrilling_depth

        cone_reference: None | str | Unset
        if isinstance(self.cone_reference, Unset):
            cone_reference = UNSET
        else:
            cone_reference = self.cone_reference

        water_depth: float | None | Unset
        if isinstance(self.water_depth, Unset):
            water_depth = UNSET
        else:
            water_depth = self.water_depth

        cone_area_ratio: float | None | Unset
        if isinstance(self.cone_area_ratio, Unset):
            cone_area_ratio = UNSET
        else:
            cone_area_ratio = self.cone_area_ratio

        sleeve_area_ratio: float | None | Unset
        if isinstance(self.sleeve_area_ratio, Unset):
            sleeve_area_ratio = UNSET
        else:
            sleeve_area_ratio = self.sleeve_area_ratio

        application_class: int | Unset = UNSET
        if not isinstance(self.application_class, Unset):
            application_class = self.application_class.value

        application_class_depth: int | Unset = UNSET
        if not isinstance(self.application_class_depth, Unset):
            application_class_depth = self.application_class_depth.value

        application_class_resistance: int | Unset = UNSET
        if not isinstance(self.application_class_resistance, Unset):
            application_class_resistance = self.application_class_resistance.value

        application_class_friction: int | Unset = UNSET
        if not isinstance(self.application_class_friction, Unset):
            application_class_friction = self.application_class_friction.value

        application_class_pressure: int | Unset = UNSET
        if not isinstance(self.application_class_pressure, Unset):
            application_class_pressure = self.application_class_pressure.value

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
        if predrilling_depth is not UNSET:
            field_dict["predrilling_depth"] = predrilling_depth
        if cone_reference is not UNSET:
            field_dict["cone_reference"] = cone_reference
        if water_depth is not UNSET:
            field_dict["water_depth"] = water_depth
        if cone_area_ratio is not UNSET:
            field_dict["cone_area_ratio"] = cone_area_ratio
        if sleeve_area_ratio is not UNSET:
            field_dict["sleeve_area_ratio"] = sleeve_area_ratio
        if application_class is not UNSET:
            field_dict["application_class"] = application_class
        if application_class_depth is not UNSET:
            field_dict["application_class_depth"] = application_class_depth
        if application_class_resistance is not UNSET:
            field_dict["application_class_resistance"] = application_class_resistance
        if application_class_friction is not UNSET:
            field_dict["application_class_friction"] = application_class_friction
        if application_class_pressure is not UNSET:
            field_dict["application_class_pressure"] = application_class_pressure
        if depth_top is not UNSET:
            field_dict["depth_top"] = depth_top
        if depth_base is not UNSET:
            field_dict["depth_base"] = depth_base
        if stopcode is not UNSET:
            field_dict["stopcode"] = stopcode

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

        method_type_id = cast(Literal[1] | Unset, d.pop("method_type_id", UNSET))
        if method_type_id != 1 and not isinstance(method_type_id, Unset):
            raise ValueError(f"method_type_id must match const 1, got '{method_type_id}'")

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

        def _parse_predrilling_depth(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        predrilling_depth = _parse_predrilling_depth(d.pop("predrilling_depth", UNSET))

        def _parse_cone_reference(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cone_reference = _parse_cone_reference(d.pop("cone_reference", UNSET))

        def _parse_water_depth(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        water_depth = _parse_water_depth(d.pop("water_depth", UNSET))

        def _parse_cone_area_ratio(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        cone_area_ratio = _parse_cone_area_ratio(d.pop("cone_area_ratio", UNSET))

        def _parse_sleeve_area_ratio(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        sleeve_area_ratio = _parse_sleeve_area_ratio(d.pop("sleeve_area_ratio", UNSET))

        _application_class = d.pop("application_class", UNSET)
        application_class: ApplicationClassEnum | Unset
        if isinstance(_application_class, Unset):
            application_class = UNSET
        else:
            application_class = ApplicationClassEnum(_application_class)

        _application_class_depth = d.pop("application_class_depth", UNSET)
        application_class_depth: ApplicationClassEnum | Unset
        if isinstance(_application_class_depth, Unset):
            application_class_depth = UNSET
        else:
            application_class_depth = ApplicationClassEnum(_application_class_depth)

        _application_class_resistance = d.pop("application_class_resistance", UNSET)
        application_class_resistance: ApplicationClassEnum | Unset
        if isinstance(_application_class_resistance, Unset):
            application_class_resistance = UNSET
        else:
            application_class_resistance = ApplicationClassEnum(_application_class_resistance)

        _application_class_friction = d.pop("application_class_friction", UNSET)
        application_class_friction: ApplicationClassEnum | Unset
        if isinstance(_application_class_friction, Unset):
            application_class_friction = UNSET
        else:
            application_class_friction = ApplicationClassEnum(_application_class_friction)

        _application_class_pressure = d.pop("application_class_pressure", UNSET)
        application_class_pressure: ApplicationClassEnum | Unset
        if isinstance(_application_class_pressure, Unset):
            application_class_pressure = UNSET
        else:
            application_class_pressure = ApplicationClassEnum(_application_class_pressure)

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

        method_cpt = cls(
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
            predrilling_depth=predrilling_depth,
            cone_reference=cone_reference,
            water_depth=water_depth,
            cone_area_ratio=cone_area_ratio,
            sleeve_area_ratio=sleeve_area_ratio,
            application_class=application_class,
            application_class_depth=application_class_depth,
            application_class_resistance=application_class_resistance,
            application_class_friction=application_class_friction,
            application_class_pressure=application_class_pressure,
            depth_top=depth_top,
            depth_base=depth_base,
            stopcode=stopcode,
        )

        method_cpt.additional_properties = d
        return method_cpt

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
