from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.method_rcd_data_update_method_type_id import MethodRCDDataUpdateMethodTypeId
from ..types import UNSET, Unset

T = TypeVar("T", bound="MethodRCDDataUpdate")


@_attrs_define
class MethodRCDDataUpdate:
    """
    Attributes:
        method_type_id (Union[Unset, MethodRCDDataUpdateMethodTypeId]):  Default:
            MethodRCDDataUpdateMethodTypeId.VALUE_8.
        depth (Union[None, Unset, float, str]):
        remarks (Union[None, Unset, str]):
        comment_code (Union[None, Unset, int]):
        penetration_rate (Union[None, Unset, float, str]):
    """

    method_type_id: Union[Unset, MethodRCDDataUpdateMethodTypeId] = MethodRCDDataUpdateMethodTypeId.VALUE_8
    depth: Union[None, Unset, float, str] = UNSET
    remarks: Union[None, Unset, str] = UNSET
    comment_code: Union[None, Unset, int] = UNSET
    penetration_rate: Union[None, Unset, float, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        method_type_id: Union[Unset, int] = UNSET
        if not isinstance(self.method_type_id, Unset):
            method_type_id = self.method_type_id.value

        depth: Union[None, Unset, float, str]
        if isinstance(self.depth, Unset):
            depth = UNSET
        else:
            depth = self.depth

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

        penetration_rate: Union[None, Unset, float, str]
        if isinstance(self.penetration_rate, Unset):
            penetration_rate = UNSET
        else:
            penetration_rate = self.penetration_rate

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if method_type_id is not UNSET:
            field_dict["method_type_id"] = method_type_id
        if depth is not UNSET:
            field_dict["depth"] = depth
        if remarks is not UNSET:
            field_dict["remarks"] = remarks
        if comment_code is not UNSET:
            field_dict["comment_code"] = comment_code
        if penetration_rate is not UNSET:
            field_dict["penetration_rate"] = penetration_rate

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _method_type_id = d.pop("method_type_id", UNSET)
        method_type_id: Union[Unset, MethodRCDDataUpdateMethodTypeId]
        if isinstance(_method_type_id, Unset):
            method_type_id = UNSET
        else:
            method_type_id = MethodRCDDataUpdateMethodTypeId(_method_type_id)

        def _parse_depth(data: object) -> Union[None, Unset, float, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, str], data)

        depth = _parse_depth(d.pop("depth", UNSET))

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

        def _parse_penetration_rate(data: object) -> Union[None, Unset, float, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, str], data)

        penetration_rate = _parse_penetration_rate(d.pop("penetration_rate", UNSET))

        method_rcd_data_update = cls(
            method_type_id=method_type_id,
            depth=depth,
            remarks=remarks,
            comment_code=comment_code,
            penetration_rate=penetration_rate,
        )

        method_rcd_data_update.additional_properties = d
        return method_rcd_data_update

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
