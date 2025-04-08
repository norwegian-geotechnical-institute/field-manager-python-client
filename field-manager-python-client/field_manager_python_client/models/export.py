import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
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
        location_ids (Union[Unset, list[UUID]]): Used when export_type is one of `LocationCSV`, `LocationGeoJSON`,
            `LocationKOF`, `LocationLAS` or `LocationXLS`
        file_ids (Union[Unset, list[UUID]]): Used when export_type is `ProjectFiles`
        method_status_ids (Union[Unset, list[int]]): Filter methods by status. Empty list means all statuses.
        method_type_ids (Union[Unset, list[int]]): Filter methods by type. Empty list means all types.
        srid (Union[None, Unset, int]): Specify the output file coordinate system for KOF and SND export. If not
            specified, the project coordinate system will be used.
        method_conducted_from (Union[None, Unset, datetime.datetime]): Filter methods by conducted date from this time
        method_conducted_to (Union[None, Unset, datetime.datetime]): Filter methods by conducted date from (this time +
            1 day)
        swap_x_y (Union[None, Unset, bool]):  Default: False.
    """

    export_type: ExportType
    location_ids: Union[Unset, list[UUID]] = UNSET
    file_ids: Union[Unset, list[UUID]] = UNSET
    method_status_ids: Union[Unset, list[int]] = UNSET
    method_type_ids: Union[Unset, list[int]] = UNSET
    srid: Union[None, Unset, int] = UNSET
    method_conducted_from: Union[None, Unset, datetime.datetime] = UNSET
    method_conducted_to: Union[None, Unset, datetime.datetime] = UNSET
    swap_x_y: Union[None, Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        export_type = self.export_type.value

        location_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.location_ids, Unset):
            location_ids = []
            for location_ids_item_data in self.location_ids:
                location_ids_item = str(location_ids_item_data)
                location_ids.append(location_ids_item)

        file_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.file_ids, Unset):
            file_ids = []
            for file_ids_item_data in self.file_ids:
                file_ids_item = str(file_ids_item_data)
                file_ids.append(file_ids_item)

        method_status_ids: Union[Unset, list[int]] = UNSET
        if not isinstance(self.method_status_ids, Unset):
            method_status_ids = self.method_status_ids

        method_type_ids: Union[Unset, list[int]] = UNSET
        if not isinstance(self.method_type_ids, Unset):
            method_type_ids = self.method_type_ids

        srid: Union[None, Unset, int]
        if isinstance(self.srid, Unset):
            srid = UNSET
        else:
            srid = self.srid

        method_conducted_from: Union[None, Unset, str]
        if isinstance(self.method_conducted_from, Unset):
            method_conducted_from = UNSET
        elif isinstance(self.method_conducted_from, datetime.datetime):
            method_conducted_from = self.method_conducted_from.isoformat()
        else:
            method_conducted_from = self.method_conducted_from

        method_conducted_to: Union[None, Unset, str]
        if isinstance(self.method_conducted_to, Unset):
            method_conducted_to = UNSET
        elif isinstance(self.method_conducted_to, datetime.datetime):
            method_conducted_to = self.method_conducted_to.isoformat()
        else:
            method_conducted_to = self.method_conducted_to

        swap_x_y: Union[None, Unset, bool]
        if isinstance(self.swap_x_y, Unset):
            swap_x_y = UNSET
        else:
            swap_x_y = self.swap_x_y

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
        if swap_x_y is not UNSET:
            field_dict["swap_x_y"] = swap_x_y

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        export_type = ExportType(d.pop("export_type"))

        location_ids = []
        _location_ids = d.pop("location_ids", UNSET)
        for location_ids_item_data in _location_ids or []:
            location_ids_item = UUID(location_ids_item_data)

            location_ids.append(location_ids_item)

        file_ids = []
        _file_ids = d.pop("file_ids", UNSET)
        for file_ids_item_data in _file_ids or []:
            file_ids_item = UUID(file_ids_item_data)

            file_ids.append(file_ids_item)

        method_status_ids = cast(list[int], d.pop("method_status_ids", UNSET))

        method_type_ids = cast(list[int], d.pop("method_type_ids", UNSET))

        def _parse_srid(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        srid = _parse_srid(d.pop("srid", UNSET))

        def _parse_method_conducted_from(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                method_conducted_from_type_0 = isoparse(data)

                return method_conducted_from_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        method_conducted_from = _parse_method_conducted_from(d.pop("method_conducted_from", UNSET))

        def _parse_method_conducted_to(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                method_conducted_to_type_0 = isoparse(data)

                return method_conducted_to_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        method_conducted_to = _parse_method_conducted_to(d.pop("method_conducted_to", UNSET))

        def _parse_swap_x_y(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        swap_x_y = _parse_swap_x_y(d.pop("swap_x_y", UNSET))

        export = cls(
            export_type=export_type,
            location_ids=location_ids,
            file_ids=file_ids,
            method_status_ids=method_status_ids,
            method_type_ids=method_type_ids,
            srid=srid,
            method_conducted_from=method_conducted_from,
            method_conducted_to=method_conducted_to,
            swap_x_y=swap_x_y,
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
