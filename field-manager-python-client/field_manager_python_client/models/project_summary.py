import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.height_reference import HeightReference
from ..models.standard_type import StandardType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.location_summary import LocationSummary
    from ..models.organization_min import OrganizationMin
    from ..models.role import Role


T = TypeVar("T", bound="ProjectSummary")


@_attrs_define
class ProjectSummary:
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
        height_reference (Union[HeightReference, None]):
        number_of_locations (int):
        created_at (Union[None, Unset, datetime.datetime]):
        updated_at (Union[None, Unset, datetime.datetime]):
        external_id_source (Union[None, Unset, str]):
        description (Union[None, Unset, str]):
        tags (Union[None, Unset, list[str]]):
        organization (Union['OrganizationMin', None, Unset]):
        effective_role (Union['Role', None, Unset]):
        last_updated (Union[None, Unset, datetime.datetime]):
        favorite (Union[Unset, bool]):  Default: False.
        locations (Union[Unset, list['LocationSummary']]):
    """

    project_id: UUID
    external_id: str
    organization_id: UUID
    name: str
    standard_id: StandardType
    srid: int
    height_reference: Union[HeightReference, None]
    number_of_locations: int
    created_at: Union[None, Unset, datetime.datetime] = UNSET
    updated_at: Union[None, Unset, datetime.datetime] = UNSET
    external_id_source: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    tags: Union[None, Unset, list[str]] = UNSET
    organization: Union["OrganizationMin", None, Unset] = UNSET
    effective_role: Union["Role", None, Unset] = UNSET
    last_updated: Union[None, Unset, datetime.datetime] = UNSET
    favorite: Union[Unset, bool] = False
    locations: Union[Unset, list["LocationSummary"]] = UNSET
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

        height_reference: Union[None, str]
        if isinstance(self.height_reference, HeightReference):
            height_reference = self.height_reference.value
        else:
            height_reference = self.height_reference

        number_of_locations = self.number_of_locations

        created_at: Union[None, Unset, str]
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        updated_at: Union[None, Unset, str]
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        external_id_source: Union[None, Unset, str]
        if isinstance(self.external_id_source, Unset):
            external_id_source = UNSET
        else:
            external_id_source = self.external_id_source

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        tags: Union[None, Unset, list[str]]
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        organization: Union[None, Unset, dict[str, Any]]
        if isinstance(self.organization, Unset):
            organization = UNSET
        elif isinstance(self.organization, OrganizationMin):
            organization = self.organization.to_dict()
        else:
            organization = self.organization

        effective_role: Union[None, Unset, dict[str, Any]]
        if isinstance(self.effective_role, Unset):
            effective_role = UNSET
        elif isinstance(self.effective_role, Role):
            effective_role = self.effective_role.to_dict()
        else:
            effective_role = self.effective_role

        last_updated: Union[None, Unset, str]
        if isinstance(self.last_updated, Unset):
            last_updated = UNSET
        elif isinstance(self.last_updated, datetime.datetime):
            last_updated = self.last_updated.isoformat()
        else:
            last_updated = self.last_updated

        favorite = self.favorite

        locations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.locations, Unset):
            locations = []
            for locations_item_data in self.locations:
                locations_item = locations_item_data.to_dict()
                locations.append(locations_item)

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
                "height_reference": height_reference,
                "number_of_locations": number_of_locations,
            }
        )
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if external_id_source is not UNSET:
            field_dict["external_id_source"] = external_id_source
        if description is not UNSET:
            field_dict["description"] = description
        if tags is not UNSET:
            field_dict["tags"] = tags
        if organization is not UNSET:
            field_dict["organization"] = organization
        if effective_role is not UNSET:
            field_dict["effective_role"] = effective_role
        if last_updated is not UNSET:
            field_dict["last_updated"] = last_updated
        if favorite is not UNSET:
            field_dict["favorite"] = favorite
        if locations is not UNSET:
            field_dict["locations"] = locations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.location_summary import LocationSummary
        from ..models.organization_min import OrganizationMin
        from ..models.role import Role

        d = src_dict.copy()
        project_id = UUID(d.pop("project_id"))

        external_id = d.pop("external_id")

        organization_id = UUID(d.pop("organization_id"))

        name = d.pop("name")

        standard_id = StandardType(d.pop("standard_id"))

        srid = d.pop("srid")

        def _parse_height_reference(data: object) -> Union[HeightReference, None]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                height_reference_type_0 = HeightReference(data)

                return height_reference_type_0
            except:  # noqa: E722
                pass
            return cast(Union[HeightReference, None], data)

        height_reference = _parse_height_reference(d.pop("height_reference"))

        number_of_locations = d.pop("number_of_locations")

        def _parse_created_at(data: object) -> Union[None, Unset, datetime.datetime]:
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
            return cast(Union[None, Unset, datetime.datetime], data)

        created_at = _parse_created_at(d.pop("created_at", UNSET))

        def _parse_updated_at(data: object) -> Union[None, Unset, datetime.datetime]:
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
            return cast(Union[None, Unset, datetime.datetime], data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))

        def _parse_external_id_source(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id_source = _parse_external_id_source(d.pop("external_id_source", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_tags(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = cast(list[str], data)

                return tags_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        tags = _parse_tags(d.pop("tags", UNSET))

        def _parse_organization(data: object) -> Union["OrganizationMin", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                organization_type_0 = OrganizationMin.from_dict(data)

                return organization_type_0
            except:  # noqa: E722
                pass
            return cast(Union["OrganizationMin", None, Unset], data)

        organization = _parse_organization(d.pop("organization", UNSET))

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

        favorite = d.pop("favorite", UNSET)

        locations = []
        _locations = d.pop("locations", UNSET)
        for locations_item_data in _locations or []:
            locations_item = LocationSummary.from_dict(locations_item_data)

            locations.append(locations_item)

        project_summary = cls(
            project_id=project_id,
            external_id=external_id,
            organization_id=organization_id,
            name=name,
            standard_id=standard_id,
            srid=srid,
            height_reference=height_reference,
            number_of_locations=number_of_locations,
            created_at=created_at,
            updated_at=updated_at,
            external_id_source=external_id_source,
            description=description,
            tags=tags,
            organization=organization,
            effective_role=effective_role,
            last_updated=last_updated,
            favorite=favorite,
            locations=locations,
        )

        project_summary.additional_properties = d
        return project_summary

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
