from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.transformation_type import TransformationType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.piezometer_vendor import PiezometerVendor


T = TypeVar("T", bound="PiezometerModel")


@_attrs_define
class PiezometerModel:
    """
    Attributes:
        model_id (UUID):
        vendor_id (UUID):
        name (str):
        default_pore_pressure_unit (str):
        vendor (PiezometerVendor):
        piezometer_type (Union[None, Unset, str]):
        default_transformation_type (Union[None, TransformationType, Unset]):
        sort_order (Union[None, Unset, int]):
    """

    model_id: UUID
    vendor_id: UUID
    name: str
    default_pore_pressure_unit: str
    vendor: "PiezometerVendor"
    piezometer_type: Union[None, Unset, str] = UNSET
    default_transformation_type: Union[None, TransformationType, Unset] = UNSET
    sort_order: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model_id = str(self.model_id)

        vendor_id = str(self.vendor_id)

        name = self.name

        default_pore_pressure_unit = self.default_pore_pressure_unit

        vendor = self.vendor.to_dict()

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "model_id": model_id,
                "vendor_id": vendor_id,
                "name": name,
                "default_pore_pressure_unit": default_pore_pressure_unit,
                "vendor": vendor,
            }
        )
        if piezometer_type is not UNSET:
            field_dict["piezometer_type"] = piezometer_type
        if default_transformation_type is not UNSET:
            field_dict["default_transformation_type"] = default_transformation_type
        if sort_order is not UNSET:
            field_dict["sort_order"] = sort_order

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.piezometer_vendor import PiezometerVendor

        d = dict(src_dict)
        model_id = UUID(d.pop("model_id"))

        vendor_id = UUID(d.pop("vendor_id"))

        name = d.pop("name")

        default_pore_pressure_unit = d.pop("default_pore_pressure_unit")

        vendor = PiezometerVendor.from_dict(d.pop("vendor"))

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

        piezometer_model = cls(
            model_id=model_id,
            vendor_id=vendor_id,
            name=name,
            default_pore_pressure_unit=default_pore_pressure_unit,
            vendor=vendor,
            piezometer_type=piezometer_type,
            default_transformation_type=default_transformation_type,
            sort_order=sort_order,
        )

        piezometer_model.additional_properties = d
        return piezometer_model

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
