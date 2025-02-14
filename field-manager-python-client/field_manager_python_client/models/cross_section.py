import datetime
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.language import Language
from ..types import UNSET, Unset

T = TypeVar("T", bound="CrossSection")


@_attrs_define
class CrossSection:
    """
    Attributes:
        cross_section_id (UUID):
        horizontal_scale (str):
        vertical_scale (str):
        method_ids (list[UUID]):
        name (str):
        width (float):
        polyline_linestring (str):
        project_id (UUID):
        srid (int):
        created_by (UUID):
        polyline_coordinates (list[list[float]]): Compute the polyline_coordinates from the polyline_linestring
        language (Union[Unset, Language]): ISO 639-2 language three-letter codes (set 2)
        updated_at (Union[None, Unset, datetime.datetime]):
        updated_by (Union[None, UUID, Unset]):
        created_at (Union[None, Unset, datetime.datetime]):
    """

    cross_section_id: UUID
    horizontal_scale: str
    vertical_scale: str
    method_ids: list[UUID]
    name: str
    width: float
    polyline_linestring: str
    project_id: UUID
    srid: int
    created_by: UUID
    polyline_coordinates: list[list[float]]
    language: Union[Unset, Language] = UNSET
    updated_at: Union[None, Unset, datetime.datetime] = UNSET
    updated_by: Union[None, UUID, Unset] = UNSET
    created_at: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cross_section_id = str(self.cross_section_id)

        horizontal_scale = self.horizontal_scale

        vertical_scale = self.vertical_scale

        method_ids = []
        for method_ids_item_data in self.method_ids:
            method_ids_item = str(method_ids_item_data)
            method_ids.append(method_ids_item)

        name = self.name

        width = self.width

        polyline_linestring = self.polyline_linestring

        project_id = str(self.project_id)

        srid = self.srid

        created_by = str(self.created_by)

        polyline_coordinates = []
        for polyline_coordinates_item_data in self.polyline_coordinates:
            polyline_coordinates_item = []
            for polyline_coordinates_item_item_data in polyline_coordinates_item_data:
                polyline_coordinates_item_item: float
                polyline_coordinates_item_item = polyline_coordinates_item_item_data
                polyline_coordinates_item.append(polyline_coordinates_item_item)

            polyline_coordinates.append(polyline_coordinates_item)

        language: Union[Unset, str] = UNSET
        if not isinstance(self.language, Unset):
            language = self.language.value

        updated_at: Union[None, Unset, str]
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        updated_by: Union[None, Unset, str]
        if isinstance(self.updated_by, Unset):
            updated_by = UNSET
        elif isinstance(self.updated_by, UUID):
            updated_by = str(self.updated_by)
        else:
            updated_by = self.updated_by

        created_at: Union[None, Unset, str]
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cross_section_id": cross_section_id,
                "horizontal_scale": horizontal_scale,
                "vertical_scale": vertical_scale,
                "method_ids": method_ids,
                "name": name,
                "width": width,
                "polyline_linestring": polyline_linestring,
                "project_id": project_id,
                "srid": srid,
                "created_by": created_by,
                "polyline_coordinates": polyline_coordinates,
            }
        )
        if language is not UNSET:
            field_dict["language"] = language
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if updated_by is not UNSET:
            field_dict["updated_by"] = updated_by
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        cross_section_id = UUID(d.pop("cross_section_id"))

        horizontal_scale = d.pop("horizontal_scale")

        vertical_scale = d.pop("vertical_scale")

        method_ids = []
        _method_ids = d.pop("method_ids")
        for method_ids_item_data in _method_ids:
            method_ids_item = UUID(method_ids_item_data)

            method_ids.append(method_ids_item)

        name = d.pop("name")

        width = d.pop("width")

        polyline_linestring = d.pop("polyline_linestring")

        project_id = UUID(d.pop("project_id"))

        srid = d.pop("srid")

        created_by = UUID(d.pop("created_by"))

        polyline_coordinates = []
        _polyline_coordinates = d.pop("polyline_coordinates")
        for polyline_coordinates_item_data in _polyline_coordinates:
            polyline_coordinates_item = []
            _polyline_coordinates_item = polyline_coordinates_item_data
            for polyline_coordinates_item_item_data in _polyline_coordinates_item:

                def _parse_polyline_coordinates_item_item(data: object) -> float:
                    return cast(float, data)

                polyline_coordinates_item_item = _parse_polyline_coordinates_item_item(
                    polyline_coordinates_item_item_data
                )

                polyline_coordinates_item.append(polyline_coordinates_item_item)

            polyline_coordinates.append(polyline_coordinates_item)

        _language = d.pop("language", UNSET)
        language: Union[Unset, Language]
        if isinstance(_language, Unset):
            language = UNSET
        else:
            language = Language(_language)

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

        def _parse_updated_by(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_by_type_0 = UUID(data)

                return updated_by_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        updated_by = _parse_updated_by(d.pop("updated_by", UNSET))

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

        cross_section = cls(
            cross_section_id=cross_section_id,
            horizontal_scale=horizontal_scale,
            vertical_scale=vertical_scale,
            method_ids=method_ids,
            name=name,
            width=width,
            polyline_linestring=polyline_linestring,
            project_id=project_id,
            srid=srid,
            created_by=created_by,
            polyline_coordinates=polyline_coordinates,
            language=language,
            updated_at=updated_at,
            updated_by=updated_by,
            created_at=created_at,
        )

        cross_section.additional_properties = d
        return cross_section

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
