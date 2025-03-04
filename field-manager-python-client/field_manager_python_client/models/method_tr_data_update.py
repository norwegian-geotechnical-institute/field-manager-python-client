from typing import Any, Literal, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MethodTRDataUpdate")


@_attrs_define
class MethodTRDataUpdate:
    """
    Attributes:
        method_type_id (Union[Literal[16], Unset]):  Default: 16.
        depth (Union[None, Unset, float, str]): Depth (m). SGF code D.
        penetration_rate (Union[None, Unset, float, str]): Penetration rate (mm/s)
        penetration_force (Union[None, Unset, float, str]): Penetration force (kN)
        rotation_rate (Union[None, Unset, float, str]): Rotation rate (rpm)
        rod_friction (Union[None, Unset, float, str]): Rod friction (kN)
        increased_rotation_rate (Union[None, Unset, bool]): Increased rotation rate
    """

    method_type_id: Union[Literal[16], Unset] = 16
    depth: Union[None, Unset, float, str] = UNSET
    penetration_rate: Union[None, Unset, float, str] = UNSET
    penetration_force: Union[None, Unset, float, str] = UNSET
    rotation_rate: Union[None, Unset, float, str] = UNSET
    rod_friction: Union[None, Unset, float, str] = UNSET
    increased_rotation_rate: Union[None, Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        method_type_id = self.method_type_id

        depth: Union[None, Unset, float, str]
        if isinstance(self.depth, Unset):
            depth = UNSET
        else:
            depth = self.depth

        penetration_rate: Union[None, Unset, float, str]
        if isinstance(self.penetration_rate, Unset):
            penetration_rate = UNSET
        else:
            penetration_rate = self.penetration_rate

        penetration_force: Union[None, Unset, float, str]
        if isinstance(self.penetration_force, Unset):
            penetration_force = UNSET
        else:
            penetration_force = self.penetration_force

        rotation_rate: Union[None, Unset, float, str]
        if isinstance(self.rotation_rate, Unset):
            rotation_rate = UNSET
        else:
            rotation_rate = self.rotation_rate

        rod_friction: Union[None, Unset, float, str]
        if isinstance(self.rod_friction, Unset):
            rod_friction = UNSET
        else:
            rod_friction = self.rod_friction

        increased_rotation_rate: Union[None, Unset, bool]
        if isinstance(self.increased_rotation_rate, Unset):
            increased_rotation_rate = UNSET
        else:
            increased_rotation_rate = self.increased_rotation_rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if method_type_id is not UNSET:
            field_dict["method_type_id"] = method_type_id
        if depth is not UNSET:
            field_dict["depth"] = depth
        if penetration_rate is not UNSET:
            field_dict["penetration_rate"] = penetration_rate
        if penetration_force is not UNSET:
            field_dict["penetration_force"] = penetration_force
        if rotation_rate is not UNSET:
            field_dict["rotation_rate"] = rotation_rate
        if rod_friction is not UNSET:
            field_dict["rod_friction"] = rod_friction
        if increased_rotation_rate is not UNSET:
            field_dict["increased_rotation_rate"] = increased_rotation_rate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        method_type_id = cast(Union[Literal[16], Unset], d.pop("method_type_id", UNSET))
        if method_type_id != 16 and not isinstance(method_type_id, Unset):
            raise ValueError(f"method_type_id must match const 16, got '{method_type_id}'")

        def _parse_depth(data: object) -> Union[None, Unset, float, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, str], data)

        depth = _parse_depth(d.pop("depth", UNSET))

        def _parse_penetration_rate(data: object) -> Union[None, Unset, float, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, str], data)

        penetration_rate = _parse_penetration_rate(d.pop("penetration_rate", UNSET))

        def _parse_penetration_force(data: object) -> Union[None, Unset, float, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, str], data)

        penetration_force = _parse_penetration_force(d.pop("penetration_force", UNSET))

        def _parse_rotation_rate(data: object) -> Union[None, Unset, float, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, str], data)

        rotation_rate = _parse_rotation_rate(d.pop("rotation_rate", UNSET))

        def _parse_rod_friction(data: object) -> Union[None, Unset, float, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, str], data)

        rod_friction = _parse_rod_friction(d.pop("rod_friction", UNSET))

        def _parse_increased_rotation_rate(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        increased_rotation_rate = _parse_increased_rotation_rate(d.pop("increased_rotation_rate", UNSET))

        method_tr_data_update = cls(
            method_type_id=method_type_id,
            depth=depth,
            penetration_rate=penetration_rate,
            penetration_force=penetration_force,
            rotation_rate=rotation_rate,
            rod_friction=rod_friction,
            increased_rotation_rate=increased_rotation_rate,
        )

        method_tr_data_update.additional_properties = d
        return method_tr_data_update

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
