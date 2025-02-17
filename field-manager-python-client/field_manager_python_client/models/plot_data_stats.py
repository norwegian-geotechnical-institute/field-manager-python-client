from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.plot_data_stats_percentiles import PlotDataStatsPercentiles


T = TypeVar("T", bound="PlotDataStats")


@_attrs_define
class PlotDataStats:
    """
    Attributes:
        value_min (Union[float, str]):
        value_max (Union[float, str]):
        count (int):
        mean (Union[float, str]):
        std (Union[float, str]):
        percentiles (Union[Unset, PlotDataStatsPercentiles]):
    """

    value_min: Union[float, str]
    value_max: Union[float, str]
    count: int
    mean: Union[float, str]
    std: Union[float, str]
    percentiles: Union[Unset, "PlotDataStatsPercentiles"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value_min: Union[float, str]
        value_min = self.value_min

        value_max: Union[float, str]
        value_max = self.value_max

        count = self.count

        mean: Union[float, str]
        mean = self.mean

        std: Union[float, str]
        std = self.std

        percentiles: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.percentiles, Unset):
            percentiles = self.percentiles.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value_min": value_min,
                "value_max": value_max,
                "count": count,
                "mean": mean,
                "std": std,
            }
        )
        if percentiles is not UNSET:
            field_dict["percentiles"] = percentiles

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.plot_data_stats_percentiles import PlotDataStatsPercentiles

        d = src_dict.copy()

        def _parse_value_min(data: object) -> Union[float, str]:
            return cast(Union[float, str], data)

        value_min = _parse_value_min(d.pop("value_min"))

        def _parse_value_max(data: object) -> Union[float, str]:
            return cast(Union[float, str], data)

        value_max = _parse_value_max(d.pop("value_max"))

        count = d.pop("count")

        def _parse_mean(data: object) -> Union[float, str]:
            return cast(Union[float, str], data)

        mean = _parse_mean(d.pop("mean"))

        def _parse_std(data: object) -> Union[float, str]:
            return cast(Union[float, str], data)

        std = _parse_std(d.pop("std"))

        _percentiles = d.pop("percentiles", UNSET)
        percentiles: Union[Unset, PlotDataStatsPercentiles]
        if isinstance(_percentiles, Unset):
            percentiles = UNSET
        else:
            percentiles = PlotDataStatsPercentiles.from_dict(_percentiles)

        plot_data_stats = cls(
            value_min=value_min,
            value_max=value_max,
            count=count,
            mean=mean,
            std=std,
            percentiles=percentiles,
        )

        plot_data_stats.additional_properties = d
        return plot_data_stats

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
