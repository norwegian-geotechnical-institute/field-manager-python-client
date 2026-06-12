from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.soil_unit import SoilUnit


T = TypeVar("T", bound="LayerGroupWithSoilUnits")


@_attrs_define
class LayerGroupWithSoilUnits:
    """LayerGroup with nested soil units.

    Attributes:
        name (str):
        layer_group_id (UUID):
        project_id (UUID):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        created_by (None | str):
        updated_by (None | str):
        is_deleted (bool):
        is_default (bool | Unset):  Default: False.
        soil_units (list[SoilUnit] | Unset):
    """

    name: str
    layer_group_id: UUID
    project_id: UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    created_by: None | str
    updated_by: None | str
    is_deleted: bool
    is_default: bool | Unset = False
    soil_units: list[SoilUnit] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        layer_group_id = str(self.layer_group_id)

        project_id = str(self.project_id)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        created_by: None | str
        created_by = self.created_by

        updated_by: None | str
        updated_by = self.updated_by

        is_deleted = self.is_deleted

        is_default = self.is_default

        soil_units: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.soil_units, Unset):
            soil_units = []
            for soil_units_item_data in self.soil_units:
                soil_units_item = soil_units_item_data.to_dict()
                soil_units.append(soil_units_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "layer_group_id": layer_group_id,
                "project_id": project_id,
                "created_at": created_at,
                "updated_at": updated_at,
                "created_by": created_by,
                "updated_by": updated_by,
                "is_deleted": is_deleted,
            }
        )
        if is_default is not UNSET:
            field_dict["is_default"] = is_default
        if soil_units is not UNSET:
            field_dict["soil_units"] = soil_units

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.soil_unit import SoilUnit

        d = dict(src_dict)
        name = d.pop("name")

        layer_group_id = UUID(d.pop("layer_group_id"))

        project_id = UUID(d.pop("project_id"))

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

        is_default = d.pop("is_default", UNSET)

        _soil_units = d.pop("soil_units", UNSET)
        soil_units: list[SoilUnit] | Unset = UNSET
        if _soil_units is not UNSET:
            soil_units = []
            for soil_units_item_data in _soil_units:
                soil_units_item = SoilUnit.from_dict(soil_units_item_data)

                soil_units.append(soil_units_item)

        layer_group_with_soil_units = cls(
            name=name,
            layer_group_id=layer_group_id,
            project_id=project_id,
            created_at=created_at,
            updated_at=updated_at,
            created_by=created_by,
            updated_by=updated_by,
            is_deleted=is_deleted,
            is_default=is_default,
            soil_units=soil_units,
        )

        layer_group_with_soil_units.additional_properties = d
        return layer_group_with_soil_units

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
