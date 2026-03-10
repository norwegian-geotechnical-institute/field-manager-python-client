from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.soil_type_enum import SoilTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="LocationLayerFilterRequest")


@_attrs_define
class LocationLayerFilterRequest:
    """
    Attributes:
        layer_group_id (None | Unset | UUID):
        soil_unit_ids (list[UUID] | Unset):
        exclude_soil_types (list[SoilTypeEnum] | Unset):
    """

    layer_group_id: None | Unset | UUID = UNSET
    soil_unit_ids: list[UUID] | Unset = UNSET
    exclude_soil_types: list[SoilTypeEnum] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        layer_group_id: None | str | Unset
        if isinstance(self.layer_group_id, Unset):
            layer_group_id = UNSET
        elif isinstance(self.layer_group_id, UUID):
            layer_group_id = str(self.layer_group_id)
        else:
            layer_group_id = self.layer_group_id

        soil_unit_ids: list[str] | Unset = UNSET
        if not isinstance(self.soil_unit_ids, Unset):
            soil_unit_ids = []
            for soil_unit_ids_item_data in self.soil_unit_ids:
                soil_unit_ids_item = str(soil_unit_ids_item_data)
                soil_unit_ids.append(soil_unit_ids_item)

        exclude_soil_types: list[str] | Unset = UNSET
        if not isinstance(self.exclude_soil_types, Unset):
            exclude_soil_types = []
            for exclude_soil_types_item_data in self.exclude_soil_types:
                exclude_soil_types_item = exclude_soil_types_item_data.value
                exclude_soil_types.append(exclude_soil_types_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if layer_group_id is not UNSET:
            field_dict["layer_group_id"] = layer_group_id
        if soil_unit_ids is not UNSET:
            field_dict["soil_unit_ids"] = soil_unit_ids
        if exclude_soil_types is not UNSET:
            field_dict["exclude_soil_types"] = exclude_soil_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_layer_group_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                layer_group_id_type_0 = UUID(data)

                return layer_group_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        layer_group_id = _parse_layer_group_id(d.pop("layer_group_id", UNSET))

        _soil_unit_ids = d.pop("soil_unit_ids", UNSET)
        soil_unit_ids: list[UUID] | Unset = UNSET
        if _soil_unit_ids is not UNSET:
            soil_unit_ids = []
            for soil_unit_ids_item_data in _soil_unit_ids:
                soil_unit_ids_item = UUID(soil_unit_ids_item_data)

                soil_unit_ids.append(soil_unit_ids_item)

        _exclude_soil_types = d.pop("exclude_soil_types", UNSET)
        exclude_soil_types: list[SoilTypeEnum] | Unset = UNSET
        if _exclude_soil_types is not UNSET:
            exclude_soil_types = []
            for exclude_soil_types_item_data in _exclude_soil_types:
                exclude_soil_types_item = SoilTypeEnum(exclude_soil_types_item_data)

                exclude_soil_types.append(exclude_soil_types_item)

        location_layer_filter_request = cls(
            layer_group_id=layer_group_id,
            soil_unit_ids=soil_unit_ids,
            exclude_soil_types=exclude_soil_types,
        )

        location_layer_filter_request.additional_properties = d
        return location_layer_filter_request

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
