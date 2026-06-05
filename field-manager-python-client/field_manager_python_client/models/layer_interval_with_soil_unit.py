from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.soil_unit import SoilUnit


T = TypeVar("T", bound="LayerIntervalWithSoilUnit")


@_attrs_define
class LayerIntervalWithSoilUnit:
    """LayerInterval with nested soil unit details.

    Attributes:
        soil_unit_id (UUID):
        start_depth (float):
        end_depth (float):
        layer_interval_id (UUID):
        layer_group_location_association_id (UUID):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        created_by (None | str):
        updated_by (None | str):
        is_deleted (bool):
        soil_unit (SoilUnit): Full SoilUnit schema returned from API.
    """

    soil_unit_id: UUID
    start_depth: float
    end_depth: float
    layer_interval_id: UUID
    layer_group_location_association_id: UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    created_by: None | str
    updated_by: None | str
    is_deleted: bool
    soil_unit: SoilUnit
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        soil_unit_id = str(self.soil_unit_id)

        start_depth = self.start_depth

        end_depth = self.end_depth

        layer_interval_id = str(self.layer_interval_id)

        layer_group_location_association_id = str(self.layer_group_location_association_id)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        created_by: None | str
        created_by = self.created_by

        updated_by: None | str
        updated_by = self.updated_by

        is_deleted = self.is_deleted

        soil_unit = self.soil_unit.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "soil_unit_id": soil_unit_id,
                "start_depth": start_depth,
                "end_depth": end_depth,
                "layer_interval_id": layer_interval_id,
                "layer_group_location_association_id": layer_group_location_association_id,
                "created_at": created_at,
                "updated_at": updated_at,
                "created_by": created_by,
                "updated_by": updated_by,
                "is_deleted": is_deleted,
                "soil_unit": soil_unit,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.soil_unit import SoilUnit

        d = dict(src_dict)
        soil_unit_id = UUID(d.pop("soil_unit_id"))

        start_depth = d.pop("start_depth")

        end_depth = d.pop("end_depth")

        layer_interval_id = UUID(d.pop("layer_interval_id"))

        layer_group_location_association_id = UUID(d.pop("layer_group_location_association_id"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_created_by(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        created_by = _parse_created_by(d.pop("created_by"))

        def _parse_updated_by(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        updated_by = _parse_updated_by(d.pop("updated_by"))

        is_deleted = d.pop("is_deleted")

        soil_unit = SoilUnit.from_dict(d.pop("soil_unit"))

        layer_interval_with_soil_unit = cls(
            soil_unit_id=soil_unit_id,
            start_depth=start_depth,
            end_depth=end_depth,
            layer_interval_id=layer_interval_id,
            layer_group_location_association_id=layer_group_location_association_id,
            created_at=created_at,
            updated_at=updated_at,
            created_by=created_by,
            updated_by=updated_by,
            is_deleted=is_deleted,
            soil_unit=soil_unit,
        )

        layer_interval_with_soil_unit.additional_properties = d
        return layer_interval_with_soil_unit

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
