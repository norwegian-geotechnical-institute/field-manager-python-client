from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.project_info import ProjectInfo


T = TypeVar("T", bound="ProjectAreaLinkableProject")


@_attrs_define
class ProjectAreaLinkableProject:
    """
    Attributes:
        project (ProjectInfo):  Example: {'external_id': '2020193232', 'height_reference': 'NN2000', 'name': 'Project
            Name', 'organization_id': 'fff31299-1f3d-48e3-ad70-8c9c37370900', 'project_id':
            'e66a377d-3816-4cf8-ad79-d954a3ba632d', 'srid': 3857}.
        locations_in_project_area_count (int):
        total_location_count (int):
        is_already_linked (bool):
    """

    project: ProjectInfo
    locations_in_project_area_count: int
    total_location_count: int
    is_already_linked: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project = self.project.to_dict()

        locations_in_project_area_count = self.locations_in_project_area_count

        total_location_count = self.total_location_count

        is_already_linked = self.is_already_linked

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "project": project,
                "locations_in_project_area_count": locations_in_project_area_count,
                "total_location_count": total_location_count,
                "is_already_linked": is_already_linked,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.project_info import ProjectInfo

        d = dict(src_dict)
        project = ProjectInfo.from_dict(d.pop("project"))

        locations_in_project_area_count = d.pop("locations_in_project_area_count")

        total_location_count = d.pop("total_location_count")

        is_already_linked = d.pop("is_already_linked")

        project_area_linkable_project = cls(
            project=project,
            locations_in_project_area_count=locations_in_project_area_count,
            total_location_count=total_location_count,
            is_already_linked=is_already_linked,
        )

        project_area_linkable_project.additional_properties = d
        return project_area_linkable_project

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
