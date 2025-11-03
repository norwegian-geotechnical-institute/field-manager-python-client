from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.reading_type import ReadingType
from ..types import UNSET, Unset

T = TypeVar("T", bound="MethodPZData")


@_attrs_define
class MethodPZData:
    """
    Attributes:
        method_data_id (UUID):
        method_id (UUID):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        reading_type (ReadingType):
        date (datetime.datetime):
        method_type_id (Literal[5] | Unset):  Default: 5.
        pore_pressure (float | None | Unset):
        barometric_pressure (float | None | Unset):
        temperature (float | None | Unset):
        remarks (None | str | Unset):
        calculated_pore_pressure (float | None | Unset):
        calculated_piezometric_head (float | None | Unset):
        calculated_piezometric_potential_level (float | None | Unset):
    """

    method_data_id: UUID
    method_id: UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    reading_type: ReadingType
    date: datetime.datetime
    method_type_id: Literal[5] | Unset = 5
    pore_pressure: float | None | Unset = UNSET
    barometric_pressure: float | None | Unset = UNSET
    temperature: float | None | Unset = UNSET
    remarks: None | str | Unset = UNSET
    calculated_pore_pressure: float | None | Unset = UNSET
    calculated_piezometric_head: float | None | Unset = UNSET
    calculated_piezometric_potential_level: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        method_data_id = str(self.method_data_id)

        method_id = str(self.method_id)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        reading_type = self.reading_type.value

        date = self.date.isoformat()

        method_type_id = self.method_type_id

        pore_pressure: float | None | Unset
        if isinstance(self.pore_pressure, Unset):
            pore_pressure = UNSET
        else:
            pore_pressure = self.pore_pressure

        barometric_pressure: float | None | Unset
        if isinstance(self.barometric_pressure, Unset):
            barometric_pressure = UNSET
        else:
            barometric_pressure = self.barometric_pressure

        temperature: float | None | Unset
        if isinstance(self.temperature, Unset):
            temperature = UNSET
        else:
            temperature = self.temperature

        remarks: None | str | Unset
        if isinstance(self.remarks, Unset):
            remarks = UNSET
        else:
            remarks = self.remarks

        calculated_pore_pressure: float | None | Unset
        if isinstance(self.calculated_pore_pressure, Unset):
            calculated_pore_pressure = UNSET
        else:
            calculated_pore_pressure = self.calculated_pore_pressure

        calculated_piezometric_head: float | None | Unset
        if isinstance(self.calculated_piezometric_head, Unset):
            calculated_piezometric_head = UNSET
        else:
            calculated_piezometric_head = self.calculated_piezometric_head

        calculated_piezometric_potential_level: float | None | Unset
        if isinstance(self.calculated_piezometric_potential_level, Unset):
            calculated_piezometric_potential_level = UNSET
        else:
            calculated_piezometric_potential_level = self.calculated_piezometric_potential_level

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "method_data_id": method_data_id,
                "method_id": method_id,
                "created_at": created_at,
                "updated_at": updated_at,
                "reading_type": reading_type,
                "date": date,
            }
        )
        if method_type_id is not UNSET:
            field_dict["method_type_id"] = method_type_id
        if pore_pressure is not UNSET:
            field_dict["pore_pressure"] = pore_pressure
        if barometric_pressure is not UNSET:
            field_dict["barometric_pressure"] = barometric_pressure
        if temperature is not UNSET:
            field_dict["temperature"] = temperature
        if remarks is not UNSET:
            field_dict["remarks"] = remarks
        if calculated_pore_pressure is not UNSET:
            field_dict["calculated_pore_pressure"] = calculated_pore_pressure
        if calculated_piezometric_head is not UNSET:
            field_dict["calculated_piezometric_head"] = calculated_piezometric_head
        if calculated_piezometric_potential_level is not UNSET:
            field_dict["calculated_piezometric_potential_level"] = calculated_piezometric_potential_level

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        method_data_id = UUID(d.pop("method_data_id"))

        method_id = UUID(d.pop("method_id"))

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        reading_type = ReadingType(d.pop("reading_type"))

        date = isoparse(d.pop("date"))

        method_type_id = cast(Literal[5] | Unset, d.pop("method_type_id", UNSET))
        if method_type_id != 5 and not isinstance(method_type_id, Unset):
            raise ValueError(f"method_type_id must match const 5, got '{method_type_id}'")

        def _parse_pore_pressure(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pore_pressure = _parse_pore_pressure(d.pop("pore_pressure", UNSET))

        def _parse_barometric_pressure(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        barometric_pressure = _parse_barometric_pressure(d.pop("barometric_pressure", UNSET))

        def _parse_temperature(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        temperature = _parse_temperature(d.pop("temperature", UNSET))

        def _parse_remarks(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remarks = _parse_remarks(d.pop("remarks", UNSET))

        def _parse_calculated_pore_pressure(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        calculated_pore_pressure = _parse_calculated_pore_pressure(d.pop("calculated_pore_pressure", UNSET))

        def _parse_calculated_piezometric_head(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        calculated_piezometric_head = _parse_calculated_piezometric_head(d.pop("calculated_piezometric_head", UNSET))

        def _parse_calculated_piezometric_potential_level(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        calculated_piezometric_potential_level = _parse_calculated_piezometric_potential_level(
            d.pop("calculated_piezometric_potential_level", UNSET)
        )

        method_pz_data = cls(
            method_data_id=method_data_id,
            method_id=method_id,
            created_at=created_at,
            updated_at=updated_at,
            reading_type=reading_type,
            date=date,
            method_type_id=method_type_id,
            pore_pressure=pore_pressure,
            barometric_pressure=barometric_pressure,
            temperature=temperature,
            remarks=remarks,
            calculated_pore_pressure=calculated_pore_pressure,
            calculated_piezometric_head=calculated_piezometric_head,
            calculated_piezometric_potential_level=calculated_piezometric_potential_level,
        )

        method_pz_data.additional_properties = d
        return method_pz_data

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
