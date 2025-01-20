import datetime
from typing import TYPE_CHECKING, Any, Literal, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.method_status_enum import MethodStatusEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file import File


T = TypeVar("T", bound="MethodCD")


@_attrs_define
class MethodCD:
    """Core Drilling (CD) (Kjerneboring)

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
        remarks (Union[None, Unset, str]):
        method_type_id (Union[Literal[12], Unset]):  Default: 12.
        created_by (Union[None, Unset, str]):
        updated_by (Union[None, Unset, str]):
        conducted_at (Union[None, Unset, datetime.datetime]):
        conducted_by (Union[None, Unset, str]):
        files (Union[Unset, list['File']]):
        self_ (Union[None, Unset, str]):
        sampler_type_id (Union[None, Unset, int]):
        inclination (Union[None, Unset, float]): Inclination angle (deg).
        azimuth (Union[None, Unset, float]): Azimuth angle relative to N (deg).
        length_in_soil (Union[None, Unset, float]): Length drilled in soil (m).
        total_length (Union[None, Unset, float]): Total length drilled (m).
        casing_length (Union[None, Unset, float]): Length of casing (m).
        casing_size (Union[None, Unset, float]): Size of casing (mm).
        removed_casing (Union[None, Unset, bool]): Casing removed.
        length_in_rock (Union[None, Unset, float]): Calculated length in rock (m).
        total_depth (Union[None, Unset, float]): Calculated total depth (m).
        depth_in_soil (Union[None, Unset, float]): Calculated depth in soil (m).
        depth_in_rock (Union[None, Unset, float]): Calculated depth in rock (m).
        bedrock_elevation (Union[None, Unset, float]): Calculated bedrock elevation according to location (m).
        horizontal_total_length (Union[None, Unset, float]): Calculated horizontal length in rock (m).
        horizontal_length_in_soil (Union[None, Unset, float]): Calculated horizontal length in soil (m).
        depth_top (Union[None, Unset, float]): Calculated horizontal length in soil (m).
        depth_base (Union[None, Unset, float]): Calculated horizontal length in soil (m).
    """

    method_id: UUID
    name: str
    location_id: UUID
    method_status_id: MethodStatusEnum
    created_at: datetime.datetime
    updated_at: datetime.datetime
    remarks: Union[None, Unset, str] = UNSET
    method_type_id: Union[Literal[12], Unset] = 12
    created_by: Union[None, Unset, str] = UNSET
    updated_by: Union[None, Unset, str] = UNSET
    conducted_at: Union[None, Unset, datetime.datetime] = UNSET
    conducted_by: Union[None, Unset, str] = UNSET
    files: Union[Unset, list["File"]] = UNSET
    self_: Union[None, Unset, str] = UNSET
    sampler_type_id: Union[None, Unset, int] = UNSET
    inclination: Union[None, Unset, float] = UNSET
    azimuth: Union[None, Unset, float] = UNSET
    length_in_soil: Union[None, Unset, float] = UNSET
    total_length: Union[None, Unset, float] = UNSET
    casing_length: Union[None, Unset, float] = UNSET
    casing_size: Union[None, Unset, float] = UNSET
    removed_casing: Union[None, Unset, bool] = UNSET
    length_in_rock: Union[None, Unset, float] = UNSET
    total_depth: Union[None, Unset, float] = UNSET
    depth_in_soil: Union[None, Unset, float] = UNSET
    depth_in_rock: Union[None, Unset, float] = UNSET
    bedrock_elevation: Union[None, Unset, float] = UNSET
    horizontal_total_length: Union[None, Unset, float] = UNSET
    horizontal_length_in_soil: Union[None, Unset, float] = UNSET
    depth_top: Union[None, Unset, float] = UNSET
    depth_base: Union[None, Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        method_id = str(self.method_id)

        name = self.name

        location_id = str(self.location_id)

        method_status_id = self.method_status_id.value

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        remarks: Union[None, Unset, str]
        if isinstance(self.remarks, Unset):
            remarks = UNSET
        else:
            remarks = self.remarks

        method_type_id = self.method_type_id

        created_by: Union[None, Unset, str]
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        else:
            created_by = self.created_by

        updated_by: Union[None, Unset, str]
        if isinstance(self.updated_by, Unset):
            updated_by = UNSET
        else:
            updated_by = self.updated_by

        conducted_at: Union[None, Unset, str]
        if isinstance(self.conducted_at, Unset):
            conducted_at = UNSET
        elif isinstance(self.conducted_at, datetime.datetime):
            conducted_at = self.conducted_at.isoformat()
        else:
            conducted_at = self.conducted_at

        conducted_by: Union[None, Unset, str]
        if isinstance(self.conducted_by, Unset):
            conducted_by = UNSET
        else:
            conducted_by = self.conducted_by

        files: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.files, Unset):
            files = []
            for files_item_data in self.files:
                files_item = files_item_data.to_dict()
                files.append(files_item)

        self_: Union[None, Unset, str]
        if isinstance(self.self_, Unset):
            self_ = UNSET
        else:
            self_ = self.self_

        sampler_type_id: Union[None, Unset, int]
        if isinstance(self.sampler_type_id, Unset):
            sampler_type_id = UNSET
        else:
            sampler_type_id = self.sampler_type_id

        inclination: Union[None, Unset, float]
        if isinstance(self.inclination, Unset):
            inclination = UNSET
        else:
            inclination = self.inclination

        azimuth: Union[None, Unset, float]
        if isinstance(self.azimuth, Unset):
            azimuth = UNSET
        else:
            azimuth = self.azimuth

        length_in_soil: Union[None, Unset, float]
        if isinstance(self.length_in_soil, Unset):
            length_in_soil = UNSET
        else:
            length_in_soil = self.length_in_soil

        total_length: Union[None, Unset, float]
        if isinstance(self.total_length, Unset):
            total_length = UNSET
        else:
            total_length = self.total_length

        casing_length: Union[None, Unset, float]
        if isinstance(self.casing_length, Unset):
            casing_length = UNSET
        else:
            casing_length = self.casing_length

        casing_size: Union[None, Unset, float]
        if isinstance(self.casing_size, Unset):
            casing_size = UNSET
        else:
            casing_size = self.casing_size

        removed_casing: Union[None, Unset, bool]
        if isinstance(self.removed_casing, Unset):
            removed_casing = UNSET
        else:
            removed_casing = self.removed_casing

        length_in_rock: Union[None, Unset, float]
        if isinstance(self.length_in_rock, Unset):
            length_in_rock = UNSET
        else:
            length_in_rock = self.length_in_rock

        total_depth: Union[None, Unset, float]
        if isinstance(self.total_depth, Unset):
            total_depth = UNSET
        else:
            total_depth = self.total_depth

        depth_in_soil: Union[None, Unset, float]
        if isinstance(self.depth_in_soil, Unset):
            depth_in_soil = UNSET
        else:
            depth_in_soil = self.depth_in_soil

        depth_in_rock: Union[None, Unset, float]
        if isinstance(self.depth_in_rock, Unset):
            depth_in_rock = UNSET
        else:
            depth_in_rock = self.depth_in_rock

        bedrock_elevation: Union[None, Unset, float]
        if isinstance(self.bedrock_elevation, Unset):
            bedrock_elevation = UNSET
        else:
            bedrock_elevation = self.bedrock_elevation

        horizontal_total_length: Union[None, Unset, float]
        if isinstance(self.horizontal_total_length, Unset):
            horizontal_total_length = UNSET
        else:
            horizontal_total_length = self.horizontal_total_length

        horizontal_length_in_soil: Union[None, Unset, float]
        if isinstance(self.horizontal_length_in_soil, Unset):
            horizontal_length_in_soil = UNSET
        else:
            horizontal_length_in_soil = self.horizontal_length_in_soil

        depth_top: Union[None, Unset, float]
        if isinstance(self.depth_top, Unset):
            depth_top = UNSET
        else:
            depth_top = self.depth_top

        depth_base: Union[None, Unset, float]
        if isinstance(self.depth_base, Unset):
            depth_base = UNSET
        else:
            depth_base = self.depth_base

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
        if length_in_rock is not UNSET:
            field_dict["length_in_rock"] = length_in_rock
        if total_depth is not UNSET:
            field_dict["total_depth"] = total_depth
        if depth_in_soil is not UNSET:
            field_dict["depth_in_soil"] = depth_in_soil
        if depth_in_rock is not UNSET:
            field_dict["depth_in_rock"] = depth_in_rock
        if bedrock_elevation is not UNSET:
            field_dict["bedrock_elevation"] = bedrock_elevation
        if horizontal_total_length is not UNSET:
            field_dict["horizontal_total_length"] = horizontal_total_length
        if horizontal_length_in_soil is not UNSET:
            field_dict["horizontal_length_in_soil"] = horizontal_length_in_soil
        if depth_top is not UNSET:
            field_dict["depth_top"] = depth_top
        if depth_base is not UNSET:
            field_dict["depth_base"] = depth_base

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.file import File

        d = src_dict.copy()
        method_id = UUID(d.pop("method_id"))

        name = d.pop("name")

        location_id = UUID(d.pop("location_id"))

        method_status_id = MethodStatusEnum(d.pop("method_status_id"))

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        def _parse_remarks(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        remarks = _parse_remarks(d.pop("remarks", UNSET))

        method_type_id = cast(Union[Literal[12], Unset], d.pop("method_type_id", UNSET))
        if method_type_id != 12 and not isinstance(method_type_id, Unset):
            raise ValueError(f"method_type_id must match const 12, got '{method_type_id}'")

        def _parse_created_by(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        created_by = _parse_created_by(d.pop("created_by", UNSET))

        def _parse_updated_by(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        updated_by = _parse_updated_by(d.pop("updated_by", UNSET))

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

        def _parse_conducted_by(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        conducted_by = _parse_conducted_by(d.pop("conducted_by", UNSET))

        files = []
        _files = d.pop("files", UNSET)
        for files_item_data in _files or []:
            files_item = File.from_dict(files_item_data)

            files.append(files_item)

        def _parse_self_(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        self_ = _parse_self_(d.pop("self", UNSET))

        def _parse_sampler_type_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        sampler_type_id = _parse_sampler_type_id(d.pop("sampler_type_id", UNSET))

        def _parse_inclination(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        inclination = _parse_inclination(d.pop("inclination", UNSET))

        def _parse_azimuth(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        azimuth = _parse_azimuth(d.pop("azimuth", UNSET))

        def _parse_length_in_soil(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        length_in_soil = _parse_length_in_soil(d.pop("length_in_soil", UNSET))

        def _parse_total_length(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        total_length = _parse_total_length(d.pop("total_length", UNSET))

        def _parse_casing_length(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        casing_length = _parse_casing_length(d.pop("casing_length", UNSET))

        def _parse_casing_size(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        casing_size = _parse_casing_size(d.pop("casing_size", UNSET))

        def _parse_removed_casing(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        removed_casing = _parse_removed_casing(d.pop("removed_casing", UNSET))

        def _parse_length_in_rock(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        length_in_rock = _parse_length_in_rock(d.pop("length_in_rock", UNSET))

        def _parse_total_depth(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        total_depth = _parse_total_depth(d.pop("total_depth", UNSET))

        def _parse_depth_in_soil(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        depth_in_soil = _parse_depth_in_soil(d.pop("depth_in_soil", UNSET))

        def _parse_depth_in_rock(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        depth_in_rock = _parse_depth_in_rock(d.pop("depth_in_rock", UNSET))

        def _parse_bedrock_elevation(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        bedrock_elevation = _parse_bedrock_elevation(d.pop("bedrock_elevation", UNSET))

        def _parse_horizontal_total_length(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        horizontal_total_length = _parse_horizontal_total_length(d.pop("horizontal_total_length", UNSET))

        def _parse_horizontal_length_in_soil(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        horizontal_length_in_soil = _parse_horizontal_length_in_soil(d.pop("horizontal_length_in_soil", UNSET))

        def _parse_depth_top(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        depth_top = _parse_depth_top(d.pop("depth_top", UNSET))

        def _parse_depth_base(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        depth_base = _parse_depth_base(d.pop("depth_base", UNSET))

        method_cd = cls(
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
            sampler_type_id=sampler_type_id,
            inclination=inclination,
            azimuth=azimuth,
            length_in_soil=length_in_soil,
            total_length=total_length,
            casing_length=casing_length,
            casing_size=casing_size,
            removed_casing=removed_casing,
            length_in_rock=length_in_rock,
            total_depth=total_depth,
            depth_in_soil=depth_in_soil,
            depth_in_rock=depth_in_rock,
            bedrock_elevation=bedrock_elevation,
            horizontal_total_length=horizontal_total_length,
            horizontal_length_in_soil=horizontal_length_in_soil,
            depth_top=depth_top,
            depth_base=depth_base,
        )

        method_cd.additional_properties = d
        return method_cd

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
