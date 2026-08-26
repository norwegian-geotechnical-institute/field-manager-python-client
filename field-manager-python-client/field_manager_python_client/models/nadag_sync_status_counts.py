from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="NadagSyncStatusCounts")


@_attrs_define
class NadagSyncStatusCounts:
    """
    Attributes:
        reports (int):
        report_candidates (int):
        locations (int):
        location_candidates (int):
        methods (int):
        method_candidates (int):
        blockers (int):
        failed_syncs (int):
    """

    reports: int
    report_candidates: int
    locations: int
    location_candidates: int
    methods: int
    method_candidates: int
    blockers: int
    failed_syncs: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reports = self.reports

        report_candidates = self.report_candidates

        locations = self.locations

        location_candidates = self.location_candidates

        methods = self.methods

        method_candidates = self.method_candidates

        blockers = self.blockers

        failed_syncs = self.failed_syncs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reports": reports,
                "report_candidates": report_candidates,
                "locations": locations,
                "location_candidates": location_candidates,
                "methods": methods,
                "method_candidates": method_candidates,
                "blockers": blockers,
                "failed_syncs": failed_syncs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reports = d.pop("reports")

        report_candidates = d.pop("report_candidates")

        locations = d.pop("locations")

        location_candidates = d.pop("location_candidates")

        methods = d.pop("methods")

        method_candidates = d.pop("method_candidates")

        blockers = d.pop("blockers")

        failed_syncs = d.pop("failed_syncs")

        nadag_sync_status_counts = cls(
            reports=reports,
            report_candidates=report_candidates,
            locations=locations,
            location_candidates=location_candidates,
            methods=methods,
            method_candidates=method_candidates,
            blockers=blockers,
            failed_syncs=failed_syncs,
        )

        nadag_sync_status_counts.additional_properties = d
        return nadag_sync_status_counts

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
