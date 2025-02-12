import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.method_pz_data_method_type_id import MethodPZDataMethodTypeId
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
        method_type_id (Union[Unset, MethodPZDataMethodTypeId]):  Default: MethodPZDataMethodTypeId.VALUE_5.
        pore_pressure (Union[None, Unset, float]):
        barometric_pressure (Union[None, Unset, float]):
        temperature (Union[None, Unset, float]):
        remarks (Union[None, Unset, str]):
        calculated_pore_pressure (Union[None, Unset, float]):
        calculated_piezometric_head (Union[None, Unset, float]):
        calculated_piezometric_potential_level (Union[None, Unset, float]):
    """

    method_data_id: UUID
    method_id: UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    reading_type: ReadingType
    date: datetime.datetime
    method_type_id: Union[Unset, MethodPZDataMethodTypeId] = MethodPZDataMethodTypeId.VALUE_5
    pore_pressure: Union[None, Unset, float] = UNSET
    barometric_pressure: Union[None, Unset, float] = UNSET
    temperature: Union[None, Unset, float] = UNSET
    remarks: Union[None, Unset, str] = UNSET
    calculated_pore_pressure: Union[None, Unset, float] = UNSET
    calculated_piezometric_head: Union[None, Unset, float] = UNSET
    calculated_piezometric_potential_level: Union[None, Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        method_data_id = str(self.method_data_id)

        method_id = str(self.method_id)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        reading_type = self.reading_type.value

        date = self.date.isoformat()

        method_type_id: Union[Unset, int] = UNSET
        if not isinstance(self.method_type_id, Unset):
            method_type_id = self.method_type_id.value

        pore_pressure: Union[None, Unset, float]
        if isinstance(self.pore_pressure, Unset):
            pore_pressure = UNSET
        else:
            pore_pressure = self.pore_pressure

        barometric_pressure: Union[None, Unset, float]
        if isinstance(self.barometric_pressure, Unset):
            barometric_pressure = UNSET
        else:
            barometric_pressure = self.barometric_pressure

        temperature: Union[None, Unset, float]
        if isinstance(self.temperature, Unset):
            temperature = UNSET
        else:
            temperature = self.temperature

        remarks: Union[None, Unset, str]
        if isinstance(self.remarks, Unset):
            remarks = UNSET
        else:
            remarks = self.remarks

        calculated_pore_pressure: Union[None, Unset, float]
        if isinstance(self.calculated_pore_pressure, Unset):
            calculated_pore_pressure = UNSET
        else:
            calculated_pore_pressure = self.calculated_pore_pressure

        calculated_piezometric_head: Union[None, Unset, float]
        if isinstance(self.calculated_piezometric_head, Unset):
            calculated_piezometric_head = UNSET
        else:
            calculated_piezometric_head = self.calculated_piezometric_head

        calculated_piezometric_potential_level: Union[None, Unset, float]
        if isinstance(self.calculated_piezometric_potential_level, Unset):
            calculated_piezometric_potential_level = UNSET
        else:
            calculated_piezometric_potential_level = self.calculated_piezometric_potential_level

        field_dict: Dict[str, Any] = {}
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
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        method_data_id = UUID(d.pop("method_data_id"))

        method_id = UUID(d.pop("method_id"))

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        reading_type = ReadingType(d.pop("reading_type"))

        date = isoparse(d.pop("date"))

        _method_type_id = d.pop("method_type_id", UNSET)
        method_type_id: Union[Unset, MethodPZDataMethodTypeId]
        if isinstance(_method_type_id, Unset):
            method_type_id = UNSET
        else:
            method_type_id = MethodPZDataMethodTypeId(_method_type_id)

        def _parse_pore_pressure(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        pore_pressure = _parse_pore_pressure(d.pop("pore_pressure", UNSET))

        def _parse_barometric_pressure(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        barometric_pressure = _parse_barometric_pressure(d.pop("barometric_pressure", UNSET))

        def _parse_temperature(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        temperature = _parse_temperature(d.pop("temperature", UNSET))

        def _parse_remarks(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        remarks = _parse_remarks(d.pop("remarks", UNSET))

        def _parse_calculated_pore_pressure(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        calculated_pore_pressure = _parse_calculated_pore_pressure(d.pop("calculated_pore_pressure", UNSET))

        def _parse_calculated_piezometric_head(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        calculated_piezometric_head = _parse_calculated_piezometric_head(d.pop("calculated_piezometric_head", UNSET))

        def _parse_calculated_piezometric_potential_level(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

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
