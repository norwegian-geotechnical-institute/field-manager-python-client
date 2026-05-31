from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.export_type import ExportType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Export")


@_attrs_define
class Export:
    """
    Attributes:
        export_type (ExportType):
        location_ids (list[UUID] | Unset): Used when export_type is one of `LocationCSV`, `LocationGeoJSON`,
            `LocationKOF`, `LocationLAS` or `LocationXLS`
        file_ids (list[UUID] | Unset): Used when export_type is `ProjectFiles`
        method_status_ids (list[int] | Unset): Filter methods by status. Empty list means all statuses.
        method_type_ids (list[int] | Unset): Filter methods by type. Empty list means all types.
        srid (int | None | Unset): Specify the output file coordinate system for KOF and SND export. If not specified,
            the project coordinate system will be used.
        method_conducted_from (datetime.datetime | None | Unset): Filter methods by conducted date from this time
        method_conducted_to (datetime.datetime | None | Unset): Filter methods by conducted date from (this time + 1
            day)
        updated_after (datetime.datetime | None | Unset): Filter locations by last modified from this time
        min_x (float | None | Unset): Filter locations by position in project's coordinate system
        min_y (float | None | Unset): Filter locations by position in project's coordinate system
        max_x (float | None | Unset): Filter locations by position in project's coordinate system
        max_y (float | None | Unset): Filter locations by position in project's coordinate system
        swap_x_y (bool | None | Unset):  Default: False.
        include_layer_intervals_csv (bool | Unset):  Default: False.
    """

    export_type: ExportType
    location_ids: list[UUID] | Unset = UNSET
    file_ids: list[UUID] | Unset = UNSET
    method_status_ids: list[int] | Unset = UNSET
    method_type_ids: list[int] | Unset = UNSET
    srid: int | None | Unset = UNSET
    method_conducted_from: datetime.datetime | None | Unset = UNSET
    method_conducted_to: datetime.datetime | None | Unset = UNSET
    updated_after: datetime.datetime | None | Unset = UNSET
    min_x: float | None | Unset = UNSET
    min_y: float | None | Unset = UNSET
    max_x: float | None | Unset = UNSET
    max_y: float | None | Unset = UNSET
    swap_x_y: bool | None | Unset = False
    include_layer_intervals_csv: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        export_type = self.export_type.value

        location_ids: list[str] | Unset = UNSET
        if not isinstance(self.location_ids, Unset):
            location_ids = []
            for location_ids_item_data in self.location_ids:
                location_ids_item = str(location_ids_item_data)
                location_ids.append(location_ids_item)

        file_ids: list[str] | Unset = UNSET
        if not isinstance(self.file_ids, Unset):
            file_ids = []
            for file_ids_item_data in self.file_ids:
                file_ids_item = str(file_ids_item_data)
                file_ids.append(file_ids_item)

        method_status_ids: list[int] | Unset = UNSET
        if not isinstance(self.method_status_ids, Unset):
            method_status_ids = self.method_status_ids

        method_type_ids: list[int] | Unset = UNSET
        if not isinstance(self.method_type_ids, Unset):
            method_type_ids = self.method_type_ids

        srid: int | None | Unset
        if isinstance(self.srid, Unset):
            srid = UNSET
        else:
            srid = self.srid

        method_conducted_from: None | str | Unset
        if isinstance(self.method_conducted_from, Unset):
            method_conducted_from = UNSET
        elif isinstance(self.method_conducted_from, datetime.datetime):
            method_conducted_from = self.method_conducted_from.isoformat()
        else:
            method_conducted_from = self.method_conducted_from

        method_conducted_to: None | str | Unset
        if isinstance(self.method_conducted_to, Unset):
            method_conducted_to = UNSET
        elif isinstance(self.method_conducted_to, datetime.datetime):
            method_conducted_to = self.method_conducted_to.isoformat()
        else:
            method_conducted_to = self.method_conducted_to

        updated_after: None | str | Unset
        if isinstance(self.updated_after, Unset):
            updated_after = UNSET
        elif isinstance(self.updated_after, datetime.datetime):
            updated_after = self.updated_after.isoformat()
        else:
            updated_after = self.updated_after

        min_x: float | None | Unset
        if isinstance(self.min_x, Unset):
            min_x = UNSET
        else:
            min_x = self.min_x

        min_y: float | None | Unset
        if isinstance(self.min_y, Unset):
            min_y = UNSET
        else:
            min_y = self.min_y

        max_x: float | None | Unset
        if isinstance(self.max_x, Unset):
            max_x = UNSET
        else:
            max_x = self.max_x

        max_y: float | None | Unset
        if isinstance(self.max_y, Unset):
            max_y = UNSET
        else:
            max_y = self.max_y

        swap_x_y: bool | None | Unset
        if isinstance(self.swap_x_y, Unset):
            swap_x_y = UNSET
        else:
            swap_x_y = self.swap_x_y

        include_layer_intervals_csv = self.include_layer_intervals_csv

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "export_type": export_type,
            }
        )
        if location_ids is not UNSET:
            field_dict["location_ids"] = location_ids
        if file_ids is not UNSET:
            field_dict["file_ids"] = file_ids
        if method_status_ids is not UNSET:
            field_dict["method_status_ids"] = method_status_ids
        if method_type_ids is not UNSET:
            field_dict["method_type_ids"] = method_type_ids
        if srid is not UNSET:
            field_dict["srid"] = srid
        if method_conducted_from is not UNSET:
            field_dict["method_conducted_from"] = method_conducted_from
        if method_conducted_to is not UNSET:
            field_dict["method_conducted_to"] = method_conducted_to
        if updated_after is not UNSET:
            field_dict["updated_after"] = updated_after
        if min_x is not UNSET:
            field_dict["min_x"] = min_x
        if min_y is not UNSET:
            field_dict["min_y"] = min_y
        if max_x is not UNSET:
            field_dict["max_x"] = max_x
        if max_y is not UNSET:
            field_dict["max_y"] = max_y
        if swap_x_y is not UNSET:
            field_dict["swap_x_y"] = swap_x_y
        if include_layer_intervals_csv is not UNSET:
            field_dict["include_layer_intervals_csv"] = include_layer_intervals_csv

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        export_type = ExportType(d.pop("export_type"))

        _location_ids = d.pop("location_ids", UNSET)
        location_ids: list[UUID] | Unset = UNSET
        if _location_ids is not UNSET:
            location_ids = []
            for location_ids_item_data in _location_ids:
                location_ids_item = UUID(location_ids_item_data)

                location_ids.append(location_ids_item)

        _file_ids = d.pop("file_ids", UNSET)
        file_ids: list[UUID] | Unset = UNSET
        if _file_ids is not UNSET:
            file_ids = []
            for file_ids_item_data in _file_ids:
                file_ids_item = UUID(file_ids_item_data)

                file_ids.append(file_ids_item)

        method_status_ids = cast(list[int], d.pop("method_status_ids", UNSET))

        method_type_ids = cast(list[int], d.pop("method_type_ids", UNSET))

        def _parse_srid(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        srid = _parse_srid(d.pop("srid", UNSET))

        def _parse_method_conducted_from(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                method_conducted_from_type_0 = isoparse(data)

                return method_conducted_from_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        method_conducted_from = _parse_method_conducted_from(d.pop("method_conducted_from", UNSET))

        def _parse_method_conducted_to(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                method_conducted_to_type_0 = isoparse(data)

                return method_conducted_to_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        method_conducted_to = _parse_method_conducted_to(d.pop("method_conducted_to", UNSET))

        def _parse_updated_after(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_after_type_0 = isoparse(data)

                return updated_after_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_after = _parse_updated_after(d.pop("updated_after", UNSET))

        def _parse_min_x(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        min_x = _parse_min_x(d.pop("min_x", UNSET))

        def _parse_min_y(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        min_y = _parse_min_y(d.pop("min_y", UNSET))

        def _parse_max_x(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        max_x = _parse_max_x(d.pop("max_x", UNSET))

        def _parse_max_y(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        max_y = _parse_max_y(d.pop("max_y", UNSET))

        def _parse_swap_x_y(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        swap_x_y = _parse_swap_x_y(d.pop("swap_x_y", UNSET))

        include_layer_intervals_csv = d.pop("include_layer_intervals_csv", UNSET)

        export = cls(
            export_type=export_type,
            location_ids=location_ids,
            file_ids=file_ids,
            method_status_ids=method_status_ids,
            method_type_ids=method_type_ids,
            srid=srid,
            method_conducted_from=method_conducted_from,
            method_conducted_to=method_conducted_to,
            updated_after=updated_after,
            min_x=min_x,
            min_y=min_y,
            max_x=max_x,
            max_y=max_y,
            swap_x_y=swap_x_y,
            include_layer_intervals_csv=include_layer_intervals_csv,
        )

        export.additional_properties = d
        return export

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
