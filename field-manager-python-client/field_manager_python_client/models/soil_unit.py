from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.hatch_style_enum import HatchStyleEnum
from ..models.soil_type_enum import SoilTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="SoilUnit")


@_attrs_define
class SoilUnit:
    """Full SoilUnit schema returned from API.

    Attributes:
        name (str):
        soil_type (SoilTypeEnum): Standardized soil type classifications
        soil_unit_id (UUID):
        layer_group_id (UUID):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        created_by (None | str):
        updated_by (None | str):
        is_deleted (bool):
        color (None | str | Unset):
        hatch_style (HatchStyleEnum | None | Unset):
    """

    name: str
    soil_type: SoilTypeEnum
    soil_unit_id: UUID
    layer_group_id: UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    created_by: None | str
    updated_by: None | str
    is_deleted: bool
    color: None | str | Unset = UNSET
    hatch_style: HatchStyleEnum | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        soil_type = self.soil_type.value

        soil_unit_id = str(self.soil_unit_id)

        layer_group_id = str(self.layer_group_id)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        created_by: None | str
        created_by = self.created_by

        updated_by: None | str
        updated_by = self.updated_by

        is_deleted = self.is_deleted

        color: None | str | Unset
        if isinstance(self.color, Unset):
            color = UNSET
        else:
            color = self.color

        hatch_style: None | str | Unset
        if isinstance(self.hatch_style, Unset):
            hatch_style = UNSET
        elif isinstance(self.hatch_style, HatchStyleEnum):
            hatch_style = self.hatch_style.value
        else:
            hatch_style = self.hatch_style

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "soil_type": soil_type,
                "soil_unit_id": soil_unit_id,
                "layer_group_id": layer_group_id,
                "created_at": created_at,
                "updated_at": updated_at,
                "created_by": created_by,
                "updated_by": updated_by,
                "is_deleted": is_deleted,
            }
        )
        if color is not UNSET:
            field_dict["color"] = color
        if hatch_style is not UNSET:
            field_dict["hatch_style"] = hatch_style

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        soil_type = SoilTypeEnum(d.pop("soil_type"))

        soil_unit_id = UUID(d.pop("soil_unit_id"))

        layer_group_id = UUID(d.pop("layer_group_id"))

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

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

        def _parse_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        color = _parse_color(d.pop("color", UNSET))

        def _parse_hatch_style(data: object) -> HatchStyleEnum | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                hatch_style_type_0 = HatchStyleEnum(data)

                return hatch_style_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HatchStyleEnum | None | Unset, data)

        hatch_style = _parse_hatch_style(d.pop("hatch_style", UNSET))

        soil_unit = cls(
            name=name,
            soil_type=soil_type,
            soil_unit_id=soil_unit_id,
            layer_group_id=layer_group_id,
            created_at=created_at,
            updated_at=updated_at,
            created_by=created_by,
            updated_by=updated_by,
            is_deleted=is_deleted,
            color=color,
            hatch_style=hatch_style,
        )

        soil_unit.additional_properties = d
        return soil_unit

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
