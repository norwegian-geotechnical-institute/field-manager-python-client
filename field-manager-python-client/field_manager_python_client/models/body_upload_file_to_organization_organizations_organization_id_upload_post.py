from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, File, Unset

T = TypeVar("T", bound="BodyUploadFileToOrganizationOrganizationsOrganizationIdUploadPost")


@_attrs_define
class BodyUploadFileToOrganizationOrganizationsOrganizationIdUploadPost:
    """
    Attributes:
        file (File):
        comment (Union[None, Unset, str]):  Default: ''.
    """

    file: File
    comment: Union[None, Unset, str] = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file = self.file.to_tuple()

        comment: Union[None, Unset, str]
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file": file,
            }
        )
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        file = self.file.to_tuple()

        comment: Union[Unset, tuple[None, bytes, str]]

        if isinstance(self.comment, Unset):
            comment = UNSET
        elif isinstance(self.comment, str):
            comment = (None, str(self.comment).encode(), "text/plain")
        else:
            comment = (None, str(self.comment).encode(), "text/plain")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "file": file,
            }
        )
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file = File(payload=BytesIO(d.pop("file")))

        def _parse_comment(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        comment = _parse_comment(d.pop("comment", UNSET))

        body_upload_file_to_organization_organizations_organization_id_upload_post = cls(
            file=file,
            comment=comment,
        )

        body_upload_file_to_organization_organizations_organization_id_upload_post.additional_properties = d
        return body_upload_file_to_organization_organizations_organization_id_upload_post

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
