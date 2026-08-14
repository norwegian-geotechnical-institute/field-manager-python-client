from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NadagSyncReadyReport")


@_attrs_define
class NadagSyncReadyReport:
    """
    Attributes:
        file_id (UUID):
        name (str):
        original_filename (str):
        last_updated_at (datetime.datetime | None | Unset):
        last_successful_sync_at (datetime.datetime | None | Unset):
    """

    file_id: UUID
    name: str
    original_filename: str
    last_updated_at: datetime.datetime | None | Unset = UNSET
    last_successful_sync_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_id = str(self.file_id)

        name = self.name

        original_filename = self.original_filename

        last_updated_at: None | str | Unset
        if isinstance(self.last_updated_at, Unset):
            last_updated_at = UNSET
        elif isinstance(self.last_updated_at, datetime.datetime):
            last_updated_at = self.last_updated_at.isoformat()
        else:
            last_updated_at = self.last_updated_at

        last_successful_sync_at: None | str | Unset
        if isinstance(self.last_successful_sync_at, Unset):
            last_successful_sync_at = UNSET
        elif isinstance(self.last_successful_sync_at, datetime.datetime):
            last_successful_sync_at = self.last_successful_sync_at.isoformat()
        else:
            last_successful_sync_at = self.last_successful_sync_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file_id": file_id,
                "name": name,
                "original_filename": original_filename,
            }
        )
        if last_updated_at is not UNSET:
            field_dict["last_updated_at"] = last_updated_at
        if last_successful_sync_at is not UNSET:
            field_dict["last_successful_sync_at"] = last_successful_sync_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file_id = UUID(d.pop("file_id"))

        name = d.pop("name")

        original_filename = d.pop("original_filename")

        def _parse_last_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_updated_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_updated_at = _parse_last_updated_at(d.pop("last_updated_at", UNSET))

        def _parse_last_successful_sync_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_successful_sync_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_successful_sync_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_successful_sync_at = _parse_last_successful_sync_at(d.pop("last_successful_sync_at", UNSET))

        nadag_sync_ready_report = cls(
            file_id=file_id,
            name=name,
            original_filename=original_filename,
            last_updated_at=last_updated_at,
            last_successful_sync_at=last_successful_sync_at,
        )

        nadag_sync_ready_report.additional_properties = d
        return nadag_sync_ready_report

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
