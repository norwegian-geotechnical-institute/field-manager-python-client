from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.method_type_enum import MethodTypeEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_extension import FileExtension


T = TypeVar("T", bound="MethodType")


@_attrs_define
class MethodType:
    """
    Attributes:
        method_type_id (MethodTypeEnum): (
            CPT=1,
            TOT=2,
            RP=3,
            SA=4,
            PZ=5,
            SS=6,
            RWS=7,
            RCD=8,
            RS=9,
            SVT=10,
            SPT=11,
            CD=12,
            TP=13,
            PT=14,
            ESA=15,
            TR=16,
            AD=17,
            RO=18,
            INC=19,
            DEF=20,
            IW=21,
            DT=22,
            OTHER=23,
            SRS=24,
            DP=25,
            WST=26,
            SLB = 27,
            STI = 28,
            )
        name (str):
        description (str):
        category (str):
        sort_order (int):
        file_extensions (list['FileExtension']):
        raw_file_extensions (Union[Unset, list['FileExtension']]): Deprecated, use 'file_extensions' instead.
    """

    method_type_id: MethodTypeEnum
    name: str
    description: str
    category: str
    sort_order: int
    file_extensions: list["FileExtension"]
    raw_file_extensions: Union[Unset, list["FileExtension"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        method_type_id = self.method_type_id.value

        name = self.name

        description = self.description

        category = self.category

        sort_order = self.sort_order

        file_extensions = []
        for file_extensions_item_data in self.file_extensions:
            file_extensions_item = file_extensions_item_data.to_dict()
            file_extensions.append(file_extensions_item)

        raw_file_extensions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.raw_file_extensions, Unset):
            raw_file_extensions = []
            for raw_file_extensions_item_data in self.raw_file_extensions:
                raw_file_extensions_item = raw_file_extensions_item_data.to_dict()
                raw_file_extensions.append(raw_file_extensions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "method_type_id": method_type_id,
                "name": name,
                "description": description,
                "category": category,
                "sort_order": sort_order,
                "file_extensions": file_extensions,
            }
        )
        if raw_file_extensions is not UNSET:
            field_dict["raw_file_extensions"] = raw_file_extensions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.file_extension import FileExtension

        d = src_dict.copy()
        method_type_id = MethodTypeEnum(d.pop("method_type_id"))

        name = d.pop("name")

        description = d.pop("description")

        category = d.pop("category")

        sort_order = d.pop("sort_order")

        file_extensions = []
        _file_extensions = d.pop("file_extensions")
        for file_extensions_item_data in _file_extensions:
            file_extensions_item = FileExtension.from_dict(file_extensions_item_data)

            file_extensions.append(file_extensions_item)

        raw_file_extensions = []
        _raw_file_extensions = d.pop("raw_file_extensions", UNSET)
        for raw_file_extensions_item_data in _raw_file_extensions or []:
            raw_file_extensions_item = FileExtension.from_dict(raw_file_extensions_item_data)

            raw_file_extensions.append(raw_file_extensions_item)

        method_type = cls(
            method_type_id=method_type_id,
            name=name,
            description=description,
            category=category,
            sort_order=sort_order,
            file_extensions=file_extensions,
            raw_file_extensions=raw_file_extensions,
        )

        method_type.additional_properties = d
        return method_type

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
