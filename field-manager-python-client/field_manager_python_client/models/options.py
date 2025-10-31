from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.plot_type import PlotType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fm_plot_options import FMPlotOptions
    from ..models.pdf_options import PdfOptions


T = TypeVar("T", bound="Options")


@_attrs_define
class Options:
    """
    Attributes:
        location_ids (list[UUID]):
        pdf (PdfOptions | Unset):
        plot (FMPlotOptions | Unset):
        auto_set_depth (bool | Unset):  Default: False.
        methods (list[PlotType] | Unset):
    """

    location_ids: list[UUID]
    pdf: PdfOptions | Unset = UNSET
    plot: FMPlotOptions | Unset = UNSET
    auto_set_depth: bool | Unset = False
    methods: list[PlotType] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        location_ids = []
        for location_ids_item_data in self.location_ids:
            location_ids_item = str(location_ids_item_data)
            location_ids.append(location_ids_item)

        pdf: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pdf, Unset):
            pdf = self.pdf.to_dict()

        plot: dict[str, Any] | Unset = UNSET
        if not isinstance(self.plot, Unset):
            plot = self.plot.to_dict()

        auto_set_depth = self.auto_set_depth

        methods: list[str] | Unset = UNSET
        if not isinstance(self.methods, Unset):
            methods = []
            for methods_item_data in self.methods:
                methods_item = methods_item_data.value
                methods.append(methods_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "location_ids": location_ids,
            }
        )
        if pdf is not UNSET:
            field_dict["pdf"] = pdf
        if plot is not UNSET:
            field_dict["plot"] = plot
        if auto_set_depth is not UNSET:
            field_dict["auto_set_depth"] = auto_set_depth
        if methods is not UNSET:
            field_dict["methods"] = methods

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fm_plot_options import FMPlotOptions
        from ..models.pdf_options import PdfOptions

        d = dict(src_dict)
        location_ids = []
        _location_ids = d.pop("location_ids")
        for location_ids_item_data in _location_ids:
            location_ids_item = UUID(location_ids_item_data)

            location_ids.append(location_ids_item)

        _pdf = d.pop("pdf", UNSET)
        pdf: PdfOptions | Unset
        if isinstance(_pdf, Unset):
            pdf = UNSET
        else:
            pdf = PdfOptions.from_dict(_pdf)

        _plot = d.pop("plot", UNSET)
        plot: FMPlotOptions | Unset
        if isinstance(_plot, Unset):
            plot = UNSET
        else:
            plot = FMPlotOptions.from_dict(_plot)

        auto_set_depth = d.pop("auto_set_depth", UNSET)

        methods = []
        _methods = d.pop("methods", UNSET)
        for methods_item_data in _methods or []:
            methods_item = PlotType(methods_item_data)

            methods.append(methods_item)

        options = cls(
            location_ids=location_ids,
            pdf=pdf,
            plot=plot,
            auto_set_depth=auto_set_depth,
            methods=methods,
        )

        options.additional_properties = d
        return options

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
