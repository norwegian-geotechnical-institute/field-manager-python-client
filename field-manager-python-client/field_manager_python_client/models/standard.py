from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.standard_type import StandardType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.method_type import MethodType


T = TypeVar("T", bound="Standard")


@_attrs_define
class Standard:
    """
    Attributes:
        standard_id (StandardType):
        name (str):
        description (str):
        sort_order (int):
        method_types (Union[Unset, list['MethodType']]):
    """

    standard_id: StandardType
    name: str
    description: str
    sort_order: int
    method_types: Union[Unset, list["MethodType"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        standard_id = self.standard_id.value

        name = self.name

        description = self.description

        sort_order = self.sort_order

        method_types: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.method_types, Unset):
            method_types = []
            for method_types_item_data in self.method_types:
                method_types_item = method_types_item_data.to_dict()
                method_types.append(method_types_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "standard_id": standard_id,
                "name": name,
                "description": description,
                "sort_order": sort_order,
            }
        )
        if method_types is not UNSET:
            field_dict["method_types"] = method_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.method_type import MethodType

        d = dict(src_dict)
        standard_id = StandardType(d.pop("standard_id"))

        name = d.pop("name")

        description = d.pop("description")

        sort_order = d.pop("sort_order")

        method_types = []
        _method_types = d.pop("method_types", UNSET)
        for method_types_item_data in _method_types or []:
            method_types_item = MethodType.from_dict(method_types_item_data)

            method_types.append(method_types_item)

        standard = cls(
            standard_id=standard_id,
            name=name,
            description=description,
            sort_order=sort_order,
            method_types=method_types,
        )

        standard.additional_properties = d
        return standard

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
