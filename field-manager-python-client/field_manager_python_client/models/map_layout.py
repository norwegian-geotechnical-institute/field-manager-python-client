import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.map_layout_version import MapLayoutVersion


T = TypeVar("T", bound="MapLayout")


@_attrs_define
class MapLayout:
    """Map Layout

    Any MapLayoutVersions

        Attributes:
            map_layout_id (UUID):
            project_id (UUID):
            name (str):
            versions (list['MapLayoutVersion']):
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
            created_by (Union[None, Unset, str]):
            updated_by (Union[None, Unset, str]):
    """

    map_layout_id: UUID
    project_id: UUID
    name: str
    versions: list["MapLayoutVersion"]
    created_at: datetime.datetime
    updated_at: datetime.datetime
    created_by: Union[None, Unset, str] = UNSET
    updated_by: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        map_layout_id = str(self.map_layout_id)

        project_id = str(self.project_id)

        name = self.name

        versions = []
        for versions_item_data in self.versions:
            versions_item = versions_item_data.to_dict()
            versions.append(versions_item)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        created_by: Union[None, Unset, str]
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        else:
            created_by = self.created_by

        updated_by: Union[None, Unset, str]
        if isinstance(self.updated_by, Unset):
            updated_by = UNSET
        else:
            updated_by = self.updated_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "map_layout_id": map_layout_id,
                "project_id": project_id,
                "name": name,
                "versions": versions,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if updated_by is not UNSET:
            field_dict["updated_by"] = updated_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.map_layout_version import MapLayoutVersion

        d = src_dict.copy()
        map_layout_id = UUID(d.pop("map_layout_id"))

        project_id = UUID(d.pop("project_id"))

        name = d.pop("name")

        versions = []
        _versions = d.pop("versions")
        for versions_item_data in _versions:
            versions_item = MapLayoutVersion.from_dict(versions_item_data)

            versions.append(versions_item)

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        def _parse_created_by(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        created_by = _parse_created_by(d.pop("created_by", UNSET))

        def _parse_updated_by(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        updated_by = _parse_updated_by(d.pop("updated_by", UNSET))

        map_layout = cls(
            map_layout_id=map_layout_id,
            project_id=project_id,
            name=name,
            versions=versions,
            created_at=created_at,
            updated_at=updated_at,
            created_by=created_by,
            updated_by=updated_by,
        )

        map_layout.additional_properties = d
        return map_layout

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
