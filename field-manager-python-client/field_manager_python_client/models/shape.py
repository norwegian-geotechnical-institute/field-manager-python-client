from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.shape_color import ShapeColor
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_min import FileMin
    from ..models.sub_shape import SubShape


T = TypeVar("T", bound="Shape")


@_attrs_define
class Shape:
    """
    Attributes:
        shape_id (UUID):
        project_id (UUID):
        input_geometry_file (FileMin):
        attached_file_ids (list[UUID]):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        created_by (None | str):
        updated_by (None | str):
        name (str):
        line_thickness (int | None | Unset):
        color (None | ShapeColor | Unset):
        sub_shapes (list[SubShape] | Unset):
    """

    shape_id: UUID
    project_id: UUID
    input_geometry_file: FileMin
    attached_file_ids: list[UUID]
    created_at: datetime.datetime
    updated_at: datetime.datetime
    created_by: None | str
    updated_by: None | str
    name: str
    line_thickness: int | None | Unset = UNSET
    color: None | ShapeColor | Unset = UNSET
    sub_shapes: list[SubShape] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        shape_id = str(self.shape_id)

        project_id = str(self.project_id)

        input_geometry_file = self.input_geometry_file.to_dict()

        attached_file_ids = []
        for attached_file_ids_item_data in self.attached_file_ids:
            attached_file_ids_item = str(attached_file_ids_item_data)
            attached_file_ids.append(attached_file_ids_item)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        created_by: None | str
        created_by = self.created_by

        updated_by: None | str
        updated_by = self.updated_by

        name = self.name

        line_thickness: int | None | Unset
        if isinstance(self.line_thickness, Unset):
            line_thickness = UNSET
        else:
            line_thickness = self.line_thickness

        color: None | str | Unset
        if isinstance(self.color, Unset):
            color = UNSET
        elif isinstance(self.color, ShapeColor):
            color = self.color.value
        else:
            color = self.color

        sub_shapes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sub_shapes, Unset):
            sub_shapes = []
            for sub_shapes_item_data in self.sub_shapes:
                sub_shapes_item = sub_shapes_item_data.to_dict()
                sub_shapes.append(sub_shapes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "shape_id": shape_id,
                "project_id": project_id,
                "input_geometry_file": input_geometry_file,
                "attached_file_ids": attached_file_ids,
                "created_at": created_at,
                "updated_at": updated_at,
                "created_by": created_by,
                "updated_by": updated_by,
                "name": name,
            }
        )
        if line_thickness is not UNSET:
            field_dict["line_thickness"] = line_thickness
        if color is not UNSET:
            field_dict["color"] = color
        if sub_shapes is not UNSET:
            field_dict["sub_shapes"] = sub_shapes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file_min import FileMin
        from ..models.sub_shape import SubShape

        d = dict(src_dict)
        shape_id = UUID(d.pop("shape_id"))

        project_id = UUID(d.pop("project_id"))

        input_geometry_file = FileMin.from_dict(d.pop("input_geometry_file"))

        attached_file_ids = []
        _attached_file_ids = d.pop("attached_file_ids")
        for attached_file_ids_item_data in _attached_file_ids:
            attached_file_ids_item = UUID(attached_file_ids_item_data)

            attached_file_ids.append(attached_file_ids_item)

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        def _parse_created_by(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        created_by = _parse_created_by(d.pop("created_by"))

        def _parse_updated_by(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        updated_by = _parse_updated_by(d.pop("updated_by"))

        name = d.pop("name")

        def _parse_line_thickness(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        line_thickness = _parse_line_thickness(d.pop("line_thickness", UNSET))

        def _parse_color(data: object) -> None | ShapeColor | Unset:
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
            return cast(None | ShapeColor | Unset, data)

        color = _parse_color(d.pop("color", UNSET))

        sub_shapes = []
        _sub_shapes = d.pop("sub_shapes", UNSET)
        for sub_shapes_item_data in _sub_shapes or []:
            sub_shapes_item = SubShape.from_dict(sub_shapes_item_data)

            sub_shapes.append(sub_shapes_item)

        shape = cls(
            shape_id=shape_id,
            project_id=project_id,
            input_geometry_file=input_geometry_file,
            attached_file_ids=attached_file_ids,
            created_at=created_at,
            updated_at=updated_at,
            created_by=created_by,
            updated_by=updated_by,
            name=name,
            line_thickness=line_thickness,
            color=color,
            sub_shapes=sub_shapes,
        )

        shape.additional_properties = d
        return shape

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
