import datetime
from collections.abc import Mapping
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

T = TypeVar("T", bound="MapLayoutVersion")


@_attrs_define
class MapLayoutVersion:
    """Map Layout Version

    Attributes:
        map_layout_version_id (UUID):
        report_number (Union[None, str]):
        report_date (Union[None, datetime.date]):
        client_name (Union[None, str]):
        description (Union[None, str]):
        drawn_by (Union[None, str]):
        approved_by (Union[None, str]):
        controlled_by (Union[None, str]):
        language (Language): ISO 639-2 language three-letter codes (set 2)
        date_format (DateFormat): Date format
        show_method_status (bool):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        name (Union[None, Unset, str]):
        file_id (Union[None, UUID, Unset]):
        paper_size (Union[Unset, PaperSize]):
        orientation (Union[Unset, Orientation]): Page orientation. Default is landscape.
        dpi (Union[Unset, int]):  Default: 150.
        background_map_layer (Union[Unset, BackgroundMapLayer]): Background map layers. Default is STREET_MAP_WORLD.
        scale (Union[Unset, MapScale]): Map scales
                1:50
                1:100
                1:200
                1:500 (default)
                1:1000
                1:2000
                1:5000
                1:10000
        boundary (Union[None, Unset, str]):
        srid (Union[None, Unset, int]):
        rotation (Union[Unset, float]):  Default: 0.0.
        created_by (Union[None, Unset, str]):
        updated_by (Union[None, Unset, str]):
    """

    map_layout_version_id: UUID
    report_number: Union[None, str]
    report_date: Union[None, datetime.date]
    client_name: Union[None, str]
    description: Union[None, str]
    drawn_by: Union[None, str]
    approved_by: Union[None, str]
    controlled_by: Union[None, str]
    language: Language
    date_format: DateFormat
    show_method_status: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime
    name: Union[None, Unset, str] = UNSET
    file_id: Union[None, UUID, Unset] = UNSET
    paper_size: Union[Unset, PaperSize] = UNSET
    orientation: Union[Unset, Orientation] = UNSET
    dpi: Union[Unset, int] = 150
    background_map_layer: Union[Unset, BackgroundMapLayer] = UNSET
    scale: Union[Unset, MapScale] = UNSET
    boundary: Union[None, Unset, str] = UNSET
    srid: Union[None, Unset, int] = UNSET
    rotation: Union[Unset, float] = 0.0
    created_by: Union[None, Unset, str] = UNSET
    updated_by: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        map_layout_version_id = str(self.map_layout_version_id)

        report_number: Union[None, str]
        report_number = self.report_number

        report_date: Union[None, str]
        if isinstance(self.report_date, datetime.date):
            report_date = self.report_date.isoformat()
        else:
            report_date = self.report_date

        client_name: Union[None, str]
        client_name = self.client_name

        description: Union[None, str]
        description = self.description

        drawn_by: Union[None, str]
        drawn_by = self.drawn_by

        approved_by: Union[None, str]
        approved_by = self.approved_by

        controlled_by: Union[None, str]
        controlled_by = self.controlled_by

        language = self.language.value

        date_format = self.date_format.value

        show_method_status = self.show_method_status

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

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

        created_by: Union[None, Unset, str]
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        else:
            created_by = self.created_by

        updated_by: Union[None, Unset, str]
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

        def _parse_report_number(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        report_number = _parse_report_number(d.pop("report_number"))

        def _parse_report_date(data: object) -> Union[None, datetime.date]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                report_date_type_0 = isoparse(data).date()

                return report_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.date], data)

        report_date = _parse_report_date(d.pop("report_date"))

        def _parse_client_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        client_name = _parse_client_name(d.pop("client_name"))

        def _parse_description(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        description = _parse_description(d.pop("description"))

        def _parse_drawn_by(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        drawn_by = _parse_drawn_by(d.pop("drawn_by"))

        def _parse_approved_by(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        approved_by = _parse_approved_by(d.pop("approved_by"))

        def _parse_controlled_by(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        controlled_by = _parse_controlled_by(d.pop("controlled_by"))

        language = Language(d.pop("language"))

        date_format = DateFormat(d.pop("date_format"))

        show_method_status = d.pop("show_method_status")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

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

        def _parse_created_by(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        created_by = _parse_created_by(d.pop("created_by", UNSET))

        def _parse_updated_by(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

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
