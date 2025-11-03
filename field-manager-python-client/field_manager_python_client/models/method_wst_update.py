from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.method_status_enum import MethodStatusEnum
from ..models.operation import Operation
from ..types import UNSET, Unset

T = TypeVar("T", bound="MethodWSTUpdate")


@_attrs_define
class MethodWSTUpdate:
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
        method_type_id (Literal[26] | Unset):  Default: 26.
        operation (None | Operation | Unset):
    """

    method_id: None | Unset | UUID = UNSET
    name: None | str | Unset = UNSET
    remarks: None | str | Unset = UNSET
    method_status_id: MethodStatusEnum | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    updated_by: None | str | Unset = UNSET
    conducted_by: None | str | Unset = UNSET
    conducted_at: datetime.datetime | None | Unset = UNSET
    method_type_id: Literal[26] | Unset = 26
    operation: None | Operation | Unset = UNSET
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

        operation: None | str | Unset
        if isinstance(self.operation, Unset):
            operation = UNSET
        elif isinstance(self.operation, Operation):
            operation = self.operation.value
        else:
            operation = self.operation

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
        if operation is not UNSET:
            field_dict["operation"] = operation

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

        method_type_id = cast(Literal[26] | Unset, d.pop("method_type_id", UNSET))
        if method_type_id != 26 and not isinstance(method_type_id, Unset):
            raise ValueError(f"method_type_id must match const 26, got '{method_type_id}'")

        def _parse_operation(data: object) -> None | Operation | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                operation_type_0 = Operation(data)

                return operation_type_0
            except:  # noqa: E722
                pass
            return cast(None | Operation | Unset, data)

        operation = _parse_operation(d.pop("operation", UNSET))

        method_wst_update = cls(
            method_id=method_id,
            name=name,
            remarks=remarks,
            method_status_id=method_status_id,
            updated_at=updated_at,
            updated_by=updated_by,
            conducted_by=conducted_by,
            conducted_at=conducted_at,
            method_type_id=method_type_id,
            operation=operation,
        )

        method_wst_update.additional_properties = d
        return method_wst_update

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
