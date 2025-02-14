import datetime
from typing import Any, Literal, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="MethodWSTData")


@_attrs_define
class MethodWSTData:
    """
    Attributes:
        method_data_id (UUID):
        method_id (UUID):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        depth (float): Depth (m). SGF code D.
        method_type_id (Union[Literal[26], Unset]):  Default: 26.
        turning (Union[None, Unset, float]): Turning (half revolution/0.2 m)
        load (Union[None, Unset, float]): Load (kN)
        penetration_rate (Union[None, Unset, float]): Penetration rate (mm/s)
        hammering (Union[None, Unset, bool]): Hammering 0=off 1=on SGF code AP.
        rotation_rate (Union[None, Unset, float]): Rotation rate (rpm)
    """

    method_data_id: UUID
    method_id: UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    depth: float
    method_type_id: Union[Literal[26], Unset] = 26
    turning: Union[None, Unset, float] = UNSET
    load: Union[None, Unset, float] = UNSET
    penetration_rate: Union[None, Unset, float] = UNSET
    hammering: Union[None, Unset, bool] = UNSET
    rotation_rate: Union[None, Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        method_data_id = str(self.method_data_id)

        method_id = str(self.method_id)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        depth = self.depth

        method_type_id = self.method_type_id

        turning: Union[None, Unset, float]
        if isinstance(self.turning, Unset):
            turning = UNSET
        else:
            turning = self.turning

        load: Union[None, Unset, float]
        if isinstance(self.load, Unset):
            load = UNSET
        else:
            load = self.load

        penetration_rate: Union[None, Unset, float]
        if isinstance(self.penetration_rate, Unset):
            penetration_rate = UNSET
        else:
            penetration_rate = self.penetration_rate

        hammering: Union[None, Unset, bool]
        if isinstance(self.hammering, Unset):
            hammering = UNSET
        else:
            hammering = self.hammering

        rotation_rate: Union[None, Unset, float]
        if isinstance(self.rotation_rate, Unset):
            rotation_rate = UNSET
        else:
            rotation_rate = self.rotation_rate

        field_dict: dict[str, Any] = {}
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
        if turning is not UNSET:
            field_dict["turning"] = turning
        if load is not UNSET:
            field_dict["load"] = load
        if penetration_rate is not UNSET:
            field_dict["penetration_rate"] = penetration_rate
        if hammering is not UNSET:
            field_dict["hammering"] = hammering
        if rotation_rate is not UNSET:
            field_dict["rotation_rate"] = rotation_rate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        method_data_id = UUID(d.pop("method_data_id"))

        method_id = UUID(d.pop("method_id"))

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        depth = d.pop("depth")

        method_type_id = cast(Union[Literal[26], Unset], d.pop("method_type_id", UNSET))
        if method_type_id != 26 and not isinstance(method_type_id, Unset):
            raise ValueError(f"method_type_id must match const 26, got '{method_type_id}'")

        def _parse_turning(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        turning = _parse_turning(d.pop("turning", UNSET))

        def _parse_load(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        load = _parse_load(d.pop("load", UNSET))

        def _parse_penetration_rate(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        penetration_rate = _parse_penetration_rate(d.pop("penetration_rate", UNSET))

        def _parse_hammering(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        hammering = _parse_hammering(d.pop("hammering", UNSET))

        def _parse_rotation_rate(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        rotation_rate = _parse_rotation_rate(d.pop("rotation_rate", UNSET))

        method_wst_data = cls(
            method_data_id=method_data_id,
            method_id=method_id,
            created_at=created_at,
            updated_at=updated_at,
            depth=depth,
            method_type_id=method_type_id,
            turning=turning,
            load=load,
            penetration_rate=penetration_rate,
            hammering=hammering,
            rotation_rate=rotation_rate,
        )

        method_wst_data.additional_properties = d
        return method_wst_data

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
