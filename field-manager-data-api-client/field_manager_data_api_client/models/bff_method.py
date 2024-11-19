from typing import Any, Dict, List, Type, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BFFMethod")


@_attrs_define
class BFFMethod:
    """
    Attributes:
        location_id (UUID):
        method_id (UUID):
        location_name (str):
        name (str):
    """

    location_id: UUID
    method_id: UUID
    location_name: str
    name: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        location_id = str(self.location_id)

        method_id = str(self.method_id)

        location_name = self.location_name

        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "location_id": location_id,
                "method_id": method_id,
                "location_name": location_name,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        location_id = UUID(d.pop("location_id"))

        method_id = UUID(d.pop("method_id"))

        location_name = d.pop("location_name")

        name = d.pop("name")

        bff_method = cls(
            location_id=location_id,
            method_id=method_id,
            location_name=location_name,
            name=name,
        )

        bff_method.additional_properties = d
        return bff_method

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
