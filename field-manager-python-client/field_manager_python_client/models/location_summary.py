from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.iogp_type_enum import IOGPTypeEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.method_summary import MethodSummary


T = TypeVar("T", bound="LocationSummary")


@_attrs_define
class LocationSummary:
    """
    Attributes:
        location_id (UUID):
        name (str):
        last_updated (datetime.datetime):
        iogp_type_id (IOGPTypeEnum | None | Unset):
        point_easting (float | None | Unset):
        point_northing (float | None | Unset):
        point_z (float | None | Unset):
        srid (int | None | Unset):
        point_x_wgs84_web (float | None | Unset):
        point_y_wgs84_web (float | None | Unset):
        point_x_wgs84_pseudo (float | None | Unset):
        point_y_wgs84_pseudo (float | None | Unset):
        created_at (datetime.datetime | None | Unset): Will be removed in a future release
        created_by (None | str | Unset): Will be removed in a future release
        updated_at (datetime.datetime | None | Unset): Will be removed in a future release
        updated_by (None | str | Unset): Will be removed in a future release
        methods (list[MethodSummary] | Unset):
        tags (list[str] | Unset):
    """

    location_id: UUID
    name: str
    last_updated: datetime.datetime
    iogp_type_id: IOGPTypeEnum | None | Unset = UNSET
    point_easting: float | None | Unset = UNSET
    point_northing: float | None | Unset = UNSET
    point_z: float | None | Unset = UNSET
    srid: int | None | Unset = UNSET
    point_x_wgs84_web: float | None | Unset = UNSET
    point_y_wgs84_web: float | None | Unset = UNSET
    point_x_wgs84_pseudo: float | None | Unset = UNSET
    point_y_wgs84_pseudo: float | None | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    created_by: None | str | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    updated_by: None | str | Unset = UNSET
    methods: list[MethodSummary] | Unset = UNSET
    tags: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        location_id = str(self.location_id)

        name = self.name

        last_updated = self.last_updated.isoformat()

        iogp_type_id: None | str | Unset
        if isinstance(self.iogp_type_id, Unset):
            iogp_type_id = UNSET
        elif isinstance(self.iogp_type_id, IOGPTypeEnum):
            iogp_type_id = self.iogp_type_id.value
        else:
            iogp_type_id = self.iogp_type_id

        point_easting: float | None | Unset
        if isinstance(self.point_easting, Unset):
            point_easting = UNSET
        else:
            point_easting = self.point_easting

        point_northing: float | None | Unset
        if isinstance(self.point_northing, Unset):
            point_northing = UNSET
        else:
            point_northing = self.point_northing

        point_z: float | None | Unset
        if isinstance(self.point_z, Unset):
            point_z = UNSET
        else:
            point_z = self.point_z

        srid: int | None | Unset
        if isinstance(self.srid, Unset):
            srid = UNSET
        else:
            srid = self.srid

        point_x_wgs84_web: float | None | Unset
        if isinstance(self.point_x_wgs84_web, Unset):
            point_x_wgs84_web = UNSET
        else:
            point_x_wgs84_web = self.point_x_wgs84_web

        point_y_wgs84_web: float | None | Unset
        if isinstance(self.point_y_wgs84_web, Unset):
            point_y_wgs84_web = UNSET
        else:
            point_y_wgs84_web = self.point_y_wgs84_web

        point_x_wgs84_pseudo: float | None | Unset
        if isinstance(self.point_x_wgs84_pseudo, Unset):
            point_x_wgs84_pseudo = UNSET
        else:
            point_x_wgs84_pseudo = self.point_x_wgs84_pseudo

        point_y_wgs84_pseudo: float | None | Unset
        if isinstance(self.point_y_wgs84_pseudo, Unset):
            point_y_wgs84_pseudo = UNSET
        else:
            point_y_wgs84_pseudo = self.point_y_wgs84_pseudo

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        created_by: None | str | Unset
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        else:
            created_by = self.created_by

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        updated_by: None | str | Unset
        if isinstance(self.updated_by, Unset):
            updated_by = UNSET
        else:
            updated_by = self.updated_by

        methods: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.methods, Unset):
            methods = []
            for methods_item_data in self.methods:
                methods_item = methods_item_data.to_dict()
                methods.append(methods_item)

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "location_id": location_id,
                "name": name,
                "last_updated": last_updated,
            }
        )
        if iogp_type_id is not UNSET:
            field_dict["iogp_type_id"] = iogp_type_id
        if point_easting is not UNSET:
            field_dict["point_easting"] = point_easting
        if point_northing is not UNSET:
            field_dict["point_northing"] = point_northing
        if point_z is not UNSET:
            field_dict["point_z"] = point_z
        if srid is not UNSET:
            field_dict["srid"] = srid
        if point_x_wgs84_web is not UNSET:
            field_dict["point_x_wgs84_web"] = point_x_wgs84_web
        if point_y_wgs84_web is not UNSET:
            field_dict["point_y_wgs84_web"] = point_y_wgs84_web
        if point_x_wgs84_pseudo is not UNSET:
            field_dict["point_x_wgs84_pseudo"] = point_x_wgs84_pseudo
        if point_y_wgs84_pseudo is not UNSET:
            field_dict["point_y_wgs84_pseudo"] = point_y_wgs84_pseudo
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if updated_by is not UNSET:
            field_dict["updated_by"] = updated_by
        if methods is not UNSET:
            field_dict["methods"] = methods
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.method_summary import MethodSummary

        d = dict(src_dict)
        location_id = UUID(d.pop("location_id"))

        name = d.pop("name")

        last_updated = datetime.datetime.fromisoformat(d.pop("last_updated"))

        def _parse_iogp_type_id(data: object) -> IOGPTypeEnum | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                iogp_type_id_type_0 = IOGPTypeEnum(data)

                return iogp_type_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(IOGPTypeEnum | None | Unset, data)

        iogp_type_id = _parse_iogp_type_id(d.pop("iogp_type_id", UNSET))

        def _parse_point_easting(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        point_easting = _parse_point_easting(d.pop("point_easting", UNSET))

        def _parse_point_northing(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        point_northing = _parse_point_northing(d.pop("point_northing", UNSET))

        def _parse_point_z(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        point_z = _parse_point_z(d.pop("point_z", UNSET))

        def _parse_srid(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        srid = _parse_srid(d.pop("srid", UNSET))

        def _parse_point_x_wgs84_web(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        point_x_wgs84_web = _parse_point_x_wgs84_web(d.pop("point_x_wgs84_web", UNSET))

        def _parse_point_y_wgs84_web(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        point_y_wgs84_web = _parse_point_y_wgs84_web(d.pop("point_y_wgs84_web", UNSET))

        def _parse_point_x_wgs84_pseudo(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        point_x_wgs84_pseudo = _parse_point_x_wgs84_pseudo(d.pop("point_x_wgs84_pseudo", UNSET))

        def _parse_point_y_wgs84_pseudo(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        point_y_wgs84_pseudo = _parse_point_y_wgs84_pseudo(d.pop("point_y_wgs84_pseudo", UNSET))

        def _parse_created_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = datetime.datetime.fromisoformat(data)

                return created_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        created_at = _parse_created_at(d.pop("created_at", UNSET))

        def _parse_created_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_by = _parse_created_by(d.pop("created_by", UNSET))

        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = datetime.datetime.fromisoformat(data)

                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))

        def _parse_updated_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        updated_by = _parse_updated_by(d.pop("updated_by", UNSET))

        _methods = d.pop("methods", UNSET)
        methods: list[MethodSummary] | Unset = UNSET
        if _methods is not UNSET:
            methods = []
            for methods_item_data in _methods:
                methods_item = MethodSummary.from_dict(methods_item_data)

                methods.append(methods_item)

        tags = cast(list[str], d.pop("tags", UNSET))

        location_summary = cls(
            location_id=location_id,
            name=name,
            last_updated=last_updated,
            iogp_type_id=iogp_type_id,
            point_easting=point_easting,
            point_northing=point_northing,
            point_z=point_z,
            srid=srid,
            point_x_wgs84_web=point_x_wgs84_web,
            point_y_wgs84_web=point_y_wgs84_web,
            point_x_wgs84_pseudo=point_x_wgs84_pseudo,
            point_y_wgs84_pseudo=point_y_wgs84_pseudo,
            created_at=created_at,
            created_by=created_by,
            updated_at=updated_at,
            updated_by=updated_by,
            methods=methods,
            tags=tags,
        )

        location_summary.additional_properties = d
        return location_summary

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
