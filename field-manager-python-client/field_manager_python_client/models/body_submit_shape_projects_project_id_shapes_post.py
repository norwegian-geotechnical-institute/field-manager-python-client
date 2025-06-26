from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.shape_color import ShapeColor
from ..types import UNSET, File, Unset

T = TypeVar("T", bound="BodySubmitShapeProjectsProjectIdShapesPost")


@_attrs_define
class BodySubmitShapeProjectsProjectIdShapesPost:
    """
    Attributes:
        name (str):
        file (File):
        color (Union[None, ShapeColor, Unset, str]): One of the ShapeColor enum values (e.g. 'NEON_RED'), or
            'null'/''/None to use the default color in the geojson
        line_thickness (Union[None, Unset, int, str]): An integer (e.g. 3), , or 'null'/''/None to use the default color
            in the geojson
        srid (Union[None, Unset, str]):
    """

    name: str
    file: File
    color: Union[None, ShapeColor, Unset, str] = UNSET
    line_thickness: Union[None, Unset, int, str] = UNSET
    srid: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        file = self.file.to_tuple()

        color: Union[None, Unset, str]
        if isinstance(self.color, Unset):
            color = UNSET
        elif isinstance(self.color, ShapeColor):
            color = self.color.value
        else:
            color = self.color

        line_thickness: Union[None, Unset, int, str]
        if isinstance(self.line_thickness, Unset):
            line_thickness = UNSET
        else:
            line_thickness = self.line_thickness

        srid: Union[None, Unset, str]
        if isinstance(self.srid, Unset):
            srid = UNSET
        else:
            srid = self.srid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "file": file,
            }
        )
        if color is not UNSET:
            field_dict["color"] = color
        if line_thickness is not UNSET:
            field_dict["line_thickness"] = line_thickness
        if srid is not UNSET:
            field_dict["srid"] = srid

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("name", (None, str(self.name).encode(), "text/plain")))

        files.append(("file", self.file.to_tuple()))

        if not isinstance(self.color, Unset):
            if isinstance(self.color, ShapeColor):
                files.append(("color", (None, str(self.color.value).encode(), "text/plain")))
            elif isinstance(self.color, str):
                files.append(("color", (None, str(self.color).encode(), "text/plain")))
            else:
                files.append(("color", (None, str(self.color).encode(), "text/plain")))

        if not isinstance(self.line_thickness, Unset):
            if isinstance(self.line_thickness, int):
                files.append(("line_thickness", (None, str(self.line_thickness).encode(), "text/plain")))
            elif isinstance(self.line_thickness, str):
                files.append(("line_thickness", (None, str(self.line_thickness).encode(), "text/plain")))
            else:
                files.append(("line_thickness", (None, str(self.line_thickness).encode(), "text/plain")))

        if not isinstance(self.srid, Unset):
            if isinstance(self.srid, str):
                files.append(("srid", (None, str(self.srid).encode(), "text/plain")))
            else:
                files.append(("srid", (None, str(self.srid).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        file = File(payload=BytesIO(d.pop("file")))

        def _parse_color(data: object) -> Union[None, ShapeColor, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                color_type_0 = ShapeColor(data)

                return color_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, ShapeColor, Unset, str], data)

        color = _parse_color(d.pop("color", UNSET))

        def _parse_line_thickness(data: object) -> Union[None, Unset, int, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int, str], data)

        line_thickness = _parse_line_thickness(d.pop("line_thickness", UNSET))

        def _parse_srid(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        srid = _parse_srid(d.pop("srid", UNSET))

        body_submit_shape_projects_project_id_shapes_post = cls(
            name=name,
            file=file,
            color=color,
            line_thickness=line_thickness,
            srid=srid,
        )

        body_submit_shape_projects_project_id_shapes_post.additional_properties = d
        return body_submit_shape_projects_project_id_shapes_post

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
