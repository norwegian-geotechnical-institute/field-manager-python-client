from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.piezometer_type import PiezometerType
from ..models.transformation_type import TransformationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PizeometerUnits")


@_attrs_define
class PizeometerUnits:
    """
    Attributes:
        type (Union[Unset, PiezometerType]): (
            ELECTRIC = Piezometer Electric,
            HYDRAULIC = Piezometer Hydraulic,
            STANDPIPE = Piezometer Standpipe,
            )
        transformation (Union[Unset, TransformationType]): Piezometer Transformation Types
        units (Union[Unset, List[Union[None, str]]]):
        default_unit (Union[None, Unset, str]):
    """

    type: Union[Unset, PiezometerType] = UNSET
    transformation: Union[Unset, TransformationType] = UNSET
    units: Union[Unset, List[Union[None, str]]] = UNSET
    default_unit: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        transformation: Union[Unset, str] = UNSET
        if not isinstance(self.transformation, Unset):
            transformation = self.transformation.value

        units: Union[Unset, List[Union[None, str]]] = UNSET
        if not isinstance(self.units, Unset):
            units = []
            for units_item_data in self.units:
                units_item: Union[None, str]
                units_item = units_item_data
                units.append(units_item)

        default_unit: Union[None, Unset, str]
        if isinstance(self.default_unit, Unset):
            default_unit = UNSET
        else:
            default_unit = self.default_unit

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if transformation is not UNSET:
            field_dict["transformation"] = transformation
        if units is not UNSET:
            field_dict["units"] = units
        if default_unit is not UNSET:
            field_dict["default_unit"] = default_unit

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[Unset, PiezometerType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = PiezometerType(_type)

        _transformation = d.pop("transformation", UNSET)
        transformation: Union[Unset, TransformationType]
        if isinstance(_transformation, Unset):
            transformation = UNSET
        else:
            transformation = TransformationType(_transformation)

        units = []
        _units = d.pop("units", UNSET)
        for units_item_data in _units or []:

            def _parse_units_item(data: object) -> Union[None, str]:
                if data is None:
                    return data
                return cast(Union[None, str], data)

            units_item = _parse_units_item(units_item_data)

            units.append(units_item)

        def _parse_default_unit(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        default_unit = _parse_default_unit(d.pop("default_unit", UNSET))

        pizeometer_units = cls(
            type=type,
            transformation=transformation,
            units=units,
            default_unit=default_unit,
        )

        pizeometer_units.additional_properties = d
        return pizeometer_units

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
