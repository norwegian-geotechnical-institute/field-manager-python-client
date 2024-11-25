from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.location_type_enum import LocationTypeEnum
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import cast, List
from typing import cast, Union
from typing import Union
from uuid import UUID
import datetime






T = TypeVar("T", bound="ProjectLocationMethodTypes")


@_attrs_define
class ProjectLocationMethodTypes:
    """ 
        Attributes:
            project_id (UUID):
            project_number (str):
            project_name (str):
            location_id (UUID):
            name (str):
            geometry (Union[None, str]):
            point_z (Union[None, float]):
            is_deleted (bool):
            updated_at (datetime.datetime):
            external_id_source (Union[None, Unset, str]):
            location_type_id (Union[LocationTypeEnum, None, Unset]): Use Project.standard_id instead.
            method_types (Union[List[str], None, Unset]):
     """

    project_id: UUID
    project_number: str
    project_name: str
    location_id: UUID
    name: str
    geometry: Union[None, str]
    point_z: Union[None, float]
    is_deleted: bool
    updated_at: datetime.datetime
    external_id_source: Union[None, Unset, str] = UNSET
    location_type_id: Union[LocationTypeEnum, None, Unset] = UNSET
    method_types: Union[List[str], None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        project_id = str(self.project_id)

        project_number = self.project_number

        project_name = self.project_name

        location_id = str(self.location_id)

        name = self.name

        geometry: Union[None, str]
        geometry = self.geometry

        point_z: Union[None, float]
        point_z = self.point_z

        is_deleted = self.is_deleted

        updated_at = self.updated_at.isoformat()

        external_id_source: Union[None, Unset, str]
        if isinstance(self.external_id_source, Unset):
            external_id_source = UNSET
        else:
            external_id_source = self.external_id_source

        location_type_id: Union[None, Unset, int]
        if isinstance(self.location_type_id, Unset):
            location_type_id = UNSET
        elif isinstance(self.location_type_id, LocationTypeEnum):
            location_type_id = self.location_type_id.value
        else:
            location_type_id = self.location_type_id

        method_types: Union[List[str], None, Unset]
        if isinstance(self.method_types, Unset):
            method_types = UNSET
        elif isinstance(self.method_types, list):
            method_types = self.method_types


        else:
            method_types = self.method_types


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "project_id": project_id,
            "project_number": project_number,
            "project_name": project_name,
            "location_id": location_id,
            "name": name,
            "geometry": geometry,
            "point_z": point_z,
            "is_deleted": is_deleted,
            "updated_at": updated_at,
        })
        if external_id_source is not UNSET:
            field_dict["external_id_source"] = external_id_source
        if location_type_id is not UNSET:
            field_dict["location_type_id"] = location_type_id
        if method_types is not UNSET:
            field_dict["method_types"] = method_types

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        project_id = UUID(d.pop("project_id"))




        project_number = d.pop("project_number")

        project_name = d.pop("project_name")

        location_id = UUID(d.pop("location_id"))




        name = d.pop("name")

        def _parse_geometry(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        geometry = _parse_geometry(d.pop("geometry"))


        def _parse_point_z(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        point_z = _parse_point_z(d.pop("point_z"))


        is_deleted = d.pop("is_deleted")

        updated_at = isoparse(d.pop("updated_at"))




        def _parse_external_id_source(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id_source = _parse_external_id_source(d.pop("external_id_source", UNSET))


        def _parse_location_type_id(data: object) -> Union[LocationTypeEnum, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, int):
                    raise TypeError()
                location_type_id_type_0 = LocationTypeEnum(data)



                return location_type_id_type_0
            except: # noqa: E722
                pass
            return cast(Union[LocationTypeEnum, None, Unset], data)

        location_type_id = _parse_location_type_id(d.pop("location_type_id", UNSET))


        def _parse_method_types(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                method_types_type_0 = cast(List[str], data)

                return method_types_type_0
            except: # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        method_types = _parse_method_types(d.pop("method_types", UNSET))


        project_location_method_types = cls(
            project_id=project_id,
            project_number=project_number,
            project_name=project_name,
            location_id=location_id,
            name=name,
            geometry=geometry,
            point_z=point_z,
            is_deleted=is_deleted,
            updated_at=updated_at,
            external_id_source=external_id_source,
            location_type_id=location_type_id,
            method_types=method_types,
        )


        project_location_method_types.additional_properties = d
        return project_location_method_types

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
