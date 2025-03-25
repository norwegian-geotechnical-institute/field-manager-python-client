from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.location_type import LocationType
from ..models.plot_type import PlotType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fm_plot_options import FMPlotOptions
    from ..models.location_coordinates import LocationCoordinates
    from ..models.location_info import LocationInfo
    from ..models.method_info import MethodInfo
    from ..models.pdf_page_info import PDFPageInfo
    from ..models.plot_info_object_stats_type_0 import PlotInfoObjectStatsType0


T = TypeVar("T", bound="PlotInfoObject")


@_attrs_define
class PlotInfoObject:
    """
    Attributes:
        project_id (UUID):
        location_type (LocationType):
        location_ids (list[UUID]):
        location_names (list[str]):
        location_coordinates (list['LocationCoordinates']):
        location_info (list['LocationInfo']):
        method_info (list['MethodInfo']):
        method_ids (list[UUID]):
        method_type (str):
        is_combined_plot (bool):
        plot_type (PlotType):
        plot_options (FMPlotOptions):
        messages (Union[None, Unset, list[str]]):
        pdf_info (Union[Unset, PDFPageInfo]):
        stats (Union['PlotInfoObjectStatsType0', None, Unset]):
    """

    project_id: UUID
    location_type: LocationType
    location_ids: list[UUID]
    location_names: list[str]
    location_coordinates: list["LocationCoordinates"]
    location_info: list["LocationInfo"]
    method_info: list["MethodInfo"]
    method_ids: list[UUID]
    method_type: str
    is_combined_plot: bool
    plot_type: PlotType
    plot_options: "FMPlotOptions"
    messages: Union[None, Unset, list[str]] = UNSET
    pdf_info: Union[Unset, "PDFPageInfo"] = UNSET
    stats: Union["PlotInfoObjectStatsType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.plot_info_object_stats_type_0 import PlotInfoObjectStatsType0

        project_id = str(self.project_id)

        location_type = self.location_type.value

        location_ids = []
        for location_ids_item_data in self.location_ids:
            location_ids_item = str(location_ids_item_data)
            location_ids.append(location_ids_item)

        location_names = self.location_names

        location_coordinates = []
        for location_coordinates_item_data in self.location_coordinates:
            location_coordinates_item = location_coordinates_item_data.to_dict()
            location_coordinates.append(location_coordinates_item)

        location_info = []
        for location_info_item_data in self.location_info:
            location_info_item = location_info_item_data.to_dict()
            location_info.append(location_info_item)

        method_info = []
        for method_info_item_data in self.method_info:
            method_info_item = method_info_item_data.to_dict()
            method_info.append(method_info_item)

        method_ids = []
        for method_ids_item_data in self.method_ids:
            method_ids_item = str(method_ids_item_data)
            method_ids.append(method_ids_item)

        method_type = self.method_type

        is_combined_plot = self.is_combined_plot

        plot_type = self.plot_type.value

        plot_options = self.plot_options.to_dict()

        messages: Union[None, Unset, list[str]]
        if isinstance(self.messages, Unset):
            messages = UNSET
        elif isinstance(self.messages, list):
            messages = self.messages

        else:
            messages = self.messages

        pdf_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pdf_info, Unset):
            pdf_info = self.pdf_info.to_dict()

        stats: Union[None, Unset, dict[str, Any]]
        if isinstance(self.stats, Unset):
            stats = UNSET
        elif isinstance(self.stats, PlotInfoObjectStatsType0):
            stats = self.stats.to_dict()
        else:
            stats = self.stats

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "project_id": project_id,
                "location_type": location_type,
                "location_ids": location_ids,
                "location_names": location_names,
                "location_coordinates": location_coordinates,
                "location_info": location_info,
                "method_info": method_info,
                "method_ids": method_ids,
                "method_type": method_type,
                "is_combined_plot": is_combined_plot,
                "plot_type": plot_type,
                "plot_options": plot_options,
            }
        )
        if messages is not UNSET:
            field_dict["messages"] = messages
        if pdf_info is not UNSET:
            field_dict["pdf_info"] = pdf_info
        if stats is not UNSET:
            field_dict["stats"] = stats

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fm_plot_options import FMPlotOptions
        from ..models.location_coordinates import LocationCoordinates
        from ..models.location_info import LocationInfo
        from ..models.method_info import MethodInfo
        from ..models.pdf_page_info import PDFPageInfo
        from ..models.plot_info_object_stats_type_0 import PlotInfoObjectStatsType0

        d = dict(src_dict)
        project_id = UUID(d.pop("project_id"))

        location_type = LocationType(d.pop("location_type"))

        location_ids = []
        _location_ids = d.pop("location_ids")
        for location_ids_item_data in _location_ids:
            location_ids_item = UUID(location_ids_item_data)

            location_ids.append(location_ids_item)

        location_names = cast(list[str], d.pop("location_names"))

        location_coordinates = []
        _location_coordinates = d.pop("location_coordinates")
        for location_coordinates_item_data in _location_coordinates:
            location_coordinates_item = LocationCoordinates.from_dict(location_coordinates_item_data)

            location_coordinates.append(location_coordinates_item)

        location_info = []
        _location_info = d.pop("location_info")
        for location_info_item_data in _location_info:
            location_info_item = LocationInfo.from_dict(location_info_item_data)

            location_info.append(location_info_item)

        method_info = []
        _method_info = d.pop("method_info")
        for method_info_item_data in _method_info:
            method_info_item = MethodInfo.from_dict(method_info_item_data)

            method_info.append(method_info_item)

        method_ids = []
        _method_ids = d.pop("method_ids")
        for method_ids_item_data in _method_ids:
            method_ids_item = UUID(method_ids_item_data)

            method_ids.append(method_ids_item)

        method_type = d.pop("method_type")

        is_combined_plot = d.pop("is_combined_plot")

        plot_type = PlotType(d.pop("plot_type"))

        plot_options = FMPlotOptions.from_dict(d.pop("plot_options"))

        def _parse_messages(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                messages_type_0 = cast(list[str], data)

                return messages_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        messages = _parse_messages(d.pop("messages", UNSET))

        _pdf_info = d.pop("pdf_info", UNSET)
        pdf_info: Union[Unset, PDFPageInfo]
        if isinstance(_pdf_info, Unset):
            pdf_info = UNSET
        else:
            pdf_info = PDFPageInfo.from_dict(_pdf_info)

        def _parse_stats(data: object) -> Union["PlotInfoObjectStatsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                stats_type_0 = PlotInfoObjectStatsType0.from_dict(data)

                return stats_type_0
            except:  # noqa: E722
                pass
            return cast(Union["PlotInfoObjectStatsType0", None, Unset], data)

        stats = _parse_stats(d.pop("stats", UNSET))

        plot_info_object = cls(
            project_id=project_id,
            location_type=location_type,
            location_ids=location_ids,
            location_names=location_names,
            location_coordinates=location_coordinates,
            location_info=location_info,
            method_info=method_info,
            method_ids=method_ids,
            method_type=method_type,
            is_combined_plot=is_combined_plot,
            plot_type=plot_type,
            plot_options=plot_options,
            messages=messages,
            pdf_info=pdf_info,
            stats=stats,
        )

        plot_info_object.additional_properties = d
        return plot_info_object

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
