from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.map_layout_version_create import MapLayoutVersionCreate


T = TypeVar("T", bound="MapLayoutCreate")


@_attrs_define
class MapLayoutCreate:
    """Map Layout Create

    Attributes:
        name (str):
        versions (list['MapLayoutVersionCreate']):
        map_layout_id (Union[None, UUID, Unset]):
    """

    name: str
    versions: list["MapLayoutVersionCreate"]
    map_layout_id: Union[None, UUID, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        versions = []
        for versions_item_data in self.versions:
            versions_item = versions_item_data.to_dict()
            versions.append(versions_item)

        map_layout_id: Union[None, Unset, str]
        if isinstance(self.map_layout_id, Unset):
            map_layout_id = UNSET
        elif isinstance(self.map_layout_id, UUID):
            map_layout_id = str(self.map_layout_id)
        else:
            map_layout_id = self.map_layout_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "versions": versions,
            }
        )
        if map_layout_id is not UNSET:
            field_dict["map_layout_id"] = map_layout_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.map_layout_version_create import MapLayoutVersionCreate

        d = src_dict.copy()
        name = d.pop("name")

        versions = []
        _versions = d.pop("versions")
        for versions_item_data in _versions:
            versions_item = MapLayoutVersionCreate.from_dict(versions_item_data)

            versions.append(versions_item)

        def _parse_map_layout_id(data: object) -> Union[None, UUID, Unset]:
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
            return cast(Union[None, UUID, Unset], data)

        map_layout_id = _parse_map_layout_id(d.pop("map_layout_id", UNSET))

        map_layout_create = cls(
            name=name,
            versions=versions,
            map_layout_id=map_layout_id,
        )

        map_layout_create.additional_properties = d
        return map_layout_create

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
