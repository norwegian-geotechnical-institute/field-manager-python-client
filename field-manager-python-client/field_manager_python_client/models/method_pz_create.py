import datetime
from typing import Any, Literal, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.method_status_enum import MethodStatusEnum
from ..models.piezometer_type import PiezometerType
from ..models.transformation_type import TransformationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="MethodPZCreate")


@_attrs_define
class MethodPZCreate:
    """
    Attributes:
        method_id (Union[None, UUID, Unset]):
        name (Union[None, Unset, str]):  Default: 'PZ'.
        remarks (Union[None, Unset, str]):
        method_status_id (Union[Unset, MethodStatusEnum]): (
            PLANNED=1,
            READY=2,
            CONDUCTED=3,
            VOIDED=4,
            APPROVED=5,
            )
        created_at (Union[None, Unset, datetime.datetime]):
        created_by (Union[None, Unset, str]):
        updated_at (Union[None, Unset, datetime.datetime]):
        updated_by (Union[None, Unset, str]):
        conducted_by (Union[None, Unset, str]):
        conducted_at (Union[None, Unset, datetime.datetime]):
        method_type_id (Union[Literal[5], Unset]):  Default: 5.
        piezometer_type (Union[None, PiezometerType, Unset]):  Default: PiezometerType.ELECTRIC.
        depth_top (Union[None, Unset, float, str]):
        depth_base (Union[None, Unset, float, str]):
        distance_over_terrain (Union[None, Unset, float, str]):
        model_id (Union[None, UUID, Unset]):
        serial_number (Union[None, Unset, str]):
        transformation_type (Union[Unset, TransformationType]): Piezometer Transformation Types
        mandatory_barometric_pressure (Union[None, Unset, bool]):  Default: False.
        mandatory_temperature (Union[None, Unset, bool]):  Default: False.
        pore_pressure_unit (Union[None, Unset, str]):
        default_barometric_pressure (Union[None, Unset, float, str]):
        polynomial_factor_a (Union[None, Unset, float, str]):
        polynomial_factor_b (Union[None, Unset, float, str]):
        polynomial_factor_k (Union[None, Unset, float, str]):
        zero_reading_pore_pressure (Union[None, Unset, float, str]):
        zero_reading_barometric_pressure (Union[None, Unset, float, str]):
        zero_reading_temperature (Union[None, Unset, float, str]):
    """

    method_id: Union[None, UUID, Unset] = UNSET
    name: Union[None, Unset, str] = "PZ"
    remarks: Union[None, Unset, str] = UNSET
    method_status_id: Union[Unset, MethodStatusEnum] = UNSET
    created_at: Union[None, Unset, datetime.datetime] = UNSET
    created_by: Union[None, Unset, str] = UNSET
    updated_at: Union[None, Unset, datetime.datetime] = UNSET
    updated_by: Union[None, Unset, str] = UNSET
    conducted_by: Union[None, Unset, str] = UNSET
    conducted_at: Union[None, Unset, datetime.datetime] = UNSET
    method_type_id: Union[Literal[5], Unset] = 5
    piezometer_type: Union[None, PiezometerType, Unset] = PiezometerType.ELECTRIC
    depth_top: Union[None, Unset, float, str] = UNSET
    depth_base: Union[None, Unset, float, str] = UNSET
    distance_over_terrain: Union[None, Unset, float, str] = UNSET
    model_id: Union[None, UUID, Unset] = UNSET
    serial_number: Union[None, Unset, str] = UNSET
    transformation_type: Union[Unset, TransformationType] = UNSET
    mandatory_barometric_pressure: Union[None, Unset, bool] = False
    mandatory_temperature: Union[None, Unset, bool] = False
    pore_pressure_unit: Union[None, Unset, str] = UNSET
    default_barometric_pressure: Union[None, Unset, float, str] = UNSET
    polynomial_factor_a: Union[None, Unset, float, str] = UNSET
    polynomial_factor_b: Union[None, Unset, float, str] = UNSET
    polynomial_factor_k: Union[None, Unset, float, str] = UNSET
    zero_reading_pore_pressure: Union[None, Unset, float, str] = UNSET
    zero_reading_barometric_pressure: Union[None, Unset, float, str] = UNSET
    zero_reading_temperature: Union[None, Unset, float, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        method_id: Union[None, Unset, str]
        if isinstance(self.method_id, Unset):
            method_id = UNSET
        elif isinstance(self.method_id, UUID):
            method_id = str(self.method_id)
        else:
            method_id = self.method_id

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        remarks: Union[None, Unset, str]
        if isinstance(self.remarks, Unset):
            remarks = UNSET
        else:
            remarks = self.remarks

        method_status_id: Union[Unset, int] = UNSET
        if not isinstance(self.method_status_id, Unset):
            method_status_id = self.method_status_id.value

        created_at: Union[None, Unset, str]
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        created_by: Union[None, Unset, str]
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        else:
            created_by = self.created_by

        updated_at: Union[None, Unset, str]
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        updated_by: Union[None, Unset, str]
        if isinstance(self.updated_by, Unset):
            updated_by = UNSET
        else:
            updated_by = self.updated_by

        conducted_by: Union[None, Unset, str]
        if isinstance(self.conducted_by, Unset):
            conducted_by = UNSET
        else:
            conducted_by = self.conducted_by

        conducted_at: Union[None, Unset, str]
        if isinstance(self.conducted_at, Unset):
            conducted_at = UNSET
        elif isinstance(self.conducted_at, datetime.datetime):
            conducted_at = self.conducted_at.isoformat()
        else:
            conducted_at = self.conducted_at

        method_type_id = self.method_type_id

        piezometer_type: Union[None, Unset, str]
        if isinstance(self.piezometer_type, Unset):
            piezometer_type = UNSET
        elif isinstance(self.piezometer_type, PiezometerType):
            piezometer_type = self.piezometer_type.value
        else:
            piezometer_type = self.piezometer_type

        depth_top: Union[None, Unset, float, str]
        if isinstance(self.depth_top, Unset):
            depth_top = UNSET
        else:
            depth_top = self.depth_top

        depth_base: Union[None, Unset, float, str]
        if isinstance(self.depth_base, Unset):
            depth_base = UNSET
        else:
            depth_base = self.depth_base

        distance_over_terrain: Union[None, Unset, float, str]
        if isinstance(self.distance_over_terrain, Unset):
            distance_over_terrain = UNSET
        else:
            distance_over_terrain = self.distance_over_terrain

        model_id: Union[None, Unset, str]
        if isinstance(self.model_id, Unset):
            model_id = UNSET
        elif isinstance(self.model_id, UUID):
            model_id = str(self.model_id)
        else:
            model_id = self.model_id

        serial_number: Union[None, Unset, str]
        if isinstance(self.serial_number, Unset):
            serial_number = UNSET
        else:
            serial_number = self.serial_number

        transformation_type: Union[Unset, str] = UNSET
        if not isinstance(self.transformation_type, Unset):
            transformation_type = self.transformation_type.value

        mandatory_barometric_pressure: Union[None, Unset, bool]
        if isinstance(self.mandatory_barometric_pressure, Unset):
            mandatory_barometric_pressure = UNSET
        else:
            mandatory_barometric_pressure = self.mandatory_barometric_pressure

        mandatory_temperature: Union[None, Unset, bool]
        if isinstance(self.mandatory_temperature, Unset):
            mandatory_temperature = UNSET
        else:
            mandatory_temperature = self.mandatory_temperature

        pore_pressure_unit: Union[None, Unset, str]
        if isinstance(self.pore_pressure_unit, Unset):
            pore_pressure_unit = UNSET
        else:
            pore_pressure_unit = self.pore_pressure_unit

        default_barometric_pressure: Union[None, Unset, float, str]
        if isinstance(self.default_barometric_pressure, Unset):
            default_barometric_pressure = UNSET
        else:
            default_barometric_pressure = self.default_barometric_pressure

        polynomial_factor_a: Union[None, Unset, float, str]
        if isinstance(self.polynomial_factor_a, Unset):
            polynomial_factor_a = UNSET
        else:
            polynomial_factor_a = self.polynomial_factor_a

        polynomial_factor_b: Union[None, Unset, float, str]
        if isinstance(self.polynomial_factor_b, Unset):
            polynomial_factor_b = UNSET
        else:
            polynomial_factor_b = self.polynomial_factor_b

        polynomial_factor_k: Union[None, Unset, float, str]
        if isinstance(self.polynomial_factor_k, Unset):
            polynomial_factor_k = UNSET
        else:
            polynomial_factor_k = self.polynomial_factor_k

        zero_reading_pore_pressure: Union[None, Unset, float, str]
        if isinstance(self.zero_reading_pore_pressure, Unset):
            zero_reading_pore_pressure = UNSET
        else:
            zero_reading_pore_pressure = self.zero_reading_pore_pressure

        zero_reading_barometric_pressure: Union[None, Unset, float, str]
        if isinstance(self.zero_reading_barometric_pressure, Unset):
            zero_reading_barometric_pressure = UNSET
        else:
            zero_reading_barometric_pressure = self.zero_reading_barometric_pressure

        zero_reading_temperature: Union[None, Unset, float, str]
        if isinstance(self.zero_reading_temperature, Unset):
            zero_reading_temperature = UNSET
        else:
            zero_reading_temperature = self.zero_reading_temperature

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if method_id is not UNSET:
            field_dict["method_id"] = method_id
        if name is not UNSET:
            field_dict["name"] = name
        if remarks is not UNSET:
            field_dict["remarks"] = remarks
        if method_status_id is not UNSET:
            field_dict["method_status_id"] = method_status_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if updated_by is not UNSET:
            field_dict["updated_by"] = updated_by
        if conducted_by is not UNSET:
            field_dict["conducted_by"] = conducted_by
        if conducted_at is not UNSET:
            field_dict["conducted_at"] = conducted_at
        if method_type_id is not UNSET:
            field_dict["method_type_id"] = method_type_id
        if piezometer_type is not UNSET:
            field_dict["piezometer_type"] = piezometer_type
        if depth_top is not UNSET:
            field_dict["depth_top"] = depth_top
        if depth_base is not UNSET:
            field_dict["depth_base"] = depth_base
        if distance_over_terrain is not UNSET:
            field_dict["distance_over_terrain"] = distance_over_terrain
        if model_id is not UNSET:
            field_dict["model_id"] = model_id
        if serial_number is not UNSET:
            field_dict["serial_number"] = serial_number
        if transformation_type is not UNSET:
            field_dict["transformation_type"] = transformation_type
        if mandatory_barometric_pressure is not UNSET:
            field_dict["mandatory_barometric_pressure"] = mandatory_barometric_pressure
        if mandatory_temperature is not UNSET:
            field_dict["mandatory_temperature"] = mandatory_temperature
        if pore_pressure_unit is not UNSET:
            field_dict["pore_pressure_unit"] = pore_pressure_unit
        if default_barometric_pressure is not UNSET:
            field_dict["default_barometric_pressure"] = default_barometric_pressure
        if polynomial_factor_a is not UNSET:
            field_dict["polynomial_factor_a"] = polynomial_factor_a
        if polynomial_factor_b is not UNSET:
            field_dict["polynomial_factor_b"] = polynomial_factor_b
        if polynomial_factor_k is not UNSET:
            field_dict["polynomial_factor_k"] = polynomial_factor_k
        if zero_reading_pore_pressure is not UNSET:
            field_dict["zero_reading_pore_pressure"] = zero_reading_pore_pressure
        if zero_reading_barometric_pressure is not UNSET:
            field_dict["zero_reading_barometric_pressure"] = zero_reading_barometric_pressure
        if zero_reading_temperature is not UNSET:
            field_dict["zero_reading_temperature"] = zero_reading_temperature

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()

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

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_remarks(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        remarks = _parse_remarks(d.pop("remarks", UNSET))

        _method_status_id = d.pop("method_status_id", UNSET)
        method_status_id: Union[Unset, MethodStatusEnum]
        if isinstance(_method_status_id, Unset):
            method_status_id = UNSET
        else:
            method_status_id = MethodStatusEnum(_method_status_id)

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

        def _parse_created_by(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        created_by = _parse_created_by(d.pop("created_by", UNSET))

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

        def _parse_updated_by(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        updated_by = _parse_updated_by(d.pop("updated_by", UNSET))

        def _parse_conducted_by(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        conducted_by = _parse_conducted_by(d.pop("conducted_by", UNSET))

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

        method_type_id = cast(Union[Literal[5], Unset], d.pop("method_type_id", UNSET))
        if method_type_id != 5 and not isinstance(method_type_id, Unset):
            raise ValueError(f"method_type_id must match const 5, got '{method_type_id}'")

        def _parse_piezometer_type(data: object) -> Union[None, PiezometerType, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                piezometer_type_type_0 = PiezometerType(data)

                return piezometer_type_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, PiezometerType, Unset], data)

        piezometer_type = _parse_piezometer_type(d.pop("piezometer_type", UNSET))

        def _parse_depth_top(data: object) -> Union[None, Unset, float, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, str], data)

        depth_top = _parse_depth_top(d.pop("depth_top", UNSET))

        def _parse_depth_base(data: object) -> Union[None, Unset, float, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, str], data)

        depth_base = _parse_depth_base(d.pop("depth_base", UNSET))

        def _parse_distance_over_terrain(data: object) -> Union[None, Unset, float, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, str], data)

        distance_over_terrain = _parse_distance_over_terrain(d.pop("distance_over_terrain", UNSET))

        def _parse_model_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                model_id_type_0 = UUID(data)

                return model_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        model_id = _parse_model_id(d.pop("model_id", UNSET))

        def _parse_serial_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        serial_number = _parse_serial_number(d.pop("serial_number", UNSET))

        _transformation_type = d.pop("transformation_type", UNSET)
        transformation_type: Union[Unset, TransformationType]
        if isinstance(_transformation_type, Unset):
            transformation_type = UNSET
        else:
            transformation_type = TransformationType(_transformation_type)

        def _parse_mandatory_barometric_pressure(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        mandatory_barometric_pressure = _parse_mandatory_barometric_pressure(
            d.pop("mandatory_barometric_pressure", UNSET)
        )

        def _parse_mandatory_temperature(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        mandatory_temperature = _parse_mandatory_temperature(d.pop("mandatory_temperature", UNSET))

        def _parse_pore_pressure_unit(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        pore_pressure_unit = _parse_pore_pressure_unit(d.pop("pore_pressure_unit", UNSET))

        def _parse_default_barometric_pressure(data: object) -> Union[None, Unset, float, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, str], data)

        default_barometric_pressure = _parse_default_barometric_pressure(d.pop("default_barometric_pressure", UNSET))

        def _parse_polynomial_factor_a(data: object) -> Union[None, Unset, float, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, str], data)

        polynomial_factor_a = _parse_polynomial_factor_a(d.pop("polynomial_factor_a", UNSET))

        def _parse_polynomial_factor_b(data: object) -> Union[None, Unset, float, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, str], data)

        polynomial_factor_b = _parse_polynomial_factor_b(d.pop("polynomial_factor_b", UNSET))

        def _parse_polynomial_factor_k(data: object) -> Union[None, Unset, float, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, str], data)

        polynomial_factor_k = _parse_polynomial_factor_k(d.pop("polynomial_factor_k", UNSET))

        def _parse_zero_reading_pore_pressure(data: object) -> Union[None, Unset, float, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, str], data)

        zero_reading_pore_pressure = _parse_zero_reading_pore_pressure(d.pop("zero_reading_pore_pressure", UNSET))

        def _parse_zero_reading_barometric_pressure(data: object) -> Union[None, Unset, float, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, str], data)

        zero_reading_barometric_pressure = _parse_zero_reading_barometric_pressure(
            d.pop("zero_reading_barometric_pressure", UNSET)
        )

        def _parse_zero_reading_temperature(data: object) -> Union[None, Unset, float, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, str], data)

        zero_reading_temperature = _parse_zero_reading_temperature(d.pop("zero_reading_temperature", UNSET))

        method_pz_create = cls(
            method_id=method_id,
            name=name,
            remarks=remarks,
            method_status_id=method_status_id,
            created_at=created_at,
            created_by=created_by,
            updated_at=updated_at,
            updated_by=updated_by,
            conducted_by=conducted_by,
            conducted_at=conducted_at,
            method_type_id=method_type_id,
            piezometer_type=piezometer_type,
            depth_top=depth_top,
            depth_base=depth_base,
            distance_over_terrain=distance_over_terrain,
            model_id=model_id,
            serial_number=serial_number,
            transformation_type=transformation_type,
            mandatory_barometric_pressure=mandatory_barometric_pressure,
            mandatory_temperature=mandatory_temperature,
            pore_pressure_unit=pore_pressure_unit,
            default_barometric_pressure=default_barometric_pressure,
            polynomial_factor_a=polynomial_factor_a,
            polynomial_factor_b=polynomial_factor_b,
            polynomial_factor_k=polynomial_factor_k,
            zero_reading_pore_pressure=zero_reading_pore_pressure,
            zero_reading_barometric_pressure=zero_reading_barometric_pressure,
            zero_reading_temperature=zero_reading_temperature,
        )

        method_pz_create.additional_properties = d
        return method_pz_create

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
