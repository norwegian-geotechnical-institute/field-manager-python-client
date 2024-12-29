from typing import Any, Literal, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MethodDTDataUpdate")


@_attrs_define
class MethodDTDataUpdate:
    """Method DT data update structure

    Attributes:
        method_type_id (Union[Literal[22], Unset]):  Default: 22.
        depth (Union[None, Unset, float, str]):
        time (Union[None, Unset, float, str]):
        qc (Union[None, Unset, float, str]):
        u2 (Union[None, Unset, float, str]):
        remarks (Union[None, Unset, str]):
    """

    method_type_id: Union[Literal[22], Unset] = 22
    depth: Union[None, Unset, float, str] = UNSET
    time: Union[None, Unset, float, str] = UNSET
    qc: Union[None, Unset, float, str] = UNSET
    u2: Union[None, Unset, float, str] = UNSET
    remarks: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        method_type_id = self.method_type_id

        depth: Union[None, Unset, float, str]
        if isinstance(self.depth, Unset):
            depth = UNSET
        else:
            depth = self.depth

        time: Union[None, Unset, float, str]
        if isinstance(self.time, Unset):
            time = UNSET
        else:
            time = self.time

        qc: Union[None, Unset, float, str]
        if isinstance(self.qc, Unset):
            qc = UNSET
        else:
            qc = self.qc

        u2: Union[None, Unset, float, str]
        if isinstance(self.u2, Unset):
            u2 = UNSET
        else:
            u2 = self.u2

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
        if depth is not UNSET:
            field_dict["depth"] = depth
        if time is not UNSET:
            field_dict["time"] = time
        if qc is not UNSET:
            field_dict["qc"] = qc
        if u2 is not UNSET:
            field_dict["u2"] = u2
        if remarks is not UNSET:
            field_dict["remarks"] = remarks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        method_type_id = cast(Union[Literal[22], Unset], d.pop("method_type_id", UNSET))
        if method_type_id != 22 and not isinstance(method_type_id, Unset):
            raise ValueError(f"method_type_id must match const 22, got '{method_type_id}'")

        def _parse_depth(data: object) -> Union[None, Unset, float, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, str], data)

        depth = _parse_depth(d.pop("depth", UNSET))

        def _parse_time(data: object) -> Union[None, Unset, float, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, str], data)

        time = _parse_time(d.pop("time", UNSET))

        def _parse_qc(data: object) -> Union[None, Unset, float, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, str], data)

        qc = _parse_qc(d.pop("qc", UNSET))

        def _parse_u2(data: object) -> Union[None, Unset, float, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, str], data)

        u2 = _parse_u2(d.pop("u2", UNSET))

        def _parse_remarks(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        remarks = _parse_remarks(d.pop("remarks", UNSET))

        method_dt_data_update = cls(
            method_type_id=method_type_id,
            depth=depth,
            time=time,
            qc=qc,
            u2=u2,
            remarks=remarks,
        )

        method_dt_data_update.additional_properties = d
        return method_dt_data_update

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
