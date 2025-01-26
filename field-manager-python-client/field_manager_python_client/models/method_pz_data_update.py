import datetime
from typing import Any, Literal, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.reading_type import ReadingType
from ..types import UNSET, Unset

T = TypeVar("T", bound="MethodPZDataUpdate")


@_attrs_define
class MethodPZDataUpdate:
    """
    Attributes:
        method_type_id (Union[Literal[5], Unset]):  Default: 5.
        reading_type (Union[None, ReadingType, Unset]):
        date (Union[None, Unset, datetime.datetime]):
        pore_pressure (Union[None, Unset, float, str]):
        barometric_pressure (Union[None, Unset, float, str]):
        temperature (Union[None, Unset, float, str]):
        remarks (Union[None, Unset, str]):
    """

    method_type_id: Union[Literal[5], Unset] = 5
    reading_type: Union[None, ReadingType, Unset] = UNSET
    date: Union[None, Unset, datetime.datetime] = UNSET
    pore_pressure: Union[None, Unset, float, str] = UNSET
    barometric_pressure: Union[None, Unset, float, str] = UNSET
    temperature: Union[None, Unset, float, str] = UNSET
    remarks: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        method_type_id = self.method_type_id

        reading_type: Union[None, Unset, str]
        if isinstance(self.reading_type, Unset):
            reading_type = UNSET
        elif isinstance(self.reading_type, ReadingType):
            reading_type = self.reading_type.value
        else:
            reading_type = self.reading_type

        date: Union[None, Unset, str]
        if isinstance(self.date, Unset):
            date = UNSET
        elif isinstance(self.date, datetime.datetime):
            date = self.date.isoformat()
        else:
            date = self.date

        pore_pressure: Union[None, Unset, float, str]
        if isinstance(self.pore_pressure, Unset):
            pore_pressure = UNSET
        else:
            pore_pressure = self.pore_pressure

        barometric_pressure: Union[None, Unset, float, str]
        if isinstance(self.barometric_pressure, Unset):
            barometric_pressure = UNSET
        else:
            barometric_pressure = self.barometric_pressure

        temperature: Union[None, Unset, float, str]
        if isinstance(self.temperature, Unset):
            temperature = UNSET
        else:
            temperature = self.temperature

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
        if reading_type is not UNSET:
            field_dict["reading_type"] = reading_type
        if date is not UNSET:
            field_dict["date"] = date
        if pore_pressure is not UNSET:
            field_dict["pore_pressure"] = pore_pressure
        if barometric_pressure is not UNSET:
            field_dict["barometric_pressure"] = barometric_pressure
        if temperature is not UNSET:
            field_dict["temperature"] = temperature
        if remarks is not UNSET:
            field_dict["remarks"] = remarks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        method_type_id = cast(Union[Literal[5], Unset], d.pop("method_type_id", UNSET))
        if method_type_id != 5 and not isinstance(method_type_id, Unset):
            raise ValueError(f"method_type_id must match const 5, got '{method_type_id}'")

        def _parse_reading_type(data: object) -> Union[None, ReadingType, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reading_type_type_0 = ReadingType(data)

                return reading_type_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, ReadingType, Unset], data)

        reading_type = _parse_reading_type(d.pop("reading_type", UNSET))

        def _parse_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_type_0 = isoparse(data)

                return date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        date = _parse_date(d.pop("date", UNSET))

        def _parse_pore_pressure(data: object) -> Union[None, Unset, float, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, str], data)

        pore_pressure = _parse_pore_pressure(d.pop("pore_pressure", UNSET))

        def _parse_barometric_pressure(data: object) -> Union[None, Unset, float, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, str], data)

        barometric_pressure = _parse_barometric_pressure(d.pop("barometric_pressure", UNSET))

        def _parse_temperature(data: object) -> Union[None, Unset, float, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, str], data)

        temperature = _parse_temperature(d.pop("temperature", UNSET))

        def _parse_remarks(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        remarks = _parse_remarks(d.pop("remarks", UNSET))

        method_pz_data_update = cls(
            method_type_id=method_type_id,
            reading_type=reading_type,
            date=date,
            pore_pressure=pore_pressure,
            barometric_pressure=barometric_pressure,
            temperature=temperature,
            remarks=remarks,
        )

        method_pz_data_update.additional_properties = d
        return method_pz_data_update

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
