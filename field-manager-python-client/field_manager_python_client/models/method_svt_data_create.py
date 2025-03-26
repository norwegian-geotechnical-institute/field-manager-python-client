import datetime
from collections.abc import Mapping
from typing import Any, Literal, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="MethodSVTDataCreate")


@_attrs_define
class MethodSVTDataCreate:
    """
    Attributes:
        depth (Union[float, str]): Depth (m).
        method_data_id (Union[None, UUID, Unset]):
        method_id (Union[None, UUID, Unset]):
        method_type_id (Union[Literal[10], Unset]):  Default: 10.
        created_at (Union[None, Unset, datetime.datetime]):
        updated_at (Union[None, Unset, datetime.datetime]):
        maximum_measurement_torque (Union[None, Unset, float, str]): Maximum measurement torque (Nm).
        maximum_measurement_torque_remoulded (Union[None, Unset, float, str]): Maximum measurement torque (Nm).
        shear_strength (Union[None, Unset, float, str]): Shear strength (kPa). SGF code AS.
        shear_strength_remoulded (Union[None, Unset, float, str]): Shear strength (kPa).
        sensitivity (Union[None, Unset, float, str]): Sensitivity (unitless). SGF code SV.
        remarks (Union[None, Unset, str]):
    """

    depth: Union[float, str]
    method_data_id: Union[None, UUID, Unset] = UNSET
    method_id: Union[None, UUID, Unset] = UNSET
    method_type_id: Union[Literal[10], Unset] = 10
    created_at: Union[None, Unset, datetime.datetime] = UNSET
    updated_at: Union[None, Unset, datetime.datetime] = UNSET
    maximum_measurement_torque: Union[None, Unset, float, str] = UNSET
    maximum_measurement_torque_remoulded: Union[None, Unset, float, str] = UNSET
    shear_strength: Union[None, Unset, float, str] = UNSET
    shear_strength_remoulded: Union[None, Unset, float, str] = UNSET
    sensitivity: Union[None, Unset, float, str] = UNSET
    remarks: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        depth: Union[float, str]
        depth = self.depth

        method_data_id: Union[None, Unset, str]
        if isinstance(self.method_data_id, Unset):
            method_data_id = UNSET
        elif isinstance(self.method_data_id, UUID):
            method_data_id = str(self.method_data_id)
        else:
            method_data_id = self.method_data_id

        method_id: Union[None, Unset, str]
        if isinstance(self.method_id, Unset):
            method_id = UNSET
        elif isinstance(self.method_id, UUID):
            method_id = str(self.method_id)
        else:
            method_id = self.method_id

        method_type_id = self.method_type_id

        created_at: Union[None, Unset, str]
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        updated_at: Union[None, Unset, str]
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

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
        field_dict.update(
            {
                "depth": depth,
            }
        )
        if method_data_id is not UNSET:
            field_dict["method_data_id"] = method_data_id
        if method_id is not UNSET:
            field_dict["method_id"] = method_id
        if method_type_id is not UNSET:
            field_dict["method_type_id"] = method_type_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
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

        def _parse_depth(data: object) -> Union[float, str]:
            return cast(Union[float, str], data)

        depth = _parse_depth(d.pop("depth"))

        def _parse_method_data_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                method_data_id_type_0 = UUID(data)

                return method_data_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        method_data_id = _parse_method_data_id(d.pop("method_data_id", UNSET))

        def _parse_method_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                method_id_type_0 = UUID(data)

                return method_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        method_id = _parse_method_id(d.pop("method_id", UNSET))

        method_type_id = cast(Union[Literal[10], Unset], d.pop("method_type_id", UNSET))
        if method_type_id != 10 and not isinstance(method_type_id, Unset):
            raise ValueError(f"method_type_id must match const 10, got '{method_type_id}'")

        def _parse_created_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = isoparse(data)

                return created_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        created_at = _parse_created_at(d.pop("created_at", UNSET))

        def _parse_updated_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = isoparse(data)

                return updated_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))

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

        method_svt_data_create = cls(
            depth=depth,
            method_data_id=method_data_id,
            method_id=method_id,
            method_type_id=method_type_id,
            created_at=created_at,
            updated_at=updated_at,
            maximum_measurement_torque=maximum_measurement_torque,
            maximum_measurement_torque_remoulded=maximum_measurement_torque_remoulded,
            shear_strength=shear_strength,
            shear_strength_remoulded=shear_strength_remoulded,
            sensitivity=sensitivity,
            remarks=remarks,
        )

        method_svt_data_create.additional_properties = d
        return method_svt_data_create

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
