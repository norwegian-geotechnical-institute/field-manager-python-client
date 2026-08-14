from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NadagSyncMessage")


@_attrs_define
class NadagSyncMessage:
    """
    Attributes:
        user_id (UUID):
        nadag_user_id (UUID):
        project_id (UUID):
        message_type (str | Unset):  Default: 'NadagSync'.
    """

    user_id: UUID
    nadag_user_id: UUID
    project_id: UUID
    message_type: str | Unset = "NadagSync"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_id = str(self.user_id)

        nadag_user_id = str(self.nadag_user_id)

        project_id = str(self.project_id)

        message_type = self.message_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user_id": user_id,
                "nadag_user_id": nadag_user_id,
                "project_id": project_id,
            }
        )
        if message_type is not UNSET:
            field_dict["message_type"] = message_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_id = UUID(d.pop("user_id"))

        nadag_user_id = UUID(d.pop("nadag_user_id"))

        project_id = UUID(d.pop("project_id"))

        message_type = d.pop("message_type", UNSET)

        nadag_sync_message = cls(
            user_id=user_id,
            nadag_user_id=nadag_user_id,
            project_id=project_id,
            message_type=message_type,
        )

        nadag_sync_message.additional_properties = d
        return nadag_sync_message

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
