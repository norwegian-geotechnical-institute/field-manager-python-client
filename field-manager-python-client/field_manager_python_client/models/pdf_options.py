from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.color_mode import ColorMode
from ..models.pdf_options_date_format import PdfOptionsDateFormat
from ..models.pdf_options_lang import PdfOptionsLang
from ..models.pdf_options_paper_size import PdfOptionsPaperSize
from ..models.pdf_options_sort_figures_by import PdfOptionsSortFiguresBy
from ..models.scales import Scales
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.page_number_prefix_by_method import PageNumberPrefixByMethod
    from ..models.page_number_start_per_method import PageNumberStartPerMethod


T = TypeVar("T", bound="PdfOptions")


@_attrs_define
class PdfOptions:
    """
    Attributes:
        lang (Union[Unset, PdfOptionsLang]):  Default: PdfOptionsLang.ENG.
        date_format (Union[Unset, PdfOptionsDateFormat]):  Default: PdfOptionsDateFormat.YYYY_MM_DD.
        date (Union[Unset, str]):  Default: ''.
        use_controlled_by (Union[Unset, bool]):  Default: False.
        use_revision (Union[Unset, bool]):  Default: True.
        report_number_suffix (Union[Unset, str]):  Default: ''.
        revision (Union[Unset, str]):  Default: ''.
        paper_size (Union[Unset, PdfOptionsPaperSize]):  Default: PdfOptionsPaperSize.A4.
        plot_scale (Union[Unset, Scales]):
        report_number (Union[Unset, str]):  Default: ''.
        client_name (Union[Unset, str]):  Default: ''.
        sort_figures_by (Union[Unset, PdfOptionsSortFiguresBy]):  Default: PdfOptionsSortFiguresBy.LOCATION.
        page_number_prefix (Union[Unset, str]):  Default: ''.
        page_number_start (Union[Unset, str]):  Default: '1'.
        page_number_prefix_per_method (Union[Unset, PageNumberPrefixByMethod]):
        page_number_start_per_method (Union[Unset, PageNumberStartPerMethod]):
        drawn_by (Union[Unset, str]):  Default: ''.
        controlled_by (Union[Unset, str]):  Default: ''.
        use_approved_by (Union[Unset, bool]):  Default: True.
        approved_by (Union[Unset, str]):  Default: ''.
        show_comment_in_plot (Union[Unset, bool]):  Default: False.
        projection_system (Union[Unset, str]):  Default: ''.
        max_pages (Union[Unset, int]):  Default: -1.
        color_mode (Union[Unset, ColorMode]):
        fill_curve (Union[Unset, bool]):  Default: True.
    """

    lang: Union[Unset, PdfOptionsLang] = PdfOptionsLang.ENG
    date_format: Union[Unset, PdfOptionsDateFormat] = PdfOptionsDateFormat.YYYY_MM_DD
    date: Union[Unset, str] = ""
    use_controlled_by: Union[Unset, bool] = False
    use_revision: Union[Unset, bool] = True
    report_number_suffix: Union[Unset, str] = ""
    revision: Union[Unset, str] = ""
    paper_size: Union[Unset, PdfOptionsPaperSize] = PdfOptionsPaperSize.A4
    plot_scale: Union[Unset, Scales] = UNSET
    report_number: Union[Unset, str] = ""
    client_name: Union[Unset, str] = ""
    sort_figures_by: Union[Unset, PdfOptionsSortFiguresBy] = PdfOptionsSortFiguresBy.LOCATION
    page_number_prefix: Union[Unset, str] = ""
    page_number_start: Union[Unset, str] = "1"
    page_number_prefix_per_method: Union[Unset, "PageNumberPrefixByMethod"] = UNSET
    page_number_start_per_method: Union[Unset, "PageNumberStartPerMethod"] = UNSET
    drawn_by: Union[Unset, str] = ""
    controlled_by: Union[Unset, str] = ""
    use_approved_by: Union[Unset, bool] = True
    approved_by: Union[Unset, str] = ""
    show_comment_in_plot: Union[Unset, bool] = False
    projection_system: Union[Unset, str] = ""
    max_pages: Union[Unset, int] = -1
    color_mode: Union[Unset, ColorMode] = UNSET
    fill_curve: Union[Unset, bool] = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lang: Union[Unset, str] = UNSET
        if not isinstance(self.lang, Unset):
            lang = self.lang.value

        date_format: Union[Unset, str] = UNSET
        if not isinstance(self.date_format, Unset):
            date_format = self.date_format.value

        date = self.date

        use_controlled_by = self.use_controlled_by

        use_revision = self.use_revision

        report_number_suffix = self.report_number_suffix

        revision = self.revision

        paper_size: Union[Unset, str] = UNSET
        if not isinstance(self.paper_size, Unset):
            paper_size = self.paper_size.value

        plot_scale: Union[Unset, str] = UNSET
        if not isinstance(self.plot_scale, Unset):
            plot_scale = self.plot_scale.value

        report_number = self.report_number

        client_name = self.client_name

        sort_figures_by: Union[Unset, str] = UNSET
        if not isinstance(self.sort_figures_by, Unset):
            sort_figures_by = self.sort_figures_by.value

        page_number_prefix = self.page_number_prefix

        page_number_start = self.page_number_start

        page_number_prefix_per_method: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.page_number_prefix_per_method, Unset):
            page_number_prefix_per_method = self.page_number_prefix_per_method.to_dict()

        page_number_start_per_method: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.page_number_start_per_method, Unset):
            page_number_start_per_method = self.page_number_start_per_method.to_dict()

        drawn_by = self.drawn_by

        controlled_by = self.controlled_by

        use_approved_by = self.use_approved_by

        approved_by = self.approved_by

        show_comment_in_plot = self.show_comment_in_plot

        projection_system = self.projection_system

        max_pages = self.max_pages

        color_mode: Union[Unset, str] = UNSET
        if not isinstance(self.color_mode, Unset):
            color_mode = self.color_mode.value

        fill_curve = self.fill_curve

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lang is not UNSET:
            field_dict["lang"] = lang
        if date_format is not UNSET:
            field_dict["date_format"] = date_format
        if date is not UNSET:
            field_dict["date"] = date
        if use_controlled_by is not UNSET:
            field_dict["use_controlled_by"] = use_controlled_by
        if use_revision is not UNSET:
            field_dict["use_revision"] = use_revision
        if report_number_suffix is not UNSET:
            field_dict["report_number_suffix"] = report_number_suffix
        if revision is not UNSET:
            field_dict["revision"] = revision
        if paper_size is not UNSET:
            field_dict["paper_size"] = paper_size
        if plot_scale is not UNSET:
            field_dict["plot_scale"] = plot_scale
        if report_number is not UNSET:
            field_dict["report_number"] = report_number
        if client_name is not UNSET:
            field_dict["client_name"] = client_name
        if sort_figures_by is not UNSET:
            field_dict["sort_figures_by"] = sort_figures_by
        if page_number_prefix is not UNSET:
            field_dict["page_number_prefix"] = page_number_prefix
        if page_number_start is not UNSET:
            field_dict["page_number_start"] = page_number_start
        if page_number_prefix_per_method is not UNSET:
            field_dict["page_number_prefix_per_method"] = page_number_prefix_per_method
        if page_number_start_per_method is not UNSET:
            field_dict["page_number_start_per_method"] = page_number_start_per_method
        if drawn_by is not UNSET:
            field_dict["drawn_by"] = drawn_by
        if controlled_by is not UNSET:
            field_dict["controlled_by"] = controlled_by
        if use_approved_by is not UNSET:
            field_dict["use_approved_by"] = use_approved_by
        if approved_by is not UNSET:
            field_dict["approved_by"] = approved_by
        if show_comment_in_plot is not UNSET:
            field_dict["show_comment_in_plot"] = show_comment_in_plot
        if projection_system is not UNSET:
            field_dict["projection_system"] = projection_system
        if max_pages is not UNSET:
            field_dict["max_pages"] = max_pages
        if color_mode is not UNSET:
            field_dict["color_mode"] = color_mode
        if fill_curve is not UNSET:
            field_dict["fill_curve"] = fill_curve

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.page_number_prefix_by_method import PageNumberPrefixByMethod
        from ..models.page_number_start_per_method import PageNumberStartPerMethod

        d = src_dict.copy()
        _lang = d.pop("lang", UNSET)
        lang: Union[Unset, PdfOptionsLang]
        if isinstance(_lang, Unset):
            lang = UNSET
        else:
            lang = PdfOptionsLang(_lang)

        _date_format = d.pop("date_format", UNSET)
        date_format: Union[Unset, PdfOptionsDateFormat]
        if isinstance(_date_format, Unset):
            date_format = UNSET
        else:
            date_format = PdfOptionsDateFormat(_date_format)

        date = d.pop("date", UNSET)

        use_controlled_by = d.pop("use_controlled_by", UNSET)

        use_revision = d.pop("use_revision", UNSET)

        report_number_suffix = d.pop("report_number_suffix", UNSET)

        revision = d.pop("revision", UNSET)

        _paper_size = d.pop("paper_size", UNSET)
        paper_size: Union[Unset, PdfOptionsPaperSize]
        if isinstance(_paper_size, Unset):
            paper_size = UNSET
        else:
            paper_size = PdfOptionsPaperSize(_paper_size)

        _plot_scale = d.pop("plot_scale", UNSET)
        plot_scale: Union[Unset, Scales]
        if isinstance(_plot_scale, Unset):
            plot_scale = UNSET
        else:
            plot_scale = Scales(_plot_scale)

        report_number = d.pop("report_number", UNSET)

        client_name = d.pop("client_name", UNSET)

        _sort_figures_by = d.pop("sort_figures_by", UNSET)
        sort_figures_by: Union[Unset, PdfOptionsSortFiguresBy]
        if isinstance(_sort_figures_by, Unset):
            sort_figures_by = UNSET
        else:
            sort_figures_by = PdfOptionsSortFiguresBy(_sort_figures_by)

        page_number_prefix = d.pop("page_number_prefix", UNSET)

        page_number_start = d.pop("page_number_start", UNSET)

        _page_number_prefix_per_method = d.pop("page_number_prefix_per_method", UNSET)
        page_number_prefix_per_method: Union[Unset, PageNumberPrefixByMethod]
        if isinstance(_page_number_prefix_per_method, Unset):
            page_number_prefix_per_method = UNSET
        else:
            page_number_prefix_per_method = PageNumberPrefixByMethod.from_dict(_page_number_prefix_per_method)

        _page_number_start_per_method = d.pop("page_number_start_per_method", UNSET)
        page_number_start_per_method: Union[Unset, PageNumberStartPerMethod]
        if isinstance(_page_number_start_per_method, Unset):
            page_number_start_per_method = UNSET
        else:
            page_number_start_per_method = PageNumberStartPerMethod.from_dict(_page_number_start_per_method)

        drawn_by = d.pop("drawn_by", UNSET)

        controlled_by = d.pop("controlled_by", UNSET)

        use_approved_by = d.pop("use_approved_by", UNSET)

        approved_by = d.pop("approved_by", UNSET)

        show_comment_in_plot = d.pop("show_comment_in_plot", UNSET)

        projection_system = d.pop("projection_system", UNSET)

        max_pages = d.pop("max_pages", UNSET)

        _color_mode = d.pop("color_mode", UNSET)
        color_mode: Union[Unset, ColorMode]
        if isinstance(_color_mode, Unset):
            color_mode = UNSET
        else:
            color_mode = ColorMode(_color_mode)

        fill_curve = d.pop("fill_curve", UNSET)

        pdf_options = cls(
            lang=lang,
            date_format=date_format,
            date=date,
            use_controlled_by=use_controlled_by,
            use_revision=use_revision,
            report_number_suffix=report_number_suffix,
            revision=revision,
            paper_size=paper_size,
            plot_scale=plot_scale,
            report_number=report_number,
            client_name=client_name,
            sort_figures_by=sort_figures_by,
            page_number_prefix=page_number_prefix,
            page_number_start=page_number_start,
            page_number_prefix_per_method=page_number_prefix_per_method,
            page_number_start_per_method=page_number_start_per_method,
            drawn_by=drawn_by,
            controlled_by=controlled_by,
            use_approved_by=use_approved_by,
            approved_by=approved_by,
            show_comment_in_plot=show_comment_in_plot,
            projection_system=projection_system,
            max_pages=max_pages,
            color_mode=color_mode,
            fill_curve=fill_curve,
        )

        pdf_options.additional_properties = d
        return pdf_options

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
