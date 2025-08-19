from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FileMin")


@_attrs_define
class FileMin:
    """
    Attributes:
        file_id (UUID):
        blob_url (str):
        original_filename (str):
        size (Union[None, Unset, int]):
    """

    file_id: UUID
    blob_url: str
    original_filename: str
    size: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_id = str(self.file_id)

        blob_url = self.blob_url

        original_filename = self.original_filename

        size: Union[None, Unset, int]
        if isinstance(self.size, Unset):
            size = UNSET
        else:
            size = self.size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file_id": file_id,
                "blob_url": blob_url,
                "original_filename": original_filename,
            }
        )
        if size is not UNSET:
            field_dict["size"] = size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file_id = UUID(d.pop("file_id"))

        blob_url = d.pop("blob_url")

        original_filename = d.pop("original_filename")

        def _parse_size(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        size = _parse_size(d.pop("size", UNSET))

        file_min = cls(
            file_id=file_id,
            blob_url=blob_url,
            original_filename=original_filename,
            size=size,
        )

        file_min.additional_properties = d
        return file_min

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
