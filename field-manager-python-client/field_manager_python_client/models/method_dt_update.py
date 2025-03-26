import datetime
from collections.abc import Mapping
from typing import Any, Literal, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.method_status_enum import MethodStatusEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="MethodDTUpdate")


@_attrs_define
class MethodDTUpdate:
    """
    Attributes:
        method_id (Union[None, UUID, Unset]):
        name (Union[None, Unset, str]):
        remarks (Union[None, Unset, str]):
        method_status_id (Union[MethodStatusEnum, None, Unset]):
        updated_at (Union[None, Unset, datetime.datetime]):
        updated_by (Union[None, Unset, str]):
        conducted_by (Union[None, Unset, str]):
        conducted_at (Union[None, Unset, datetime.datetime]):
        method_type_id (Union[Literal[22], Unset]):  Default: 22.
        depth (Union[None, Unset, float, str]):
        u2_initial (Union[None, Unset, float, str]):
        u2_equilibrium (Union[None, Unset, float, str]):
        degree_dissipation (Union[None, Unset, float, str]):
        time_dissipation (Union[None, Unset, float, str]):
        coefficient_consolidation_vertical (Union[None, Unset, float, str]):
        coefficient_consolidation_horizontal (Union[None, Unset, float, str]):
    """

    method_id: Union[None, UUID, Unset] = UNSET
    name: Union[None, Unset, str] = UNSET
    remarks: Union[None, Unset, str] = UNSET
    method_status_id: Union[MethodStatusEnum, None, Unset] = UNSET
    updated_at: Union[None, Unset, datetime.datetime] = UNSET
    updated_by: Union[None, Unset, str] = UNSET
    conducted_by: Union[None, Unset, str] = UNSET
    conducted_at: Union[None, Unset, datetime.datetime] = UNSET
    method_type_id: Union[Literal[22], Unset] = 22
    depth: Union[None, Unset, float, str] = UNSET
    u2_initial: Union[None, Unset, float, str] = UNSET
    u2_equilibrium: Union[None, Unset, float, str] = UNSET
    degree_dissipation: Union[None, Unset, float, str] = UNSET
    time_dissipation: Union[None, Unset, float, str] = UNSET
    coefficient_consolidation_vertical: Union[None, Unset, float, str] = UNSET
    coefficient_consolidation_horizontal: Union[None, Unset, float, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        method_id: Union[None, Unset, str]
        if isinstance(self.method_id, Unset):
            method_id = UNSET
        elif isinstance(self.method_id, UUID):
            method_id = str(self.method_id)
        else:
            method_id = self.method_id

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        remarks: Union[None, Unset, str]
        if isinstance(self.remarks, Unset):
            remarks = UNSET
        else:
            remarks = self.remarks

        method_status_id: Union[None, Unset, int]
        if isinstance(self.method_status_id, Unset):
            method_status_id = UNSET
        elif isinstance(self.method_status_id, MethodStatusEnum):
            method_status_id = self.method_status_id.value
        else:
            method_status_id = self.method_status_id

        updated_at: Union[None, Unset, str]
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        updated_by: Union[None, Unset, str]
        if isinstance(self.updated_by, Unset):
            updated_by = UNSET
        else:
            updated_by = self.updated_by

        conducted_by: Union[None, Unset, str]
        if isinstance(self.conducted_by, Unset):
            conducted_by = UNSET
        else:
            conducted_by = self.conducted_by

        conducted_at: Union[None, Unset, str]
        if isinstance(self.conducted_at, Unset):
            conducted_at = UNSET
        elif isinstance(self.conducted_at, datetime.datetime):
            conducted_at = self.conducted_at.isoformat()
        else:
            conducted_at = self.conducted_at

        method_type_id = self.method_type_id

        depth: Union[None, Unset, float, str]
        if isinstance(self.depth, Unset):
            depth = UNSET
        else:
            depth = self.depth

        u2_initial: Union[None, Unset, float, str]
        if isinstance(self.u2_initial, Unset):
            u2_initial = UNSET
        else:
            u2_initial = self.u2_initial

        u2_equilibrium: Union[None, Unset, float, str]
        if isinstance(self.u2_equilibrium, Unset):
            u2_equilibrium = UNSET
        else:
            u2_equilibrium = self.u2_equilibrium

        degree_dissipation: Union[None, Unset, float, str]
        if isinstance(self.degree_dissipation, Unset):
            degree_dissipation = UNSET
        else:
            degree_dissipation = self.degree_dissipation

        time_dissipation: Union[None, Unset, float, str]
        if isinstance(self.time_dissipation, Unset):
            time_dissipation = UNSET
        else:
            time_dissipation = self.time_dissipation

        coefficient_consolidation_vertical: Union[None, Unset, float, str]
        if isinstance(self.coefficient_consolidation_vertical, Unset):
            coefficient_consolidation_vertical = UNSET
        else:
            coefficient_consolidation_vertical = self.coefficient_consolidation_vertical

        coefficient_consolidation_horizontal: Union[None, Unset, float, str]
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

        def _parse_method_id(data: object) -> Union[None, UUID, Unset]:
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
            return cast(Union[None, UUID, Unset], data)

        method_id = _parse_method_id(d.pop("method_id", UNSET))

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_remarks(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        remarks = _parse_remarks(d.pop("remarks", UNSET))

        def _parse_method_status_id(data: object) -> Union[MethodStatusEnum, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, int):
                    raise TypeError()
                method_status_id_type_0 = MethodStatusEnum(data)

                return method_status_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[MethodStatusEnum, None, Unset], data)

        method_status_id = _parse_method_status_id(d.pop("method_status_id", UNSET))

        def _parse_updated_at(data: object) -> Union[None, Unset, datetime.datetime]:
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
            return cast(Union[None, Unset, datetime.datetime], data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))

        def _parse_updated_by(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        updated_by = _parse_updated_by(d.pop("updated_by", UNSET))

        def _parse_conducted_by(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        conducted_by = _parse_conducted_by(d.pop("conducted_by", UNSET))

        def _parse_conducted_at(data: object) -> Union[None, Unset, datetime.datetime]:
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
            return cast(Union[None, Unset, datetime.datetime], data)

        conducted_at = _parse_conducted_at(d.pop("conducted_at", UNSET))

        method_type_id = cast(Union[Literal[22], Unset], d.pop("method_type_id", UNSET))
        if method_type_id != 22 and not isinstance(method_type_id, Unset):
            raise ValueError(f"method_type_id must match const 22, got '{method_type_id}'")

        def _parse_depth(data: object) -> Union[None, Unset, float, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, str], data)

        depth = _parse_depth(d.pop("depth", UNSET))

        def _parse_u2_initial(data: object) -> Union[None, Unset, float, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, str], data)

        u2_initial = _parse_u2_initial(d.pop("u2_initial", UNSET))

        def _parse_u2_equilibrium(data: object) -> Union[None, Unset, float, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, str], data)

        u2_equilibrium = _parse_u2_equilibrium(d.pop("u2_equilibrium", UNSET))

        def _parse_degree_dissipation(data: object) -> Union[None, Unset, float, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, str], data)

        degree_dissipation = _parse_degree_dissipation(d.pop("degree_dissipation", UNSET))

        def _parse_time_dissipation(data: object) -> Union[None, Unset, float, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, str], data)

        time_dissipation = _parse_time_dissipation(d.pop("time_dissipation", UNSET))

        def _parse_coefficient_consolidation_vertical(data: object) -> Union[None, Unset, float, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, str], data)

        coefficient_consolidation_vertical = _parse_coefficient_consolidation_vertical(
            d.pop("coefficient_consolidation_vertical", UNSET)
        )

        def _parse_coefficient_consolidation_horizontal(data: object) -> Union[None, Unset, float, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, str], data)

        coefficient_consolidation_horizontal = _parse_coefficient_consolidation_horizontal(
            d.pop("coefficient_consolidation_horizontal", UNSET)
        )

        method_dt_update = cls(
            method_id=method_id,
            name=name,
            remarks=remarks,
            method_status_id=method_status_id,
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

        method_dt_update.additional_properties = d
        return method_dt_update

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
