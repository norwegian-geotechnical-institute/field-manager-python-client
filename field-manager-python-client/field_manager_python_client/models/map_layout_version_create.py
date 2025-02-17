import datetime
from typing import Any, TypeVar, Union, cast
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

T = TypeVar("T", bound="MapLayoutVersionCreate")


@_attrs_define
class MapLayoutVersionCreate:
    """
    Attributes:
        name (Union[None, Unset, str]):
        file_id (Union[None, UUID, Unset]):
        paper_size (Union[Unset, PaperSize]):
        orientation (Union[Unset, Orientation]): Page orientation. Default is landscape.
        dpi (Union[Unset, int]):  Default: 150.
        background_map_layer (Union[Unset, BackgroundMapLayer]): Background map layers. Default is STREET_MAP_WORLD.
        scale (Union[Unset, MapScale]): Map scales
                1:50
                1:100
                1:500 (default)
                1:1000
                1:2000
                1:5000
                1:10000
        boundary (Union[None, Unset, str]): Boundary as a Well-Known Text (WKT) 2D POLYGON. Example 'POLYGON((1184848.67
            8385496.52, 1184848.67 8386496.52,1185848.67 8386496.52, 1185848.67 8385496.52, 1184848.67 8385496.52))'
        srid (Union[None, Unset, int]): Spatial Reference Identifier (SRID) for the boundary box. Defaults to 3857 WGS
            84 / Pseudo-Mercator (unit: meter). Default: 3857.
        rotation (Union[Unset, float]):  Default: 0.0.
        report_number (Union[None, Unset, str]):
        report_date (Union[None, Unset, datetime.date]):
        client_name (Union[None, Unset, str]):
        description (Union[None, Unset, str]):
        drawn_by (Union[None, Unset, str]):
        approved_by (Union[None, Unset, str]):
        controlled_by (Union[None, Unset, str]):
        language (Union[Unset, Language]): ISO 639-2 language three-letter codes (set 2)
        date_format (Union[Unset, DateFormat]): Date format
        show_method_status (Union[Unset, bool]):  Default: False.
    """

    name: Union[None, Unset, str] = UNSET
    file_id: Union[None, UUID, Unset] = UNSET
    paper_size: Union[Unset, PaperSize] = UNSET
    orientation: Union[Unset, Orientation] = UNSET
    dpi: Union[Unset, int] = 150
    background_map_layer: Union[Unset, BackgroundMapLayer] = UNSET
    scale: Union[Unset, MapScale] = UNSET
    boundary: Union[None, Unset, str] = UNSET
    srid: Union[None, Unset, int] = 3857
    rotation: Union[Unset, float] = 0.0
    report_number: Union[None, Unset, str] = UNSET
    report_date: Union[None, Unset, datetime.date] = UNSET
    client_name: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    drawn_by: Union[None, Unset, str] = UNSET
    approved_by: Union[None, Unset, str] = UNSET
    controlled_by: Union[None, Unset, str] = UNSET
    language: Union[Unset, Language] = UNSET
    date_format: Union[Unset, DateFormat] = UNSET
    show_method_status: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        file_id: Union[None, Unset, str]
        if isinstance(self.file_id, Unset):
            file_id = UNSET
        elif isinstance(self.file_id, UUID):
            file_id = str(self.file_id)
        else:
            file_id = self.file_id

        paper_size: Union[Unset, str] = UNSET
        if not isinstance(self.paper_size, Unset):
            paper_size = self.paper_size.value

        orientation: Union[Unset, str] = UNSET
        if not isinstance(self.orientation, Unset):
            orientation = self.orientation.value

        dpi = self.dpi

        background_map_layer: Union[Unset, str] = UNSET
        if not isinstance(self.background_map_layer, Unset):
            background_map_layer = self.background_map_layer.value

        scale: Union[Unset, str] = UNSET
        if not isinstance(self.scale, Unset):
            scale = self.scale.value

        boundary: Union[None, Unset, str]
        if isinstance(self.boundary, Unset):
            boundary = UNSET
        else:
            boundary = self.boundary

        srid: Union[None, Unset, int]
        if isinstance(self.srid, Unset):
            srid = UNSET
        else:
            srid = self.srid

        rotation = self.rotation

        report_number: Union[None, Unset, str]
        if isinstance(self.report_number, Unset):
            report_number = UNSET
        else:
            report_number = self.report_number

        report_date: Union[None, Unset, str]
        if isinstance(self.report_date, Unset):
            report_date = UNSET
        elif isinstance(self.report_date, datetime.date):
            report_date = self.report_date.isoformat()
        else:
            report_date = self.report_date

        client_name: Union[None, Unset, str]
        if isinstance(self.client_name, Unset):
            client_name = UNSET
        else:
            client_name = self.client_name

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        drawn_by: Union[None, Unset, str]
        if isinstance(self.drawn_by, Unset):
            drawn_by = UNSET
        else:
            drawn_by = self.drawn_by

        approved_by: Union[None, Unset, str]
        if isinstance(self.approved_by, Unset):
            approved_by = UNSET
        else:
            approved_by = self.approved_by

        controlled_by: Union[None, Unset, str]
        if isinstance(self.controlled_by, Unset):
            controlled_by = UNSET
        else:
            controlled_by = self.controlled_by

        language: Union[Unset, str] = UNSET
        if not isinstance(self.language, Unset):
            language = self.language.value

        date_format: Union[Unset, str] = UNSET
        if not isinstance(self.date_format, Unset):
            date_format = self.date_format.value

        show_method_status = self.show_method_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_file_id(data: object) -> Union[None, UUID, Unset]:
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
            return cast(Union[None, UUID, Unset], data)

        file_id = _parse_file_id(d.pop("file_id", UNSET))

        _paper_size = d.pop("paper_size", UNSET)
        paper_size: Union[Unset, PaperSize]
        if isinstance(_paper_size, Unset):
            paper_size = UNSET
        else:
            paper_size = PaperSize(_paper_size)

        _orientation = d.pop("orientation", UNSET)
        orientation: Union[Unset, Orientation]
        if isinstance(_orientation, Unset):
            orientation = UNSET
        else:
            orientation = Orientation(_orientation)

        dpi = d.pop("dpi", UNSET)

        _background_map_layer = d.pop("background_map_layer", UNSET)
        background_map_layer: Union[Unset, BackgroundMapLayer]
        if isinstance(_background_map_layer, Unset):
            background_map_layer = UNSET
        else:
            background_map_layer = BackgroundMapLayer(_background_map_layer)

        _scale = d.pop("scale", UNSET)
        scale: Union[Unset, MapScale]
        if isinstance(_scale, Unset):
            scale = UNSET
        else:
            scale = MapScale(_scale)

        def _parse_boundary(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        boundary = _parse_boundary(d.pop("boundary", UNSET))

        def _parse_srid(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        srid = _parse_srid(d.pop("srid", UNSET))

        rotation = d.pop("rotation", UNSET)

        def _parse_report_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        report_number = _parse_report_number(d.pop("report_number", UNSET))

        def _parse_report_date(data: object) -> Union[None, Unset, datetime.date]:
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
            return cast(Union[None, Unset, datetime.date], data)

        report_date = _parse_report_date(d.pop("report_date", UNSET))

        def _parse_client_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        client_name = _parse_client_name(d.pop("client_name", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_drawn_by(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        drawn_by = _parse_drawn_by(d.pop("drawn_by", UNSET))

        def _parse_approved_by(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        approved_by = _parse_approved_by(d.pop("approved_by", UNSET))

        def _parse_controlled_by(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        controlled_by = _parse_controlled_by(d.pop("controlled_by", UNSET))

        _language = d.pop("language", UNSET)
        language: Union[Unset, Language]
        if isinstance(_language, Unset):
            language = UNSET
        else:
            language = Language(_language)

        _date_format = d.pop("date_format", UNSET)
        date_format: Union[Unset, DateFormat]
        if isinstance(_date_format, Unset):
            date_format = UNSET
        else:
            date_format = DateFormat(_date_format)

        show_method_status = d.pop("show_method_status", UNSET)

        map_layout_version_create = cls(
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

        map_layout_version_create.additional_properties = d
        return map_layout_version_create

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
