from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.project_role_enum import ProjectRoleEnum
from ..models.role_enum import RoleEnum
from ..models.standard_type import StandardType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.role import Role


T = TypeVar("T", bound="Organization")


@_attrs_define
class Organization:
    """
    Attributes:
        organization_id (UUID):
        name (str):
        number_of_projects (int):
        default_role (RoleEnum):
        can_approve_method (list[ProjectRoleEnum]):
        can_revoke_method_approval (list[ProjectRoleEnum]):
        external_id (None | str | Unset):
        short_name (None | str | Unset):
        email_domains (None | str | Unset):
        authentication_alias (None | str | Unset):
        authentication_issuer (None | str | Unset):
        created_at (datetime.datetime | None | Unset):
        updated_at (datetime.datetime | None | Unset):
        effective_role (None | Role | Unset):
        default_standard_id (None | StandardType | Unset):
        available_standard_ids (list[StandardType] | Unset):
    """

    organization_id: UUID
    name: str
    number_of_projects: int
    default_role: RoleEnum
    can_approve_method: list[ProjectRoleEnum]
    can_revoke_method_approval: list[ProjectRoleEnum]
    external_id: None | str | Unset = UNSET
    short_name: None | str | Unset = UNSET
    email_domains: None | str | Unset = UNSET
    authentication_alias: None | str | Unset = UNSET
    authentication_issuer: None | str | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    effective_role: None | Role | Unset = UNSET
    default_standard_id: None | StandardType | Unset = UNSET
    available_standard_ids: list[StandardType] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.role import Role

        organization_id = str(self.organization_id)

        name = self.name

        number_of_projects = self.number_of_projects

        default_role = self.default_role.value

        can_approve_method = []
        for can_approve_method_item_data in self.can_approve_method:
            can_approve_method_item = can_approve_method_item_data.value
            can_approve_method.append(can_approve_method_item)

        can_revoke_method_approval = []
        for can_revoke_method_approval_item_data in self.can_revoke_method_approval:
            can_revoke_method_approval_item = can_revoke_method_approval_item_data.value
            can_revoke_method_approval.append(can_revoke_method_approval_item)

        external_id: None | str | Unset
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        short_name: None | str | Unset
        if isinstance(self.short_name, Unset):
            short_name = UNSET
        else:
            short_name = self.short_name

        email_domains: None | str | Unset
        if isinstance(self.email_domains, Unset):
            email_domains = UNSET
        else:
            email_domains = self.email_domains

        authentication_alias: None | str | Unset
        if isinstance(self.authentication_alias, Unset):
            authentication_alias = UNSET
        else:
            authentication_alias = self.authentication_alias

        authentication_issuer: None | str | Unset
        if isinstance(self.authentication_issuer, Unset):
            authentication_issuer = UNSET
        else:
            authentication_issuer = self.authentication_issuer

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        effective_role: dict[str, Any] | None | Unset
        if isinstance(self.effective_role, Unset):
            effective_role = UNSET
        elif isinstance(self.effective_role, Role):
            effective_role = self.effective_role.to_dict()
        else:
            effective_role = self.effective_role

        default_standard_id: None | str | Unset
        if isinstance(self.default_standard_id, Unset):
            default_standard_id = UNSET
        elif isinstance(self.default_standard_id, StandardType):
            default_standard_id = self.default_standard_id.value
        else:
            default_standard_id = self.default_standard_id

        available_standard_ids: list[str] | Unset = UNSET
        if not isinstance(self.available_standard_ids, Unset):
            available_standard_ids = []
            for available_standard_ids_item_data in self.available_standard_ids:
                available_standard_ids_item = available_standard_ids_item_data.value
                available_standard_ids.append(available_standard_ids_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "organization_id": organization_id,
                "name": name,
                "number_of_projects": number_of_projects,
                "default_role": default_role,
                "can_approve_method": can_approve_method,
                "can_revoke_method_approval": can_revoke_method_approval,
            }
        )
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if short_name is not UNSET:
            field_dict["short_name"] = short_name
        if email_domains is not UNSET:
            field_dict["email_domains"] = email_domains
        if authentication_alias is not UNSET:
            field_dict["authentication_alias"] = authentication_alias
        if authentication_issuer is not UNSET:
            field_dict["authentication_issuer"] = authentication_issuer
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if effective_role is not UNSET:
            field_dict["effective_role"] = effective_role
        if default_standard_id is not UNSET:
            field_dict["default_standard_id"] = default_standard_id
        if available_standard_ids is not UNSET:
            field_dict["available_standard_ids"] = available_standard_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.role import Role

        d = dict(src_dict)
        organization_id = UUID(d.pop("organization_id"))

        name = d.pop("name")

        number_of_projects = d.pop("number_of_projects")

        default_role = RoleEnum(d.pop("default_role"))

        can_approve_method = []
        _can_approve_method = d.pop("can_approve_method")
        for can_approve_method_item_data in _can_approve_method:
            can_approve_method_item = ProjectRoleEnum(can_approve_method_item_data)

            can_approve_method.append(can_approve_method_item)

        can_revoke_method_approval = []
        _can_revoke_method_approval = d.pop("can_revoke_method_approval")
        for can_revoke_method_approval_item_data in _can_revoke_method_approval:
            can_revoke_method_approval_item = ProjectRoleEnum(can_revoke_method_approval_item_data)

            can_revoke_method_approval.append(can_revoke_method_approval_item)

        def _parse_external_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_id = _parse_external_id(d.pop("external_id", UNSET))

        def _parse_short_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        short_name = _parse_short_name(d.pop("short_name", UNSET))

        def _parse_email_domains(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email_domains = _parse_email_domains(d.pop("email_domains", UNSET))

        def _parse_authentication_alias(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        authentication_alias = _parse_authentication_alias(d.pop("authentication_alias", UNSET))

        def _parse_authentication_issuer(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        authentication_issuer = _parse_authentication_issuer(d.pop("authentication_issuer", UNSET))

        def _parse_created_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = isoparse(data)

                return created_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        created_at = _parse_created_at(d.pop("created_at", UNSET))

        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = isoparse(data)

                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))

        def _parse_effective_role(data: object) -> None | Role | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                effective_role_type_0 = Role.from_dict(data)

                return effective_role_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Role | Unset, data)

        effective_role = _parse_effective_role(d.pop("effective_role", UNSET))

        def _parse_default_standard_id(data: object) -> None | StandardType | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                default_standard_id_type_0 = StandardType(data)

                return default_standard_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | StandardType | Unset, data)

        default_standard_id = _parse_default_standard_id(d.pop("default_standard_id", UNSET))

        _available_standard_ids = d.pop("available_standard_ids", UNSET)
        available_standard_ids: list[StandardType] | Unset = UNSET
        if _available_standard_ids is not UNSET:
            available_standard_ids = []
            for available_standard_ids_item_data in _available_standard_ids:
                available_standard_ids_item = StandardType(available_standard_ids_item_data)

                available_standard_ids.append(available_standard_ids_item)

        organization = cls(
            organization_id=organization_id,
            name=name,
            number_of_projects=number_of_projects,
            default_role=default_role,
            can_approve_method=can_approve_method,
            can_revoke_method_approval=can_revoke_method_approval,
            external_id=external_id,
            short_name=short_name,
            email_domains=email_domains,
            authentication_alias=authentication_alias,
            authentication_issuer=authentication_issuer,
            created_at=created_at,
            updated_at=updated_at,
            effective_role=effective_role,
            default_standard_id=default_standard_id,
            available_standard_ids=available_standard_ids,
        )

        organization.additional_properties = d
        return organization

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
