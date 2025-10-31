from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.map_layout_version_update import MapLayoutVersionUpdate


T = TypeVar("T", bound="MapLayoutUpdate")


@_attrs_define
class MapLayoutUpdate:
    """Map Layout Update

    Attributes:
        map_layout_id (None | Unset | UUID):
        name (None | str | Unset):
        versions (list[MapLayoutVersionUpdate] | Unset):
    """

    map_layout_id: None | Unset | UUID = UNSET
    name: None | str | Unset = UNSET
    versions: list[MapLayoutVersionUpdate] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        map_layout_id: None | str | Unset
        if isinstance(self.map_layout_id, Unset):
            map_layout_id = UNSET
        elif isinstance(self.map_layout_id, UUID):
            map_layout_id = str(self.map_layout_id)
        else:
            map_layout_id = self.map_layout_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        versions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.versions, Unset):
            versions = []
            for versions_item_data in self.versions:
                versions_item = versions_item_data.to_dict()
                versions.append(versions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if map_layout_id is not UNSET:
            field_dict["map_layout_id"] = map_layout_id
        if name is not UNSET:
            field_dict["name"] = name
        if versions is not UNSET:
            field_dict["versions"] = versions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.map_layout_version_update import MapLayoutVersionUpdate

        d = dict(src_dict)

        def _parse_map_layout_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                map_layout_id_type_0 = UUID(data)

                return map_layout_id_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | UUID, data)

        map_layout_id = _parse_map_layout_id(d.pop("map_layout_id", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        versions = []
        _versions = d.pop("versions", UNSET)
        for versions_item_data in _versions or []:
            versions_item = MapLayoutVersionUpdate.from_dict(versions_item_data)

            versions.append(versions_item)

        map_layout_update = cls(
            map_layout_id=map_layout_id,
            name=name,
            versions=versions,
        )

        map_layout_update.additional_properties = d
        return map_layout_update

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
