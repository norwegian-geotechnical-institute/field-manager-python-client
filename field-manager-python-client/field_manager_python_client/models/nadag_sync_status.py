from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.nadag_sync_overview_status import NadagSyncOverviewStatus
from ..models.sync_status import SyncStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nadag_sync_status_counts import NadagSyncStatusCounts


T = TypeVar("T", bound="NadagSyncStatus")


@_attrs_define
class NadagSyncStatus:
    """
    Attributes:
        project_id (UUID):
        status (NadagSyncOverviewStatus):
        required_to_sync (bool):
        active_sync (bool):
        has_blockers (bool):
        counts (NadagSyncStatusCounts):
        last_successful_sync_at (datetime.datetime | None | Unset):
        latest_sync_status (None | SyncStatus | Unset):
    """

    project_id: UUID
    status: NadagSyncOverviewStatus
    required_to_sync: bool
    active_sync: bool
    has_blockers: bool
    counts: NadagSyncStatusCounts
    last_successful_sync_at: datetime.datetime | None | Unset = UNSET
    latest_sync_status: None | SyncStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_id = str(self.project_id)

        status = self.status.value

        required_to_sync = self.required_to_sync

        active_sync = self.active_sync

        has_blockers = self.has_blockers

        counts = self.counts.to_dict()

        last_successful_sync_at: None | str | Unset
        if isinstance(self.last_successful_sync_at, Unset):
            last_successful_sync_at = UNSET
        elif isinstance(self.last_successful_sync_at, datetime.datetime):
            last_successful_sync_at = self.last_successful_sync_at.isoformat()
        else:
            last_successful_sync_at = self.last_successful_sync_at

        latest_sync_status: None | str | Unset
        if isinstance(self.latest_sync_status, Unset):
            latest_sync_status = UNSET
        elif isinstance(self.latest_sync_status, SyncStatus):
            latest_sync_status = self.latest_sync_status.value
        else:
            latest_sync_status = self.latest_sync_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "project_id": project_id,
                "status": status,
                "required_to_sync": required_to_sync,
                "active_sync": active_sync,
                "has_blockers": has_blockers,
                "counts": counts,
            }
        )
        if last_successful_sync_at is not UNSET:
            field_dict["last_successful_sync_at"] = last_successful_sync_at
        if latest_sync_status is not UNSET:
            field_dict["latest_sync_status"] = latest_sync_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nadag_sync_status_counts import NadagSyncStatusCounts

        d = dict(src_dict)
        project_id = UUID(d.pop("project_id"))

        status = NadagSyncOverviewStatus(d.pop("status"))

        required_to_sync = d.pop("required_to_sync")

        active_sync = d.pop("active_sync")

        has_blockers = d.pop("has_blockers")

        counts = NadagSyncStatusCounts.from_dict(d.pop("counts"))

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

        def _parse_latest_sync_status(data: object) -> None | SyncStatus | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                latest_sync_status_type_0 = SyncStatus(data)

                return latest_sync_status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SyncStatus | Unset, data)

        latest_sync_status = _parse_latest_sync_status(d.pop("latest_sync_status", UNSET))

        nadag_sync_status = cls(
            project_id=project_id,
            status=status,
            required_to_sync=required_to_sync,
            active_sync=active_sync,
            has_blockers=has_blockers,
            counts=counts,
            last_successful_sync_at=last_successful_sync_at,
            latest_sync_status=latest_sync_status,
        )

        nadag_sync_status.additional_properties = d
        return nadag_sync_status

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
