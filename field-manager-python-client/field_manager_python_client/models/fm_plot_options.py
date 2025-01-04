from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.scales import Scales
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cpt_options import CPTOptions


T = TypeVar("T", bound="FMPlotOptions")


@_attrs_define
class FMPlotOptions:
    """
    Attributes:
        fill_curve (Union[Unset, bool]):  Default: True.
        depth_scale (Union[Unset, Scales]):
        depth_range (Union[None, Unset, list[float]]):
        cpt (Union[Unset, CPTOptions]):
    """

    fill_curve: Union[Unset, bool] = True
    depth_scale: Union[Unset, Scales] = UNSET
    depth_range: Union[None, Unset, list[float]] = UNSET
    cpt: Union[Unset, "CPTOptions"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fill_curve = self.fill_curve

        depth_scale: Union[Unset, str] = UNSET
        if not isinstance(self.depth_scale, Unset):
            depth_scale = self.depth_scale.value

        depth_range: Union[None, Unset, list[float]]
        if isinstance(self.depth_range, Unset):
            depth_range = UNSET
        elif isinstance(self.depth_range, list):
            depth_range = []
            for depth_range_type_0_item_data in self.depth_range:
                depth_range_type_0_item: float
                depth_range_type_0_item = depth_range_type_0_item_data
                depth_range.append(depth_range_type_0_item)

        else:
            depth_range = self.depth_range

        cpt: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cpt, Unset):
            cpt = self.cpt.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fill_curve is not UNSET:
            field_dict["fill_curve"] = fill_curve
        if depth_scale is not UNSET:
            field_dict["depth_scale"] = depth_scale
        if depth_range is not UNSET:
            field_dict["depth_range"] = depth_range
        if cpt is not UNSET:
            field_dict["cpt"] = cpt

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.cpt_options import CPTOptions

        d = src_dict.copy()
        fill_curve = d.pop("fill_curve", UNSET)

        _depth_scale = d.pop("depth_scale", UNSET)
        depth_scale: Union[Unset, Scales]
        if isinstance(_depth_scale, Unset):
            depth_scale = UNSET
        else:
            depth_scale = Scales(_depth_scale)

        def _parse_depth_range(data: object) -> Union[None, Unset, list[float]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                depth_range_type_0 = []
                _depth_range_type_0 = data
                for depth_range_type_0_item_data in _depth_range_type_0:

                    def _parse_depth_range_type_0_item(data: object) -> float:
                        return cast(float, data)

                    depth_range_type_0_item = _parse_depth_range_type_0_item(depth_range_type_0_item_data)

                    depth_range_type_0.append(depth_range_type_0_item)

                return depth_range_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[float]], data)

        depth_range = _parse_depth_range(d.pop("depth_range", UNSET))

        _cpt = d.pop("cpt", UNSET)
        cpt: Union[Unset, CPTOptions]
        if isinstance(_cpt, Unset):
            cpt = UNSET
        else:
            cpt = CPTOptions.from_dict(_cpt)

        fm_plot_options = cls(
            fill_curve=fill_curve,
            depth_scale=depth_scale,
            depth_range=depth_range,
            cpt=cpt,
        )

        fm_plot_options.additional_properties = d
        return fm_plot_options

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
