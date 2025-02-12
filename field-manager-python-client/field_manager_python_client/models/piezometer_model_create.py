from typing import Any, Dict, List, Type, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.transformation_type import TransformationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PiezometerModelCreate")


@_attrs_define
class PiezometerModelCreate:
    """
    Attributes:
        vendor_id (UUID):
        name (str):
        default_pore_pressure_unit (str):
        model_id (Union[None, UUID, Unset]):
        piezometer_type (Union[None, Unset, str]):
        default_transformation_type (Union[None, TransformationType, Unset]):
        sort_order (Union[None, Unset, int]):
    """

    vendor_id: UUID
    name: str
    default_pore_pressure_unit: str
    model_id: Union[None, UUID, Unset] = UNSET
    piezometer_type: Union[None, Unset, str] = UNSET
    default_transformation_type: Union[None, TransformationType, Unset] = UNSET
    sort_order: Union[None, Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        vendor_id = str(self.vendor_id)

        name = self.name

        default_pore_pressure_unit = self.default_pore_pressure_unit

        model_id: Union[None, Unset, str]
        if isinstance(self.model_id, Unset):
            model_id = UNSET
        elif isinstance(self.model_id, UUID):
            model_id = str(self.model_id)
        else:
            model_id = self.model_id

        piezometer_type: Union[None, Unset, str]
        if isinstance(self.piezometer_type, Unset):
            piezometer_type = UNSET
        else:
            piezometer_type = self.piezometer_type

        default_transformation_type: Union[None, Unset, str]
        if isinstance(self.default_transformation_type, Unset):
            default_transformation_type = UNSET
        elif isinstance(self.default_transformation_type, TransformationType):
            default_transformation_type = self.default_transformation_type.value
        else:
            default_transformation_type = self.default_transformation_type

        sort_order: Union[None, Unset, int]
        if isinstance(self.sort_order, Unset):
            sort_order = UNSET
        else:
            sort_order = self.sort_order

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "vendor_id": vendor_id,
                "name": name,
                "default_pore_pressure_unit": default_pore_pressure_unit,
            }
        )
        if model_id is not UNSET:
            field_dict["model_id"] = model_id
        if piezometer_type is not UNSET:
            field_dict["piezometer_type"] = piezometer_type
        if default_transformation_type is not UNSET:
            field_dict["default_transformation_type"] = default_transformation_type
        if sort_order is not UNSET:
            field_dict["sort_order"] = sort_order

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        vendor_id = UUID(d.pop("vendor_id"))

        name = d.pop("name")

        default_pore_pressure_unit = d.pop("default_pore_pressure_unit")

        def _parse_model_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                model_id_type_0 = UUID(data)

                return model_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        model_id = _parse_model_id(d.pop("model_id", UNSET))

        def _parse_piezometer_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        piezometer_type = _parse_piezometer_type(d.pop("piezometer_type", UNSET))

        def _parse_default_transformation_type(data: object) -> Union[None, TransformationType, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                default_transformation_type_type_0 = TransformationType(data)

                return default_transformation_type_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, TransformationType, Unset], data)

        default_transformation_type = _parse_default_transformation_type(d.pop("default_transformation_type", UNSET))

        def _parse_sort_order(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        sort_order = _parse_sort_order(d.pop("sort_order", UNSET))

        piezometer_model_create = cls(
            vendor_id=vendor_id,
            name=name,
            default_pore_pressure_unit=default_pore_pressure_unit,
            model_id=model_id,
            piezometer_type=piezometer_type,
            default_transformation_type=default_transformation_type,
            sort_order=sort_order,
        )

        piezometer_model_create.additional_properties = d
        return piezometer_model_create

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
