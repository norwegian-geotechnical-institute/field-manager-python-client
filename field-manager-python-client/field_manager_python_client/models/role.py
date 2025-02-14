from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.role_entity_enum import RoleEntityEnum
from ..models.role_enum import RoleEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="Role")


@_attrs_define
class Role:
    """
    Attributes:
        role_type (RoleEnum):
        role_entity_type (Union[None, RoleEntityEnum, Unset]):
        role_entity_id (Union[None, UUID, Unset]):
    """

    role_type: RoleEnum
    role_entity_type: Union[None, RoleEntityEnum, Unset] = UNSET
    role_entity_id: Union[None, UUID, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        role_type = self.role_type.value

        role_entity_type: Union[None, Unset, str]
        if isinstance(self.role_entity_type, Unset):
            role_entity_type = UNSET
        elif isinstance(self.role_entity_type, RoleEntityEnum):
            role_entity_type = self.role_entity_type.value
        else:
            role_entity_type = self.role_entity_type

        role_entity_id: Union[None, Unset, str]
        if isinstance(self.role_entity_id, Unset):
            role_entity_id = UNSET
        elif isinstance(self.role_entity_id, UUID):
            role_entity_id = str(self.role_entity_id)
        else:
            role_entity_id = self.role_entity_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "role_type": role_type,
            }
        )
        if role_entity_type is not UNSET:
            field_dict["role_entity_type"] = role_entity_type
        if role_entity_id is not UNSET:
            field_dict["role_entity_id"] = role_entity_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        role_type = RoleEnum(d.pop("role_type"))

        def _parse_role_entity_type(data: object) -> Union[None, RoleEntityEnum, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                role_entity_type_type_0 = RoleEntityEnum(data)

                return role_entity_type_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, RoleEntityEnum, Unset], data)

        role_entity_type = _parse_role_entity_type(d.pop("role_entity_type", UNSET))

        def _parse_role_entity_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                role_entity_id_type_0 = UUID(data)

                return role_entity_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        role_entity_id = _parse_role_entity_id(d.pop("role_entity_id", UNSET))

        role = cls(
            role_type=role_type,
            role_entity_type=role_entity_type,
            role_entity_id=role_entity_id,
        )

        role.additional_properties = d
        return role

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
