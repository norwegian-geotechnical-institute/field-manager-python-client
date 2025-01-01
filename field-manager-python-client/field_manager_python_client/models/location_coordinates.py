from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LocationCoordinates")


@_attrs_define
class LocationCoordinates:
    """
    Attributes:
        easting (Union[None, Unset, float]):
        northing (Union[None, Unset, float]):
        elevation (Union[None, Unset, float]):
    """

    easting: Union[None, Unset, float] = UNSET
    northing: Union[None, Unset, float] = UNSET
    elevation: Union[None, Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        easting: Union[None, Unset, float]
        if isinstance(self.easting, Unset):
            easting = UNSET
        else:
            easting = self.easting

        northing: Union[None, Unset, float]
        if isinstance(self.northing, Unset):
            northing = UNSET
        else:
            northing = self.northing

        elevation: Union[None, Unset, float]
        if isinstance(self.elevation, Unset):
            elevation = UNSET
        else:
            elevation = self.elevation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if easting is not UNSET:
            field_dict["easting"] = easting
        if northing is not UNSET:
            field_dict["northing"] = northing
        if elevation is not UNSET:
            field_dict["elevation"] = elevation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_easting(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        easting = _parse_easting(d.pop("easting", UNSET))

        def _parse_northing(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        northing = _parse_northing(d.pop("northing", UNSET))

        def _parse_elevation(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        elevation = _parse_elevation(d.pop("elevation", UNSET))

        location_coordinates = cls(
            easting=easting,
            northing=northing,
            elevation=elevation,
        )

        location_coordinates.additional_properties = d
        return location_coordinates

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
