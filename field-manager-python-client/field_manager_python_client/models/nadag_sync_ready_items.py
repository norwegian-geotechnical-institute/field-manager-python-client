from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nadag_sync_ready_location import NadagSyncReadyLocation
    from ..models.nadag_sync_ready_method import NadagSyncReadyMethod
    from ..models.nadag_sync_ready_project import NadagSyncReadyProject
    from ..models.nadag_sync_ready_report import NadagSyncReadyReport


T = TypeVar("T", bound="NadagSyncReadyItems")


@_attrs_define
class NadagSyncReadyItems:
    """
    Attributes:
        project (NadagSyncReadyProject | None | Unset):
        reports (list[NadagSyncReadyReport] | Unset):
        locations (list[NadagSyncReadyLocation] | Unset):
        methods (list[NadagSyncReadyMethod] | Unset):
    """

    project: NadagSyncReadyProject | None | Unset = UNSET
    reports: list[NadagSyncReadyReport] | Unset = UNSET
    locations: list[NadagSyncReadyLocation] | Unset = UNSET
    methods: list[NadagSyncReadyMethod] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.nadag_sync_ready_project import NadagSyncReadyProject

        project: dict[str, Any] | None | Unset
        if isinstance(self.project, Unset):
            project = UNSET
        elif isinstance(self.project, NadagSyncReadyProject):
            project = self.project.to_dict()
        else:
            project = self.project

        reports: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.reports, Unset):
            reports = []
            for reports_item_data in self.reports:
                reports_item = reports_item_data.to_dict()
                reports.append(reports_item)

        locations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.locations, Unset):
            locations = []
            for locations_item_data in self.locations:
                locations_item = locations_item_data.to_dict()
                locations.append(locations_item)

        methods: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.methods, Unset):
            methods = []
            for methods_item_data in self.methods:
                methods_item = methods_item_data.to_dict()
                methods.append(methods_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if project is not UNSET:
            field_dict["project"] = project
        if reports is not UNSET:
            field_dict["reports"] = reports
        if locations is not UNSET:
            field_dict["locations"] = locations
        if methods is not UNSET:
            field_dict["methods"] = methods

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nadag_sync_ready_location import NadagSyncReadyLocation
        from ..models.nadag_sync_ready_method import NadagSyncReadyMethod
        from ..models.nadag_sync_ready_project import NadagSyncReadyProject
        from ..models.nadag_sync_ready_report import NadagSyncReadyReport

        d = dict(src_dict)

        def _parse_project(data: object) -> NadagSyncReadyProject | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                project_type_0 = NadagSyncReadyProject.from_dict(data)

                return project_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NadagSyncReadyProject | None | Unset, data)

        project = _parse_project(d.pop("project", UNSET))

        _reports = d.pop("reports", UNSET)
        reports: list[NadagSyncReadyReport] | Unset = UNSET
        if _reports is not UNSET:
            reports = []
            for reports_item_data in _reports:
                reports_item = NadagSyncReadyReport.from_dict(reports_item_data)

                reports.append(reports_item)

        _locations = d.pop("locations", UNSET)
        locations: list[NadagSyncReadyLocation] | Unset = UNSET
        if _locations is not UNSET:
            locations = []
            for locations_item_data in _locations:
                locations_item = NadagSyncReadyLocation.from_dict(locations_item_data)

                locations.append(locations_item)

        _methods = d.pop("methods", UNSET)
        methods: list[NadagSyncReadyMethod] | Unset = UNSET
        if _methods is not UNSET:
            methods = []
            for methods_item_data in _methods:
                methods_item = NadagSyncReadyMethod.from_dict(methods_item_data)

                methods.append(methods_item)

        nadag_sync_ready_items = cls(
            project=project,
            reports=reports,
            locations=locations,
            methods=methods,
        )

        nadag_sync_ready_items.additional_properties = d
        return nadag_sync_ready_items

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
