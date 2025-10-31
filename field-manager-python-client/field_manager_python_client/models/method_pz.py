from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.method_status_enum import MethodStatusEnum
from ..models.piezometer_type import PiezometerType
from ..models.transformation_type import TransformationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file import File


T = TypeVar("T", bound="MethodPZ")


@_attrs_define
class MethodPZ:
    """PZ

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
        piezometer_type (PiezometerType): (
            ELECTRIC = Piezometer Electric,
            HYDRAULIC = Piezometer Hydraulic,
            STANDPIPE = Piezometer Standpipe,
            )
        transformation_type (TransformationType): Piezometer Transformation Types
        mandatory_barometric_pressure (bool):
        mandatory_temperature (bool):
        remarks (None | str | Unset):
        method_type_id (Literal[5] | Unset):  Default: 5.
        created_by (None | str | Unset):
        updated_by (None | str | Unset):
        conducted_at (datetime.datetime | None | Unset):
        conducted_by (None | str | Unset):
        files (list[File] | Unset):
        self_ (None | str | Unset):
        depth_top (float | None | Unset):
        depth_base (float | None | Unset):
        distance_over_terrain (float | None | Unset):
        model_id (None | Unset | UUID):
        pore_pressure_unit (None | str | Unset):
        serial_number (None | str | Unset):
        default_barometric_pressure (float | None | Unset):
        polynomial_factor_a (float | None | Unset):
        polynomial_factor_b (float | None | Unset):
        polynomial_factor_k (float | None | Unset):
        polynomial_factor_a_unit (None | str | Unset):
        polynomial_factor_b_unit (None | str | Unset):
        polynomial_factor_k_unit (None | str | Unset):
        zero_reading_pore_pressure (float | None | Unset):
        zero_reading_barometric_pressure (float | None | Unset):
        zero_reading_temperature (float | None | Unset):
        missing_variables_pore_pressure (list[str] | None | Unset): Missing variables to calculate pore pressure.
        missing_variables_piezometric_head (list[str] | None | Unset): Missing variables to calculate piezometric head.
        missing_variables_piezometric_potential (list[str] | None | Unset): Missing variables to calculate piezometric
            potential.
    """

    method_id: UUID
    name: str
    location_id: UUID
    method_status_id: MethodStatusEnum
    created_at: datetime.datetime
    updated_at: datetime.datetime
    piezometer_type: PiezometerType
    transformation_type: TransformationType
    mandatory_barometric_pressure: bool
    mandatory_temperature: bool
    remarks: None | str | Unset = UNSET
    method_type_id: Literal[5] | Unset = 5
    created_by: None | str | Unset = UNSET
    updated_by: None | str | Unset = UNSET
    conducted_at: datetime.datetime | None | Unset = UNSET
    conducted_by: None | str | Unset = UNSET
    files: list[File] | Unset = UNSET
    self_: None | str | Unset = UNSET
    depth_top: float | None | Unset = UNSET
    depth_base: float | None | Unset = UNSET
    distance_over_terrain: float | None | Unset = UNSET
    model_id: None | Unset | UUID = UNSET
    pore_pressure_unit: None | str | Unset = UNSET
    serial_number: None | str | Unset = UNSET
    default_barometric_pressure: float | None | Unset = UNSET
    polynomial_factor_a: float | None | Unset = UNSET
    polynomial_factor_b: float | None | Unset = UNSET
    polynomial_factor_k: float | None | Unset = UNSET
    polynomial_factor_a_unit: None | str | Unset = UNSET
    polynomial_factor_b_unit: None | str | Unset = UNSET
    polynomial_factor_k_unit: None | str | Unset = UNSET
    zero_reading_pore_pressure: float | None | Unset = UNSET
    zero_reading_barometric_pressure: float | None | Unset = UNSET
    zero_reading_temperature: float | None | Unset = UNSET
    missing_variables_pore_pressure: list[str] | None | Unset = UNSET
    missing_variables_piezometric_head: list[str] | None | Unset = UNSET
    missing_variables_piezometric_potential: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        method_id = str(self.method_id)

        name = self.name

        location_id = str(self.location_id)

        method_status_id = self.method_status_id.value

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        piezometer_type = self.piezometer_type.value

        transformation_type = self.transformation_type.value

        mandatory_barometric_pressure = self.mandatory_barometric_pressure

        mandatory_temperature = self.mandatory_temperature

        remarks: None | str | Unset
        if isinstance(self.remarks, Unset):
            remarks = UNSET
        else:
            remarks = self.remarks

        method_type_id = self.method_type_id

        created_by: None | str | Unset
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        else:
            created_by = self.created_by

        updated_by: None | str | Unset
        if isinstance(self.updated_by, Unset):
            updated_by = UNSET
        else:
            updated_by = self.updated_by

        conducted_at: None | str | Unset
        if isinstance(self.conducted_at, Unset):
            conducted_at = UNSET
        elif isinstance(self.conducted_at, datetime.datetime):
            conducted_at = self.conducted_at.isoformat()
        else:
            conducted_at = self.conducted_at

        conducted_by: None | str | Unset
        if isinstance(self.conducted_by, Unset):
            conducted_by = UNSET
        else:
            conducted_by = self.conducted_by

        files: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = []
            for files_item_data in self.files:
                files_item = files_item_data.to_dict()
                files.append(files_item)

        self_: None | str | Unset
        if isinstance(self.self_, Unset):
            self_ = UNSET
        else:
            self_ = self.self_

        depth_top: float | None | Unset
        if isinstance(self.depth_top, Unset):
            depth_top = UNSET
        else:
            depth_top = self.depth_top

        depth_base: float | None | Unset
        if isinstance(self.depth_base, Unset):
            depth_base = UNSET
        else:
            depth_base = self.depth_base

        distance_over_terrain: float | None | Unset
        if isinstance(self.distance_over_terrain, Unset):
            distance_over_terrain = UNSET
        else:
            distance_over_terrain = self.distance_over_terrain

        model_id: None | str | Unset
        if isinstance(self.model_id, Unset):
            model_id = UNSET
        elif isinstance(self.model_id, UUID):
            model_id = str(self.model_id)
        else:
            model_id = self.model_id

        pore_pressure_unit: None | str | Unset
        if isinstance(self.pore_pressure_unit, Unset):
            pore_pressure_unit = UNSET
        else:
            pore_pressure_unit = self.pore_pressure_unit

        serial_number: None | str | Unset
        if isinstance(self.serial_number, Unset):
            serial_number = UNSET
        else:
            serial_number = self.serial_number

        default_barometric_pressure: float | None | Unset
        if isinstance(self.default_barometric_pressure, Unset):
            default_barometric_pressure = UNSET
        else:
            default_barometric_pressure = self.default_barometric_pressure

        polynomial_factor_a: float | None | Unset
        if isinstance(self.polynomial_factor_a, Unset):
            polynomial_factor_a = UNSET
        else:
            polynomial_factor_a = self.polynomial_factor_a

        polynomial_factor_b: float | None | Unset
        if isinstance(self.polynomial_factor_b, Unset):
            polynomial_factor_b = UNSET
        else:
            polynomial_factor_b = self.polynomial_factor_b

        polynomial_factor_k: float | None | Unset
        if isinstance(self.polynomial_factor_k, Unset):
            polynomial_factor_k = UNSET
        else:
            polynomial_factor_k = self.polynomial_factor_k

        polynomial_factor_a_unit: None | str | Unset
        if isinstance(self.polynomial_factor_a_unit, Unset):
            polynomial_factor_a_unit = UNSET
        else:
            polynomial_factor_a_unit = self.polynomial_factor_a_unit

        polynomial_factor_b_unit: None | str | Unset
        if isinstance(self.polynomial_factor_b_unit, Unset):
            polynomial_factor_b_unit = UNSET
        else:
            polynomial_factor_b_unit = self.polynomial_factor_b_unit

        polynomial_factor_k_unit: None | str | Unset
        if isinstance(self.polynomial_factor_k_unit, Unset):
            polynomial_factor_k_unit = UNSET
        else:
            polynomial_factor_k_unit = self.polynomial_factor_k_unit

        zero_reading_pore_pressure: float | None | Unset
        if isinstance(self.zero_reading_pore_pressure, Unset):
            zero_reading_pore_pressure = UNSET
        else:
            zero_reading_pore_pressure = self.zero_reading_pore_pressure

        zero_reading_barometric_pressure: float | None | Unset
        if isinstance(self.zero_reading_barometric_pressure, Unset):
            zero_reading_barometric_pressure = UNSET
        else:
            zero_reading_barometric_pressure = self.zero_reading_barometric_pressure

        zero_reading_temperature: float | None | Unset
        if isinstance(self.zero_reading_temperature, Unset):
            zero_reading_temperature = UNSET
        else:
            zero_reading_temperature = self.zero_reading_temperature

        missing_variables_pore_pressure: list[str] | None | Unset
        if isinstance(self.missing_variables_pore_pressure, Unset):
            missing_variables_pore_pressure = UNSET
        elif isinstance(self.missing_variables_pore_pressure, list):
            missing_variables_pore_pressure = self.missing_variables_pore_pressure

        else:
            missing_variables_pore_pressure = self.missing_variables_pore_pressure

        missing_variables_piezometric_head: list[str] | None | Unset
        if isinstance(self.missing_variables_piezometric_head, Unset):
            missing_variables_piezometric_head = UNSET
        elif isinstance(self.missing_variables_piezometric_head, list):
            missing_variables_piezometric_head = self.missing_variables_piezometric_head

        else:
            missing_variables_piezometric_head = self.missing_variables_piezometric_head

        missing_variables_piezometric_potential: list[str] | None | Unset
        if isinstance(self.missing_variables_piezometric_potential, Unset):
            missing_variables_piezometric_potential = UNSET
        elif isinstance(self.missing_variables_piezometric_potential, list):
            missing_variables_piezometric_potential = self.missing_variables_piezometric_potential

        else:
            missing_variables_piezometric_potential = self.missing_variables_piezometric_potential

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "method_id": method_id,
                "name": name,
                "location_id": location_id,
                "method_status_id": method_status_id,
                "created_at": created_at,
                "updated_at": updated_at,
                "piezometer_type": piezometer_type,
                "transformation_type": transformation_type,
                "mandatory_barometric_pressure": mandatory_barometric_pressure,
                "mandatory_temperature": mandatory_temperature,
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
        if depth_top is not UNSET:
            field_dict["depth_top"] = depth_top
        if depth_base is not UNSET:
            field_dict["depth_base"] = depth_base
        if distance_over_terrain is not UNSET:
            field_dict["distance_over_terrain"] = distance_over_terrain
        if model_id is not UNSET:
            field_dict["model_id"] = model_id
        if pore_pressure_unit is not UNSET:
            field_dict["pore_pressure_unit"] = pore_pressure_unit
        if serial_number is not UNSET:
            field_dict["serial_number"] = serial_number
        if default_barometric_pressure is not UNSET:
            field_dict["default_barometric_pressure"] = default_barometric_pressure
        if polynomial_factor_a is not UNSET:
            field_dict["polynomial_factor_a"] = polynomial_factor_a
        if polynomial_factor_b is not UNSET:
            field_dict["polynomial_factor_b"] = polynomial_factor_b
        if polynomial_factor_k is not UNSET:
            field_dict["polynomial_factor_k"] = polynomial_factor_k
        if polynomial_factor_a_unit is not UNSET:
            field_dict["polynomial_factor_a_unit"] = polynomial_factor_a_unit
        if polynomial_factor_b_unit is not UNSET:
            field_dict["polynomial_factor_b_unit"] = polynomial_factor_b_unit
        if polynomial_factor_k_unit is not UNSET:
            field_dict["polynomial_factor_k_unit"] = polynomial_factor_k_unit
        if zero_reading_pore_pressure is not UNSET:
            field_dict["zero_reading_pore_pressure"] = zero_reading_pore_pressure
        if zero_reading_barometric_pressure is not UNSET:
            field_dict["zero_reading_barometric_pressure"] = zero_reading_barometric_pressure
        if zero_reading_temperature is not UNSET:
            field_dict["zero_reading_temperature"] = zero_reading_temperature
        if missing_variables_pore_pressure is not UNSET:
            field_dict["missing_variables_pore_pressure"] = missing_variables_pore_pressure
        if missing_variables_piezometric_head is not UNSET:
            field_dict["missing_variables_piezometric_head"] = missing_variables_piezometric_head
        if missing_variables_piezometric_potential is not UNSET:
            field_dict["missing_variables_piezometric_potential"] = missing_variables_piezometric_potential

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file import File

        d = dict(src_dict)
        method_id = UUID(d.pop("method_id"))

        name = d.pop("name")

        location_id = UUID(d.pop("location_id"))

        method_status_id = MethodStatusEnum(d.pop("method_status_id"))

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        piezometer_type = PiezometerType(d.pop("piezometer_type"))

        transformation_type = TransformationType(d.pop("transformation_type"))

        mandatory_barometric_pressure = d.pop("mandatory_barometric_pressure")

        mandatory_temperature = d.pop("mandatory_temperature")

        def _parse_remarks(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remarks = _parse_remarks(d.pop("remarks", UNSET))

        method_type_id = cast(Literal[5] | Unset, d.pop("method_type_id", UNSET))
        if method_type_id != 5 and not isinstance(method_type_id, Unset):
            raise ValueError(f"method_type_id must match const 5, got '{method_type_id}'")

        def _parse_created_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_by = _parse_created_by(d.pop("created_by", UNSET))

        def _parse_updated_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        updated_by = _parse_updated_by(d.pop("updated_by", UNSET))

        def _parse_conducted_at(data: object) -> datetime.datetime | None | Unset:
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
            return cast(datetime.datetime | None | Unset, data)

        conducted_at = _parse_conducted_at(d.pop("conducted_at", UNSET))

        def _parse_conducted_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        conducted_by = _parse_conducted_by(d.pop("conducted_by", UNSET))

        files = []
        _files = d.pop("files", UNSET)
        for files_item_data in _files or []:
            files_item = File.from_dict(files_item_data)

            files.append(files_item)

        def _parse_self_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        self_ = _parse_self_(d.pop("self", UNSET))

        def _parse_depth_top(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        depth_top = _parse_depth_top(d.pop("depth_top", UNSET))

        def _parse_depth_base(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        depth_base = _parse_depth_base(d.pop("depth_base", UNSET))

        def _parse_distance_over_terrain(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        distance_over_terrain = _parse_distance_over_terrain(d.pop("distance_over_terrain", UNSET))

        def _parse_model_id(data: object) -> None | Unset | UUID:
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
            return cast(None | Unset | UUID, data)

        model_id = _parse_model_id(d.pop("model_id", UNSET))

        def _parse_pore_pressure_unit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pore_pressure_unit = _parse_pore_pressure_unit(d.pop("pore_pressure_unit", UNSET))

        def _parse_serial_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        serial_number = _parse_serial_number(d.pop("serial_number", UNSET))

        def _parse_default_barometric_pressure(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        default_barometric_pressure = _parse_default_barometric_pressure(d.pop("default_barometric_pressure", UNSET))

        def _parse_polynomial_factor_a(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        polynomial_factor_a = _parse_polynomial_factor_a(d.pop("polynomial_factor_a", UNSET))

        def _parse_polynomial_factor_b(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        polynomial_factor_b = _parse_polynomial_factor_b(d.pop("polynomial_factor_b", UNSET))

        def _parse_polynomial_factor_k(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        polynomial_factor_k = _parse_polynomial_factor_k(d.pop("polynomial_factor_k", UNSET))

        def _parse_polynomial_factor_a_unit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        polynomial_factor_a_unit = _parse_polynomial_factor_a_unit(d.pop("polynomial_factor_a_unit", UNSET))

        def _parse_polynomial_factor_b_unit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        polynomial_factor_b_unit = _parse_polynomial_factor_b_unit(d.pop("polynomial_factor_b_unit", UNSET))

        def _parse_polynomial_factor_k_unit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        polynomial_factor_k_unit = _parse_polynomial_factor_k_unit(d.pop("polynomial_factor_k_unit", UNSET))

        def _parse_zero_reading_pore_pressure(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        zero_reading_pore_pressure = _parse_zero_reading_pore_pressure(d.pop("zero_reading_pore_pressure", UNSET))

        def _parse_zero_reading_barometric_pressure(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        zero_reading_barometric_pressure = _parse_zero_reading_barometric_pressure(
            d.pop("zero_reading_barometric_pressure", UNSET)
        )

        def _parse_zero_reading_temperature(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        zero_reading_temperature = _parse_zero_reading_temperature(d.pop("zero_reading_temperature", UNSET))

        def _parse_missing_variables_pore_pressure(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                missing_variables_pore_pressure_type_0 = cast(list[str], data)

                return missing_variables_pore_pressure_type_0
            except:  # noqa: E722
                pass
            return cast(list[str] | None | Unset, data)

        missing_variables_pore_pressure = _parse_missing_variables_pore_pressure(
            d.pop("missing_variables_pore_pressure", UNSET)
        )

        def _parse_missing_variables_piezometric_head(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                missing_variables_piezometric_head_type_0 = cast(list[str], data)

                return missing_variables_piezometric_head_type_0
            except:  # noqa: E722
                pass
            return cast(list[str] | None | Unset, data)

        missing_variables_piezometric_head = _parse_missing_variables_piezometric_head(
            d.pop("missing_variables_piezometric_head", UNSET)
        )

        def _parse_missing_variables_piezometric_potential(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                missing_variables_piezometric_potential_type_0 = cast(list[str], data)

                return missing_variables_piezometric_potential_type_0
            except:  # noqa: E722
                pass
            return cast(list[str] | None | Unset, data)

        missing_variables_piezometric_potential = _parse_missing_variables_piezometric_potential(
            d.pop("missing_variables_piezometric_potential", UNSET)
        )

        method_pz = cls(
            method_id=method_id,
            name=name,
            location_id=location_id,
            method_status_id=method_status_id,
            created_at=created_at,
            updated_at=updated_at,
            piezometer_type=piezometer_type,
            transformation_type=transformation_type,
            mandatory_barometric_pressure=mandatory_barometric_pressure,
            mandatory_temperature=mandatory_temperature,
            remarks=remarks,
            method_type_id=method_type_id,
            created_by=created_by,
            updated_by=updated_by,
            conducted_at=conducted_at,
            conducted_by=conducted_by,
            files=files,
            self_=self_,
            depth_top=depth_top,
            depth_base=depth_base,
            distance_over_terrain=distance_over_terrain,
            model_id=model_id,
            pore_pressure_unit=pore_pressure_unit,
            serial_number=serial_number,
            default_barometric_pressure=default_barometric_pressure,
            polynomial_factor_a=polynomial_factor_a,
            polynomial_factor_b=polynomial_factor_b,
            polynomial_factor_k=polynomial_factor_k,
            polynomial_factor_a_unit=polynomial_factor_a_unit,
            polynomial_factor_b_unit=polynomial_factor_b_unit,
            polynomial_factor_k_unit=polynomial_factor_k_unit,
            zero_reading_pore_pressure=zero_reading_pore_pressure,
            zero_reading_barometric_pressure=zero_reading_barometric_pressure,
            zero_reading_temperature=zero_reading_temperature,
            missing_variables_pore_pressure=missing_variables_pore_pressure,
            missing_variables_piezometric_head=missing_variables_piezometric_head,
            missing_variables_piezometric_potential=missing_variables_piezometric_potential,
        )

        method_pz.additional_properties = d
        return method_pz

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
