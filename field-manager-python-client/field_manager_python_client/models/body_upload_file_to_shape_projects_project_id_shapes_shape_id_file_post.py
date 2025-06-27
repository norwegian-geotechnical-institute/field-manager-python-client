from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, File, Unset

T = TypeVar("T", bound="BodyUploadFileToShapeProjectsProjectIdShapesShapeIdFilePost")


@_attrs_define
class BodyUploadFileToShapeProjectsProjectIdShapesShapeIdFilePost:
    """
    Attributes:
        file (File):
        feature_index (Union[None, Unset, int, str]):
    """

    file: File
    feature_index: Union[None, Unset, int, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file = self.file.to_tuple()

        feature_index: Union[None, Unset, int, str]
        if isinstance(self.feature_index, Unset):
            feature_index = UNSET
        else:
            feature_index = self.feature_index

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file": file,
            }
        )
        if feature_index is not UNSET:
            field_dict["feature_index"] = feature_index

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("file", self.file.to_tuple()))

        if not isinstance(self.feature_index, Unset):
            if isinstance(self.feature_index, int):
                files.append(("feature_index", (None, str(self.feature_index).encode(), "text/plain")))
            elif isinstance(self.feature_index, str):
                files.append(("feature_index", (None, str(self.feature_index).encode(), "text/plain")))
            else:
                files.append(("feature_index", (None, str(self.feature_index).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file = File(payload=BytesIO(d.pop("file")))

        def _parse_feature_index(data: object) -> Union[None, Unset, int, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int, str], data)

        feature_index = _parse_feature_index(d.pop("feature_index", UNSET))

        body_upload_file_to_shape_projects_project_id_shapes_shape_id_file_post = cls(
            file=file,
            feature_index=feature_index,
        )

        body_upload_file_to_shape_projects_project_id_shapes_shape_id_file_post.additional_properties = d
        return body_upload_file_to_shape_projects_project_id_shapes_shape_id_file_post

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
