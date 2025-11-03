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

T = TypeVar("T", bound="MapLayoutVersionUpdate")


@_attrs_define
class MapLayoutVersionUpdate:
    """Map Layout Version Update. The map_layout_version_id in the url will override the map_layout_version_id in the body.

    Attributes:
        map_layout_version_id (None | Unset | UUID):
        name (None | str | Unset):
        file_id (None | Unset | UUID):
        paper_size (None | PaperSize | Unset):
        orientation (None | Orientation | Unset):
        dpi (int | None | Unset):
        background_map_layer (BackgroundMapLayer | None | Unset):
        scale (MapScale | None | Unset):
        boundary (None | str | Unset): Boundary as a Well-Known Text (WKT) 2D POLYGON. Example 'POLYGON((1184848.67
            8385496.52, 1184848.67 8386496.52,1185848.67 8386496.52, 1185848.67 8385496.52, 1184848.67 8385496.52))'
        srid (int | None | Unset): Spatial Reference Identifier (SRID) for the boundary box. Defaults to 3857 WGS 84 /
            Pseudo-Mercator (unit: meter). Default: 3857.
        rotation (float | None | Unset):
        report_number (None | str | Unset):
        report_date (datetime.date | None | Unset):
        client_name (None | str | Unset):
        description (None | str | Unset):
        drawn_by (None | str | Unset):
        approved_by (None | str | Unset):
        controlled_by (None | str | Unset):
        language (Language | Unset): ISO 639-2 language three-letter codes (set 2)
        date_format (DateFormat | None | Unset):
        show_method_status (bool | None | Unset):
    """

    map_layout_version_id: None | Unset | UUID = UNSET
    name: None | str | Unset = UNSET
    file_id: None | Unset | UUID = UNSET
    paper_size: None | PaperSize | Unset = UNSET
    orientation: None | Orientation | Unset = UNSET
    dpi: int | None | Unset = UNSET
    background_map_layer: BackgroundMapLayer | None | Unset = UNSET
    scale: MapScale | None | Unset = UNSET
    boundary: None | str | Unset = UNSET
    srid: int | None | Unset = 3857
    rotation: float | None | Unset = UNSET
    report_number: None | str | Unset = UNSET
    report_date: datetime.date | None | Unset = UNSET
    client_name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    drawn_by: None | str | Unset = UNSET
    approved_by: None | str | Unset = UNSET
    controlled_by: None | str | Unset = UNSET
    language: Language | Unset = UNSET
    date_format: DateFormat | None | Unset = UNSET
    show_method_status: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        map_layout_version_id: None | str | Unset
        if isinstance(self.map_layout_version_id, Unset):
            map_layout_version_id = UNSET
        elif isinstance(self.map_layout_version_id, UUID):
            map_layout_version_id = str(self.map_layout_version_id)
        else:
            map_layout_version_id = self.map_layout_version_id

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

        paper_size: None | str | Unset
        if isinstance(self.paper_size, Unset):
            paper_size = UNSET
        elif isinstance(self.paper_size, PaperSize):
            paper_size = self.paper_size.value
        else:
            paper_size = self.paper_size

        orientation: None | str | Unset
        if isinstance(self.orientation, Unset):
            orientation = UNSET
        elif isinstance(self.orientation, Orientation):
            orientation = self.orientation.value
        else:
            orientation = self.orientation

        dpi: int | None | Unset
        if isinstance(self.dpi, Unset):
            dpi = UNSET
        else:
            dpi = self.dpi

        background_map_layer: None | str | Unset
        if isinstance(self.background_map_layer, Unset):
            background_map_layer = UNSET
        elif isinstance(self.background_map_layer, BackgroundMapLayer):
            background_map_layer = self.background_map_layer.value
        else:
            background_map_layer = self.background_map_layer

        scale: None | str | Unset
        if isinstance(self.scale, Unset):
            scale = UNSET
        elif isinstance(self.scale, MapScale):
            scale = self.scale.value
        else:
            scale = self.scale

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

        rotation: float | None | Unset
        if isinstance(self.rotation, Unset):
            rotation = UNSET
        else:
            rotation = self.rotation

        report_number: None | str | Unset
        if isinstance(self.report_number, Unset):
            report_number = UNSET
        else:
            report_number = self.report_number

        report_date: None | str | Unset
        if isinstance(self.report_date, Unset):
            report_date = UNSET
        elif isinstance(self.report_date, datetime.date):
            report_date = self.report_date.isoformat()
        else:
            report_date = self.report_date

        client_name: None | str | Unset
        if isinstance(self.client_name, Unset):
            client_name = UNSET
        else:
            client_name = self.client_name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        drawn_by: None | str | Unset
        if isinstance(self.drawn_by, Unset):
            drawn_by = UNSET
        else:
            drawn_by = self.drawn_by

        approved_by: None | str | Unset
        if isinstance(self.approved_by, Unset):
            approved_by = UNSET
        else:
            approved_by = self.approved_by

        controlled_by: None | str | Unset
        if isinstance(self.controlled_by, Unset):
            controlled_by = UNSET
        else:
            controlled_by = self.controlled_by

        language: str | Unset = UNSET
        if not isinstance(self.language, Unset):
            language = self.language.value

        date_format: None | str | Unset
        if isinstance(self.date_format, Unset):
            date_format = UNSET
        elif isinstance(self.date_format, DateFormat):
            date_format = self.date_format.value
        else:
            date_format = self.date_format

        show_method_status: bool | None | Unset
        if isinstance(self.show_method_status, Unset):
            show_method_status = UNSET
        else:
            show_method_status = self.show_method_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if map_layout_version_id is not UNSET:
            field_dict["map_layout_version_id"] = map_layout_version_id
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
        if report_number is not UNSET:
            field_dict["report_number"] = report_number
        if report_date is not UNSET:
            field_dict["report_date"] = report_date
        if client_name is not UNSET:
            field_dict["client_name"] = client_name
        if description is not UNSET:
            field_dict["description"] = description
        if drawn_by is not UNSET:
            field_dict["drawn_by"] = drawn_by
        if approved_by is not UNSET:
            field_dict["approved_by"] = approved_by
        if controlled_by is not UNSET:
            field_dict["controlled_by"] = controlled_by
        if language is not UNSET:
            field_dict["language"] = language
        if date_format is not UNSET:
            field_dict["date_format"] = date_format
        if show_method_status is not UNSET:
            field_dict["show_method_status"] = show_method_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_map_layout_version_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                map_layout_version_id_type_0 = UUID(data)

                return map_layout_version_id_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | UUID, data)

        map_layout_version_id = _parse_map_layout_version_id(d.pop("map_layout_version_id", UNSET))

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

        def _parse_paper_size(data: object) -> None | PaperSize | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                paper_size_type_0 = PaperSize(data)

                return paper_size_type_0
            except:  # noqa: E722
                pass
            return cast(None | PaperSize | Unset, data)

        paper_size = _parse_paper_size(d.pop("paper_size", UNSET))

        def _parse_orientation(data: object) -> None | Orientation | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                orientation_type_0 = Orientation(data)

                return orientation_type_0
            except:  # noqa: E722
                pass
            return cast(None | Orientation | Unset, data)

        orientation = _parse_orientation(d.pop("orientation", UNSET))

        def _parse_dpi(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        dpi = _parse_dpi(d.pop("dpi", UNSET))

        def _parse_background_map_layer(data: object) -> BackgroundMapLayer | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                background_map_layer_type_0 = BackgroundMapLayer(data)

                return background_map_layer_type_0
            except:  # noqa: E722
                pass
            return cast(BackgroundMapLayer | None | Unset, data)

        background_map_layer = _parse_background_map_layer(d.pop("background_map_layer", UNSET))

        def _parse_scale(data: object) -> MapScale | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                scale_type_0 = MapScale(data)

                return scale_type_0
            except:  # noqa: E722
                pass
            return cast(MapScale | None | Unset, data)

        scale = _parse_scale(d.pop("scale", UNSET))

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

        def _parse_rotation(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        rotation = _parse_rotation(d.pop("rotation", UNSET))

        def _parse_report_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        report_number = _parse_report_number(d.pop("report_number", UNSET))

        def _parse_report_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                report_date_type_0 = isoparse(data).date()

                return report_date_type_0
            except:  # noqa: E722
                pass
            return cast(datetime.date | None | Unset, data)

        report_date = _parse_report_date(d.pop("report_date", UNSET))

        def _parse_client_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        client_name = _parse_client_name(d.pop("client_name", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_drawn_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        drawn_by = _parse_drawn_by(d.pop("drawn_by", UNSET))

        def _parse_approved_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        approved_by = _parse_approved_by(d.pop("approved_by", UNSET))

        def _parse_controlled_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        controlled_by = _parse_controlled_by(d.pop("controlled_by", UNSET))

        _language = d.pop("language", UNSET)
        language: Language | Unset
        if isinstance(_language, Unset):
            language = UNSET
        else:
            language = Language(_language)

        def _parse_date_format(data: object) -> DateFormat | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_format_type_0 = DateFormat(data)

                return date_format_type_0
            except:  # noqa: E722
                pass
            return cast(DateFormat | None | Unset, data)

        date_format = _parse_date_format(d.pop("date_format", UNSET))

        def _parse_show_method_status(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        show_method_status = _parse_show_method_status(d.pop("show_method_status", UNSET))

        map_layout_version_update = cls(
            map_layout_version_id=map_layout_version_id,
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
        )

        map_layout_version_update.additional_properties = d
        return map_layout_version_update

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
