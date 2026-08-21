from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.standard_type import StandardType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.soil_unit_create import SoilUnitCreate


T = TypeVar("T", bound="LayerGroupCreate")


@_attrs_define
class LayerGroupCreate:
    """
    Attributes:
        name (None | str | Unset):
        is_default (bool | Unset):  Default: False.
        standard_id (None | StandardType | Unset):
        organization_layer_group_id (None | Unset | UUID):
        soil_units (list[SoilUnitCreate] | Unset):
    """

    name: None | str | Unset = UNSET
    is_default: bool | Unset = False
    standard_id: None | StandardType | Unset = UNSET
    organization_layer_group_id: None | Unset | UUID = UNSET
    soil_units: list[SoilUnitCreate] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        is_default = self.is_default

        standard_id: None | str | Unset
        if isinstance(self.standard_id, Unset):
            standard_id = UNSET
        elif isinstance(self.standard_id, StandardType):
            standard_id = self.standard_id.value
        else:
            standard_id = self.standard_id

        organization_layer_group_id: None | str | Unset
        if isinstance(self.organization_layer_group_id, Unset):
            organization_layer_group_id = UNSET
        elif isinstance(self.organization_layer_group_id, UUID):
            organization_layer_group_id = str(self.organization_layer_group_id)
        else:
            organization_layer_group_id = self.organization_layer_group_id

        soil_units: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.soil_units, Unset):
            soil_units = []
            for soil_units_item_data in self.soil_units:
                soil_units_item = soil_units_item_data.to_dict()
                soil_units.append(soil_units_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if is_default is not UNSET:
            field_dict["is_default"] = is_default
        if standard_id is not UNSET:
            field_dict["standard_id"] = standard_id
        if organization_layer_group_id is not UNSET:
            field_dict["organization_layer_group_id"] = organization_layer_group_id
        if soil_units is not UNSET:
            field_dict["soil_units"] = soil_units

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.soil_unit_create import SoilUnitCreate

        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        is_default = d.pop("is_default", UNSET)

        def _parse_standard_id(data: object) -> None | StandardType | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                standard_id_type_0 = StandardType(data)

                return standard_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | StandardType | Unset, data)

        standard_id = _parse_standard_id(d.pop("standard_id", UNSET))

        def _parse_organization_layer_group_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                organization_layer_group_id_type_0 = UUID(data)

                return organization_layer_group_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        organization_layer_group_id = _parse_organization_layer_group_id(d.pop("organization_layer_group_id", UNSET))

        _soil_units = d.pop("soil_units", UNSET)
        soil_units: list[SoilUnitCreate] | Unset = UNSET
        if _soil_units is not UNSET:
            soil_units = []
            for soil_units_item_data in _soil_units:
                soil_units_item = SoilUnitCreate.from_dict(soil_units_item_data)

                soil_units.append(soil_units_item)

        layer_group_create = cls(
            name=name,
            is_default=is_default,
            standard_id=standard_id,
            organization_layer_group_id=organization_layer_group_id,
            soil_units=soil_units,
        )

        layer_group_create.additional_properties = d
        return layer_group_create

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
