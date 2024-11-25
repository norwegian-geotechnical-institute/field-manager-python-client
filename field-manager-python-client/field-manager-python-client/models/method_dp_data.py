import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.method_dp_data_method_type_id import MethodDPDataMethodTypeId
from ..types import UNSET, Unset

T = TypeVar("T", bound="MethodDPData")


@_attrs_define
class MethodDPData:
    """
    Attributes:
        method_data_id (UUID):
        method_id (UUID):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        depth (float): Depth (m). SGF code D.
        method_type_id (Union[Unset, MethodDPDataMethodTypeId]):  Default: MethodDPDataMethodTypeId.VALUE_25.
        comment_code (Union[None, Unset, int]): Comment code. Two digit value.
        remarks (Union[None, Unset, str]):
        penetration_force (Union[None, Unset, float]): Penetration force (kN)
        penetration_rate (Union[None, Unset, float]): Penetration rate (mm/s)
        torque (Union[None, Unset, float]): Torque (kNm)
        ramming (Union[None, Unset, float]): Ramming (blow/0.2m)
        rotation_rate (Union[None, Unset, float]): Rotation rate (rpm)
        increased_rotation_rate (Union[None, Unset, bool]): rotation
    """

    method_data_id: UUID
    method_id: UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    depth: float
    method_type_id: Union[Unset, MethodDPDataMethodTypeId] = MethodDPDataMethodTypeId.VALUE_25
    comment_code: Union[None, Unset, int] = UNSET
    remarks: Union[None, Unset, str] = UNSET
    penetration_force: Union[None, Unset, float] = UNSET
    penetration_rate: Union[None, Unset, float] = UNSET
    torque: Union[None, Unset, float] = UNSET
    ramming: Union[None, Unset, float] = UNSET
    rotation_rate: Union[None, Unset, float] = UNSET
    increased_rotation_rate: Union[None, Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        method_data_id = str(self.method_data_id)

        method_id = str(self.method_id)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        depth = self.depth

        method_type_id: Union[Unset, int] = UNSET
        if not isinstance(self.method_type_id, Unset):
            method_type_id = self.method_type_id.value

        comment_code: Union[None, Unset, int]
        if isinstance(self.comment_code, Unset):
            comment_code = UNSET
        else:
            comment_code = self.comment_code

        remarks: Union[None, Unset, str]
        if isinstance(self.remarks, Unset):
            remarks = UNSET
        else:
            remarks = self.remarks

        penetration_force: Union[None, Unset, float]
        if isinstance(self.penetration_force, Unset):
            penetration_force = UNSET
        else:
            penetration_force = self.penetration_force

        penetration_rate: Union[None, Unset, float]
        if isinstance(self.penetration_rate, Unset):
            penetration_rate = UNSET
        else:
            penetration_rate = self.penetration_rate

        torque: Union[None, Unset, float]
        if isinstance(self.torque, Unset):
            torque = UNSET
        else:
            torque = self.torque

        ramming: Union[None, Unset, float]
        if isinstance(self.ramming, Unset):
            ramming = UNSET
        else:
            ramming = self.ramming

        rotation_rate: Union[None, Unset, float]
        if isinstance(self.rotation_rate, Unset):
            rotation_rate = UNSET
        else:
            rotation_rate = self.rotation_rate

        increased_rotation_rate: Union[None, Unset, bool]
        if isinstance(self.increased_rotation_rate, Unset):
            increased_rotation_rate = UNSET
        else:
            increased_rotation_rate = self.increased_rotation_rate

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "method_data_id": method_data_id,
                "method_id": method_id,
                "created_at": created_at,
                "updated_at": updated_at,
                "depth": depth,
            }
        )
        if method_type_id is not UNSET:
            field_dict["method_type_id"] = method_type_id
        if comment_code is not UNSET:
            field_dict["comment_code"] = comment_code
        if remarks is not UNSET:
            field_dict["remarks"] = remarks
        if penetration_force is not UNSET:
            field_dict["penetration_force"] = penetration_force
        if penetration_rate is not UNSET:
            field_dict["penetration_rate"] = penetration_rate
        if torque is not UNSET:
            field_dict["torque"] = torque
        if ramming is not UNSET:
            field_dict["ramming"] = ramming
        if rotation_rate is not UNSET:
            field_dict["rotation_rate"] = rotation_rate
        if increased_rotation_rate is not UNSET:
            field_dict["increased_rotation_rate"] = increased_rotation_rate

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        method_data_id = UUID(d.pop("method_data_id"))

        method_id = UUID(d.pop("method_id"))

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        depth = d.pop("depth")

        _method_type_id = d.pop("method_type_id", UNSET)
        method_type_id: Union[Unset, MethodDPDataMethodTypeId]
        if isinstance(_method_type_id, Unset):
            method_type_id = UNSET
        else:
            method_type_id = MethodDPDataMethodTypeId(_method_type_id)

        def _parse_comment_code(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        comment_code = _parse_comment_code(d.pop("comment_code", UNSET))

        def _parse_remarks(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        remarks = _parse_remarks(d.pop("remarks", UNSET))

        def _parse_penetration_force(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        penetration_force = _parse_penetration_force(d.pop("penetration_force", UNSET))

        def _parse_penetration_rate(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        penetration_rate = _parse_penetration_rate(d.pop("penetration_rate", UNSET))

        def _parse_torque(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        torque = _parse_torque(d.pop("torque", UNSET))

        def _parse_ramming(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        ramming = _parse_ramming(d.pop("ramming", UNSET))

        def _parse_rotation_rate(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        rotation_rate = _parse_rotation_rate(d.pop("rotation_rate", UNSET))

        def _parse_increased_rotation_rate(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        increased_rotation_rate = _parse_increased_rotation_rate(d.pop("increased_rotation_rate", UNSET))

        method_dp_data = cls(
            method_data_id=method_data_id,
            method_id=method_id,
            created_at=created_at,
            updated_at=updated_at,
            depth=depth,
            method_type_id=method_type_id,
            comment_code=comment_code,
            remarks=remarks,
            penetration_force=penetration_force,
            penetration_rate=penetration_rate,
            torque=torque,
            ramming=ramming,
            rotation_rate=rotation_rate,
            increased_rotation_rate=increased_rotation_rate,
        )

        method_dp_data.additional_properties = d
        return method_dp_data

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
