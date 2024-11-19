import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.role import Role


T = TypeVar("T", bound="BFFProjectSummary")


@_attrs_define
class BFFProjectSummary:
    """
    Attributes:
        project_id (UUID):
        external_id (str):
        name (str):
        organization_id (UUID):
        number_of_locations (int):
        tags (Union[Unset, List[str]]):
        last_updated (Union[None, Unset, datetime.datetime]):
        effective_role (Union['Role', None, Unset]):
        favorite (Union[Unset, bool]):  Default: False.
        geometry (Union[None, Unset, str]):
        centroid (Union[None, Unset, str]):
    """

    project_id: UUID
    external_id: str
    name: str
    organization_id: UUID
    number_of_locations: int
    tags: Union[Unset, List[str]] = UNSET
    last_updated: Union[None, Unset, datetime.datetime] = UNSET
    effective_role: Union["Role", None, Unset] = UNSET
    favorite: Union[Unset, bool] = False
    geometry: Union[None, Unset, str] = UNSET
    centroid: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.role import Role

        project_id = str(self.project_id)

        external_id = self.external_id

        name = self.name

        organization_id = str(self.organization_id)

        number_of_locations = self.number_of_locations

        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        last_updated: Union[None, Unset, str]
        if isinstance(self.last_updated, Unset):
            last_updated = UNSET
        elif isinstance(self.last_updated, datetime.datetime):
            last_updated = self.last_updated.isoformat()
        else:
            last_updated = self.last_updated

        effective_role: Union[Dict[str, Any], None, Unset]
        if isinstance(self.effective_role, Unset):
            effective_role = UNSET
        elif isinstance(self.effective_role, Role):
            effective_role = self.effective_role.to_dict()
        else:
            effective_role = self.effective_role

        favorite = self.favorite

        geometry: Union[None, Unset, str]
        if isinstance(self.geometry, Unset):
            geometry = UNSET
        else:
            geometry = self.geometry

        centroid: Union[None, Unset, str]
        if isinstance(self.centroid, Unset):
            centroid = UNSET
        else:
            centroid = self.centroid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "project_id": project_id,
                "external_id": external_id,
                "name": name,
                "organization_id": organization_id,
                "number_of_locations": number_of_locations,
            }
        )
        if tags is not UNSET:
            field_dict["tags"] = tags
        if last_updated is not UNSET:
            field_dict["last_updated"] = last_updated
        if effective_role is not UNSET:
            field_dict["effective_role"] = effective_role
        if favorite is not UNSET:
            field_dict["favorite"] = favorite
        if geometry is not UNSET:
            field_dict["geometry"] = geometry
        if centroid is not UNSET:
            field_dict["centroid"] = centroid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.role import Role

        d = src_dict.copy()
        project_id = UUID(d.pop("project_id"))

        external_id = d.pop("external_id")

        name = d.pop("name")

        organization_id = UUID(d.pop("organization_id"))

        number_of_locations = d.pop("number_of_locations")

        tags = cast(List[str], d.pop("tags", UNSET))

        def _parse_last_updated(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_updated_type_0 = isoparse(data)

                return last_updated_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        last_updated = _parse_last_updated(d.pop("last_updated", UNSET))

        def _parse_effective_role(data: object) -> Union["Role", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                effective_role_type_0 = Role.from_dict(data)

                return effective_role_type_0
            except:  # noqa: E722
                pass
            return cast(Union["Role", None, Unset], data)

        effective_role = _parse_effective_role(d.pop("effective_role", UNSET))

        favorite = d.pop("favorite", UNSET)

        def _parse_geometry(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        geometry = _parse_geometry(d.pop("geometry", UNSET))

        def _parse_centroid(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        centroid = _parse_centroid(d.pop("centroid", UNSET))

        bff_project_summary = cls(
            project_id=project_id,
            external_id=external_id,
            name=name,
            organization_id=organization_id,
            number_of_locations=number_of_locations,
            tags=tags,
            last_updated=last_updated,
            effective_role=effective_role,
            favorite=favorite,
            geometry=geometry,
            centroid=centroid,
        )

        bff_project_summary.additional_properties = d
        return bff_project_summary

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
