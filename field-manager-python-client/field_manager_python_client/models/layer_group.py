from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LayerGroup")


@_attrs_define
class LayerGroup:
    """Full LayerGroup schema returned from API.

    Attributes:
        name (str):
        layer_group_id (UUID):
        project_id (None | UUID):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        created_by (None | str):
        updated_by (None | str):
        is_deleted (bool):
        is_default (bool | Unset):  Default: False.
        organization_id (None | Unset | UUID):
    """

    name: str
    layer_group_id: UUID
    project_id: None | UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    created_by: None | str
    updated_by: None | str
    is_deleted: bool
    is_default: bool | Unset = False
    organization_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        layer_group_id = str(self.layer_group_id)

        project_id: None | str
        if isinstance(self.project_id, UUID):
            project_id = str(self.project_id)
        else:
            project_id = self.project_id

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        created_by: None | str
        created_by = self.created_by

        updated_by: None | str
        updated_by = self.updated_by

        is_deleted = self.is_deleted

        is_default = self.is_default

        organization_id: None | str | Unset
        if isinstance(self.organization_id, Unset):
            organization_id = UNSET
        elif isinstance(self.organization_id, UUID):
            organization_id = str(self.organization_id)
        else:
            organization_id = self.organization_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "layer_group_id": layer_group_id,
                "project_id": project_id,
                "created_at": created_at,
                "updated_at": updated_at,
                "created_by": created_by,
                "updated_by": updated_by,
                "is_deleted": is_deleted,
            }
        )
        if is_default is not UNSET:
            field_dict["is_default"] = is_default
        if organization_id is not UNSET:
            field_dict["organization_id"] = organization_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        layer_group_id = UUID(d.pop("layer_group_id"))

        def _parse_project_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                project_id_type_0 = UUID(data)

                return project_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        project_id = _parse_project_id(d.pop("project_id"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_created_by(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        created_by = _parse_created_by(d.pop("created_by"))

        def _parse_updated_by(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        updated_by = _parse_updated_by(d.pop("updated_by"))

        is_deleted = d.pop("is_deleted")

        is_default = d.pop("is_default", UNSET)

        def _parse_organization_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                organization_id_type_0 = UUID(data)

                return organization_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        organization_id = _parse_organization_id(d.pop("organization_id", UNSET))

        layer_group = cls(
            name=name,
            layer_group_id=layer_group_id,
            project_id=project_id,
            created_at=created_at,
            updated_at=updated_at,
            created_by=created_by,
            updated_by=updated_by,
            is_deleted=is_deleted,
            is_default=is_default,
            organization_id=organization_id,
        )

        layer_group.additional_properties = d
        return layer_group

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
