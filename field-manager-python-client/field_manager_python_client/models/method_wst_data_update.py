from typing import Any, Literal, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MethodWSTDataUpdate")


@_attrs_define
class MethodWSTDataUpdate:
    """
    Attributes:
        method_type_id (Union[Literal[26], Unset]):  Default: 26.
        depth (Union[None, Unset, float, str]): Depth (m). SGF code D.
        turning (Union[None, Unset, float, str]): Turning (half revolution/0.2 m)
        load (Union[None, Unset, float, str]): Load (kN)
        penetration_rate (Union[None, Unset, float, str]): Penetration rate (mm/s)
        hammering (Union[None, Unset, bool]):
        rotation_rate (Union[None, Unset, float, str]): Rotation rate (rpm)
    """

    method_type_id: Union[Literal[26], Unset] = 26
    depth: Union[None, Unset, float, str] = UNSET
    turning: Union[None, Unset, float, str] = UNSET
    load: Union[None, Unset, float, str] = UNSET
    penetration_rate: Union[None, Unset, float, str] = UNSET
    hammering: Union[None, Unset, bool] = UNSET
    rotation_rate: Union[None, Unset, float, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        method_type_id = self.method_type_id

        depth: Union[None, Unset, float, str]
        if isinstance(self.depth, Unset):
            depth = UNSET
        else:
            depth = self.depth

        turning: Union[None, Unset, float, str]
        if isinstance(self.turning, Unset):
            turning = UNSET
        else:
            turning = self.turning

        load: Union[None, Unset, float, str]
        if isinstance(self.load, Unset):
            load = UNSET
        else:
            load = self.load

        penetration_rate: Union[None, Unset, float, str]
        if isinstance(self.penetration_rate, Unset):
            penetration_rate = UNSET
        else:
            penetration_rate = self.penetration_rate

        hammering: Union[None, Unset, bool]
        if isinstance(self.hammering, Unset):
            hammering = UNSET
        else:
            hammering = self.hammering

        rotation_rate: Union[None, Unset, float, str]
        if isinstance(self.rotation_rate, Unset):
            rotation_rate = UNSET
        else:
            rotation_rate = self.rotation_rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if method_type_id is not UNSET:
            field_dict["method_type_id"] = method_type_id
        if depth is not UNSET:
            field_dict["depth"] = depth
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
        method_type_id = cast(Union[Literal[26], Unset], d.pop("method_type_id", UNSET))
        if method_type_id != 26 and not isinstance(method_type_id, Unset):
            raise ValueError(f"method_type_id must match const 26, got '{method_type_id}'")

        def _parse_depth(data: object) -> Union[None, Unset, float, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, str], data)

        depth = _parse_depth(d.pop("depth", UNSET))

        def _parse_turning(data: object) -> Union[None, Unset, float, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, str], data)

        turning = _parse_turning(d.pop("turning", UNSET))

        def _parse_load(data: object) -> Union[None, Unset, float, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, str], data)

        load = _parse_load(d.pop("load", UNSET))

        def _parse_penetration_rate(data: object) -> Union[None, Unset, float, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, str], data)

        penetration_rate = _parse_penetration_rate(d.pop("penetration_rate", UNSET))

        def _parse_hammering(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        hammering = _parse_hammering(d.pop("hammering", UNSET))

        def _parse_rotation_rate(data: object) -> Union[None, Unset, float, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, str], data)

        rotation_rate = _parse_rotation_rate(d.pop("rotation_rate", UNSET))

        method_wst_data_update = cls(
            method_type_id=method_type_id,
            depth=depth,
            turning=turning,
            load=load,
            penetration_rate=penetration_rate,
            hammering=hammering,
            rotation_rate=rotation_rate,
        )

        method_wst_data_update.additional_properties = d
        return method_wst_data_update

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
