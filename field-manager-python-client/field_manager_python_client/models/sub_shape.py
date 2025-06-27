from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SubShape")


@_attrs_define
class SubShape:
    """
    Attributes:
        shape_id (UUID):
        sub_shape_id (UUID):
        name (str):
        feature_id (Union[None, str]):
        feature_index (int):
        attached_file_ids (list[UUID]):
    """

    shape_id: UUID
    sub_shape_id: UUID
    name: str
    feature_id: Union[None, str]
    feature_index: int
    attached_file_ids: list[UUID]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        shape_id = str(self.shape_id)

        sub_shape_id = str(self.sub_shape_id)

        name = self.name

        feature_id: Union[None, str]
        feature_id = self.feature_id

        feature_index = self.feature_index

        attached_file_ids = []
        for attached_file_ids_item_data in self.attached_file_ids:
            attached_file_ids_item = str(attached_file_ids_item_data)
            attached_file_ids.append(attached_file_ids_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "shape_id": shape_id,
                "sub_shape_id": sub_shape_id,
                "name": name,
                "feature_id": feature_id,
                "feature_index": feature_index,
                "attached_file_ids": attached_file_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        shape_id = UUID(d.pop("shape_id"))

        sub_shape_id = UUID(d.pop("sub_shape_id"))

        name = d.pop("name")

        def _parse_feature_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        feature_id = _parse_feature_id(d.pop("feature_id"))

        feature_index = d.pop("feature_index")

        attached_file_ids = []
        _attached_file_ids = d.pop("attached_file_ids")
        for attached_file_ids_item_data in _attached_file_ids:
            attached_file_ids_item = UUID(attached_file_ids_item_data)

            attached_file_ids.append(attached_file_ids_item)

        sub_shape = cls(
            shape_id=shape_id,
            sub_shape_id=sub_shape_id,
            name=name,
            feature_id=feature_id,
            feature_index=feature_index,
            attached_file_ids=attached_file_ids,
        )

        sub_shape.additional_properties = d
        return sub_shape

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
