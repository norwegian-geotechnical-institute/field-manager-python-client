import datetime
from collections.abc import Mapping
from typing import Any, Literal, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.method_status_enum import MethodStatusEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="MethodSAUpdate")


@_attrs_define
class MethodSAUpdate:
    """
    Attributes:
        method_id (Union[None, UUID, Unset]):
        name (Union[None, Unset, str]):
        remarks (Union[None, Unset, str]):
        method_status_id (Union[MethodStatusEnum, None, Unset]):
        updated_at (Union[None, Unset, datetime.datetime]):
        updated_by (Union[None, Unset, str]):
        conducted_by (Union[None, Unset, str]):
        conducted_at (Union[None, Unset, datetime.datetime]):
        method_type_id (Union[Literal[4], Unset]):  Default: 4.
        depth_top (Union[None, Unset, float, str]):
        depth_base (Union[None, Unset, float, str]):
        diameter (Union[None, Unset, float, str]):
        sample_container_id (Union[None, Unset, str]):
        sample_container_type_id (Union[None, Unset, int]):
        sample_material_ids (Union[Unset, list[int]]):
        ags_sample_type (Union[None, Unset, str]):
        sampling_technique_id (Union[None, Unset, int]):
    """

    method_id: Union[None, UUID, Unset] = UNSET
    name: Union[None, Unset, str] = UNSET
    remarks: Union[None, Unset, str] = UNSET
    method_status_id: Union[MethodStatusEnum, None, Unset] = UNSET
    updated_at: Union[None, Unset, datetime.datetime] = UNSET
    updated_by: Union[None, Unset, str] = UNSET
    conducted_by: Union[None, Unset, str] = UNSET
    conducted_at: Union[None, Unset, datetime.datetime] = UNSET
    method_type_id: Union[Literal[4], Unset] = 4
    depth_top: Union[None, Unset, float, str] = UNSET
    depth_base: Union[None, Unset, float, str] = UNSET
    diameter: Union[None, Unset, float, str] = UNSET
    sample_container_id: Union[None, Unset, str] = UNSET
    sample_container_type_id: Union[None, Unset, int] = UNSET
    sample_material_ids: Union[Unset, list[int]] = UNSET
    ags_sample_type: Union[None, Unset, str] = UNSET
    sampling_technique_id: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        method_id: Union[None, Unset, str]
        if isinstance(self.method_id, Unset):
            method_id = UNSET
        elif isinstance(self.method_id, UUID):
            method_id = str(self.method_id)
        else:
            method_id = self.method_id

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        remarks: Union[None, Unset, str]
        if isinstance(self.remarks, Unset):
            remarks = UNSET
        else:
            remarks = self.remarks

        method_status_id: Union[None, Unset, int]
        if isinstance(self.method_status_id, Unset):
            method_status_id = UNSET
        elif isinstance(self.method_status_id, MethodStatusEnum):
            method_status_id = self.method_status_id.value
        else:
            method_status_id = self.method_status_id

        updated_at: Union[None, Unset, str]
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        updated_by: Union[None, Unset, str]
        if isinstance(self.updated_by, Unset):
            updated_by = UNSET
        else:
            updated_by = self.updated_by

        conducted_by: Union[None, Unset, str]
        if isinstance(self.conducted_by, Unset):
            conducted_by = UNSET
        else:
            conducted_by = self.conducted_by

        conducted_at: Union[None, Unset, str]
        if isinstance(self.conducted_at, Unset):
            conducted_at = UNSET
        elif isinstance(self.conducted_at, datetime.datetime):
            conducted_at = self.conducted_at.isoformat()
        else:
            conducted_at = self.conducted_at

        method_type_id = self.method_type_id

        depth_top: Union[None, Unset, float, str]
        if isinstance(self.depth_top, Unset):
            depth_top = UNSET
        else:
            depth_top = self.depth_top

        depth_base: Union[None, Unset, float, str]
        if isinstance(self.depth_base, Unset):
            depth_base = UNSET
        else:
            depth_base = self.depth_base

        diameter: Union[None, Unset, float, str]
        if isinstance(self.diameter, Unset):
            diameter = UNSET
        else:
            diameter = self.diameter

        sample_container_id: Union[None, Unset, str]
        if isinstance(self.sample_container_id, Unset):
            sample_container_id = UNSET
        else:
            sample_container_id = self.sample_container_id

        sample_container_type_id: Union[None, Unset, int]
        if isinstance(self.sample_container_type_id, Unset):
            sample_container_type_id = UNSET
        else:
            sample_container_type_id = self.sample_container_type_id

        sample_material_ids: Union[Unset, list[int]] = UNSET
        if not isinstance(self.sample_material_ids, Unset):
            sample_material_ids = self.sample_material_ids

        ags_sample_type: Union[None, Unset, str]
        if isinstance(self.ags_sample_type, Unset):
            ags_sample_type = UNSET
        else:
            ags_sample_type = self.ags_sample_type

        sampling_technique_id: Union[None, Unset, int]
        if isinstance(self.sampling_technique_id, Unset):
            sampling_technique_id = UNSET
        else:
            sampling_technique_id = self.sampling_technique_id

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
        if depth_top is not UNSET:
            field_dict["depth_top"] = depth_top
        if depth_base is not UNSET:
            field_dict["depth_base"] = depth_base
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_method_id(data: object) -> Union[None, UUID, Unset]:
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
            return cast(Union[None, UUID, Unset], data)

        method_id = _parse_method_id(d.pop("method_id", UNSET))

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_remarks(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        remarks = _parse_remarks(d.pop("remarks", UNSET))

        def _parse_method_status_id(data: object) -> Union[MethodStatusEnum, None, Unset]:
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
            return cast(Union[MethodStatusEnum, None, Unset], data)

        method_status_id = _parse_method_status_id(d.pop("method_status_id", UNSET))

        def _parse_updated_at(data: object) -> Union[None, Unset, datetime.datetime]:
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
            return cast(Union[None, Unset, datetime.datetime], data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))

        def _parse_updated_by(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        updated_by = _parse_updated_by(d.pop("updated_by", UNSET))

        def _parse_conducted_by(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        conducted_by = _parse_conducted_by(d.pop("conducted_by", UNSET))

        def _parse_conducted_at(data: object) -> Union[None, Unset, datetime.datetime]:
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
            return cast(Union[None, Unset, datetime.datetime], data)

        conducted_at = _parse_conducted_at(d.pop("conducted_at", UNSET))

        method_type_id = cast(Union[Literal[4], Unset], d.pop("method_type_id", UNSET))
        if method_type_id != 4 and not isinstance(method_type_id, Unset):
            raise ValueError(f"method_type_id must match const 4, got '{method_type_id}'")

        def _parse_depth_top(data: object) -> Union[None, Unset, float, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, str], data)

        depth_top = _parse_depth_top(d.pop("depth_top", UNSET))

        def _parse_depth_base(data: object) -> Union[None, Unset, float, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, str], data)

        depth_base = _parse_depth_base(d.pop("depth_base", UNSET))

        def _parse_diameter(data: object) -> Union[None, Unset, float, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, str], data)

        diameter = _parse_diameter(d.pop("diameter", UNSET))

        def _parse_sample_container_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        sample_container_id = _parse_sample_container_id(d.pop("sample_container_id", UNSET))

        def _parse_sample_container_type_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        sample_container_type_id = _parse_sample_container_type_id(d.pop("sample_container_type_id", UNSET))

        sample_material_ids = cast(list[int], d.pop("sample_material_ids", UNSET))

        def _parse_ags_sample_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        ags_sample_type = _parse_ags_sample_type(d.pop("ags_sample_type", UNSET))

        def _parse_sampling_technique_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        sampling_technique_id = _parse_sampling_technique_id(d.pop("sampling_technique_id", UNSET))

        method_sa_update = cls(
            method_id=method_id,
            name=name,
            remarks=remarks,
            method_status_id=method_status_id,
            updated_at=updated_at,
            updated_by=updated_by,
            conducted_by=conducted_by,
            conducted_at=conducted_at,
            method_type_id=method_type_id,
            depth_top=depth_top,
            depth_base=depth_base,
            diameter=diameter,
            sample_container_id=sample_container_id,
            sample_container_type_id=sample_container_type_id,
            sample_material_ids=sample_material_ids,
            ags_sample_type=ags_sample_type,
            sampling_technique_id=sampling_technique_id,
        )

        method_sa_update.additional_properties = d
        return method_sa_update

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
