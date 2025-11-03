from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.method_status_enum import MethodStatusEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file import File


T = TypeVar("T", bound="MethodSA")


@_attrs_define
class MethodSA:
    """
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
        method_type_id (Literal[4] | Unset):  Default: 4.
        created_by (None | str | Unset):
        updated_by (None | str | Unset):
        conducted_at (datetime.datetime | None | Unset):
        conducted_by (None | str | Unset):
        files (list[File] | Unset):
        self_ (None | str | Unset):
        depth_top (float | None | Unset): Depth top (m).
        depth_base (float | None | Unset): Depth base (m).
        length (float | None | Unset):
        diameter (float | None | Unset): Diameter (mm).
        sample_container_id (None | str | Unset):
        sample_container_type_id (int | None | Unset):
        sample_material_ids (list[int] | Unset):
        ags_sample_type (None | str | Unset): Original AGS SAMP_TYPE value used to populate sampling_technique_id during
            AGS file import.
        sampling_technique_id (int | None | Unset):
        is_disturbed (bool | None | Unset): Depending on chosen sampling technique. Output only.
    """

    method_id: UUID
    name: str
    location_id: UUID
    method_status_id: MethodStatusEnum
    created_at: datetime.datetime
    updated_at: datetime.datetime
    remarks: None | str | Unset = UNSET
    method_type_id: Literal[4] | Unset = 4
    created_by: None | str | Unset = UNSET
    updated_by: None | str | Unset = UNSET
    conducted_at: datetime.datetime | None | Unset = UNSET
    conducted_by: None | str | Unset = UNSET
    files: list[File] | Unset = UNSET
    self_: None | str | Unset = UNSET
    depth_top: float | None | Unset = UNSET
    depth_base: float | None | Unset = UNSET
    length: float | None | Unset = UNSET
    diameter: float | None | Unset = UNSET
    sample_container_id: None | str | Unset = UNSET
    sample_container_type_id: int | None | Unset = UNSET
    sample_material_ids: list[int] | Unset = UNSET
    ags_sample_type: None | str | Unset = UNSET
    sampling_technique_id: int | None | Unset = UNSET
    is_disturbed: bool | None | Unset = UNSET
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

        length: float | None | Unset
        if isinstance(self.length, Unset):
            length = UNSET
        else:
            length = self.length

        diameter: float | None | Unset
        if isinstance(self.diameter, Unset):
            diameter = UNSET
        else:
            diameter = self.diameter

        sample_container_id: None | str | Unset
        if isinstance(self.sample_container_id, Unset):
            sample_container_id = UNSET
        else:
            sample_container_id = self.sample_container_id

        sample_container_type_id: int | None | Unset
        if isinstance(self.sample_container_type_id, Unset):
            sample_container_type_id = UNSET
        else:
            sample_container_type_id = self.sample_container_type_id

        sample_material_ids: list[int] | Unset = UNSET
        if not isinstance(self.sample_material_ids, Unset):
            sample_material_ids = self.sample_material_ids

        ags_sample_type: None | str | Unset
        if isinstance(self.ags_sample_type, Unset):
            ags_sample_type = UNSET
        else:
            ags_sample_type = self.ags_sample_type

        sampling_technique_id: int | None | Unset
        if isinstance(self.sampling_technique_id, Unset):
            sampling_technique_id = UNSET
        else:
            sampling_technique_id = self.sampling_technique_id

        is_disturbed: bool | None | Unset
        if isinstance(self.is_disturbed, Unset):
            is_disturbed = UNSET
        else:
            is_disturbed = self.is_disturbed

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
        if depth_top is not UNSET:
            field_dict["depth_top"] = depth_top
        if depth_base is not UNSET:
            field_dict["depth_base"] = depth_base
        if length is not UNSET:
            field_dict["length"] = length
        if diameter is not UNSET:
            field_dict["diameter"] = diameter
        if sample_container_id is not UNSET:
            field_dict["sample_container_id"] = sample_container_id
        if sample_container_type_id is not UNSET:
            field_dict["sample_container_type_id"] = sample_container_type_id
        if sample_material_ids is not UNSET:
            field_dict["sample_material_ids"] = sample_material_ids
        if ags_sample_type is not UNSET:
            field_dict["ags_sample_type"] = ags_sample_type
        if sampling_technique_id is not UNSET:
            field_dict["sampling_technique_id"] = sampling_technique_id
        if is_disturbed is not UNSET:
            field_dict["is_disturbed"] = is_disturbed

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

        method_type_id = cast(Literal[4] | Unset, d.pop("method_type_id", UNSET))
        if method_type_id != 4 and not isinstance(method_type_id, Unset):
            raise ValueError(f"method_type_id must match const 4, got '{method_type_id}'")

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

        def _parse_length(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        length = _parse_length(d.pop("length", UNSET))

        def _parse_diameter(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        diameter = _parse_diameter(d.pop("diameter", UNSET))

        def _parse_sample_container_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sample_container_id = _parse_sample_container_id(d.pop("sample_container_id", UNSET))

        def _parse_sample_container_type_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sample_container_type_id = _parse_sample_container_type_id(d.pop("sample_container_type_id", UNSET))

        sample_material_ids = cast(list[int], d.pop("sample_material_ids", UNSET))

        def _parse_ags_sample_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ags_sample_type = _parse_ags_sample_type(d.pop("ags_sample_type", UNSET))

        def _parse_sampling_technique_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sampling_technique_id = _parse_sampling_technique_id(d.pop("sampling_technique_id", UNSET))

        def _parse_is_disturbed(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_disturbed = _parse_is_disturbed(d.pop("is_disturbed", UNSET))

        method_sa = cls(
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
            depth_top=depth_top,
            depth_base=depth_base,
            length=length,
            diameter=diameter,
            sample_container_id=sample_container_id,
            sample_container_type_id=sample_container_type_id,
            sample_material_ids=sample_material_ids,
            ags_sample_type=ags_sample_type,
            sampling_technique_id=sampling_technique_id,
            is_disturbed=is_disturbed,
        )

        method_sa.additional_properties = d
        return method_sa

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
