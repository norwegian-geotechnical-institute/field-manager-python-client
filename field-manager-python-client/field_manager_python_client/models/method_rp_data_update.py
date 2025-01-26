from typing import Any, Literal, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MethodRPDataUpdate")


@_attrs_define
class MethodRPDataUpdate:
    """Method RP data update structure

    Attributes:
        method_type_id (Union[Literal[3], Unset]):  Default: 3.
        comment_code (Union[None, Unset, int]):
        remarks (Union[None, Unset, str]):
    """

    method_type_id: Union[Literal[3], Unset] = 3
    comment_code: Union[None, Unset, int] = UNSET
    remarks: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        method_type_id = self.method_type_id

        comment_code: Union[None, Unset, int]
        if isinstance(self.comment_code, Unset):
            comment_code = UNSET
        else:
            comment_code = self.comment_code

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
        if comment_code is not UNSET:
            field_dict["comment_code"] = comment_code
        if remarks is not UNSET:
            field_dict["remarks"] = remarks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        method_type_id = cast(Union[Literal[3], Unset], d.pop("method_type_id", UNSET))
        if method_type_id != 3 and not isinstance(method_type_id, Unset):
            raise ValueError(f"method_type_id must match const 3, got '{method_type_id}'")

        def _parse_comment_code(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        comment_code = _parse_comment_code(d.pop("comment_code", UNSET))

        def _parse_remarks(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        remarks = _parse_remarks(d.pop("remarks", UNSET))

        method_rp_data_update = cls(
            method_type_id=method_type_id,
            comment_code=comment_code,
            remarks=remarks,
        )

        method_rp_data_update.additional_properties = d
        return method_rp_data_update

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
