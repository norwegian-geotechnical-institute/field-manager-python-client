from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.plot_type import PlotType
from ..types import UNSET, Unset
from typing import cast
from typing import cast, List
from typing import Dict
from typing import Union
from uuid import UUID

if TYPE_CHECKING:
  from ..models.fm_plot_options import FMPlotOptions
  from ..models.pdf_options import PdfOptions





T = TypeVar("T", bound="Options")


@_attrs_define
class Options:
    """ 
        Attributes:
            location_ids (List[UUID]):
            pdf (Union[Unset, PdfOptions]):
            plot (Union[Unset, FMPlotOptions]):
            auto_set_depth (Union[Unset, bool]):  Default: False.
            methods (Union[Unset, List[PlotType]]):
     """

    location_ids: List[UUID]
    pdf: Union[Unset, 'PdfOptions'] = UNSET
    plot: Union[Unset, 'FMPlotOptions'] = UNSET
    auto_set_depth: Union[Unset, bool] = False
    methods: Union[Unset, List[PlotType]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.fm_plot_options import FMPlotOptions
        from ..models.pdf_options import PdfOptions
        location_ids = []
        for location_ids_item_data in self.location_ids:
            location_ids_item = str(location_ids_item_data)
            location_ids.append(location_ids_item)



        pdf: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pdf, Unset):
            pdf = self.pdf.to_dict()

        plot: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.plot, Unset):
            plot = self.plot.to_dict()

        auto_set_depth = self.auto_set_depth

        methods: Union[Unset, List[str]] = UNSET
        if not isinstance(self.methods, Unset):
            methods = []
            for methods_item_data in self.methods:
                methods_item = methods_item_data.value
                methods.append(methods_item)




        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "location_ids": location_ids,
        })
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
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fm_plot_options import FMPlotOptions
        from ..models.pdf_options import PdfOptions
        d = src_dict.copy()
        location_ids = []
        _location_ids = d.pop("location_ids")
        for location_ids_item_data in (_location_ids):
            location_ids_item = UUID(location_ids_item_data)



            location_ids.append(location_ids_item)


        _pdf = d.pop("pdf", UNSET)
        pdf: Union[Unset, PdfOptions]
        if isinstance(_pdf,  Unset):
            pdf = UNSET
        else:
            pdf = PdfOptions.from_dict(_pdf)




        _plot = d.pop("plot", UNSET)
        plot: Union[Unset, FMPlotOptions]
        if isinstance(_plot,  Unset):
            plot = UNSET
        else:
            plot = FMPlotOptions.from_dict(_plot)




        auto_set_depth = d.pop("auto_set_depth", UNSET)

        methods = []
        _methods = d.pop("methods", UNSET)
        for methods_item_data in (_methods or []):
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
