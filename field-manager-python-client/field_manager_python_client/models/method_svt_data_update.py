from collections.abc import Mapping
from typing import Any, Literal, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MethodSVTDataUpdate")


@_attrs_define
class MethodSVTDataUpdate:
    """
    Attributes:
        method_type_id (Union[Literal[10], Unset]):  Default: 10.
        depth_top (Union[None, Unset, float, str]): Depth (m).
        maximum_measurement_torque (Union[None, Unset, float, str]): Maximum measurement torque (Nm).
        maximum_measurement_torque_remoulded (Union[None, Unset, float, str]): Maximum measurement torque (Nm).
        shear_strength (Union[None, Unset, float, str]): Shear strength (kPa). SGF code AS.
        shear_strength_remoulded (Union[None, Unset, float, str]): Shear strength (kPa).
        sensitivity (Union[None, Unset, float, str]): Sensitivity (unitless). SGF code SV.
        remarks (Union[None, Unset, str]):
    """

    method_type_id: Union[Literal[10], Unset] = 10
    depth_top: Union[None, Unset, float, str] = UNSET
    maximum_measurement_torque: Union[None, Unset, float, str] = UNSET
    maximum_measurement_torque_remoulded: Union[None, Unset, float, str] = UNSET
    shear_strength: Union[None, Unset, float, str] = UNSET
    shear_strength_remoulded: Union[None, Unset, float, str] = UNSET
    sensitivity: Union[None, Unset, float, str] = UNSET
    remarks: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        method_type_id = self.method_type_id

        depth_top: Union[None, Unset, float, str]
        if isinstance(self.depth_top, Unset):
            depth_top = UNSET
        else:
            depth_top = self.depth_top

        maximum_measurement_torque: Union[None, Unset, float, str]
        if isinstance(self.maximum_measurement_torque, Unset):
            maximum_measurement_torque = UNSET
        else:
            maximum_measurement_torque = self.maximum_measurement_torque

        maximum_measurement_torque_remoulded: Union[None, Unset, float, str]
        if isinstance(self.maximum_measurement_torque_remoulded, Unset):
            maximum_measurement_torque_remoulded = UNSET
        else:
            maximum_measurement_torque_remoulded = self.maximum_measurement_torque_remoulded

        shear_strength: Union[None, Unset, float, str]
        if isinstance(self.shear_strength, Unset):
            shear_strength = UNSET
        else:
            shear_strength = self.shear_strength

        shear_strength_remoulded: Union[None, Unset, float, str]
        if isinstance(self.shear_strength_remoulded, Unset):
            shear_strength_remoulded = UNSET
        else:
            shear_strength_remoulded = self.shear_strength_remoulded

        sensitivity: Union[None, Unset, float, str]
        if isinstance(self.sensitivity, Unset):
            sensitivity = UNSET
        else:
            sensitivity = self.sensitivity

        remarks: Union[None, Unset, str]
        if isinstance(self.remarks, Unset):
            remarks = UNSET
        else:
            remarks = self.remarks

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if method_type_id is not UNSET:
            field_dict["method_type_id"] = method_type_id
        if depth_top is not UNSET:
            field_dict["depth_top"] = depth_top
        if maximum_measurement_torque is not UNSET:
            field_dict["maximum_measurement_torque"] = maximum_measurement_torque
        if maximum_measurement_torque_remoulded is not UNSET:
            field_dict["maximum_measurement_torque_remoulded"] = maximum_measurement_torque_remoulded
        if shear_strength is not UNSET:
            field_dict["shear_strength"] = shear_strength
        if shear_strength_remoulded is not UNSET:
            field_dict["shear_strength_remoulded"] = shear_strength_remoulded
        if sensitivity is not UNSET:
            field_dict["sensitivity"] = sensitivity
        if remarks is not UNSET:
            field_dict["remarks"] = remarks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        method_type_id = cast(Union[Literal[10], Unset], d.pop("method_type_id", UNSET))
        if method_type_id != 10 and not isinstance(method_type_id, Unset):
            raise ValueError(f"method_type_id must match const 10, got '{method_type_id}'")

        def _parse_depth_top(data: object) -> Union[None, Unset, float, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, str], data)

        depth_top = _parse_depth_top(d.pop("depth_top", UNSET))

        def _parse_maximum_measurement_torque(data: object) -> Union[None, Unset, float, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, str], data)

        maximum_measurement_torque = _parse_maximum_measurement_torque(d.pop("maximum_measurement_torque", UNSET))

        def _parse_maximum_measurement_torque_remoulded(data: object) -> Union[None, Unset, float, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, str], data)

        maximum_measurement_torque_remoulded = _parse_maximum_measurement_torque_remoulded(
            d.pop("maximum_measurement_torque_remoulded", UNSET)
        )

        def _parse_shear_strength(data: object) -> Union[None, Unset, float, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, str], data)

        shear_strength = _parse_shear_strength(d.pop("shear_strength", UNSET))

        def _parse_shear_strength_remoulded(data: object) -> Union[None, Unset, float, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, str], data)

        shear_strength_remoulded = _parse_shear_strength_remoulded(d.pop("shear_strength_remoulded", UNSET))

        def _parse_sensitivity(data: object) -> Union[None, Unset, float, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, str], data)

        sensitivity = _parse_sensitivity(d.pop("sensitivity", UNSET))

        def _parse_remarks(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        remarks = _parse_remarks(d.pop("remarks", UNSET))

        method_svt_data_update = cls(
            method_type_id=method_type_id,
            depth_top=depth_top,
            maximum_measurement_torque=maximum_measurement_torque,
            maximum_measurement_torque_remoulded=maximum_measurement_torque_remoulded,
            shear_strength=shear_strength,
            shear_strength_remoulded=shear_strength_remoulded,
            sensitivity=sensitivity,
            remarks=remarks,
        )

        method_svt_data_update.additional_properties = d
        return method_svt_data_update

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
