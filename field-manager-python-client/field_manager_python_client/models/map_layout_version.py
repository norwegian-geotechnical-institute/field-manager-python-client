from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.background_map_layer import BackgroundMapLayer
from ..models.date_format import DateFormat
from ..models.language import Language
from ..models.map_scale import MapScale
from ..models.orientation import Orientation
from ..models.paper_size import PaperSize
from ..types import UNSET, Unset

T = TypeVar("T", bound="MapLayoutVersion")


@_attrs_define
class MapLayoutVersion:
    """Map Layout Version

    Attributes:
        map_layout_version_id (UUID):
        report_number (None | str):
        report_date (datetime.date | None):
        client_name (None | str):
        description (None | str):
        drawn_by (None | str):
        approved_by (None | str):
        controlled_by (None | str):
        language (Language): ISO 639-2 language three-letter codes (set 2)
        date_format (DateFormat): Date format
        show_method_status (bool):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        name (None | str | Unset):
        file_id (None | Unset | UUID):
        paper_size (PaperSize | Unset):
        orientation (Orientation | Unset): Page orientation. Default is landscape.
        dpi (int | Unset):  Default: 150.
        background_map_layer (BackgroundMapLayer | Unset): Background map layers. Default is STREET_MAP_WORLD.
        scale (MapScale | Unset): Map scales
                1:50
                1:100
                1:200
                1:500 (default)
                1:1000
                1:2000
                1:5000
                1:10000
        boundary (None | str | Unset):
        srid (int | None | Unset):
        rotation (float | Unset):  Default: 0.0.
        created_by (None | str | Unset):
        updated_by (None | str | Unset):
    """

    map_layout_version_id: UUID
    report_number: None | str
    report_date: datetime.date | None
    client_name: None | str
    description: None | str
    drawn_by: None | str
    approved_by: None | str
    controlled_by: None | str
    language: Language
    date_format: DateFormat
    show_method_status: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime
    name: None | str | Unset = UNSET
    file_id: None | Unset | UUID = UNSET
    paper_size: PaperSize | Unset = UNSET
    orientation: Orientation | Unset = UNSET
    dpi: int | Unset = 150
    background_map_layer: BackgroundMapLayer | Unset = UNSET
    scale: MapScale | Unset = UNSET
    boundary: None | str | Unset = UNSET
    srid: int | None | Unset = UNSET
    rotation: float | Unset = 0.0
    created_by: None | str | Unset = UNSET
    updated_by: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        map_layout_version_id = str(self.map_layout_version_id)

        report_number: None | str
        report_number = self.report_number

        report_date: None | str
        if isinstance(self.report_date, datetime.date):
            report_date = self.report_date.isoformat()
        else:
            report_date = self.report_date

        client_name: None | str
        client_name = self.client_name

        description: None | str
        description = self.description

        drawn_by: None | str
        drawn_by = self.drawn_by

        approved_by: None | str
        approved_by = self.approved_by

        controlled_by: None | str
        controlled_by = self.controlled_by

        language = self.language.value

        date_format = self.date_format.value

        show_method_status = self.show_method_status

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        file_id: None | str | Unset
        if isinstance(self.file_id, Unset):
            file_id = UNSET
        elif isinstance(self.file_id, UUID):
            file_id = str(self.file_id)
        else:
            file_id = self.file_id

        paper_size: str | Unset = UNSET
        if not isinstance(self.paper_size, Unset):
            paper_size = self.paper_size.value

        orientation: str | Unset = UNSET
        if not isinstance(self.orientation, Unset):
            orientation = self.orientation.value

        dpi = self.dpi

        background_map_layer: str | Unset = UNSET
        if not isinstance(self.background_map_layer, Unset):
            background_map_layer = self.background_map_layer.value

        scale: str | Unset = UNSET
        if not isinstance(self.scale, Unset):
            scale = self.scale.value

        boundary: None | str | Unset
        if isinstance(self.boundary, Unset):
            boundary = UNSET
        else:
            boundary = self.boundary

        srid: int | None | Unset
        if isinstance(self.srid, Unset):
            srid = UNSET
        else:
            srid = self.srid

        rotation = self.rotation

        created_by: None | str | Unset
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        else:
            created_by = self.created_by

        updated_by: None | str | Unset
        if isinstance(self.updated_by, Unset):
            updated_by = UNSET
        else:
            updated_by = self.updated_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "map_layout_version_id": map_layout_version_id,
                "report_number": report_number,
                "report_date": report_date,
                "client_name": client_name,
                "description": description,
                "drawn_by": drawn_by,
                "approved_by": approved_by,
                "controlled_by": controlled_by,
                "language": language,
                "date_format": date_format,
                "show_method_status": show_method_status,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if file_id is not UNSET:
            field_dict["file_id"] = file_id
        if paper_size is not UNSET:
            field_dict["paper_size"] = paper_size
        if orientation is not UNSET:
            field_dict["orientation"] = orientation
        if dpi is not UNSET:
            field_dict["dpi"] = dpi
        if background_map_layer is not UNSET:
            field_dict["background_map_layer"] = background_map_layer
        if scale is not UNSET:
            field_dict["scale"] = scale
        if boundary is not UNSET:
            field_dict["boundary"] = boundary
        if srid is not UNSET:
            field_dict["srid"] = srid
        if rotation is not UNSET:
            field_dict["rotation"] = rotation
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if updated_by is not UNSET:
            field_dict["updated_by"] = updated_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        map_layout_version_id = UUID(d.pop("map_layout_version_id"))

        def _parse_report_number(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        report_number = _parse_report_number(d.pop("report_number"))

        def _parse_report_date(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                report_date_type_0 = isoparse(data).date()

                return report_date_type_0
            except:  # noqa: E722
                pass
            return cast(datetime.date | None, data)

        report_date = _parse_report_date(d.pop("report_date"))

        def _parse_client_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        client_name = _parse_client_name(d.pop("client_name"))

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        def _parse_drawn_by(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        drawn_by = _parse_drawn_by(d.pop("drawn_by"))

        def _parse_approved_by(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        approved_by = _parse_approved_by(d.pop("approved_by"))

        def _parse_controlled_by(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        controlled_by = _parse_controlled_by(d.pop("controlled_by"))

        language = Language(d.pop("language"))

        date_format = DateFormat(d.pop("date_format"))

        show_method_status = d.pop("show_method_status")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_file_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                file_id_type_0 = UUID(data)

                return file_id_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | UUID, data)

        file_id = _parse_file_id(d.pop("file_id", UNSET))

        _paper_size = d.pop("paper_size", UNSET)
        paper_size: PaperSize | Unset
        if isinstance(_paper_size, Unset):
            paper_size = UNSET
        else:
            paper_size = PaperSize(_paper_size)

        _orientation = d.pop("orientation", UNSET)
        orientation: Orientation | Unset
        if isinstance(_orientation, Unset):
            orientation = UNSET
        else:
            orientation = Orientation(_orientation)

        dpi = d.pop("dpi", UNSET)

        _background_map_layer = d.pop("background_map_layer", UNSET)
        background_map_layer: BackgroundMapLayer | Unset
        if isinstance(_background_map_layer, Unset):
            background_map_layer = UNSET
        else:
            background_map_layer = BackgroundMapLayer(_background_map_layer)

        _scale = d.pop("scale", UNSET)
        scale: MapScale | Unset
        if isinstance(_scale, Unset):
            scale = UNSET
        else:
            scale = MapScale(_scale)

        def _parse_boundary(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        boundary = _parse_boundary(d.pop("boundary", UNSET))

        def _parse_srid(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        srid = _parse_srid(d.pop("srid", UNSET))

        rotation = d.pop("rotation", UNSET)

        def _parse_created_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_by = _parse_created_by(d.pop("created_by", UNSET))

        def _parse_updated_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        updated_by = _parse_updated_by(d.pop("updated_by", UNSET))

        map_layout_version = cls(
            map_layout_version_id=map_layout_version_id,
            report_number=report_number,
            report_date=report_date,
            client_name=client_name,
            description=description,
            drawn_by=drawn_by,
            approved_by=approved_by,
            controlled_by=controlled_by,
            language=language,
            date_format=date_format,
            show_method_status=show_method_status,
            created_at=created_at,
            updated_at=updated_at,
            name=name,
            file_id=file_id,
            paper_size=paper_size,
            orientation=orientation,
            dpi=dpi,
            background_map_layer=background_map_layer,
            scale=scale,
            boundary=boundary,
            srid=srid,
            rotation=rotation,
            created_by=created_by,
            updated_by=updated_by,
        )

        map_layout_version.additional_properties = d
        return map_layout_version

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
