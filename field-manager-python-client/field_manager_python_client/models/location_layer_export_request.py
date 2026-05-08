from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.layer_interpretation_export_format import LayerInterpretationExportFormat
from ..models.soil_type_enum import SoilTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="LocationLayerExportRequest")


@_attrs_define
class LocationLayerExportRequest:
    """
    Attributes:
        layer_group_id (None | Unset | UUID):
        soil_unit_ids (list[UUID] | Unset):
        exclude_soil_types (list[SoilTypeEnum] | Unset):
        export_format (LayerInterpretationExportFormat | Unset):
        srid (int | None | Unset):
        swap_x_y (bool | Unset):  Default: False.
    """

    layer_group_id: None | Unset | UUID = UNSET
    soil_unit_ids: list[UUID] | Unset = UNSET
    exclude_soil_types: list[SoilTypeEnum] | Unset = UNSET
    export_format: LayerInterpretationExportFormat | Unset = UNSET
    srid: int | None | Unset = UNSET
    swap_x_y: bool | Unset = False
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

        export_format: str | Unset = UNSET
        if not isinstance(self.export_format, Unset):
            export_format = self.export_format.value

        srid: int | None | Unset
        if isinstance(self.srid, Unset):
            srid = UNSET
        else:
            srid = self.srid

        swap_x_y = self.swap_x_y

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if layer_group_id is not UNSET:
            field_dict["layer_group_id"] = layer_group_id
        if soil_unit_ids is not UNSET:
            field_dict["soil_unit_ids"] = soil_unit_ids
        if exclude_soil_types is not UNSET:
            field_dict["exclude_soil_types"] = exclude_soil_types
        if export_format is not UNSET:
            field_dict["export_format"] = export_format
        if srid is not UNSET:
            field_dict["srid"] = srid
        if swap_x_y is not UNSET:
            field_dict["swap_x_y"] = swap_x_y

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

        _export_format = d.pop("export_format", UNSET)
        export_format: LayerInterpretationExportFormat | Unset
        if isinstance(_export_format, Unset):
            export_format = UNSET
        else:
            export_format = LayerInterpretationExportFormat(_export_format)

        def _parse_srid(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        srid = _parse_srid(d.pop("srid", UNSET))

        swap_x_y = d.pop("swap_x_y", UNSET)

        location_layer_export_request = cls(
            layer_group_id=layer_group_id,
            soil_unit_ids=soil_unit_ids,
            exclude_soil_types=exclude_soil_types,
            export_format=export_format,
            srid=srid,
            swap_x_y=swap_x_y,
        )

        location_layer_export_request.additional_properties = d
        return location_layer_export_request

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
