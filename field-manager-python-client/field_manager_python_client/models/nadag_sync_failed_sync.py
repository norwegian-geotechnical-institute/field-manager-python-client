from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.nadag_sync_failed_entity_type import NadagSyncFailedEntityType
from ..models.sync_status import SyncStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="NadagSyncFailedSync")


@_attrs_define
class NadagSyncFailedSync:
    """
    Attributes:
        entity_type (NadagSyncFailedEntityType):
        sync_id (UUID):
        sync_command_id (UUID):
        sync_status (SyncStatus): Sync status

            (
                PENDING=Sync has not started yet,
                IN_PROGRESS=Sync is in progress,
                SUCCESS=Sync has completed successfully without errors,
                FAILED=Sync has completed with errors,
            )
        error_message (None | str | Unset):
        error_data (Any | None | Unset):
        external_id (None | str | Unset):
        project_id (None | Unset | UUID):
        file_id (None | Unset | UUID):
        file_name (None | str | Unset):
        location_id (None | Unset | UUID):
        location_name (None | str | Unset):
        synced_at (datetime.datetime | None | Unset):
        updated_at (datetime.datetime | None | Unset):
    """

    entity_type: NadagSyncFailedEntityType
    sync_id: UUID
    sync_command_id: UUID
    sync_status: SyncStatus
    error_message: None | str | Unset = UNSET
    error_data: Any | None | Unset = UNSET
    external_id: None | str | Unset = UNSET
    project_id: None | Unset | UUID = UNSET
    file_id: None | Unset | UUID = UNSET
    file_name: None | str | Unset = UNSET
    location_id: None | Unset | UUID = UNSET
    location_name: None | str | Unset = UNSET
    synced_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entity_type = self.entity_type.value

        sync_id = str(self.sync_id)

        sync_command_id = str(self.sync_command_id)

        sync_status = self.sync_status.value

        error_message: None | str | Unset
        if isinstance(self.error_message, Unset):
            error_message = UNSET
        else:
            error_message = self.error_message

        error_data: Any | None | Unset
        if isinstance(self.error_data, Unset):
            error_data = UNSET
        else:
            error_data = self.error_data

        external_id: None | str | Unset
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        project_id: None | str | Unset
        if isinstance(self.project_id, Unset):
            project_id = UNSET
        elif isinstance(self.project_id, UUID):
            project_id = str(self.project_id)
        else:
            project_id = self.project_id

        file_id: None | str | Unset
        if isinstance(self.file_id, Unset):
            file_id = UNSET
        elif isinstance(self.file_id, UUID):
            file_id = str(self.file_id)
        else:
            file_id = self.file_id

        file_name: None | str | Unset
        if isinstance(self.file_name, Unset):
            file_name = UNSET
        else:
            file_name = self.file_name

        location_id: None | str | Unset
        if isinstance(self.location_id, Unset):
            location_id = UNSET
        elif isinstance(self.location_id, UUID):
            location_id = str(self.location_id)
        else:
            location_id = self.location_id

        location_name: None | str | Unset
        if isinstance(self.location_name, Unset):
            location_name = UNSET
        else:
            location_name = self.location_name

        synced_at: None | str | Unset
        if isinstance(self.synced_at, Unset):
            synced_at = UNSET
        elif isinstance(self.synced_at, datetime.datetime):
            synced_at = self.synced_at.isoformat()
        else:
            synced_at = self.synced_at

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "entity_type": entity_type,
                "sync_id": sync_id,
                "sync_command_id": sync_command_id,
                "sync_status": sync_status,
            }
        )
        if error_message is not UNSET:
            field_dict["error_message"] = error_message
        if error_data is not UNSET:
            field_dict["error_data"] = error_data
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if file_id is not UNSET:
            field_dict["file_id"] = file_id
        if file_name is not UNSET:
            field_dict["file_name"] = file_name
        if location_id is not UNSET:
            field_dict["location_id"] = location_id
        if location_name is not UNSET:
            field_dict["location_name"] = location_name
        if synced_at is not UNSET:
            field_dict["synced_at"] = synced_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        entity_type = NadagSyncFailedEntityType(d.pop("entity_type"))

        sync_id = UUID(d.pop("sync_id"))

        sync_command_id = UUID(d.pop("sync_command_id"))

        sync_status = SyncStatus(d.pop("sync_status"))

        def _parse_error_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_message = _parse_error_message(d.pop("error_message", UNSET))

        def _parse_error_data(data: object) -> Any | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Any | None | Unset, data)

        error_data = _parse_error_data(d.pop("error_data", UNSET))

        def _parse_external_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_id = _parse_external_id(d.pop("external_id", UNSET))

        def _parse_project_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                project_id_type_0 = UUID(data)

                return project_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        project_id = _parse_project_id(d.pop("project_id", UNSET))

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
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        file_id = _parse_file_id(d.pop("file_id", UNSET))

        def _parse_file_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_name = _parse_file_name(d.pop("file_name", UNSET))

        def _parse_location_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                location_id_type_0 = UUID(data)

                return location_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        location_id = _parse_location_id(d.pop("location_id", UNSET))

        def _parse_location_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_name = _parse_location_name(d.pop("location_name", UNSET))

        def _parse_synced_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                synced_at_type_0 = datetime.datetime.fromisoformat(data)

                return synced_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        synced_at = _parse_synced_at(d.pop("synced_at", UNSET))

        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = datetime.datetime.fromisoformat(data)

                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))

        nadag_sync_failed_sync = cls(
            entity_type=entity_type,
            sync_id=sync_id,
            sync_command_id=sync_command_id,
            sync_status=sync_status,
            error_message=error_message,
            error_data=error_data,
            external_id=external_id,
            project_id=project_id,
            file_id=file_id,
            file_name=file_name,
            location_id=location_id,
            location_name=location_name,
            synced_at=synced_at,
            updated_at=updated_at,
        )

        nadag_sync_failed_sync.additional_properties = d
        return nadag_sync_failed_sync

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
