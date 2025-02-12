import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.dp_type import DPType
from ..models.method_dp_method_type_id import MethodDPMethodTypeId
from ..models.method_status_enum import MethodStatusEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file import File


T = TypeVar("T", bound="MethodDP")


@_attrs_define
class MethodDP:
    """DP method
    Dynamic Probing
    Swedish Ram sounding (Swedish hejarsondering)

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
            method_type_id (Union[Unset, MethodDPMethodTypeId]):  Default: MethodDPMethodTypeId.VALUE_25.
            created_by (Union[None, Unset, str]):
            updated_by (Union[None, Unset, str]):
            conducted_at (Union[None, Unset, datetime.datetime]):
            conducted_by (Union[None, Unset, str]):
            files (Union[Unset, List['File']]):
            self_ (Union[None, Unset, str]):
            type (Union[Unset, DPType]): (Dynamic Probing) DP Type
            predrilling_depth (Union[Unset, float]):  Default: 0.0.
            cone_type (Union[None, Unset, str]):
            cushion_type (Union[None, Unset, str]):
            use_damper (Union[None, Unset, bool]):
            depth_top (Union[None, Unset, float]):
            depth_base (Union[None, Unset, float]):
            stopcode (Union[None, Unset, int]):
            depth_in_soil (Union[None, Unset, float]):
    """

    method_id: UUID
    name: str
    location_id: UUID
    method_status_id: MethodStatusEnum
    created_at: datetime.datetime
    updated_at: datetime.datetime
    remarks: Union[None, Unset, str] = UNSET
    method_type_id: Union[Unset, MethodDPMethodTypeId] = MethodDPMethodTypeId.VALUE_25
    created_by: Union[None, Unset, str] = UNSET
    updated_by: Union[None, Unset, str] = UNSET
    conducted_at: Union[None, Unset, datetime.datetime] = UNSET
    conducted_by: Union[None, Unset, str] = UNSET
    files: Union[Unset, List["File"]] = UNSET
    self_: Union[None, Unset, str] = UNSET
    type: Union[Unset, DPType] = UNSET
    predrilling_depth: Union[Unset, float] = 0.0
    cone_type: Union[None, Unset, str] = UNSET
    cushion_type: Union[None, Unset, str] = UNSET
    use_damper: Union[None, Unset, bool] = UNSET
    depth_top: Union[None, Unset, float] = UNSET
    depth_base: Union[None, Unset, float] = UNSET
    stopcode: Union[None, Unset, int] = UNSET
    depth_in_soil: Union[None, Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
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

        method_type_id: Union[Unset, int] = UNSET
        if not isinstance(self.method_type_id, Unset):
            method_type_id = self.method_type_id.value

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

        files: Union[Unset, List[Dict[str, Any]]] = UNSET
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

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        predrilling_depth = self.predrilling_depth

        cone_type: Union[None, Unset, str]
        if isinstance(self.cone_type, Unset):
            cone_type = UNSET
        else:
            cone_type = self.cone_type

        cushion_type: Union[None, Unset, str]
        if isinstance(self.cushion_type, Unset):
            cushion_type = UNSET
        else:
            cushion_type = self.cushion_type

        use_damper: Union[None, Unset, bool]
        if isinstance(self.use_damper, Unset):
            use_damper = UNSET
        else:
            use_damper = self.use_damper

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

        stopcode: Union[None, Unset, int]
        if isinstance(self.stopcode, Unset):
            stopcode = UNSET
        else:
            stopcode = self.stopcode

        depth_in_soil: Union[None, Unset, float]
        if isinstance(self.depth_in_soil, Unset):
            depth_in_soil = UNSET
        else:
            depth_in_soil = self.depth_in_soil

        field_dict: Dict[str, Any] = {}
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
        if type is not UNSET:
            field_dict["type"] = type
        if predrilling_depth is not UNSET:
            field_dict["predrilling_depth"] = predrilling_depth
        if cone_type is not UNSET:
            field_dict["cone_type"] = cone_type
        if cushion_type is not UNSET:
            field_dict["cushion_type"] = cushion_type
        if use_damper is not UNSET:
            field_dict["use_damper"] = use_damper
        if depth_top is not UNSET:
            field_dict["depth_top"] = depth_top
        if depth_base is not UNSET:
            field_dict["depth_base"] = depth_base
        if stopcode is not UNSET:
            field_dict["stopcode"] = stopcode
        if depth_in_soil is not UNSET:
            field_dict["depth_in_soil"] = depth_in_soil

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
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

        _method_type_id = d.pop("method_type_id", UNSET)
        method_type_id: Union[Unset, MethodDPMethodTypeId]
        if isinstance(_method_type_id, Unset):
            method_type_id = UNSET
        else:
            method_type_id = MethodDPMethodTypeId(_method_type_id)

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

        _type = d.pop("type", UNSET)
        type: Union[Unset, DPType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = DPType(_type)

        predrilling_depth = d.pop("predrilling_depth", UNSET)

        def _parse_cone_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cone_type = _parse_cone_type(d.pop("cone_type", UNSET))

        def _parse_cushion_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cushion_type = _parse_cushion_type(d.pop("cushion_type", UNSET))

        def _parse_use_damper(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        use_damper = _parse_use_damper(d.pop("use_damper", UNSET))

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

        def _parse_stopcode(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        stopcode = _parse_stopcode(d.pop("stopcode", UNSET))

        def _parse_depth_in_soil(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        depth_in_soil = _parse_depth_in_soil(d.pop("depth_in_soil", UNSET))

        method_dp = cls(
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
            type=type,
            predrilling_depth=predrilling_depth,
            cone_type=cone_type,
            cushion_type=cushion_type,
            use_damper=use_damper,
            depth_top=depth_top,
            depth_base=depth_base,
            stopcode=stopcode,
            depth_in_soil=depth_in_soil,
        )

        method_dp.additional_properties = d
        return method_dp

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
