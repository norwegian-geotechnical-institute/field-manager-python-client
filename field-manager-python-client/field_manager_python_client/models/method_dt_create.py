from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.method_status_enum import MethodStatusEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="MethodDTCreate")


@_attrs_define
class MethodDTCreate:
    """Structure for creating a new DT method. All parameters are optional and defaults values are provided.

    Attributes:
        method_id (None | Unset | UUID):
        name (str | Unset):  Default: 'DT'.
        remarks (None | str | Unset):
        method_status_id (MethodStatusEnum | Unset): (
            PLANNED=1,
            READY=2,
            CONDUCTED=3,
            VOIDED=4,
            APPROVED=5,
            )
        created_at (datetime.datetime | None | Unset):
        created_by (None | str | Unset):
        updated_at (datetime.datetime | None | Unset):
        updated_by (None | str | Unset):
        conducted_by (None | str | Unset):
        conducted_at (datetime.datetime | None | Unset):
        method_type_id (Literal[22] | Unset):  Default: 22.
        depth (float | None | str | Unset): Depth (m). SGF code D.
        u2_initial (float | None | str | Unset):
        u2_equilibrium (float | None | str | Unset):
        degree_dissipation (float | None | str | Unset):
        time_dissipation (float | None | str | Unset):
        coefficient_consolidation_vertical (float | None | str | Unset):
        coefficient_consolidation_horizontal (float | None | str | Unset):
    """

    method_id: None | Unset | UUID = UNSET
    name: str | Unset = "DT"
    remarks: None | str | Unset = UNSET
    method_status_id: MethodStatusEnum | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    created_by: None | str | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    updated_by: None | str | Unset = UNSET
    conducted_by: None | str | Unset = UNSET
    conducted_at: datetime.datetime | None | Unset = UNSET
    method_type_id: Literal[22] | Unset = 22
    depth: float | None | str | Unset = UNSET
    u2_initial: float | None | str | Unset = UNSET
    u2_equilibrium: float | None | str | Unset = UNSET
    degree_dissipation: float | None | str | Unset = UNSET
    time_dissipation: float | None | str | Unset = UNSET
    coefficient_consolidation_vertical: float | None | str | Unset = UNSET
    coefficient_consolidation_horizontal: float | None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        method_id: None | str | Unset
        if isinstance(self.method_id, Unset):
            method_id = UNSET
        elif isinstance(self.method_id, UUID):
            method_id = str(self.method_id)
        else:
            method_id = self.method_id

        name = self.name

        remarks: None | str | Unset
        if isinstance(self.remarks, Unset):
            remarks = UNSET
        else:
            remarks = self.remarks

        method_status_id: int | Unset = UNSET
        if not isinstance(self.method_status_id, Unset):
            method_status_id = self.method_status_id.value

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        created_by: None | str | Unset
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        else:
            created_by = self.created_by

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        updated_by: None | str | Unset
        if isinstance(self.updated_by, Unset):
            updated_by = UNSET
        else:
            updated_by = self.updated_by

        conducted_by: None | str | Unset
        if isinstance(self.conducted_by, Unset):
            conducted_by = UNSET
        else:
            conducted_by = self.conducted_by

        conducted_at: None | str | Unset
        if isinstance(self.conducted_at, Unset):
            conducted_at = UNSET
        elif isinstance(self.conducted_at, datetime.datetime):
            conducted_at = self.conducted_at.isoformat()
        else:
            conducted_at = self.conducted_at

        method_type_id = self.method_type_id

        depth: float | None | str | Unset
        if isinstance(self.depth, Unset):
            depth = UNSET
        else:
            depth = self.depth

        u2_initial: float | None | str | Unset
        if isinstance(self.u2_initial, Unset):
            u2_initial = UNSET
        else:
            u2_initial = self.u2_initial

        u2_equilibrium: float | None | str | Unset
        if isinstance(self.u2_equilibrium, Unset):
            u2_equilibrium = UNSET
        else:
            u2_equilibrium = self.u2_equilibrium

        degree_dissipation: float | None | str | Unset
        if isinstance(self.degree_dissipation, Unset):
            degree_dissipation = UNSET
        else:
            degree_dissipation = self.degree_dissipation

        time_dissipation: float | None | str | Unset
        if isinstance(self.time_dissipation, Unset):
            time_dissipation = UNSET
        else:
            time_dissipation = self.time_dissipation

        coefficient_consolidation_vertical: float | None | str | Unset
        if isinstance(self.coefficient_consolidation_vertical, Unset):
            coefficient_consolidation_vertical = UNSET
        else:
            coefficient_consolidation_vertical = self.coefficient_consolidation_vertical

        coefficient_consolidation_horizontal: float | None | str | Unset
        if isinstance(self.coefficient_consolidation_horizontal, Unset):
            coefficient_consolidation_horizontal = UNSET
        else:
            coefficient_consolidation_horizontal = self.coefficient_consolidation_horizontal

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if method_id is not UNSET:
            field_dict["method_id"] = method_id
        if name is not UNSET:
            field_dict["name"] = name
        if remarks is not UNSET:
            field_dict["remarks"] = remarks
        if method_status_id is not UNSET:
            field_dict["method_status_id"] = method_status_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if updated_by is not UNSET:
            field_dict["updated_by"] = updated_by
        if conducted_by is not UNSET:
            field_dict["conducted_by"] = conducted_by
        if conducted_at is not UNSET:
            field_dict["conducted_at"] = conducted_at
        if method_type_id is not UNSET:
            field_dict["method_type_id"] = method_type_id
        if depth is not UNSET:
            field_dict["depth"] = depth
        if u2_initial is not UNSET:
            field_dict["u2_initial"] = u2_initial
        if u2_equilibrium is not UNSET:
            field_dict["u2_equilibrium"] = u2_equilibrium
        if degree_dissipation is not UNSET:
            field_dict["degree_dissipation"] = degree_dissipation
        if time_dissipation is not UNSET:
            field_dict["time_dissipation"] = time_dissipation
        if coefficient_consolidation_vertical is not UNSET:
            field_dict["coefficient_consolidation_vertical"] = coefficient_consolidation_vertical
        if coefficient_consolidation_horizontal is not UNSET:
            field_dict["coefficient_consolidation_horizontal"] = coefficient_consolidation_horizontal

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_method_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                method_id_type_0 = UUID(data)

                return method_id_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | UUID, data)

        method_id = _parse_method_id(d.pop("method_id", UNSET))

        name = d.pop("name", UNSET)

        def _parse_remarks(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remarks = _parse_remarks(d.pop("remarks", UNSET))

        _method_status_id = d.pop("method_status_id", UNSET)
        method_status_id: MethodStatusEnum | Unset
        if isinstance(_method_status_id, Unset):
            method_status_id = UNSET
        else:
            method_status_id = MethodStatusEnum(_method_status_id)

        def _parse_created_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = isoparse(data)

                return created_at_type_0
            except:  # noqa: E722
                pass
            return cast(datetime.datetime | None | Unset, data)

        created_at = _parse_created_at(d.pop("created_at", UNSET))

        def _parse_created_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_by = _parse_created_by(d.pop("created_by", UNSET))

        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = isoparse(data)

                return updated_at_type_0
            except:  # noqa: E722
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))

        def _parse_updated_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        updated_by = _parse_updated_by(d.pop("updated_by", UNSET))

        def _parse_conducted_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        conducted_by = _parse_conducted_by(d.pop("conducted_by", UNSET))

        def _parse_conducted_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                conducted_at_type_0 = isoparse(data)

                return conducted_at_type_0
            except:  # noqa: E722
                pass
            return cast(datetime.datetime | None | Unset, data)

        conducted_at = _parse_conducted_at(d.pop("conducted_at", UNSET))

        method_type_id = cast(Literal[22] | Unset, d.pop("method_type_id", UNSET))
        if method_type_id != 22 and not isinstance(method_type_id, Unset):
            raise ValueError(f"method_type_id must match const 22, got '{method_type_id}'")

        def _parse_depth(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        depth = _parse_depth(d.pop("depth", UNSET))

        def _parse_u2_initial(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        u2_initial = _parse_u2_initial(d.pop("u2_initial", UNSET))

        def _parse_u2_equilibrium(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        u2_equilibrium = _parse_u2_equilibrium(d.pop("u2_equilibrium", UNSET))

        def _parse_degree_dissipation(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        degree_dissipation = _parse_degree_dissipation(d.pop("degree_dissipation", UNSET))

        def _parse_time_dissipation(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        time_dissipation = _parse_time_dissipation(d.pop("time_dissipation", UNSET))

        def _parse_coefficient_consolidation_vertical(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        coefficient_consolidation_vertical = _parse_coefficient_consolidation_vertical(
            d.pop("coefficient_consolidation_vertical", UNSET)
        )

        def _parse_coefficient_consolidation_horizontal(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        coefficient_consolidation_horizontal = _parse_coefficient_consolidation_horizontal(
            d.pop("coefficient_consolidation_horizontal", UNSET)
        )

        method_dt_create = cls(
            method_id=method_id,
            name=name,
            remarks=remarks,
            method_status_id=method_status_id,
            created_at=created_at,
            created_by=created_by,
            updated_at=updated_at,
            updated_by=updated_by,
            conducted_by=conducted_by,
            conducted_at=conducted_at,
            method_type_id=method_type_id,
            depth=depth,
            u2_initial=u2_initial,
            u2_equilibrium=u2_equilibrium,
            degree_dissipation=degree_dissipation,
            time_dissipation=time_dissipation,
            coefficient_consolidation_vertical=coefficient_consolidation_vertical,
            coefficient_consolidation_horizontal=coefficient_consolidation_horizontal,
        )

        method_dt_create.additional_properties = d
        return method_dt_create

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
