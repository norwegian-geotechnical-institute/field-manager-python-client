from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.height_reference import HeightReference
from ..models.standard_type import StandardType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectUpdate")


@_attrs_define
class ProjectUpdate:
    """
    Example:
        {'external_id': '2020193232', 'height_reference': 'NN2000', 'name': 'Project Name', 'srid': 3857}

    Attributes:
        external_id (Union[None, Unset, str]):
        external_id_source (Union[None, Unset, str]):
        name (Union[None, Unset, str]):
        standard_id (Union[None, StandardType, Unset]):
        srid (Union[None, Unset, int]):
        height_reference (Union[HeightReference, None, Unset]):
        description (Union[None, Unset, str]):
        tags (Union[None, Unset, list[str]]):
    """

    external_id: Union[None, Unset, str] = UNSET
    external_id_source: Union[None, Unset, str] = UNSET
    name: Union[None, Unset, str] = UNSET
    standard_id: Union[None, StandardType, Unset] = UNSET
    srid: Union[None, Unset, int] = UNSET
    height_reference: Union[HeightReference, None, Unset] = UNSET
    description: Union[None, Unset, str] = UNSET
    tags: Union[None, Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        external_id: Union[None, Unset, str]
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        external_id_source: Union[None, Unset, str]
        if isinstance(self.external_id_source, Unset):
            external_id_source = UNSET
        else:
            external_id_source = self.external_id_source

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        standard_id: Union[None, Unset, str]
        if isinstance(self.standard_id, Unset):
            standard_id = UNSET
        elif isinstance(self.standard_id, StandardType):
            standard_id = self.standard_id.value
        else:
            standard_id = self.standard_id

        srid: Union[None, Unset, int]
        if isinstance(self.srid, Unset):
            srid = UNSET
        else:
            srid = self.srid

        height_reference: Union[None, Unset, str]
        if isinstance(self.height_reference, Unset):
            height_reference = UNSET
        elif isinstance(self.height_reference, HeightReference):
            height_reference = self.height_reference.value
        else:
            height_reference = self.height_reference

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if external_id_source is not UNSET:
            field_dict["external_id_source"] = external_id_source
        if name is not UNSET:
            field_dict["name"] = name
        if standard_id is not UNSET:
            field_dict["standard_id"] = standard_id
        if srid is not UNSET:
            field_dict["srid"] = srid
        if height_reference is not UNSET:
            field_dict["height_reference"] = height_reference
        if description is not UNSET:
            field_dict["description"] = description
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id = _parse_external_id(d.pop("external_id", UNSET))

        def _parse_external_id_source(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id_source = _parse_external_id_source(d.pop("external_id_source", UNSET))

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_standard_id(data: object) -> Union[None, StandardType, Unset]:
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
            return cast(Union[None, StandardType, Unset], data)

        standard_id = _parse_standard_id(d.pop("standard_id", UNSET))

        def _parse_srid(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        srid = _parse_srid(d.pop("srid", UNSET))

        def _parse_height_reference(data: object) -> Union[HeightReference, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                height_reference_type_0 = HeightReference(data)

                return height_reference_type_0
            except:  # noqa: E722
                pass
            return cast(Union[HeightReference, None, Unset], data)

        height_reference = _parse_height_reference(d.pop("height_reference", UNSET))

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

        project_update = cls(
            external_id=external_id,
            external_id_source=external_id_source,
            name=name,
            standard_id=standard_id,
            srid=srid,
            height_reference=height_reference,
            description=description,
            tags=tags,
        )

        project_update.additional_properties = d
        return project_update

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
