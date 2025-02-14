import datetime
from typing import Any, Literal, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.method_status_enum import MethodStatusEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="MethodCDCreate")


@_attrs_define
class MethodCDCreate:
    """
    Attributes:
        method_id (Union[None, UUID, Unset]):
        name (Union[None, Unset, str]):  Default: 'CD'.
        remarks (Union[None, Unset, str]):
        method_status_id (Union[Unset, MethodStatusEnum]): (
            PLANNED=1,
            READY=2,
            CONDUCTED=3,
            VOIDED=4,
            APPROVED=5,
            )
        created_at (Union[None, Unset, datetime.datetime]):
        created_by (Union[None, Unset, str]):
        updated_at (Union[None, Unset, datetime.datetime]):
        updated_by (Union[None, Unset, str]):
        conducted_by (Union[None, Unset, str]):
        conducted_at (Union[None, Unset, datetime.datetime]):
        method_type_id (Union[Literal[12], Unset]):  Default: 12.
        sampler_type_id (Union[None, Unset, int]):
        inclination (Union[None, Unset, float, str]): Inclination angle (deg).
        azimuth (Union[None, Unset, float, str]): Azimuth angle relative to N (deg).
        length_in_soil (Union[None, Unset, float, str]): Length drilled in soil (m).
        total_length (Union[None, Unset, float, str]): Total length drilled (m).
        casing_length (Union[None, Unset, float, str]): Length of casing (m).
        casing_size (Union[None, Unset, float, str]): Size of casing (mm).
        removed_casing (Union[None, Unset, bool]): Casing removed.
    """

    method_id: Union[None, UUID, Unset] = UNSET
    name: Union[None, Unset, str] = "CD"
    remarks: Union[None, Unset, str] = UNSET
    method_status_id: Union[Unset, MethodStatusEnum] = UNSET
    created_at: Union[None, Unset, datetime.datetime] = UNSET
    created_by: Union[None, Unset, str] = UNSET
    updated_at: Union[None, Unset, datetime.datetime] = UNSET
    updated_by: Union[None, Unset, str] = UNSET
    conducted_by: Union[None, Unset, str] = UNSET
    conducted_at: Union[None, Unset, datetime.datetime] = UNSET
    method_type_id: Union[Literal[12], Unset] = 12
    sampler_type_id: Union[None, Unset, int] = UNSET
    inclination: Union[None, Unset, float, str] = UNSET
    azimuth: Union[None, Unset, float, str] = UNSET
    length_in_soil: Union[None, Unset, float, str] = UNSET
    total_length: Union[None, Unset, float, str] = UNSET
    casing_length: Union[None, Unset, float, str] = UNSET
    casing_size: Union[None, Unset, float, str] = UNSET
    removed_casing: Union[None, Unset, bool] = UNSET
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

        method_status_id: Union[Unset, int] = UNSET
        if not isinstance(self.method_status_id, Unset):
            method_status_id = self.method_status_id.value

        created_at: Union[None, Unset, str]
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        created_by: Union[None, Unset, str]
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        else:
            created_by = self.created_by

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

        sampler_type_id: Union[None, Unset, int]
        if isinstance(self.sampler_type_id, Unset):
            sampler_type_id = UNSET
        else:
            sampler_type_id = self.sampler_type_id

        inclination: Union[None, Unset, float, str]
        if isinstance(self.inclination, Unset):
            inclination = UNSET
        else:
            inclination = self.inclination

        azimuth: Union[None, Unset, float, str]
        if isinstance(self.azimuth, Unset):
            azimuth = UNSET
        else:
            azimuth = self.azimuth

        length_in_soil: Union[None, Unset, float, str]
        if isinstance(self.length_in_soil, Unset):
            length_in_soil = UNSET
        else:
            length_in_soil = self.length_in_soil

        total_length: Union[None, Unset, float, str]
        if isinstance(self.total_length, Unset):
            total_length = UNSET
        else:
            total_length = self.total_length

        casing_length: Union[None, Unset, float, str]
        if isinstance(self.casing_length, Unset):
            casing_length = UNSET
        else:
            casing_length = self.casing_length

        casing_size: Union[None, Unset, float, str]
        if isinstance(self.casing_size, Unset):
            casing_size = UNSET
        else:
            casing_size = self.casing_size

        removed_casing: Union[None, Unset, bool]
        if isinstance(self.removed_casing, Unset):
            removed_casing = UNSET
        else:
            removed_casing = self.removed_casing

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
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
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
        if sampler_type_id is not UNSET:
            field_dict["sampler_type_id"] = sampler_type_id
        if inclination is not UNSET:
            field_dict["inclination"] = inclination
        if azimuth is not UNSET:
            field_dict["azimuth"] = azimuth
        if length_in_soil is not UNSET:
            field_dict["length_in_soil"] = length_in_soil
        if total_length is not UNSET:
            field_dict["total_length"] = total_length
        if casing_length is not UNSET:
            field_dict["casing_length"] = casing_length
        if casing_size is not UNSET:
            field_dict["casing_size"] = casing_size
        if removed_casing is not UNSET:
            field_dict["removed_casing"] = removed_casing

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()

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

        _method_status_id = d.pop("method_status_id", UNSET)
        method_status_id: Union[Unset, MethodStatusEnum]
        if isinstance(_method_status_id, Unset):
            method_status_id = UNSET
        else:
            method_status_id = MethodStatusEnum(_method_status_id)

        def _parse_created_at(data: object) -> Union[None, Unset, datetime.datetime]:
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
            return cast(Union[None, Unset, datetime.datetime], data)

        created_at = _parse_created_at(d.pop("created_at", UNSET))

        def _parse_created_by(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        created_by = _parse_created_by(d.pop("created_by", UNSET))

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

        method_type_id = cast(Union[Literal[12], Unset], d.pop("method_type_id", UNSET))
        if method_type_id != 12 and not isinstance(method_type_id, Unset):
            raise ValueError(f"method_type_id must match const 12, got '{method_type_id}'")

        def _parse_sampler_type_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        sampler_type_id = _parse_sampler_type_id(d.pop("sampler_type_id", UNSET))

        def _parse_inclination(data: object) -> Union[None, Unset, float, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, str], data)

        inclination = _parse_inclination(d.pop("inclination", UNSET))

        def _parse_azimuth(data: object) -> Union[None, Unset, float, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, str], data)

        azimuth = _parse_azimuth(d.pop("azimuth", UNSET))

        def _parse_length_in_soil(data: object) -> Union[None, Unset, float, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, str], data)

        length_in_soil = _parse_length_in_soil(d.pop("length_in_soil", UNSET))

        def _parse_total_length(data: object) -> Union[None, Unset, float, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, str], data)

        total_length = _parse_total_length(d.pop("total_length", UNSET))

        def _parse_casing_length(data: object) -> Union[None, Unset, float, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, str], data)

        casing_length = _parse_casing_length(d.pop("casing_length", UNSET))

        def _parse_casing_size(data: object) -> Union[None, Unset, float, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, str], data)

        casing_size = _parse_casing_size(d.pop("casing_size", UNSET))

        def _parse_removed_casing(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        removed_casing = _parse_removed_casing(d.pop("removed_casing", UNSET))

        method_cd_create = cls(
            method_id=method_id,
            name=name,
            remarks=remarks,
            method_status_id=method_status_id,
            created_at=created_at,
            created_by=created_by,
            updated_at=updated_at,
            updated_by=updated_by,
            conducted_by=conducted_by,
            conducted_at=conducted_at,
            method_type_id=method_type_id,
            sampler_type_id=sampler_type_id,
            inclination=inclination,
            azimuth=azimuth,
            length_in_soil=length_in_soil,
            total_length=total_length,
            casing_length=casing_length,
            casing_size=casing_size,
            removed_casing=removed_casing,
        )

        method_cd_create.additional_properties = d
        return method_cd_create

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
