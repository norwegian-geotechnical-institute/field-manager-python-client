import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.method_srs_data_method_type_id import MethodSRSDataMethodTypeId
from ..types import UNSET, Unset

T = TypeVar("T", bound="MethodSRSData")


@_attrs_define
class MethodSRSData:
    """
    Attributes:
        method_data_id (UUID):
        method_id (UUID):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        depth (float): Depth (m). SGF code D.
        method_type_id (Union[Unset, MethodSRSDataMethodTypeId]):  Default: MethodSRSDataMethodTypeId.VALUE_24.
        remarks (Union[None, Unset, str]): Remarks. SGF code T
        comment_code (Union[None, Unset, int]): Comment code. Two digit value.
        penetration_rate (Union[None, Unset, float]): Penetration rate (mm/s). SGF code B.
        penetration_force (Union[None, Unset, float]): Penetration force (kN). SGF code A.
        hammering_pressure (Union[None, Unset, float]): Hammering pressure (MPa). SGF code AZ.
        hammering (Union[None, Unset, bool]): Hammering 0=off 1=on. SGF code AP.
        engine_pressure (Union[None, Unset, float]): Engine pressure (MPa). SGF code P.
        torque (Union[None, Unset, float]): Torque (kNm). SGF code V.
        rotation_rate (Union[None, Unset, float]): Rotation rate (rpm). SGF code R.
        flushing (Union[None, Unset, bool]): Flushing 0=off 1=on. SGF code AR.
        flushing_pressure (Union[None, Unset, float]): Flushing pressure (MPa). SGF code I.
        flushing_flow (Union[None, Unset, float]): Flushing flow (liter/minute). SGF code J.
    """

    method_data_id: UUID
    method_id: UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    depth: float
    method_type_id: Union[Unset, MethodSRSDataMethodTypeId] = MethodSRSDataMethodTypeId.VALUE_24
    remarks: Union[None, Unset, str] = UNSET
    comment_code: Union[None, Unset, int] = UNSET
    penetration_rate: Union[None, Unset, float] = UNSET
    penetration_force: Union[None, Unset, float] = UNSET
    hammering_pressure: Union[None, Unset, float] = UNSET
    hammering: Union[None, Unset, bool] = UNSET
    engine_pressure: Union[None, Unset, float] = UNSET
    torque: Union[None, Unset, float] = UNSET
    rotation_rate: Union[None, Unset, float] = UNSET
    flushing: Union[None, Unset, bool] = UNSET
    flushing_pressure: Union[None, Unset, float] = UNSET
    flushing_flow: Union[None, Unset, float] = UNSET
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

        remarks: Union[None, Unset, str]
        if isinstance(self.remarks, Unset):
            remarks = UNSET
        else:
            remarks = self.remarks

        comment_code: Union[None, Unset, int]
        if isinstance(self.comment_code, Unset):
            comment_code = UNSET
        else:
            comment_code = self.comment_code

        penetration_rate: Union[None, Unset, float]
        if isinstance(self.penetration_rate, Unset):
            penetration_rate = UNSET
        else:
            penetration_rate = self.penetration_rate

        penetration_force: Union[None, Unset, float]
        if isinstance(self.penetration_force, Unset):
            penetration_force = UNSET
        else:
            penetration_force = self.penetration_force

        hammering_pressure: Union[None, Unset, float]
        if isinstance(self.hammering_pressure, Unset):
            hammering_pressure = UNSET
        else:
            hammering_pressure = self.hammering_pressure

        hammering: Union[None, Unset, bool]
        if isinstance(self.hammering, Unset):
            hammering = UNSET
        else:
            hammering = self.hammering

        engine_pressure: Union[None, Unset, float]
        if isinstance(self.engine_pressure, Unset):
            engine_pressure = UNSET
        else:
            engine_pressure = self.engine_pressure

        torque: Union[None, Unset, float]
        if isinstance(self.torque, Unset):
            torque = UNSET
        else:
            torque = self.torque

        rotation_rate: Union[None, Unset, float]
        if isinstance(self.rotation_rate, Unset):
            rotation_rate = UNSET
        else:
            rotation_rate = self.rotation_rate

        flushing: Union[None, Unset, bool]
        if isinstance(self.flushing, Unset):
            flushing = UNSET
        else:
            flushing = self.flushing

        flushing_pressure: Union[None, Unset, float]
        if isinstance(self.flushing_pressure, Unset):
            flushing_pressure = UNSET
        else:
            flushing_pressure = self.flushing_pressure

        flushing_flow: Union[None, Unset, float]
        if isinstance(self.flushing_flow, Unset):
            flushing_flow = UNSET
        else:
            flushing_flow = self.flushing_flow

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
        if remarks is not UNSET:
            field_dict["remarks"] = remarks
        if comment_code is not UNSET:
            field_dict["comment_code"] = comment_code
        if penetration_rate is not UNSET:
            field_dict["penetration_rate"] = penetration_rate
        if penetration_force is not UNSET:
            field_dict["penetration_force"] = penetration_force
        if hammering_pressure is not UNSET:
            field_dict["hammering_pressure"] = hammering_pressure
        if hammering is not UNSET:
            field_dict["hammering"] = hammering
        if engine_pressure is not UNSET:
            field_dict["engine_pressure"] = engine_pressure
        if torque is not UNSET:
            field_dict["torque"] = torque
        if rotation_rate is not UNSET:
            field_dict["rotation_rate"] = rotation_rate
        if flushing is not UNSET:
            field_dict["flushing"] = flushing
        if flushing_pressure is not UNSET:
            field_dict["flushing_pressure"] = flushing_pressure
        if flushing_flow is not UNSET:
            field_dict["flushing_flow"] = flushing_flow

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
        method_type_id: Union[Unset, MethodSRSDataMethodTypeId]
        if isinstance(_method_type_id, Unset):
            method_type_id = UNSET
        else:
            method_type_id = MethodSRSDataMethodTypeId(_method_type_id)

        def _parse_remarks(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        remarks = _parse_remarks(d.pop("remarks", UNSET))

        def _parse_comment_code(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        comment_code = _parse_comment_code(d.pop("comment_code", UNSET))

        def _parse_penetration_rate(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        penetration_rate = _parse_penetration_rate(d.pop("penetration_rate", UNSET))

        def _parse_penetration_force(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        penetration_force = _parse_penetration_force(d.pop("penetration_force", UNSET))

        def _parse_hammering_pressure(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        hammering_pressure = _parse_hammering_pressure(d.pop("hammering_pressure", UNSET))

        def _parse_hammering(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        hammering = _parse_hammering(d.pop("hammering", UNSET))

        def _parse_engine_pressure(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        engine_pressure = _parse_engine_pressure(d.pop("engine_pressure", UNSET))

        def _parse_torque(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        torque = _parse_torque(d.pop("torque", UNSET))

        def _parse_rotation_rate(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        rotation_rate = _parse_rotation_rate(d.pop("rotation_rate", UNSET))

        def _parse_flushing(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        flushing = _parse_flushing(d.pop("flushing", UNSET))

        def _parse_flushing_pressure(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        flushing_pressure = _parse_flushing_pressure(d.pop("flushing_pressure", UNSET))

        def _parse_flushing_flow(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        flushing_flow = _parse_flushing_flow(d.pop("flushing_flow", UNSET))

        method_srs_data = cls(
            method_data_id=method_data_id,
            method_id=method_id,
            created_at=created_at,
            updated_at=updated_at,
            depth=depth,
            method_type_id=method_type_id,
            remarks=remarks,
            comment_code=comment_code,
            penetration_rate=penetration_rate,
            penetration_force=penetration_force,
            hammering_pressure=hammering_pressure,
            hammering=hammering,
            engine_pressure=engine_pressure,
            torque=torque,
            rotation_rate=rotation_rate,
            flushing=flushing,
            flushing_pressure=flushing_pressure,
            flushing_flow=flushing_flow,
        )

        method_srs_data.additional_properties = d
        return method_srs_data

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
