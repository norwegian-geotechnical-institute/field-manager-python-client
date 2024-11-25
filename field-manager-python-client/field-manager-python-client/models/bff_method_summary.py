from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.method_status_enum import MethodStatusEnum
from ..models.method_type_enum import MethodTypeEnum
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import cast, Union
from typing import Union
from uuid import UUID
import datetime






T = TypeVar("T", bound="BFFMethodSummary")


@_attrs_define
class BFFMethodSummary:
    """ 
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
                AD=17,
                RO=18,
                INC=19,
                SR=20,
                IW=21,
                DT=22,
                OTHER=23,
                SRS=24,
                DP=25,
                WST=26,
                )
            method_status_id (MethodStatusEnum): (
                PLANNED=1,
                READY=2,
                CONDUCTED=3,
                VOIDED=4,
                APPROVED=5,
                )
            updated_at (datetime.datetime):
            name (Union[None, Unset, str]):
            remarks (Union[None, Unset, str]):
            conducted_at (Union[None, Unset, datetime.datetime]):
            depth_top (Union[None, Unset, float]): Top depth of the sample (m).
            depth_base (Union[None, Unset, float]): Base depth of the sample (m).
            sample_container_id (Union[None, Unset, str]):
            sample_container_type_id (Union[None, Unset, int]):
            sampling_technique_id (Union[None, Unset, int]):
            diameter (Union[None, Unset, float]):
            inclination (Union[None, Unset, float]): Inclination angle (deg).
            azimuth (Union[None, Unset, float]): Azimuth angle relative to N (deg).
            total_length (Union[None, Unset, float]): Total length drilled (m).
            length_in_rock (Union[None, Unset, float]): Calculated length in rock (m).
     """

    method_id: UUID
    method_type_id: MethodTypeEnum
    method_status_id: MethodStatusEnum
    updated_at: datetime.datetime
    name: Union[None, Unset, str] = UNSET
    remarks: Union[None, Unset, str] = UNSET
    conducted_at: Union[None, Unset, datetime.datetime] = UNSET
    depth_top: Union[None, Unset, float] = UNSET
    depth_base: Union[None, Unset, float] = UNSET
    sample_container_id: Union[None, Unset, str] = UNSET
    sample_container_type_id: Union[None, Unset, int] = UNSET
    sampling_technique_id: Union[None, Unset, int] = UNSET
    diameter: Union[None, Unset, float] = UNSET
    inclination: Union[None, Unset, float] = UNSET
    azimuth: Union[None, Unset, float] = UNSET
    total_length: Union[None, Unset, float] = UNSET
    length_in_rock: Union[None, Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        method_id = str(self.method_id)

        method_type_id = self.method_type_id.value

        method_status_id = self.method_status_id.value

        updated_at = self.updated_at.isoformat()

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

        conducted_at: Union[None, Unset, str]
        if isinstance(self.conducted_at, Unset):
            conducted_at = UNSET
        elif isinstance(self.conducted_at, datetime.datetime):
            conducted_at = self.conducted_at.isoformat()
        else:
            conducted_at = self.conducted_at

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

        sampling_technique_id: Union[None, Unset, int]
        if isinstance(self.sampling_technique_id, Unset):
            sampling_technique_id = UNSET
        else:
            sampling_technique_id = self.sampling_technique_id

        diameter: Union[None, Unset, float]
        if isinstance(self.diameter, Unset):
            diameter = UNSET
        else:
            diameter = self.diameter

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

        total_length: Union[None, Unset, float]
        if isinstance(self.total_length, Unset):
            total_length = UNSET
        else:
            total_length = self.total_length

        length_in_rock: Union[None, Unset, float]
        if isinstance(self.length_in_rock, Unset):
            length_in_rock = UNSET
        else:
            length_in_rock = self.length_in_rock


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "method_id": method_id,
            "method_type_id": method_type_id,
            "method_status_id": method_status_id,
            "updated_at": updated_at,
        })
        if name is not UNSET:
            field_dict["name"] = name
        if remarks is not UNSET:
            field_dict["remarks"] = remarks
        if conducted_at is not UNSET:
            field_dict["conducted_at"] = conducted_at
        if depth_top is not UNSET:
            field_dict["depth_top"] = depth_top
        if depth_base is not UNSET:
            field_dict["depth_base"] = depth_base
        if sample_container_id is not UNSET:
            field_dict["sample_container_id"] = sample_container_id
        if sample_container_type_id is not UNSET:
            field_dict["sample_container_type_id"] = sample_container_type_id
        if sampling_technique_id is not UNSET:
            field_dict["sampling_technique_id"] = sampling_technique_id
        if diameter is not UNSET:
            field_dict["diameter"] = diameter
        if inclination is not UNSET:
            field_dict["inclination"] = inclination
        if azimuth is not UNSET:
            field_dict["azimuth"] = azimuth
        if total_length is not UNSET:
            field_dict["total_length"] = total_length
        if length_in_rock is not UNSET:
            field_dict["length_in_rock"] = length_in_rock

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        method_id = UUID(d.pop("method_id"))




        method_type_id = MethodTypeEnum(d.pop("method_type_id"))




        method_status_id = MethodStatusEnum(d.pop("method_status_id"))




        updated_at = isoparse(d.pop("updated_at"))




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
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        conducted_at = _parse_conducted_at(d.pop("conducted_at", UNSET))


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


        def _parse_sampling_technique_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        sampling_technique_id = _parse_sampling_technique_id(d.pop("sampling_technique_id", UNSET))


        def _parse_diameter(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        diameter = _parse_diameter(d.pop("diameter", UNSET))


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


        def _parse_total_length(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        total_length = _parse_total_length(d.pop("total_length", UNSET))


        def _parse_length_in_rock(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        length_in_rock = _parse_length_in_rock(d.pop("length_in_rock", UNSET))


        bff_method_summary = cls(
            method_id=method_id,
            method_type_id=method_type_id,
            method_status_id=method_status_id,
            updated_at=updated_at,
            name=name,
            remarks=remarks,
            conducted_at=conducted_at,
            depth_top=depth_top,
            depth_base=depth_base,
            sample_container_id=sample_container_id,
            sample_container_type_id=sample_container_type_id,
            sampling_technique_id=sampling_technique_id,
            diameter=diameter,
            inclination=inclination,
            azimuth=azimuth,
            total_length=total_length,
            length_in_rock=length_in_rock,
        )


        bff_method_summary.additional_properties = d
        return bff_method_summary

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
