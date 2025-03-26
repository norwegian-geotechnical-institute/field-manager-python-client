import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.method_status_enum import MethodStatusEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file import File


T = TypeVar("T", bound="MethodDT")


@_attrs_define
class MethodDT:
    """DT

    Attributes:
        method_id (UUID):
        name (str):
        location_id (UUID):
        method_status_id (MethodStatusEnum): (
            PLANNED=1,
            READY=2,
            CONDUCTED=3,
            VOIDED=4,
            APPROVED=5,
            )
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        remarks (Union[None, Unset, str]):
        method_type_id (Union[Literal[22], Unset]):  Default: 22.
        created_by (Union[None, Unset, str]):
        updated_by (Union[None, Unset, str]):
        conducted_at (Union[None, Unset, datetime.datetime]):
        conducted_by (Union[None, Unset, str]):
        files (Union[Unset, list['File']]):
        self_ (Union[None, Unset, str]):
        depth (Union[None, Unset, float]): Depth (m). SGF code D.
        u2_initial (Union[None, Unset, float]): Initial shoulder pressure (kPa).
        u2_equilibrium (Union[None, Unset, float]): Equilibrium shoulder pressure (kPa).
        degree_dissipation (Union[None, Unset, float]): Degree of dissipation (%).
        time_dissipation (Union[None, Unset, float]): Time of dissipation (s).
        coefficient_consolidation_vertical (Union[None, Unset, float]): Vertical consolidation coefficient (m**2/year).
        coefficient_consolidation_horizontal (Union[None, Unset, float]): Horizontal consolidation coefficient
            (m**2/year). Year = 365.25 * days.
    """

    method_id: UUID
    name: str
    location_id: UUID
    method_status_id: MethodStatusEnum
    created_at: datetime.datetime
    updated_at: datetime.datetime
    remarks: Union[None, Unset, str] = UNSET
    method_type_id: Union[Literal[22], Unset] = 22
    created_by: Union[None, Unset, str] = UNSET
    updated_by: Union[None, Unset, str] = UNSET
    conducted_at: Union[None, Unset, datetime.datetime] = UNSET
    conducted_by: Union[None, Unset, str] = UNSET
    files: Union[Unset, list["File"]] = UNSET
    self_: Union[None, Unset, str] = UNSET
    depth: Union[None, Unset, float] = UNSET
    u2_initial: Union[None, Unset, float] = UNSET
    u2_equilibrium: Union[None, Unset, float] = UNSET
    degree_dissipation: Union[None, Unset, float] = UNSET
    time_dissipation: Union[None, Unset, float] = UNSET
    coefficient_consolidation_vertical: Union[None, Unset, float] = UNSET
    coefficient_consolidation_horizontal: Union[None, Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        method_id = str(self.method_id)

        name = self.name

        location_id = str(self.location_id)

        method_status_id = self.method_status_id.value

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        remarks: Union[None, Unset, str]
        if isinstance(self.remarks, Unset):
            remarks = UNSET
        else:
            remarks = self.remarks

        method_type_id = self.method_type_id

        created_by: Union[None, Unset, str]
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        else:
            created_by = self.created_by

        updated_by: Union[None, Unset, str]
        if isinstance(self.updated_by, Unset):
            updated_by = UNSET
        else:
            updated_by = self.updated_by

        conducted_at: Union[None, Unset, str]
        if isinstance(self.conducted_at, Unset):
            conducted_at = UNSET
        elif isinstance(self.conducted_at, datetime.datetime):
            conducted_at = self.conducted_at.isoformat()
        else:
            conducted_at = self.conducted_at

        conducted_by: Union[None, Unset, str]
        if isinstance(self.conducted_by, Unset):
            conducted_by = UNSET
        else:
            conducted_by = self.conducted_by

        files: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.files, Unset):
            files = []
            for files_item_data in self.files:
                files_item = files_item_data.to_dict()
                files.append(files_item)

        self_: Union[None, Unset, str]
        if isinstance(self.self_, Unset):
            self_ = UNSET
        else:
            self_ = self.self_

        depth: Union[None, Unset, float]
        if isinstance(self.depth, Unset):
            depth = UNSET
        else:
            depth = self.depth

        u2_initial: Union[None, Unset, float]
        if isinstance(self.u2_initial, Unset):
            u2_initial = UNSET
        else:
            u2_initial = self.u2_initial

        u2_equilibrium: Union[None, Unset, float]
        if isinstance(self.u2_equilibrium, Unset):
            u2_equilibrium = UNSET
        else:
            u2_equilibrium = self.u2_equilibrium

        degree_dissipation: Union[None, Unset, float]
        if isinstance(self.degree_dissipation, Unset):
            degree_dissipation = UNSET
        else:
            degree_dissipation = self.degree_dissipation

        time_dissipation: Union[None, Unset, float]
        if isinstance(self.time_dissipation, Unset):
            time_dissipation = UNSET
        else:
            time_dissipation = self.time_dissipation

        coefficient_consolidation_vertical: Union[None, Unset, float]
        if isinstance(self.coefficient_consolidation_vertical, Unset):
            coefficient_consolidation_vertical = UNSET
        else:
            coefficient_consolidation_vertical = self.coefficient_consolidation_vertical

        coefficient_consolidation_horizontal: Union[None, Unset, float]
        if isinstance(self.coefficient_consolidation_horizontal, Unset):
            coefficient_consolidation_horizontal = UNSET
        else:
            coefficient_consolidation_horizontal = self.coefficient_consolidation_horizontal

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "method_id": method_id,
                "name": name,
                "location_id": location_id,
                "method_status_id": method_status_id,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if remarks is not UNSET:
            field_dict["remarks"] = remarks
        if method_type_id is not UNSET:
            field_dict["method_type_id"] = method_type_id
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if updated_by is not UNSET:
            field_dict["updated_by"] = updated_by
        if conducted_at is not UNSET:
            field_dict["conducted_at"] = conducted_at
        if conducted_by is not UNSET:
            field_dict["conducted_by"] = conducted_by
        if files is not UNSET:
            field_dict["files"] = files
        if self_ is not UNSET:
            field_dict["self"] = self_
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
        from ..models.file import File

        d = dict(src_dict)
        method_id = UUID(d.pop("method_id"))

        name = d.pop("name")

        location_id = UUID(d.pop("location_id"))

        method_status_id = MethodStatusEnum(d.pop("method_status_id"))

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        def _parse_remarks(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        remarks = _parse_remarks(d.pop("remarks", UNSET))

        method_type_id = cast(Union[Literal[22], Unset], d.pop("method_type_id", UNSET))
        if method_type_id != 22 and not isinstance(method_type_id, Unset):
            raise ValueError(f"method_type_id must match const 22, got '{method_type_id}'")

        def _parse_created_by(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        created_by = _parse_created_by(d.pop("created_by", UNSET))

        def _parse_updated_by(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        updated_by = _parse_updated_by(d.pop("updated_by", UNSET))

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

        def _parse_conducted_by(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        conducted_by = _parse_conducted_by(d.pop("conducted_by", UNSET))

        files = []
        _files = d.pop("files", UNSET)
        for files_item_data in _files or []:
            files_item = File.from_dict(files_item_data)

            files.append(files_item)

        def _parse_self_(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        self_ = _parse_self_(d.pop("self", UNSET))

        def _parse_depth(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        depth = _parse_depth(d.pop("depth", UNSET))

        def _parse_u2_initial(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        u2_initial = _parse_u2_initial(d.pop("u2_initial", UNSET))

        def _parse_u2_equilibrium(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        u2_equilibrium = _parse_u2_equilibrium(d.pop("u2_equilibrium", UNSET))

        def _parse_degree_dissipation(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        degree_dissipation = _parse_degree_dissipation(d.pop("degree_dissipation", UNSET))

        def _parse_time_dissipation(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        time_dissipation = _parse_time_dissipation(d.pop("time_dissipation", UNSET))

        def _parse_coefficient_consolidation_vertical(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        coefficient_consolidation_vertical = _parse_coefficient_consolidation_vertical(
            d.pop("coefficient_consolidation_vertical", UNSET)
        )

        def _parse_coefficient_consolidation_horizontal(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        coefficient_consolidation_horizontal = _parse_coefficient_consolidation_horizontal(
            d.pop("coefficient_consolidation_horizontal", UNSET)
        )

        method_dt = cls(
            method_id=method_id,
            name=name,
            location_id=location_id,
            method_status_id=method_status_id,
            created_at=created_at,
            updated_at=updated_at,
            remarks=remarks,
            method_type_id=method_type_id,
            created_by=created_by,
            updated_by=updated_by,
            conducted_at=conducted_at,
            conducted_by=conducted_by,
            files=files,
            self_=self_,
            depth=depth,
            u2_initial=u2_initial,
            u2_equilibrium=u2_equilibrium,
            degree_dissipation=degree_dissipation,
            time_dissipation=time_dissipation,
            coefficient_consolidation_vertical=coefficient_consolidation_vertical,
            coefficient_consolidation_horizontal=coefficient_consolidation_horizontal,
        )

        method_dt.additional_properties = d
        return method_dt

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
