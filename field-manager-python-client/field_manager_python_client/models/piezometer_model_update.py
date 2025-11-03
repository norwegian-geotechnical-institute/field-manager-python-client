from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.transformation_type import TransformationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PiezometerModelUpdate")


@_attrs_define
class PiezometerModelUpdate:
    """
    Attributes:
        vendor_id (None | Unset | UUID):
        name (None | str | Unset):
        piezometer_type (None | str | Unset):
        default_transformation_type (None | TransformationType | Unset):
        default_pore_pressure_unit (None | str | Unset):
        sort_order (int | None | Unset):
    """

    vendor_id: None | Unset | UUID = UNSET
    name: None | str | Unset = UNSET
    piezometer_type: None | str | Unset = UNSET
    default_transformation_type: None | TransformationType | Unset = UNSET
    default_pore_pressure_unit: None | str | Unset = UNSET
    sort_order: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vendor_id: None | str | Unset
        if isinstance(self.vendor_id, Unset):
            vendor_id = UNSET
        elif isinstance(self.vendor_id, UUID):
            vendor_id = str(self.vendor_id)
        else:
            vendor_id = self.vendor_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        piezometer_type: None | str | Unset
        if isinstance(self.piezometer_type, Unset):
            piezometer_type = UNSET
        else:
            piezometer_type = self.piezometer_type

        default_transformation_type: None | str | Unset
        if isinstance(self.default_transformation_type, Unset):
            default_transformation_type = UNSET
        elif isinstance(self.default_transformation_type, TransformationType):
            default_transformation_type = self.default_transformation_type.value
        else:
            default_transformation_type = self.default_transformation_type

        default_pore_pressure_unit: None | str | Unset
        if isinstance(self.default_pore_pressure_unit, Unset):
            default_pore_pressure_unit = UNSET
        else:
            default_pore_pressure_unit = self.default_pore_pressure_unit

        sort_order: int | None | Unset
        if isinstance(self.sort_order, Unset):
            sort_order = UNSET
        else:
            sort_order = self.sort_order

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if vendor_id is not UNSET:
            field_dict["vendor_id"] = vendor_id
        if name is not UNSET:
            field_dict["name"] = name
        if piezometer_type is not UNSET:
            field_dict["piezometer_type"] = piezometer_type
        if default_transformation_type is not UNSET:
            field_dict["default_transformation_type"] = default_transformation_type
        if default_pore_pressure_unit is not UNSET:
            field_dict["default_pore_pressure_unit"] = default_pore_pressure_unit
        if sort_order is not UNSET:
            field_dict["sort_order"] = sort_order

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_vendor_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                vendor_id_type_0 = UUID(data)

                return vendor_id_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | UUID, data)

        vendor_id = _parse_vendor_id(d.pop("vendor_id", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_piezometer_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        piezometer_type = _parse_piezometer_type(d.pop("piezometer_type", UNSET))

        def _parse_default_transformation_type(data: object) -> None | TransformationType | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                default_transformation_type_type_0 = TransformationType(data)

                return default_transformation_type_type_0
            except:  # noqa: E722
                pass
            return cast(None | TransformationType | Unset, data)

        default_transformation_type = _parse_default_transformation_type(d.pop("default_transformation_type", UNSET))

        def _parse_default_pore_pressure_unit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        default_pore_pressure_unit = _parse_default_pore_pressure_unit(d.pop("default_pore_pressure_unit", UNSET))

        def _parse_sort_order(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sort_order = _parse_sort_order(d.pop("sort_order", UNSET))

        piezometer_model_update = cls(
            vendor_id=vendor_id,
            name=name,
            piezometer_type=piezometer_type,
            default_transformation_type=default_transformation_type,
            default_pore_pressure_unit=default_pore_pressure_unit,
            sort_order=sort_order,
        )

        piezometer_model_update.additional_properties = d
        return piezometer_model_update

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
