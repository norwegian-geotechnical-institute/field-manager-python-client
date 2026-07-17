from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nadag_sync_blocker import NadagSyncBlocker
    from ..models.nadag_sync_failed_sync import NadagSyncFailedSync
    from ..models.nadag_sync_ready_items import NadagSyncReadyItems


T = TypeVar("T", bound="NadagSyncStatusDetails")


@_attrs_define
class NadagSyncStatusDetails:
    """
    Attributes:
        project_id (UUID):
        required_to_sync (bool):
        ready (NadagSyncReadyItems):
        blockers (list[NadagSyncBlocker] | Unset):
        failed_syncs (list[NadagSyncFailedSync] | Unset):
    """

    project_id: UUID
    required_to_sync: bool
    ready: NadagSyncReadyItems
    blockers: list[NadagSyncBlocker] | Unset = UNSET
    failed_syncs: list[NadagSyncFailedSync] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_id = str(self.project_id)

        required_to_sync = self.required_to_sync

        ready = self.ready.to_dict()

        blockers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.blockers, Unset):
            blockers = []
            for blockers_item_data in self.blockers:
                blockers_item = blockers_item_data.to_dict()
                blockers.append(blockers_item)

        failed_syncs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.failed_syncs, Unset):
            failed_syncs = []
            for failed_syncs_item_data in self.failed_syncs:
                failed_syncs_item = failed_syncs_item_data.to_dict()
                failed_syncs.append(failed_syncs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "project_id": project_id,
                "required_to_sync": required_to_sync,
                "ready": ready,
            }
        )
        if blockers is not UNSET:
            field_dict["blockers"] = blockers
        if failed_syncs is not UNSET:
            field_dict["failed_syncs"] = failed_syncs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nadag_sync_blocker import NadagSyncBlocker
        from ..models.nadag_sync_failed_sync import NadagSyncFailedSync
        from ..models.nadag_sync_ready_items import NadagSyncReadyItems

        d = dict(src_dict)
        project_id = UUID(d.pop("project_id"))

        required_to_sync = d.pop("required_to_sync")

        ready = NadagSyncReadyItems.from_dict(d.pop("ready"))

        _blockers = d.pop("blockers", UNSET)
        blockers: list[NadagSyncBlocker] | Unset = UNSET
        if _blockers is not UNSET:
            blockers = []
            for blockers_item_data in _blockers:
                blockers_item = NadagSyncBlocker.from_dict(blockers_item_data)

                blockers.append(blockers_item)

        _failed_syncs = d.pop("failed_syncs", UNSET)
        failed_syncs: list[NadagSyncFailedSync] | Unset = UNSET
        if _failed_syncs is not UNSET:
            failed_syncs = []
            for failed_syncs_item_data in _failed_syncs:
                failed_syncs_item = NadagSyncFailedSync.from_dict(failed_syncs_item_data)

                failed_syncs.append(failed_syncs_item)

        nadag_sync_status_details = cls(
            project_id=project_id,
            required_to_sync=required_to_sync,
            ready=ready,
            blockers=blockers,
            failed_syncs=failed_syncs,
        )

        nadag_sync_status_details.additional_properties = d
        return nadag_sync_status_details

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
