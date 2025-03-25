from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FileExtension")


@_attrs_define
class FileExtension:
    """File extension with description. The extension attribute starts with a period and is always lowercase like '.csv'.

    Attributes:
        extension (str):
        description (str):
        is_for_projects (bool):
        is_for_locations (bool):
    """

    extension: str
    description: str
    is_for_projects: bool
    is_for_locations: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        extension = self.extension

        description = self.description

        is_for_projects = self.is_for_projects

        is_for_locations = self.is_for_locations

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "extension": extension,
                "description": description,
                "is_for_projects": is_for_projects,
                "is_for_locations": is_for_locations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        extension = d.pop("extension")

        description = d.pop("description")

        is_for_projects = d.pop("is_for_projects")

        is_for_locations = d.pop("is_for_locations")

        file_extension = cls(
            extension=extension,
            description=description,
            is_for_projects=is_for_projects,
            is_for_locations=is_for_locations,
        )

        file_extension.additional_properties = d
        return file_extension

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
