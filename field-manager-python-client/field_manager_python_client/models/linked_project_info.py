from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.height_reference import HeightReference
from ..models.standard_type import StandardType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.organization_min import OrganizationMin
    from ..models.role import Role


T = TypeVar("T", bound="LinkedProjectInfo")


@_attrs_define
class LinkedProjectInfo:
    """
    Example:
        {'external_id': '2020193232', 'height_reference': 'NN2000', 'name': 'Project Name', 'organization_id':
            'fff31299-1f3d-48e3-ad70-8c9c37370900', 'project_id': 'e66a377d-3816-4cf8-ad79-d954a3ba632d', 'srid': 3857}

    Attributes:
        project_id (UUID):
        external_id (str):
        organization_id (UUID):
        name (str):
        standard_id (StandardType):
        srid (int):
        number_of_locations (int):
        created_at (datetime.datetime | None | Unset):
        updated_at (datetime.datetime | None | Unset):
        external_id_source (None | str | Unset):
        height_reference (HeightReference | None | Unset):
        description (None | str | Unset):
        tags (list[str] | None | Unset):
        client (None | str | Unset): NADAG client/oppdragsgiver
        contractor (None | str | Unset): NADAG contractor/oppdragstaker
        sync_with_nadag (bool | None | Unset): This project should sync with NADAG
        organization (None | OrganizationMin | Unset):
        effective_role (None | Role | Unset):
        last_updated (datetime.datetime | None | Unset):
        favorite (bool | Unset):  Default: False.
        linked_project_prefix (None | str | Unset):
    """

    project_id: UUID
    external_id: str
    organization_id: UUID
    name: str
    standard_id: StandardType
    srid: int
    number_of_locations: int
    created_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    external_id_source: None | str | Unset = UNSET
    height_reference: HeightReference | None | Unset = UNSET
    description: None | str | Unset = UNSET
    tags: list[str] | None | Unset = UNSET
    client: None | str | Unset = UNSET
    contractor: None | str | Unset = UNSET
    sync_with_nadag: bool | None | Unset = UNSET
    organization: None | OrganizationMin | Unset = UNSET
    effective_role: None | Role | Unset = UNSET
    last_updated: datetime.datetime | None | Unset = UNSET
    favorite: bool | Unset = False
    linked_project_prefix: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.organization_min import OrganizationMin
        from ..models.role import Role

        project_id = str(self.project_id)

        external_id = self.external_id

        organization_id = str(self.organization_id)

        name = self.name

        standard_id = self.standard_id.value

        srid = self.srid

        number_of_locations = self.number_of_locations

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

        external_id_source: None | str | Unset
        if isinstance(self.external_id_source, Unset):
            external_id_source = UNSET
        else:
            external_id_source = self.external_id_source

        height_reference: None | str | Unset
        if isinstance(self.height_reference, Unset):
            height_reference = UNSET
        elif isinstance(self.height_reference, HeightReference):
            height_reference = self.height_reference.value
        else:
            height_reference = self.height_reference

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        tags: list[str] | None | Unset
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        client: None | str | Unset
        if isinstance(self.client, Unset):
            client = UNSET
        else:
            client = self.client

        contractor: None | str | Unset
        if isinstance(self.contractor, Unset):
            contractor = UNSET
        else:
            contractor = self.contractor

        sync_with_nadag: bool | None | Unset
        if isinstance(self.sync_with_nadag, Unset):
            sync_with_nadag = UNSET
        else:
            sync_with_nadag = self.sync_with_nadag

        organization: dict[str, Any] | None | Unset
        if isinstance(self.organization, Unset):
            organization = UNSET
        elif isinstance(self.organization, OrganizationMin):
            organization = self.organization.to_dict()
        else:
            organization = self.organization

        effective_role: dict[str, Any] | None | Unset
        if isinstance(self.effective_role, Unset):
            effective_role = UNSET
        elif isinstance(self.effective_role, Role):
            effective_role = self.effective_role.to_dict()
        else:
            effective_role = self.effective_role

        last_updated: None | str | Unset
        if isinstance(self.last_updated, Unset):
            last_updated = UNSET
        elif isinstance(self.last_updated, datetime.datetime):
            last_updated = self.last_updated.isoformat()
        else:
            last_updated = self.last_updated

        favorite = self.favorite

        linked_project_prefix: None | str | Unset
        if isinstance(self.linked_project_prefix, Unset):
            linked_project_prefix = UNSET
        else:
            linked_project_prefix = self.linked_project_prefix

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "project_id": project_id,
                "external_id": external_id,
                "organization_id": organization_id,
                "name": name,
                "standard_id": standard_id,
                "srid": srid,
                "number_of_locations": number_of_locations,
            }
        )
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if external_id_source is not UNSET:
            field_dict["external_id_source"] = external_id_source
        if height_reference is not UNSET:
            field_dict["height_reference"] = height_reference
        if description is not UNSET:
            field_dict["description"] = description
        if tags is not UNSET:
            field_dict["tags"] = tags
        if client is not UNSET:
            field_dict["client"] = client
        if contractor is not UNSET:
            field_dict["contractor"] = contractor
        if sync_with_nadag is not UNSET:
            field_dict["sync_with_nadag"] = sync_with_nadag
        if organization is not UNSET:
            field_dict["organization"] = organization
        if effective_role is not UNSET:
            field_dict["effective_role"] = effective_role
        if last_updated is not UNSET:
            field_dict["last_updated"] = last_updated
        if favorite is not UNSET:
            field_dict["favorite"] = favorite
        if linked_project_prefix is not UNSET:
            field_dict["linked_project_prefix"] = linked_project_prefix

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.organization_min import OrganizationMin
        from ..models.role import Role

        d = dict(src_dict)
        project_id = UUID(d.pop("project_id"))

        external_id = d.pop("external_id")

        organization_id = UUID(d.pop("organization_id"))

        name = d.pop("name")

        standard_id = StandardType(d.pop("standard_id"))

        srid = d.pop("srid")

        number_of_locations = d.pop("number_of_locations")

        def _parse_created_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = datetime.datetime.fromisoformat(data)

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
                updated_at_type_0 = datetime.datetime.fromisoformat(data)

                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))

        def _parse_external_id_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_id_source = _parse_external_id_source(d.pop("external_id_source", UNSET))

        def _parse_height_reference(data: object) -> HeightReference | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                height_reference_type_0 = HeightReference(data)

                return height_reference_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HeightReference | None | Unset, data)

        height_reference = _parse_height_reference(d.pop("height_reference", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_tags(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = cast(list[str], data)

                return tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        tags = _parse_tags(d.pop("tags", UNSET))

        def _parse_client(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        client = _parse_client(d.pop("client", UNSET))

        def _parse_contractor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contractor = _parse_contractor(d.pop("contractor", UNSET))

        def _parse_sync_with_nadag(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        sync_with_nadag = _parse_sync_with_nadag(d.pop("sync_with_nadag", UNSET))

        def _parse_organization(data: object) -> None | OrganizationMin | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                organization_type_0 = OrganizationMin.from_dict(data)

                return organization_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OrganizationMin | Unset, data)

        organization = _parse_organization(d.pop("organization", UNSET))

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

        def _parse_last_updated(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_updated_type_0 = datetime.datetime.fromisoformat(data)

                return last_updated_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_updated = _parse_last_updated(d.pop("last_updated", UNSET))

        favorite = d.pop("favorite", UNSET)

        def _parse_linked_project_prefix(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        linked_project_prefix = _parse_linked_project_prefix(d.pop("linked_project_prefix", UNSET))

        linked_project_info = cls(
            project_id=project_id,
            external_id=external_id,
            organization_id=organization_id,
            name=name,
            standard_id=standard_id,
            srid=srid,
            number_of_locations=number_of_locations,
            created_at=created_at,
            updated_at=updated_at,
            external_id_source=external_id_source,
            height_reference=height_reference,
            description=description,
            tags=tags,
            client=client,
            contractor=contractor,
            sync_with_nadag=sync_with_nadag,
            organization=organization,
            effective_role=effective_role,
            last_updated=last_updated,
            favorite=favorite,
            linked_project_prefix=linked_project_prefix,
        )

        linked_project_info.additional_properties = d
        return linked_project_info

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
