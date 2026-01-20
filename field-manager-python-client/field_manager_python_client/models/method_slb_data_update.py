from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MethodSLBDataUpdate")


@_attrs_define
class MethodSLBDataUpdate:
    """Method SLB data update structure

    Attributes:
        method_type_id (Literal[27] | Unset):  Default: 27.
        remarks (None | str | Unset):
    """

    method_type_id: Literal[27] | Unset = 27
    remarks: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        method_type_id = self.method_type_id

        remarks: None | str | Unset
        if isinstance(self.remarks, Unset):
            remarks = UNSET
        else:
            remarks = self.remarks

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if method_type_id is not UNSET:
            field_dict["method_type_id"] = method_type_id
        if remarks is not UNSET:
            field_dict["remarks"] = remarks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        method_type_id = cast(Literal[27] | Unset, d.pop("method_type_id", UNSET))
        if method_type_id != 27 and not isinstance(method_type_id, Unset):
            raise ValueError(f"method_type_id must match const 27, got '{method_type_id}'")

        def _parse_remarks(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remarks = _parse_remarks(d.pop("remarks", UNSET))

        method_slb_data_update = cls(
            method_type_id=method_type_id,
            remarks=remarks,
        )

        method_slb_data_update.additional_properties = d
        return method_slb_data_update

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
