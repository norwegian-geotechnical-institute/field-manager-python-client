from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.method_status_enum import MethodStatusEnum
from ..models.method_type_enum import MethodTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="MethodSummary")


@_attrs_define
class MethodSummary:
    """Schema class for returning a subset of attributes for all kind of methods.

    Attributes:
        method_id (UUID):
        method_type_id (MethodTypeEnum): (
            CPT=1,
            TOT=2,
            RP=3,
            SA=4,
            PZ=5,
            SS=6,
            RWS=7,
            RCD=8,
            RS=9,
            SVT=10,
            SPT=11,
            CD=12,
            TP=13,
            PT=14,
            ESA=15,
            TR=16,
            AD=17,
            RO=18,
            INC=19,
            DEF=20,
            IW=21,
            DT=22,
            OTHER=23,
            SRS=24,
            DP=25,
            WST=26,
            SLB = 27,
            STI = 28,
            )
        method_status_id (MethodStatusEnum): (
            PLANNED=1,
            READY=2,
            CONDUCTED=3,
            VOIDED=4,
            APPROVED=5,
            )
        name (None | str | Unset):
        conducted_at (datetime.datetime | None | Unset):
        depth_in_soil (float | None | Unset):
        depth_in_rock (float | None | Unset):
        depth_top (float | None | Unset):
        depth_base (float | None | Unset):
        bedrock_elevation (float | None | Unset):
        sample_container_id (None | str | Unset):
        inclination (float | None | Unset):
        azimuth (float | None | Unset):
        total_length (float | None | Unset):
        length_in_rock (float | None | Unset):
        sample_container_type_id (int | None | Unset):
        sampling_technique_id (int | None | Unset):
        diameter (float | None | Unset):
    """

    method_id: UUID
    method_type_id: MethodTypeEnum
    method_status_id: MethodStatusEnum
    name: None | str | Unset = UNSET
    conducted_at: datetime.datetime | None | Unset = UNSET
    depth_in_soil: float | None | Unset = UNSET
    depth_in_rock: float | None | Unset = UNSET
    depth_top: float | None | Unset = UNSET
    depth_base: float | None | Unset = UNSET
    bedrock_elevation: float | None | Unset = UNSET
    sample_container_id: None | str | Unset = UNSET
    inclination: float | None | Unset = UNSET
    azimuth: float | None | Unset = UNSET
    total_length: float | None | Unset = UNSET
    length_in_rock: float | None | Unset = UNSET
    sample_container_type_id: int | None | Unset = UNSET
    sampling_technique_id: int | None | Unset = UNSET
    diameter: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        method_id = str(self.method_id)

        method_type_id = self.method_type_id.value

        method_status_id = self.method_status_id.value

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        conducted_at: None | str | Unset
        if isinstance(self.conducted_at, Unset):
            conducted_at = UNSET
        elif isinstance(self.conducted_at, datetime.datetime):
            conducted_at = self.conducted_at.isoformat()
        else:
            conducted_at = self.conducted_at

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

        bedrock_elevation: float | None | Unset
        if isinstance(self.bedrock_elevation, Unset):
            bedrock_elevation = UNSET
        else:
            bedrock_elevation = self.bedrock_elevation

        sample_container_id: None | str | Unset
        if isinstance(self.sample_container_id, Unset):
            sample_container_id = UNSET
        else:
            sample_container_id = self.sample_container_id

        inclination: float | None | Unset
        if isinstance(self.inclination, Unset):
            inclination = UNSET
        else:
            inclination = self.inclination

        azimuth: float | None | Unset
        if isinstance(self.azimuth, Unset):
            azimuth = UNSET
        else:
            azimuth = self.azimuth

        total_length: float | None | Unset
        if isinstance(self.total_length, Unset):
            total_length = UNSET
        else:
            total_length = self.total_length

        length_in_rock: float | None | Unset
        if isinstance(self.length_in_rock, Unset):
            length_in_rock = UNSET
        else:
            length_in_rock = self.length_in_rock

        sample_container_type_id: int | None | Unset
        if isinstance(self.sample_container_type_id, Unset):
            sample_container_type_id = UNSET
        else:
            sample_container_type_id = self.sample_container_type_id

        sampling_technique_id: int | None | Unset
        if isinstance(self.sampling_technique_id, Unset):
            sampling_technique_id = UNSET
        else:
            sampling_technique_id = self.sampling_technique_id

        diameter: float | None | Unset
        if isinstance(self.diameter, Unset):
            diameter = UNSET
        else:
            diameter = self.diameter

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "method_id": method_id,
                "method_type_id": method_type_id,
                "method_status_id": method_status_id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if conducted_at is not UNSET:
            field_dict["conducted_at"] = conducted_at
        if depth_in_soil is not UNSET:
            field_dict["depth_in_soil"] = depth_in_soil
        if depth_in_rock is not UNSET:
            field_dict["depth_in_rock"] = depth_in_rock
        if depth_top is not UNSET:
            field_dict["depth_top"] = depth_top
        if depth_base is not UNSET:
            field_dict["depth_base"] = depth_base
        if bedrock_elevation is not UNSET:
            field_dict["bedrock_elevation"] = bedrock_elevation
        if sample_container_id is not UNSET:
            field_dict["sample_container_id"] = sample_container_id
        if inclination is not UNSET:
            field_dict["inclination"] = inclination
        if azimuth is not UNSET:
            field_dict["azimuth"] = azimuth
        if total_length is not UNSET:
            field_dict["total_length"] = total_length
        if length_in_rock is not UNSET:
            field_dict["length_in_rock"] = length_in_rock
        if sample_container_type_id is not UNSET:
            field_dict["sample_container_type_id"] = sample_container_type_id
        if sampling_technique_id is not UNSET:
            field_dict["sampling_technique_id"] = sampling_technique_id
        if diameter is not UNSET:
            field_dict["diameter"] = diameter

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        method_id = UUID(d.pop("method_id"))

        method_type_id = MethodTypeEnum(d.pop("method_type_id"))

        method_status_id = MethodStatusEnum(d.pop("method_status_id"))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

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

        def _parse_bedrock_elevation(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        bedrock_elevation = _parse_bedrock_elevation(d.pop("bedrock_elevation", UNSET))

        def _parse_sample_container_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sample_container_id = _parse_sample_container_id(d.pop("sample_container_id", UNSET))

        def _parse_inclination(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        inclination = _parse_inclination(d.pop("inclination", UNSET))

        def _parse_azimuth(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        azimuth = _parse_azimuth(d.pop("azimuth", UNSET))

        def _parse_total_length(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        total_length = _parse_total_length(d.pop("total_length", UNSET))

        def _parse_length_in_rock(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        length_in_rock = _parse_length_in_rock(d.pop("length_in_rock", UNSET))

        def _parse_sample_container_type_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sample_container_type_id = _parse_sample_container_type_id(d.pop("sample_container_type_id", UNSET))

        def _parse_sampling_technique_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sampling_technique_id = _parse_sampling_technique_id(d.pop("sampling_technique_id", UNSET))

        def _parse_diameter(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        diameter = _parse_diameter(d.pop("diameter", UNSET))

        method_summary = cls(
            method_id=method_id,
            method_type_id=method_type_id,
            method_status_id=method_status_id,
            name=name,
            conducted_at=conducted_at,
            depth_in_soil=depth_in_soil,
            depth_in_rock=depth_in_rock,
            depth_top=depth_top,
            depth_base=depth_base,
            bedrock_elevation=bedrock_elevation,
            sample_container_id=sample_container_id,
            inclination=inclination,
            azimuth=azimuth,
            total_length=total_length,
            length_in_rock=length_in_rock,
            sample_container_type_id=sample_container_type_id,
            sampling_technique_id=sampling_technique_id,
            diameter=diameter,
        )

        method_summary.additional_properties = d
        return method_summary

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
