import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.location_coordinates import LocationCoordinates


T = TypeVar("T", bound="LocationInfo")


@_attrs_define
class LocationInfo:
    """
    Attributes:
        location_id (UUID):
        created_at (datetime.datetime):
        coordinates (LocationCoordinates):
        location_name (Union[None, Unset, str]):
        created_by (Union[None, Unset, str]):
    """

    location_id: UUID
    created_at: datetime.datetime
    coordinates: "LocationCoordinates"
    location_name: Union[None, Unset, str] = UNSET
    created_by: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        location_id = str(self.location_id)

        created_at = self.created_at.isoformat()

        coordinates = self.coordinates.to_dict()

        location_name: Union[None, Unset, str]
        if isinstance(self.location_name, Unset):
            location_name = UNSET
        else:
            location_name = self.location_name

        created_by: Union[None, Unset, str]
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        else:
            created_by = self.created_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "location_id": location_id,
                "created_at": created_at,
                "coordinates": coordinates,
            }
        )
        if location_name is not UNSET:
            field_dict["location_name"] = location_name
        if created_by is not UNSET:
            field_dict["created_by"] = created_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.location_coordinates import LocationCoordinates

        d = src_dict.copy()
        location_id = UUID(d.pop("location_id"))

        created_at = isoparse(d.pop("created_at"))

        coordinates = LocationCoordinates.from_dict(d.pop("coordinates"))

        def _parse_location_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        location_name = _parse_location_name(d.pop("location_name", UNSET))

        def _parse_created_by(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        created_by = _parse_created_by(d.pop("created_by", UNSET))

        location_info = cls(
            location_id=location_id,
            created_at=created_at,
            coordinates=coordinates,
            location_name=location_name,
            created_by=created_by,
        )

        location_info.additional_properties = d
        return location_info

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
