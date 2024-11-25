from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.method_ss_data_update_method_type_id import MethodSSDataUpdateMethodTypeId
from ..types import UNSET, Unset

T = TypeVar("T", bound="MethodSSDataUpdate")


@_attrs_define
class MethodSSDataUpdate:
    """Method SS data update structure

    Attributes:
        method_type_id (Union[Unset, MethodSSDataUpdateMethodTypeId]):  Default: MethodSSDataUpdateMethodTypeId.VALUE_6.
        depth_top (Union[None, Unset, float, str]): Depth top (m).
        depth_base (Union[None, Unset, float, str]): Depth base (m).
        time (Union[None, Unset, float, str]):
        remarks (Union[None, Unset, str]):
        comment_code (Union[None, Unset, int]):
    """

    method_type_id: Union[Unset, MethodSSDataUpdateMethodTypeId] = MethodSSDataUpdateMethodTypeId.VALUE_6
    depth_top: Union[None, Unset, float, str] = UNSET
    depth_base: Union[None, Unset, float, str] = UNSET
    time: Union[None, Unset, float, str] = UNSET
    remarks: Union[None, Unset, str] = UNSET
    comment_code: Union[None, Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        method_type_id: Union[Unset, int] = UNSET
        if not isinstance(self.method_type_id, Unset):
            method_type_id = self.method_type_id.value

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

        field_dict: Dict[str, Any] = {}
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
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _method_type_id = d.pop("method_type_id", UNSET)
        method_type_id: Union[Unset, MethodSSDataUpdateMethodTypeId]
        if isinstance(_method_type_id, Unset):
            method_type_id = UNSET
        else:
            method_type_id = MethodSSDataUpdateMethodTypeId(_method_type_id)

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
