import datetime
from collections.abc import Mapping
from typing import Any, Literal, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="MethodSVTData")


@_attrs_define
class MethodSVTData:
    """
    Attributes:
        method_data_id (UUID):
        method_id (UUID):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        depth (float): Depth (m). SGF code D.
        method_type_id (Union[Literal[10], Unset]):  Default: 10.
        maximum_measurement_torque (Union[None, Unset, float]): Maximum measurement torque (Nm). SGF code AB.
        maximum_measurement_torque_remoulded (Union[None, Unset, float]): Maximum measurement torque (Nm). SGF code AB2.
        shear_strength (Union[None, Unset, float]): Shear strength (kPa). SGF code AS.
        shear_strength_remoulded (Union[None, Unset, float]): Shear strength (kPa).
        sensitivity (Union[None, Unset, float]): Sensitivity (unitless). SGF code SV.
        calculated_shear_strength (Union[None, Unset, float]): Calculated shear strength (kPa).
        calculated_shear_strength_remoulded (Union[None, Unset, float]): Calculated shear strength (kPa).
        calculated_sensitivity (Union[None, Unset, float]): Calculated sensitivity (unitless).
        remarks (Union[None, Unset, str]):
    """

    method_data_id: UUID
    method_id: UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    depth: float
    method_type_id: Union[Literal[10], Unset] = 10
    maximum_measurement_torque: Union[None, Unset, float] = UNSET
    maximum_measurement_torque_remoulded: Union[None, Unset, float] = UNSET
    shear_strength: Union[None, Unset, float] = UNSET
    shear_strength_remoulded: Union[None, Unset, float] = UNSET
    sensitivity: Union[None, Unset, float] = UNSET
    calculated_shear_strength: Union[None, Unset, float] = UNSET
    calculated_shear_strength_remoulded: Union[None, Unset, float] = UNSET
    calculated_sensitivity: Union[None, Unset, float] = UNSET
    remarks: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        method_data_id = str(self.method_data_id)

        method_id = str(self.method_id)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        depth = self.depth

        method_type_id = self.method_type_id

        maximum_measurement_torque: Union[None, Unset, float]
        if isinstance(self.maximum_measurement_torque, Unset):
            maximum_measurement_torque = UNSET
        else:
            maximum_measurement_torque = self.maximum_measurement_torque

        maximum_measurement_torque_remoulded: Union[None, Unset, float]
        if isinstance(self.maximum_measurement_torque_remoulded, Unset):
            maximum_measurement_torque_remoulded = UNSET
        else:
            maximum_measurement_torque_remoulded = self.maximum_measurement_torque_remoulded

        shear_strength: Union[None, Unset, float]
        if isinstance(self.shear_strength, Unset):
            shear_strength = UNSET
        else:
            shear_strength = self.shear_strength

        shear_strength_remoulded: Union[None, Unset, float]
        if isinstance(self.shear_strength_remoulded, Unset):
            shear_strength_remoulded = UNSET
        else:
            shear_strength_remoulded = self.shear_strength_remoulded

        sensitivity: Union[None, Unset, float]
        if isinstance(self.sensitivity, Unset):
            sensitivity = UNSET
        else:
            sensitivity = self.sensitivity

        calculated_shear_strength: Union[None, Unset, float]
        if isinstance(self.calculated_shear_strength, Unset):
            calculated_shear_strength = UNSET
        else:
            calculated_shear_strength = self.calculated_shear_strength

        calculated_shear_strength_remoulded: Union[None, Unset, float]
        if isinstance(self.calculated_shear_strength_remoulded, Unset):
            calculated_shear_strength_remoulded = UNSET
        else:
            calculated_shear_strength_remoulded = self.calculated_shear_strength_remoulded

        calculated_sensitivity: Union[None, Unset, float]
        if isinstance(self.calculated_sensitivity, Unset):
            calculated_sensitivity = UNSET
        else:
            calculated_sensitivity = self.calculated_sensitivity

        remarks: Union[None, Unset, str]
        if isinstance(self.remarks, Unset):
            remarks = UNSET
        else:
            remarks = self.remarks

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
        if calculated_shear_strength is not UNSET:
            field_dict["calculated_shear_strength"] = calculated_shear_strength
        if calculated_shear_strength_remoulded is not UNSET:
            field_dict["calculated_shear_strength_remoulded"] = calculated_shear_strength_remoulded
        if calculated_sensitivity is not UNSET:
            field_dict["calculated_sensitivity"] = calculated_sensitivity
        if remarks is not UNSET:
            field_dict["remarks"] = remarks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        method_data_id = UUID(d.pop("method_data_id"))

        method_id = UUID(d.pop("method_id"))

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        depth = d.pop("depth")

        method_type_id = cast(Union[Literal[10], Unset], d.pop("method_type_id", UNSET))
        if method_type_id != 10 and not isinstance(method_type_id, Unset):
            raise ValueError(f"method_type_id must match const 10, got '{method_type_id}'")

        def _parse_maximum_measurement_torque(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        maximum_measurement_torque = _parse_maximum_measurement_torque(d.pop("maximum_measurement_torque", UNSET))

        def _parse_maximum_measurement_torque_remoulded(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        maximum_measurement_torque_remoulded = _parse_maximum_measurement_torque_remoulded(
            d.pop("maximum_measurement_torque_remoulded", UNSET)
        )

        def _parse_shear_strength(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        shear_strength = _parse_shear_strength(d.pop("shear_strength", UNSET))

        def _parse_shear_strength_remoulded(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        shear_strength_remoulded = _parse_shear_strength_remoulded(d.pop("shear_strength_remoulded", UNSET))

        def _parse_sensitivity(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        sensitivity = _parse_sensitivity(d.pop("sensitivity", UNSET))

        def _parse_calculated_shear_strength(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        calculated_shear_strength = _parse_calculated_shear_strength(d.pop("calculated_shear_strength", UNSET))

        def _parse_calculated_shear_strength_remoulded(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        calculated_shear_strength_remoulded = _parse_calculated_shear_strength_remoulded(
            d.pop("calculated_shear_strength_remoulded", UNSET)
        )

        def _parse_calculated_sensitivity(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        calculated_sensitivity = _parse_calculated_sensitivity(d.pop("calculated_sensitivity", UNSET))

        def _parse_remarks(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        remarks = _parse_remarks(d.pop("remarks", UNSET))

        method_svt_data = cls(
            method_data_id=method_data_id,
            method_id=method_id,
            created_at=created_at,
            updated_at=updated_at,
            depth=depth,
            method_type_id=method_type_id,
            maximum_measurement_torque=maximum_measurement_torque,
            maximum_measurement_torque_remoulded=maximum_measurement_torque_remoulded,
            shear_strength=shear_strength,
            shear_strength_remoulded=shear_strength_remoulded,
            sensitivity=sensitivity,
            calculated_shear_strength=calculated_shear_strength,
            calculated_shear_strength_remoulded=calculated_shear_strength_remoulded,
            calculated_sensitivity=calculated_sensitivity,
            remarks=remarks,
        )

        method_svt_data.additional_properties = d
        return method_svt_data

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
