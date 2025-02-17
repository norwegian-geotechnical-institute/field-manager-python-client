from typing import Any, Literal, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MethodSSDataUpdate")


@_attrs_define
class MethodSSDataUpdate:
    """Method SS data update structure

    Attributes:
        method_type_id (Union[Literal[6], Unset]):  Default: 6.
        depth_top (Union[None, Unset, float, str]): Depth top (m).
        depth_base (Union[None, Unset, float, str]): Depth base (m).
        time (Union[None, Unset, float, str]):
        remarks (Union[None, Unset, str]):
        comment_code (Union[None, Unset, int]):
    """

    method_type_id: Union[Literal[6], Unset] = 6
    depth_top: Union[None, Unset, float, str] = UNSET
    depth_base: Union[None, Unset, float, str] = UNSET
    time: Union[None, Unset, float, str] = UNSET
    remarks: Union[None, Unset, str] = UNSET
    comment_code: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        method_type_id = self.method_type_id

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

        time: Union[None, Unset, float, str]
        if isinstance(self.time, Unset):
            time = UNSET
        else:
            time = self.time

        remarks: Union[None, Unset, str]
        if isinstance(self.remarks, Unset):
            remarks = UNSET
        else:
            remarks = self.remarks

        comment_code: Union[None, Unset, int]
        if isinstance(self.comment_code, Unset):
            comment_code = UNSET
        else:
            comment_code = self.comment_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if method_type_id is not UNSET:
            field_dict["method_type_id"] = method_type_id
        if depth_top is not UNSET:
            field_dict["depth_top"] = depth_top
        if depth_base is not UNSET:
            field_dict["depth_base"] = depth_base
        if time is not UNSET:
            field_dict["time"] = time
        if remarks is not UNSET:
            field_dict["remarks"] = remarks
        if comment_code is not UNSET:
            field_dict["comment_code"] = comment_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        method_type_id = cast(Union[Literal[6], Unset], d.pop("method_type_id", UNSET))
        if method_type_id != 6 and not isinstance(method_type_id, Unset):
            raise ValueError(f"method_type_id must match const 6, got '{method_type_id}'")

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

        def _parse_time(data: object) -> Union[None, Unset, float, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, str], data)

        time = _parse_time(d.pop("time", UNSET))

        def _parse_remarks(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        remarks = _parse_remarks(d.pop("remarks", UNSET))

        def _parse_comment_code(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        comment_code = _parse_comment_code(d.pop("comment_code", UNSET))

        method_ss_data_update = cls(
            method_type_id=method_type_id,
            depth_top=depth_top,
            depth_base=depth_base,
            time=time,
            remarks=remarks,
            comment_code=comment_code,
        )

        method_ss_data_update.additional_properties = d
        return method_ss_data_update

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
