import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.iogp_type_enum import IOGPTypeEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bff_method_summary import BFFMethodSummary


T = TypeVar("T", bound="BFFLocationSummary")


@_attrs_define
class BFFLocationSummary:
    """
    Attributes:
        last_updated (datetime.datetime): Last updated timestamp of Location or any of its Methods.
        location_id (UUID):
        name (str):
        iogp_type_id (Union[Unset, IOGPTypeEnum]): For offshore locations, an IOGP type is required
        point_easting (Union[None, Unset, float]):
        point_northing (Union[None, Unset, float]):
        point_x_wgs84_web (Union[None, Unset, float]):
        point_y_wgs84_web (Union[None, Unset, float]):
        point_x_wgs84_pseudo (Union[None, Unset, float]):
        point_y_wgs84_pseudo (Union[None, Unset, float]):
        point_z (Union[None, Unset, float]):
        tags (Union[Unset, List[str]]):
        depth_in_soil (Union[None, Unset, float]):
        depth_in_rock (Union[None, Unset, float]):
        bedrock_elevation (Union[None, Unset, float]):
        methods (Union[Unset, List['BFFMethodSummary']]):
    """

    last_updated: datetime.datetime
    location_id: UUID
    name: str
    iogp_type_id: Union[Unset, IOGPTypeEnum] = UNSET
    point_easting: Union[None, Unset, float] = UNSET
    point_northing: Union[None, Unset, float] = UNSET
    point_x_wgs84_web: Union[None, Unset, float] = UNSET
    point_y_wgs84_web: Union[None, Unset, float] = UNSET
    point_x_wgs84_pseudo: Union[None, Unset, float] = UNSET
    point_y_wgs84_pseudo: Union[None, Unset, float] = UNSET
    point_z: Union[None, Unset, float] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    depth_in_soil: Union[None, Unset, float] = UNSET
    depth_in_rock: Union[None, Unset, float] = UNSET
    bedrock_elevation: Union[None, Unset, float] = UNSET
    methods: Union[Unset, List["BFFMethodSummary"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        last_updated = self.last_updated.isoformat()

        location_id = str(self.location_id)

        name = self.name

        iogp_type_id: Union[Unset, str] = UNSET
        if not isinstance(self.iogp_type_id, Unset):
            iogp_type_id = self.iogp_type_id.value

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

        point_x_wgs84_pseudo: Union[None, Unset, float]
        if isinstance(self.point_x_wgs84_pseudo, Unset):
            point_x_wgs84_pseudo = UNSET
        else:
            point_x_wgs84_pseudo = self.point_x_wgs84_pseudo

        point_y_wgs84_pseudo: Union[None, Unset, float]
        if isinstance(self.point_y_wgs84_pseudo, Unset):
            point_y_wgs84_pseudo = UNSET
        else:
            point_y_wgs84_pseudo = self.point_y_wgs84_pseudo

        point_z: Union[None, Unset, float]
        if isinstance(self.point_z, Unset):
            point_z = UNSET
        else:
            point_z = self.point_z

        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

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

        bedrock_elevation: Union[None, Unset, float]
        if isinstance(self.bedrock_elevation, Unset):
            bedrock_elevation = UNSET
        else:
            bedrock_elevation = self.bedrock_elevation

        methods: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.methods, Unset):
            methods = []
            for methods_item_data in self.methods:
                methods_item = methods_item_data.to_dict()
                methods.append(methods_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "last_updated": last_updated,
                "location_id": location_id,
                "name": name,
            }
        )
        if iogp_type_id is not UNSET:
            field_dict["iogp_type_id"] = iogp_type_id
        if point_easting is not UNSET:
            field_dict["point_easting"] = point_easting
        if point_northing is not UNSET:
            field_dict["point_northing"] = point_northing
        if point_x_wgs84_web is not UNSET:
            field_dict["point_x_wgs84_web"] = point_x_wgs84_web
        if point_y_wgs84_web is not UNSET:
            field_dict["point_y_wgs84_web"] = point_y_wgs84_web
        if point_x_wgs84_pseudo is not UNSET:
            field_dict["point_x_wgs84_pseudo"] = point_x_wgs84_pseudo
        if point_y_wgs84_pseudo is not UNSET:
            field_dict["point_y_wgs84_pseudo"] = point_y_wgs84_pseudo
        if point_z is not UNSET:
            field_dict["point_z"] = point_z
        if tags is not UNSET:
            field_dict["tags"] = tags
        if depth_in_soil is not UNSET:
            field_dict["depth_in_soil"] = depth_in_soil
        if depth_in_rock is not UNSET:
            field_dict["depth_in_rock"] = depth_in_rock
        if bedrock_elevation is not UNSET:
            field_dict["bedrock_elevation"] = bedrock_elevation
        if methods is not UNSET:
            field_dict["methods"] = methods

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.bff_method_summary import BFFMethodSummary

        d = src_dict.copy()
        last_updated = isoparse(d.pop("last_updated"))

        location_id = UUID(d.pop("location_id"))

        name = d.pop("name")

        _iogp_type_id = d.pop("iogp_type_id", UNSET)
        iogp_type_id: Union[Unset, IOGPTypeEnum]
        if isinstance(_iogp_type_id, Unset):
            iogp_type_id = UNSET
        else:
            iogp_type_id = IOGPTypeEnum(_iogp_type_id)

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

        def _parse_point_x_wgs84_pseudo(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        point_x_wgs84_pseudo = _parse_point_x_wgs84_pseudo(d.pop("point_x_wgs84_pseudo", UNSET))

        def _parse_point_y_wgs84_pseudo(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        point_y_wgs84_pseudo = _parse_point_y_wgs84_pseudo(d.pop("point_y_wgs84_pseudo", UNSET))

        def _parse_point_z(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        point_z = _parse_point_z(d.pop("point_z", UNSET))

        tags = cast(List[str], d.pop("tags", UNSET))

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

        def _parse_bedrock_elevation(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        bedrock_elevation = _parse_bedrock_elevation(d.pop("bedrock_elevation", UNSET))

        methods = []
        _methods = d.pop("methods", UNSET)
        for methods_item_data in _methods or []:
            methods_item = BFFMethodSummary.from_dict(methods_item_data)

            methods.append(methods_item)

        bff_location_summary = cls(
            last_updated=last_updated,
            location_id=location_id,
            name=name,
            iogp_type_id=iogp_type_id,
            point_easting=point_easting,
            point_northing=point_northing,
            point_x_wgs84_web=point_x_wgs84_web,
            point_y_wgs84_web=point_y_wgs84_web,
            point_x_wgs84_pseudo=point_x_wgs84_pseudo,
            point_y_wgs84_pseudo=point_y_wgs84_pseudo,
            point_z=point_z,
            tags=tags,
            depth_in_soil=depth_in_soil,
            depth_in_rock=depth_in_rock,
            bedrock_elevation=bedrock_elevation,
            methods=methods,
        )

        bff_location_summary.additional_properties = d
        return bff_location_summary

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
