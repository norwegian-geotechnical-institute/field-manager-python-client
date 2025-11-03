from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.height_reference import HeightReference
from ..models.standard_type import StandardType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectCreate")


@_attrs_define
class ProjectCreate:
    """
    Attributes:
        external_id (str):
        organization_id (UUID):
        name (str):
        srid (int):
        height_reference (HeightReference | None):
        project_id (None | Unset | UUID):
        created_at (datetime.datetime | None | Unset):
        updated_at (datetime.datetime | None | Unset):
        external_id_source (None | str | Unset):
        standard_id (None | StandardType | Unset):  Default: StandardType.NGF.
        description (None | str | Unset):
        tags (list[str] | Unset):
    """

    external_id: str
    organization_id: UUID
    name: str
    srid: int
    height_reference: HeightReference | None
    project_id: None | Unset | UUID = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    external_id_source: None | str | Unset = UNSET
    standard_id: None | StandardType | Unset = StandardType.NGF
    description: None | str | Unset = UNSET
    tags: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        external_id = self.external_id

        organization_id = str(self.organization_id)

        name = self.name

        srid = self.srid

        height_reference: None | str
        if isinstance(self.height_reference, HeightReference):
            height_reference = self.height_reference.value
        else:
            height_reference = self.height_reference

        project_id: None | str | Unset
        if isinstance(self.project_id, Unset):
            project_id = UNSET
        elif isinstance(self.project_id, UUID):
            project_id = str(self.project_id)
        else:
            project_id = self.project_id

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

        standard_id: None | str | Unset
        if isinstance(self.standard_id, Unset):
            standard_id = UNSET
        elif isinstance(self.standard_id, StandardType):
            standard_id = self.standard_id.value
        else:
            standard_id = self.standard_id

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "external_id": external_id,
                "organization_id": organization_id,
                "name": name,
                "srid": srid,
                "height_reference": height_reference,
            }
        )
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if external_id_source is not UNSET:
            field_dict["external_id_source"] = external_id_source
        if standard_id is not UNSET:
            field_dict["standard_id"] = standard_id
        if description is not UNSET:
            field_dict["description"] = description
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        external_id = d.pop("external_id")

        organization_id = UUID(d.pop("organization_id"))

        name = d.pop("name")

        srid = d.pop("srid")

        def _parse_height_reference(data: object) -> HeightReference | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                height_reference_type_0 = HeightReference(data)

                return height_reference_type_0
            except:  # noqa: E722
                pass
            return cast(HeightReference | None, data)

        height_reference = _parse_height_reference(d.pop("height_reference"))

        def _parse_project_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                project_id_type_0 = UUID(data)

                return project_id_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | UUID, data)

        project_id = _parse_project_id(d.pop("project_id", UNSET))

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
            except:  # noqa: E722
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
            except:  # noqa: E722
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

        def _parse_standard_id(data: object) -> None | StandardType | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                standard_id_type_0 = StandardType(data)

                return standard_id_type_0
            except:  # noqa: E722
                pass
            return cast(None | StandardType | Unset, data)

        standard_id = _parse_standard_id(d.pop("standard_id", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        tags = cast(list[str], d.pop("tags", UNSET))

        project_create = cls(
            external_id=external_id,
            organization_id=organization_id,
            name=name,
            srid=srid,
            height_reference=height_reference,
            project_id=project_id,
            created_at=created_at,
            updated_at=updated_at,
            external_id_source=external_id_source,
            standard_id=standard_id,
            description=description,
            tags=tags,
        )

        project_create.additional_properties = d
        return project_create

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
