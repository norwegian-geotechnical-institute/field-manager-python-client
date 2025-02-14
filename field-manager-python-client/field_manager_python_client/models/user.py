from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.role import Role


T = TypeVar("T", bound="User")


@_attrs_define
class User:
    """
    Attributes:
        user_id (Union[None, UUID, Unset]):
        name (Union[None, Unset, str]):
        email (Union[None, Unset, str]):
        roles (Union[Unset, list['Role']]):
        email_verified (Union[None, Unset, bool]):
    """

    user_id: Union[None, UUID, Unset] = UNSET
    name: Union[None, Unset, str] = UNSET
    email: Union[None, Unset, str] = UNSET
    roles: Union[Unset, list["Role"]] = UNSET
    email_verified: Union[None, Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_id: Union[None, Unset, str]
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        elif isinstance(self.user_id, UUID):
            user_id = str(self.user_id)
        else:
            user_id = self.user_id

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        email: Union[None, Unset, str]
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        roles: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.roles, Unset):
            roles = []
            for roles_item_data in self.roles:
                roles_item = roles_item_data.to_dict()
                roles.append(roles_item)

        email_verified: Union[None, Unset, bool]
        if isinstance(self.email_verified, Unset):
            email_verified = UNSET
        else:
            email_verified = self.email_verified

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if name is not UNSET:
            field_dict["name"] = name
        if email is not UNSET:
            field_dict["email"] = email
        if roles is not UNSET:
            field_dict["roles"] = roles
        if email_verified is not UNSET:
            field_dict["email_verified"] = email_verified

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.role import Role

        d = src_dict.copy()

        def _parse_user_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                user_id_type_0 = UUID(data)

                return user_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_email(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        email = _parse_email(d.pop("email", UNSET))

        roles = []
        _roles = d.pop("roles", UNSET)
        for roles_item_data in _roles or []:
            roles_item = Role.from_dict(roles_item_data)

            roles.append(roles_item)

        def _parse_email_verified(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        email_verified = _parse_email_verified(d.pop("email_verified", UNSET))

        user = cls(
            user_id=user_id,
            name=name,
            email=email,
            roles=roles,
            email_verified=email_verified,
        )

        user.additional_properties = d
        return user

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
