from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.dp_type import DPType
from ..models.method_status_enum import MethodStatusEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="MethodDPUpdate")


@_attrs_define
class MethodDPUpdate:
    """
    Attributes:
        method_id (None | Unset | UUID):
        name (None | str | Unset):
        remarks (None | str | Unset):
        method_status_id (MethodStatusEnum | None | Unset):
        updated_at (datetime.datetime | None | Unset):
        updated_by (None | str | Unset):
        conducted_by (None | str | Unset):
        conducted_at (datetime.datetime | None | Unset):
        method_type_id (Literal[25] | Unset):  Default: 25.
        dynamic_probing_type (DPType | None | Unset):
        predrilling_depth (float | None | str | Unset):
        cone_type (None | str | Unset):
        cushion_type (None | str | Unset):
        use_damper (bool | None | Unset):
    """

    method_id: None | Unset | UUID = UNSET
    name: None | str | Unset = UNSET
    remarks: None | str | Unset = UNSET
    method_status_id: MethodStatusEnum | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    updated_by: None | str | Unset = UNSET
    conducted_by: None | str | Unset = UNSET
    conducted_at: datetime.datetime | None | Unset = UNSET
    method_type_id: Literal[25] | Unset = 25
    dynamic_probing_type: DPType | None | Unset = UNSET
    predrilling_depth: float | None | str | Unset = UNSET
    cone_type: None | str | Unset = UNSET
    cushion_type: None | str | Unset = UNSET
    use_damper: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        method_id: None | str | Unset
        if isinstance(self.method_id, Unset):
            method_id = UNSET
        elif isinstance(self.method_id, UUID):
            method_id = str(self.method_id)
        else:
            method_id = self.method_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        remarks: None | str | Unset
        if isinstance(self.remarks, Unset):
            remarks = UNSET
        else:
            remarks = self.remarks

        method_status_id: int | None | Unset
        if isinstance(self.method_status_id, Unset):
            method_status_id = UNSET
        elif isinstance(self.method_status_id, MethodStatusEnum):
            method_status_id = self.method_status_id.value
        else:
            method_status_id = self.method_status_id

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

        dynamic_probing_type: None | str | Unset
        if isinstance(self.dynamic_probing_type, Unset):
            dynamic_probing_type = UNSET
        elif isinstance(self.dynamic_probing_type, DPType):
            dynamic_probing_type = self.dynamic_probing_type.value
        else:
            dynamic_probing_type = self.dynamic_probing_type

        predrilling_depth: float | None | str | Unset
        if isinstance(self.predrilling_depth, Unset):
            predrilling_depth = UNSET
        else:
            predrilling_depth = self.predrilling_depth

        cone_type: None | str | Unset
        if isinstance(self.cone_type, Unset):
            cone_type = UNSET
        else:
            cone_type = self.cone_type

        cushion_type: None | str | Unset
        if isinstance(self.cushion_type, Unset):
            cushion_type = UNSET
        else:
            cushion_type = self.cushion_type

        use_damper: bool | None | Unset
        if isinstance(self.use_damper, Unset):
            use_damper = UNSET
        else:
            use_damper = self.use_damper

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
        if dynamic_probing_type is not UNSET:
            field_dict["dynamic_probing_type"] = dynamic_probing_type
        if predrilling_depth is not UNSET:
            field_dict["predrilling_depth"] = predrilling_depth
        if cone_type is not UNSET:
            field_dict["cone_type"] = cone_type
        if cushion_type is not UNSET:
            field_dict["cushion_type"] = cushion_type
        if use_damper is not UNSET:
            field_dict["use_damper"] = use_damper

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

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_remarks(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remarks = _parse_remarks(d.pop("remarks", UNSET))

        def _parse_method_status_id(data: object) -> MethodStatusEnum | None | Unset:
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
            return cast(MethodStatusEnum | None | Unset, data)

        method_status_id = _parse_method_status_id(d.pop("method_status_id", UNSET))

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

        method_type_id = cast(Literal[25] | Unset, d.pop("method_type_id", UNSET))
        if method_type_id != 25 and not isinstance(method_type_id, Unset):
            raise ValueError(f"method_type_id must match const 25, got '{method_type_id}'")

        def _parse_dynamic_probing_type(data: object) -> DPType | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                dynamic_probing_type_type_0 = DPType(data)

                return dynamic_probing_type_type_0
            except:  # noqa: E722
                pass
            return cast(DPType | None | Unset, data)

        dynamic_probing_type = _parse_dynamic_probing_type(d.pop("dynamic_probing_type", UNSET))

        def _parse_predrilling_depth(data: object) -> float | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | str | Unset, data)

        predrilling_depth = _parse_predrilling_depth(d.pop("predrilling_depth", UNSET))

        def _parse_cone_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cone_type = _parse_cone_type(d.pop("cone_type", UNSET))

        def _parse_cushion_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cushion_type = _parse_cushion_type(d.pop("cushion_type", UNSET))

        def _parse_use_damper(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        use_damper = _parse_use_damper(d.pop("use_damper", UNSET))

        method_dp_update = cls(
            method_id=method_id,
            name=name,
            remarks=remarks,
            method_status_id=method_status_id,
            updated_at=updated_at,
            updated_by=updated_by,
            conducted_by=conducted_by,
            conducted_at=conducted_at,
            method_type_id=method_type_id,
            dynamic_probing_type=dynamic_probing_type,
            predrilling_depth=predrilling_depth,
            cone_type=cone_type,
            cushion_type=cushion_type,
            use_damper=use_damper,
        )

        method_dp_update.additional_properties = d
        return method_dp_update

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
