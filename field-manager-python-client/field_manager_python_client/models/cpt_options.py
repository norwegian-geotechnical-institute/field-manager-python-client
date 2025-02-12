from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.scaling_mode import ScalingMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="CPTOptions")


@_attrs_define
class CPTOptions:
    """
    Attributes:
        scaling_mode (Union[Unset, ScalingMode]):
        percentile (Union[Unset, float]):  Default: 0.975.
    """

    scaling_mode: Union[Unset, ScalingMode] = UNSET
    percentile: Union[Unset, float] = 0.975
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        scaling_mode: Union[Unset, str] = UNSET
        if not isinstance(self.scaling_mode, Unset):
            scaling_mode = self.scaling_mode.value

        percentile = self.percentile

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if scaling_mode is not UNSET:
            field_dict["scaling_mode"] = scaling_mode
        if percentile is not UNSET:
            field_dict["percentile"] = percentile

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _scaling_mode = d.pop("scaling_mode", UNSET)
        scaling_mode: Union[Unset, ScalingMode]
        if isinstance(_scaling_mode, Unset):
            scaling_mode = UNSET
        else:
            scaling_mode = ScalingMode(_scaling_mode)

        percentile = d.pop("percentile", UNSET)

        cpt_options = cls(
            scaling_mode=scaling_mode,
            percentile=percentile,
        )

        cpt_options.additional_properties = d
        return cpt_options

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
