import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.method_status_enum import MethodStatusEnum
from ..models.method_type_enum import MethodTypeEnum
from ..models.sounding_class import SoundingClass
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bedrock_info import BedrockInfo


T = TypeVar("T", bound="MethodInfo")


@_attrs_define
class MethodInfo:
    """
    Attributes:
        method_id (UUID):
        method_name (str):
        method_status (MethodStatusEnum): (
            PLANNED=1,
            READY=2,
            CONDUCTED=3,
            VOIDED=4,
            APPROVED=5,
            )
        method_type (MethodTypeEnum): (
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
        created_at (datetime.datetime):
        conducted_at (Union[None, Unset, datetime.datetime]):
        conducted_by (Union[None, Unset, str]):
        created_by (Union[None, Unset, str]):
        cone_reference (Union[None, Unset, str]):
        srs_type (Union[None, SoundingClass, Unset]):
        bedrock_info (Union['BedrockInfo', None, Unset]):
    """

    method_id: UUID
    method_name: str
    method_status: MethodStatusEnum
    method_type: MethodTypeEnum
    created_at: datetime.datetime
    conducted_at: Union[None, Unset, datetime.datetime] = UNSET
    conducted_by: Union[None, Unset, str] = UNSET
    created_by: Union[None, Unset, str] = UNSET
    cone_reference: Union[None, Unset, str] = UNSET
    srs_type: Union[None, SoundingClass, Unset] = UNSET
    bedrock_info: Union["BedrockInfo", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.bedrock_info import BedrockInfo

        method_id = str(self.method_id)

        method_name = self.method_name

        method_status = self.method_status.value

        method_type = self.method_type.value

        created_at = self.created_at.isoformat()

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

        created_by: Union[None, Unset, str]
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        else:
            created_by = self.created_by

        cone_reference: Union[None, Unset, str]
        if isinstance(self.cone_reference, Unset):
            cone_reference = UNSET
        else:
            cone_reference = self.cone_reference

        srs_type: Union[None, Unset, str]
        if isinstance(self.srs_type, Unset):
            srs_type = UNSET
        elif isinstance(self.srs_type, SoundingClass):
            srs_type = self.srs_type.value
        else:
            srs_type = self.srs_type

        bedrock_info: Union[None, Unset, dict[str, Any]]
        if isinstance(self.bedrock_info, Unset):
            bedrock_info = UNSET
        elif isinstance(self.bedrock_info, BedrockInfo):
            bedrock_info = self.bedrock_info.to_dict()
        else:
            bedrock_info = self.bedrock_info

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "method_id": method_id,
                "method_name": method_name,
                "method_status": method_status,
                "method_type": method_type,
                "created_at": created_at,
            }
        )
        if conducted_at is not UNSET:
            field_dict["conducted_at"] = conducted_at
        if conducted_by is not UNSET:
            field_dict["conducted_by"] = conducted_by
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if cone_reference is not UNSET:
            field_dict["cone_reference"] = cone_reference
        if srs_type is not UNSET:
            field_dict["srs_type"] = srs_type
        if bedrock_info is not UNSET:
            field_dict["bedrock_info"] = bedrock_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bedrock_info import BedrockInfo

        d = dict(src_dict)
        method_id = UUID(d.pop("method_id"))

        method_name = d.pop("method_name")

        method_status = MethodStatusEnum(d.pop("method_status"))

        method_type = MethodTypeEnum(d.pop("method_type"))

        created_at = isoparse(d.pop("created_at"))

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

        def _parse_created_by(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        created_by = _parse_created_by(d.pop("created_by", UNSET))

        def _parse_cone_reference(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cone_reference = _parse_cone_reference(d.pop("cone_reference", UNSET))

        def _parse_srs_type(data: object) -> Union[None, SoundingClass, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                srs_type_type_0 = SoundingClass(data)

                return srs_type_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, SoundingClass, Unset], data)

        srs_type = _parse_srs_type(d.pop("srs_type", UNSET))

        def _parse_bedrock_info(data: object) -> Union["BedrockInfo", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                bedrock_info_type_0 = BedrockInfo.from_dict(data)

                return bedrock_info_type_0
            except:  # noqa: E722
                pass
            return cast(Union["BedrockInfo", None, Unset], data)

        bedrock_info = _parse_bedrock_info(d.pop("bedrock_info", UNSET))

        method_info = cls(
            method_id=method_id,
            method_name=method_name,
            method_status=method_status,
            method_type=method_type,
            created_at=created_at,
            conducted_at=conducted_at,
            conducted_by=conducted_by,
            created_by=created_by,
            cone_reference=cone_reference,
            srs_type=srs_type,
            bedrock_info=bedrock_info,
        )

        method_info.additional_properties = d
        return method_info

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
