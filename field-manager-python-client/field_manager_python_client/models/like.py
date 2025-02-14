import datetime
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="Like")


@_attrs_define
class Like:
    """
    Attributes:
        like_id (UUID):
        user_id (UUID):
        user_name (str):
        comment_id (UUID):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        is_deleted (bool):
    """

    like_id: UUID
    user_id: UUID
    user_name: str
    comment_id: UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    is_deleted: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        like_id = str(self.like_id)

        user_id = str(self.user_id)

        user_name = self.user_name

        comment_id = str(self.comment_id)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        is_deleted = self.is_deleted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "like_id": like_id,
                "user_id": user_id,
                "user_name": user_name,
                "comment_id": comment_id,
                "created_at": created_at,
                "updated_at": updated_at,
                "is_deleted": is_deleted,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        like_id = UUID(d.pop("like_id"))

        user_id = UUID(d.pop("user_id"))

        user_name = d.pop("user_name")

        comment_id = UUID(d.pop("comment_id"))

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        is_deleted = d.pop("is_deleted")

        like = cls(
            like_id=like_id,
            user_id=user_id,
            user_name=user_name,
            comment_id=comment_id,
            created_at=created_at,
            updated_at=updated_at,
            is_deleted=is_deleted,
        )

        like.additional_properties = d
        return like

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
