import datetime
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.height_reference import HeightReference
from ..types import UNSET, Unset

T = TypeVar("T", bound="LocationGis")


@_attrs_define
class LocationGis:
    """
    Attributes:
        location_id (UUID):
        arcgisid (int):
        project_name (Union[None, Unset, str]):
        project_external_id (Union[None, Unset, str]):
        name (Union[None, Unset, str]):
        point_x_wgs84_web (Union[None, Unset, float]):
        point_y_wgs84_web (Union[None, Unset, float]):
        point_z (Union[None, Unset, float]):
        height_reference (Union[HeightReference, None, Unset]):
        point_easting (Union[None, Unset, float]):
        point_northing (Union[None, Unset, float]):
        srid (Union[None, Unset, int]):
        method_names (Union[None, Unset, str]):
        location_status (Union[None, Unset, str]):
        stopcode (Union[None, Unset, int]):
        depth_in_soil (Union[None, Unset, float]):
        depth_in_rock (Union[None, Unset, float]):
        location_url (Union[None, Unset, str]):
        updated_at (Union[None, Unset, datetime.datetime]):
    """

    location_id: UUID
    arcgisid: int
    project_name: Union[None, Unset, str] = UNSET
    project_external_id: Union[None, Unset, str] = UNSET
    name: Union[None, Unset, str] = UNSET
    point_x_wgs84_web: Union[None, Unset, float] = UNSET
    point_y_wgs84_web: Union[None, Unset, float] = UNSET
    point_z: Union[None, Unset, float] = UNSET
    height_reference: Union[HeightReference, None, Unset] = UNSET
    point_easting: Union[None, Unset, float] = UNSET
    point_northing: Union[None, Unset, float] = UNSET
    srid: Union[None, Unset, int] = UNSET
    method_names: Union[None, Unset, str] = UNSET
    location_status: Union[None, Unset, str] = UNSET
    stopcode: Union[None, Unset, int] = UNSET
    depth_in_soil: Union[None, Unset, float] = UNSET
    depth_in_rock: Union[None, Unset, float] = UNSET
    location_url: Union[None, Unset, str] = UNSET
    updated_at: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        location_id = str(self.location_id)

        arcgisid = self.arcgisid

        project_name: Union[None, Unset, str]
        if isinstance(self.project_name, Unset):
            project_name = UNSET
        else:
            project_name = self.project_name

        project_external_id: Union[None, Unset, str]
        if isinstance(self.project_external_id, Unset):
            project_external_id = UNSET
        else:
            project_external_id = self.project_external_id

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        point_x_wgs84_web: Union[None, Unset, float]
        if isinstance(self.point_x_wgs84_web, Unset):
            point_x_wgs84_web = UNSET
        else:
            point_x_wgs84_web = self.point_x_wgs84_web

        point_y_wgs84_web: Union[None, Unset, float]
        if isinstance(self.point_y_wgs84_web, Unset):
            point_y_wgs84_web = UNSET
        else:
            point_y_wgs84_web = self.point_y_wgs84_web

        point_z: Union[None, Unset, float]
        if isinstance(self.point_z, Unset):
            point_z = UNSET
        else:
            point_z = self.point_z

        height_reference: Union[None, Unset, str]
        if isinstance(self.height_reference, Unset):
            height_reference = UNSET
        elif isinstance(self.height_reference, HeightReference):
            height_reference = self.height_reference.value
        else:
            height_reference = self.height_reference

        point_easting: Union[None, Unset, float]
        if isinstance(self.point_easting, Unset):
            point_easting = UNSET
        else:
            point_easting = self.point_easting

        point_northing: Union[None, Unset, float]
        if isinstance(self.point_northing, Unset):
            point_northing = UNSET
        else:
            point_northing = self.point_northing

        srid: Union[None, Unset, int]
        if isinstance(self.srid, Unset):
            srid = UNSET
        else:
            srid = self.srid

        method_names: Union[None, Unset, str]
        if isinstance(self.method_names, Unset):
            method_names = UNSET
        else:
            method_names = self.method_names

        location_status: Union[None, Unset, str]
        if isinstance(self.location_status, Unset):
            location_status = UNSET
        else:
            location_status = self.location_status

        stopcode: Union[None, Unset, int]
        if isinstance(self.stopcode, Unset):
            stopcode = UNSET
        else:
            stopcode = self.stopcode

        depth_in_soil: Union[None, Unset, float]
        if isinstance(self.depth_in_soil, Unset):
            depth_in_soil = UNSET
        else:
            depth_in_soil = self.depth_in_soil

        depth_in_rock: Union[None, Unset, float]
        if isinstance(self.depth_in_rock, Unset):
            depth_in_rock = UNSET
        else:
            depth_in_rock = self.depth_in_rock

        location_url: Union[None, Unset, str]
        if isinstance(self.location_url, Unset):
            location_url = UNSET
        else:
            location_url = self.location_url

        updated_at: Union[None, Unset, str]
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "location_id": location_id,
                "arcgisid": arcgisid,
            }
        )
        if project_name is not UNSET:
            field_dict["project_name"] = project_name
        if project_external_id is not UNSET:
            field_dict["project_external_id"] = project_external_id
        if name is not UNSET:
            field_dict["name"] = name
        if point_x_wgs84_web is not UNSET:
            field_dict["point_x_wgs84_web"] = point_x_wgs84_web
        if point_y_wgs84_web is not UNSET:
            field_dict["point_y_wgs84_web"] = point_y_wgs84_web
        if point_z is not UNSET:
            field_dict["point_z"] = point_z
        if height_reference is not UNSET:
            field_dict["height_reference"] = height_reference
        if point_easting is not UNSET:
            field_dict["point_easting"] = point_easting
        if point_northing is not UNSET:
            field_dict["point_northing"] = point_northing
        if srid is not UNSET:
            field_dict["srid"] = srid
        if method_names is not UNSET:
            field_dict["method_names"] = method_names
        if location_status is not UNSET:
            field_dict["location_status"] = location_status
        if stopcode is not UNSET:
            field_dict["stopcode"] = stopcode
        if depth_in_soil is not UNSET:
            field_dict["depth_in_soil"] = depth_in_soil
        if depth_in_rock is not UNSET:
            field_dict["depth_in_rock"] = depth_in_rock
        if location_url is not UNSET:
            field_dict["location_url"] = location_url
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        location_id = UUID(d.pop("location_id"))

        arcgisid = d.pop("arcgisid")

        def _parse_project_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        project_name = _parse_project_name(d.pop("project_name", UNSET))

        def _parse_project_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        project_external_id = _parse_project_external_id(d.pop("project_external_id", UNSET))

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_point_x_wgs84_web(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        point_x_wgs84_web = _parse_point_x_wgs84_web(d.pop("point_x_wgs84_web", UNSET))

        def _parse_point_y_wgs84_web(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        point_y_wgs84_web = _parse_point_y_wgs84_web(d.pop("point_y_wgs84_web", UNSET))

        def _parse_point_z(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        point_z = _parse_point_z(d.pop("point_z", UNSET))

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

        def _parse_point_easting(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        point_easting = _parse_point_easting(d.pop("point_easting", UNSET))

        def _parse_point_northing(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        point_northing = _parse_point_northing(d.pop("point_northing", UNSET))

        def _parse_srid(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        srid = _parse_srid(d.pop("srid", UNSET))

        def _parse_method_names(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        method_names = _parse_method_names(d.pop("method_names", UNSET))

        def _parse_location_status(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        location_status = _parse_location_status(d.pop("location_status", UNSET))

        def _parse_stopcode(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        stopcode = _parse_stopcode(d.pop("stopcode", UNSET))

        def _parse_depth_in_soil(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        depth_in_soil = _parse_depth_in_soil(d.pop("depth_in_soil", UNSET))

        def _parse_depth_in_rock(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        depth_in_rock = _parse_depth_in_rock(d.pop("depth_in_rock", UNSET))

        def _parse_location_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        location_url = _parse_location_url(d.pop("location_url", UNSET))

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

        location_gis = cls(
            location_id=location_id,
            arcgisid=arcgisid,
            project_name=project_name,
            project_external_id=project_external_id,
            name=name,
            point_x_wgs84_web=point_x_wgs84_web,
            point_y_wgs84_web=point_y_wgs84_web,
            point_z=point_z,
            height_reference=height_reference,
            point_easting=point_easting,
            point_northing=point_northing,
            srid=srid,
            method_names=method_names,
            location_status=location_status,
            stopcode=stopcode,
            depth_in_soil=depth_in_soil,
            depth_in_rock=depth_in_rock,
            location_url=location_url,
            updated_at=updated_at,
        )

        location_gis.additional_properties = d
        return location_gis

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
