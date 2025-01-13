import datetime
from typing import Any, Literal, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.application_class_enum import ApplicationClassEnum
from ..models.method_status_enum import MethodStatusEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="MethodCPTUpdate")


@_attrs_define
class MethodCPTUpdate:
    """Structure for updating a cone penetration test method instance

    Attributes:
        method_id (Union[None, UUID, Unset]):
        name (Union[None, Unset, str]):
        remarks (Union[None, Unset, str]):
        method_status_id (Union[MethodStatusEnum, None, Unset]):
        updated_at (Union[None, Unset, datetime.datetime]):
        updated_by (Union[None, Unset, str]):
        conducted_by (Union[None, Unset, str]):
        conducted_at (Union[None, Unset, datetime.datetime]):
        method_type_id (Union[Literal[1], Unset]):  Default: 1.
        predrilling_depth (Union[None, Unset, float, str]):
        cone_reference (Union[None, Unset, str]):
        water_depth (Union[None, Unset, float, str]):
        cone_area_ratio (Union[None, Unset, float, str]):
        sleeve_area_ratio (Union[None, Unset, float, str]):
        application_class_depth (Union[Unset, ApplicationClassEnum]): (
            ONE=1,
            TWO=2,
            THREE=3,
            FOUR=4,
            OUT_OF_BOUNDS=10,
            UNKNOWN=100,
            )
        application_class_resistance (Union[Unset, ApplicationClassEnum]): (
            ONE=1,
            TWO=2,
            THREE=3,
            FOUR=4,
            OUT_OF_BOUNDS=10,
            UNKNOWN=100,
            )
        application_class_friction (Union[Unset, ApplicationClassEnum]): (
            ONE=1,
            TWO=2,
            THREE=3,
            FOUR=4,
            OUT_OF_BOUNDS=10,
            UNKNOWN=100,
            )
        application_class_pressure (Union[Unset, ApplicationClassEnum]): (
            ONE=1,
            TWO=2,
            THREE=3,
            FOUR=4,
            OUT_OF_BOUNDS=10,
            UNKNOWN=100,
            )
    """

    method_id: Union[None, UUID, Unset] = UNSET
    name: Union[None, Unset, str] = UNSET
    remarks: Union[None, Unset, str] = UNSET
    method_status_id: Union[MethodStatusEnum, None, Unset] = UNSET
    updated_at: Union[None, Unset, datetime.datetime] = UNSET
    updated_by: Union[None, Unset, str] = UNSET
    conducted_by: Union[None, Unset, str] = UNSET
    conducted_at: Union[None, Unset, datetime.datetime] = UNSET
    method_type_id: Union[Literal[1], Unset] = 1
    predrilling_depth: Union[None, Unset, float, str] = UNSET
    cone_reference: Union[None, Unset, str] = UNSET
    water_depth: Union[None, Unset, float, str] = UNSET
    cone_area_ratio: Union[None, Unset, float, str] = UNSET
    sleeve_area_ratio: Union[None, Unset, float, str] = UNSET
    application_class_depth: Union[Unset, ApplicationClassEnum] = UNSET
    application_class_resistance: Union[Unset, ApplicationClassEnum] = UNSET
    application_class_friction: Union[Unset, ApplicationClassEnum] = UNSET
    application_class_pressure: Union[Unset, ApplicationClassEnum] = UNSET
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

        predrilling_depth: Union[None, Unset, float, str]
        if isinstance(self.predrilling_depth, Unset):
            predrilling_depth = UNSET
        else:
            predrilling_depth = self.predrilling_depth

        cone_reference: Union[None, Unset, str]
        if isinstance(self.cone_reference, Unset):
            cone_reference = UNSET
        else:
            cone_reference = self.cone_reference

        water_depth: Union[None, Unset, float, str]
        if isinstance(self.water_depth, Unset):
            water_depth = UNSET
        else:
            water_depth = self.water_depth

        cone_area_ratio: Union[None, Unset, float, str]
        if isinstance(self.cone_area_ratio, Unset):
            cone_area_ratio = UNSET
        else:
            cone_area_ratio = self.cone_area_ratio

        sleeve_area_ratio: Union[None, Unset, float, str]
        if isinstance(self.sleeve_area_ratio, Unset):
            sleeve_area_ratio = UNSET
        else:
            sleeve_area_ratio = self.sleeve_area_ratio

        application_class_depth: Union[Unset, int] = UNSET
        if not isinstance(self.application_class_depth, Unset):
            application_class_depth = self.application_class_depth.value

        application_class_resistance: Union[Unset, int] = UNSET
        if not isinstance(self.application_class_resistance, Unset):
            application_class_resistance = self.application_class_resistance.value

        application_class_friction: Union[Unset, int] = UNSET
        if not isinstance(self.application_class_friction, Unset):
            application_class_friction = self.application_class_friction.value

        application_class_pressure: Union[Unset, int] = UNSET
        if not isinstance(self.application_class_pressure, Unset):
            application_class_pressure = self.application_class_pressure.value

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
        if predrilling_depth is not UNSET:
            field_dict["predrilling_depth"] = predrilling_depth
        if cone_reference is not UNSET:
            field_dict["cone_reference"] = cone_reference
        if water_depth is not UNSET:
            field_dict["water_depth"] = water_depth
        if cone_area_ratio is not UNSET:
            field_dict["cone_area_ratio"] = cone_area_ratio
        if sleeve_area_ratio is not UNSET:
            field_dict["sleeve_area_ratio"] = sleeve_area_ratio
        if application_class_depth is not UNSET:
            field_dict["application_class_depth"] = application_class_depth
        if application_class_resistance is not UNSET:
            field_dict["application_class_resistance"] = application_class_resistance
        if application_class_friction is not UNSET:
            field_dict["application_class_friction"] = application_class_friction
        if application_class_pressure is not UNSET:
            field_dict["application_class_pressure"] = application_class_pressure

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()

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

        method_type_id = cast(Union[Literal[1], Unset], d.pop("method_type_id", UNSET))
        if method_type_id != 1 and not isinstance(method_type_id, Unset):
            raise ValueError(f"method_type_id must match const 1, got '{method_type_id}'")

        def _parse_predrilling_depth(data: object) -> Union[None, Unset, float, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, str], data)

        predrilling_depth = _parse_predrilling_depth(d.pop("predrilling_depth", UNSET))

        def _parse_cone_reference(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cone_reference = _parse_cone_reference(d.pop("cone_reference", UNSET))

        def _parse_water_depth(data: object) -> Union[None, Unset, float, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, str], data)

        water_depth = _parse_water_depth(d.pop("water_depth", UNSET))

        def _parse_cone_area_ratio(data: object) -> Union[None, Unset, float, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, str], data)

        cone_area_ratio = _parse_cone_area_ratio(d.pop("cone_area_ratio", UNSET))

        def _parse_sleeve_area_ratio(data: object) -> Union[None, Unset, float, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, str], data)

        sleeve_area_ratio = _parse_sleeve_area_ratio(d.pop("sleeve_area_ratio", UNSET))

        _application_class_depth = d.pop("application_class_depth", UNSET)
        application_class_depth: Union[Unset, ApplicationClassEnum]
        if isinstance(_application_class_depth, Unset):
            application_class_depth = UNSET
        else:
            application_class_depth = ApplicationClassEnum(_application_class_depth)

        _application_class_resistance = d.pop("application_class_resistance", UNSET)
        application_class_resistance: Union[Unset, ApplicationClassEnum]
        if isinstance(_application_class_resistance, Unset):
            application_class_resistance = UNSET
        else:
            application_class_resistance = ApplicationClassEnum(_application_class_resistance)

        _application_class_friction = d.pop("application_class_friction", UNSET)
        application_class_friction: Union[Unset, ApplicationClassEnum]
        if isinstance(_application_class_friction, Unset):
            application_class_friction = UNSET
        else:
            application_class_friction = ApplicationClassEnum(_application_class_friction)

        _application_class_pressure = d.pop("application_class_pressure", UNSET)
        application_class_pressure: Union[Unset, ApplicationClassEnum]
        if isinstance(_application_class_pressure, Unset):
            application_class_pressure = UNSET
        else:
            application_class_pressure = ApplicationClassEnum(_application_class_pressure)

        method_cpt_update = cls(
            method_id=method_id,
            name=name,
            remarks=remarks,
            method_status_id=method_status_id,
            updated_at=updated_at,
            updated_by=updated_by,
            conducted_by=conducted_by,
            conducted_at=conducted_at,
            method_type_id=method_type_id,
            predrilling_depth=predrilling_depth,
            cone_reference=cone_reference,
            water_depth=water_depth,
            cone_area_ratio=cone_area_ratio,
            sleeve_area_ratio=sleeve_area_ratio,
            application_class_depth=application_class_depth,
            application_class_resistance=application_class_resistance,
            application_class_friction=application_class_friction,
            application_class_pressure=application_class_pressure,
        )

        method_cpt_update.additional_properties = d
        return method_cpt_update

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
