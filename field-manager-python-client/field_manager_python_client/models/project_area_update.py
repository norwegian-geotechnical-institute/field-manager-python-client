from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectAreaUpdate")


@_attrs_define
class ProjectAreaUpdate:
    """
    Attributes:
        project_area_id (UUID):
        name (None | str | Unset):
        boundary (None | str | Unset): Boundary as a Well-Known Text (WKT) 2D POLYGON. Example 'POLYGON((0 0,0 1,1 1,1
            0,0 0))'
    """

    project_area_id: UUID
    name: None | str | Unset = UNSET
    boundary: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_area_id = str(self.project_area_id)

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        boundary: None | str | Unset
        if isinstance(self.boundary, Unset):
            boundary = UNSET
        else:
            boundary = self.boundary

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "project_area_id": project_area_id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if boundary is not UNSET:
            field_dict["boundary"] = boundary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        project_area_id = UUID(d.pop("project_area_id"))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_boundary(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        boundary = _parse_boundary(d.pop("boundary", UNSET))

        project_area_update = cls(
            project_area_id=project_area_id,
            name=name,
            boundary=boundary,
        )

        project_area_update.additional_properties = d
        return project_area_update

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
