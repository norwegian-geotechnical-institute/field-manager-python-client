from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.nadag_sync_blocker_code import NadagSyncBlockerCode
from ..types import UNSET, Unset

T = TypeVar("T", bound="NadagSyncBlocker")


@_attrs_define
class NadagSyncBlocker:
    """
    Attributes:
        code (NadagSyncBlockerCode):
        message (str):
        project_id (None | Unset | UUID):
        location_id (None | Unset | UUID):
        location_name (None | str | Unset):
        method_ids (list[UUID] | Unset):
        method_names (list[str] | Unset):
    """

    code: NadagSyncBlockerCode
    message: str
    project_id: None | Unset | UUID = UNSET
    location_id: None | Unset | UUID = UNSET
    location_name: None | str | Unset = UNSET
    method_ids: list[UUID] | Unset = UNSET
    method_names: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code.value

        message = self.message

        project_id: None | str | Unset
        if isinstance(self.project_id, Unset):
            project_id = UNSET
        elif isinstance(self.project_id, UUID):
            project_id = str(self.project_id)
        else:
            project_id = self.project_id

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

        method_ids: list[str] | Unset = UNSET
        if not isinstance(self.method_ids, Unset):
            method_ids = []
            for method_ids_item_data in self.method_ids:
                method_ids_item = str(method_ids_item_data)
                method_ids.append(method_ids_item)

        method_names: list[str] | Unset = UNSET
        if not isinstance(self.method_names, Unset):
            method_names = self.method_names

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "message": message,
            }
        )
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if location_id is not UNSET:
            field_dict["location_id"] = location_id
        if location_name is not UNSET:
            field_dict["location_name"] = location_name
        if method_ids is not UNSET:
            field_dict["method_ids"] = method_ids
        if method_names is not UNSET:
            field_dict["method_names"] = method_names

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = NadagSyncBlockerCode(d.pop("code"))

        message = d.pop("message")

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

        _method_ids = d.pop("method_ids", UNSET)
        method_ids: list[UUID] | Unset = UNSET
        if _method_ids is not UNSET:
            method_ids = []
            for method_ids_item_data in _method_ids:
                method_ids_item = UUID(method_ids_item_data)

                method_ids.append(method_ids_item)

        method_names = cast(list[str], d.pop("method_names", UNSET))

        nadag_sync_blocker = cls(
            code=code,
            message=message,
            project_id=project_id,
            location_id=location_id,
            location_name=location_name,
            method_ids=method_ids,
            method_names=method_names,
        )

        nadag_sync_blocker.additional_properties = d
        return nadag_sync_blocker

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
