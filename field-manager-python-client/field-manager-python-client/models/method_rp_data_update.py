from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.method_rp_data_update_method_type_id import MethodRPDataUpdateMethodTypeId
from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="MethodRPDataUpdate")


@_attrs_define
class MethodRPDataUpdate:
    """ Method RP data update structure

        Attributes:
            method_type_id (Union[Unset, MethodRPDataUpdateMethodTypeId]):  Default: MethodRPDataUpdateMethodTypeId.VALUE_3.
            comment_code (Union[None, Unset, int]):
            remarks (Union[None, Unset, str]):
     """

    method_type_id: Union[Unset, MethodRPDataUpdateMethodTypeId] = MethodRPDataUpdateMethodTypeId.VALUE_3
    comment_code: Union[None, Unset, int] = UNSET
    remarks: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        method_type_id: Union[Unset, int] = UNSET
        if not isinstance(self.method_type_id, Unset):
            method_type_id = self.method_type_id.value


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


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if method_type_id is not UNSET:
            field_dict["method_type_id"] = method_type_id
        if comment_code is not UNSET:
            field_dict["comment_code"] = comment_code
        if remarks is not UNSET:
            field_dict["remarks"] = remarks

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _method_type_id = d.pop("method_type_id", UNSET)
        method_type_id: Union[Unset, MethodRPDataUpdateMethodTypeId]
        if isinstance(_method_type_id,  Unset):
            method_type_id = UNSET
        else:
            method_type_id = MethodRPDataUpdateMethodTypeId(_method_type_id)




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
