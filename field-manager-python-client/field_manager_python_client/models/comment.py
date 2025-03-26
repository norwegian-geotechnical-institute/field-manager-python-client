import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.like import Like


T = TypeVar("T", bound="Comment")


@_attrs_define
class Comment:
    """
    Attributes:
        text (str):
        created_by (UUID):
        user_name (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        is_updated (bool):
        is_deleted (bool):
        comment_id (UUID):
        location_id (Union[None, UUID]):
        method_id (Union[None, UUID]):
        likes (Union[Unset, list['Like']]):
    """

    text: str
    created_by: UUID
    user_name: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    is_updated: bool
    is_deleted: bool
    comment_id: UUID
    location_id: Union[None, UUID]
    method_id: Union[None, UUID]
    likes: Union[Unset, list["Like"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        text = self.text

        created_by = str(self.created_by)

        user_name = self.user_name

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        is_updated = self.is_updated

        is_deleted = self.is_deleted

        comment_id = str(self.comment_id)

        location_id: Union[None, str]
        if isinstance(self.location_id, UUID):
            location_id = str(self.location_id)
        else:
            location_id = self.location_id

        method_id: Union[None, str]
        if isinstance(self.method_id, UUID):
            method_id = str(self.method_id)
        else:
            method_id = self.method_id

        likes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.likes, Unset):
            likes = []
            for likes_item_data in self.likes:
                likes_item = likes_item_data.to_dict()
                likes.append(likes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "text": text,
                "created_by": created_by,
                "user_name": user_name,
                "created_at": created_at,
                "updated_at": updated_at,
                "is_updated": is_updated,
                "is_deleted": is_deleted,
                "comment_id": comment_id,
                "location_id": location_id,
                "method_id": method_id,
            }
        )
        if likes is not UNSET:
            field_dict["likes"] = likes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.like import Like

        d = dict(src_dict)
        text = d.pop("text")

        created_by = UUID(d.pop("created_by"))

        user_name = d.pop("user_name")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        is_updated = d.pop("is_updated")

        is_deleted = d.pop("is_deleted")

        comment_id = UUID(d.pop("comment_id"))

        def _parse_location_id(data: object) -> Union[None, UUID]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                location_id_type_0 = UUID(data)

                return location_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID], data)

        location_id = _parse_location_id(d.pop("location_id"))

        def _parse_method_id(data: object) -> Union[None, UUID]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                method_id_type_0 = UUID(data)

                return method_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID], data)

        method_id = _parse_method_id(d.pop("method_id"))

        likes = []
        _likes = d.pop("likes", UNSET)
        for likes_item_data in _likes or []:
            likes_item = Like.from_dict(likes_item_data)

            likes.append(likes_item)

        comment = cls(
            text=text,
            created_by=created_by,
            user_name=user_name,
            created_at=created_at,
            updated_at=updated_at,
            is_updated=is_updated,
            is_deleted=is_deleted,
            comment_id=comment_id,
            location_id=location_id,
            method_id=method_id,
            likes=likes,
        )

        comment.additional_properties = d
        return comment

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
