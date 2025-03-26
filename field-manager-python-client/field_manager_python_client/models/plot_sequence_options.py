from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pdf_options import PdfOptions


T = TypeVar("T", bound="PlotSequenceOptions")


@_attrs_define
class PlotSequenceOptions:
    """
    Attributes:
        auto_set_depth (Union[Unset, bool]):  Default: False.
        pdf_filename (Union[Unset, str]):  Default: 'factual_report.pdf'.
        pdf (Union[Unset, PdfOptions]):
    """

    auto_set_depth: Union[Unset, bool] = False
    pdf_filename: Union[Unset, str] = "factual_report.pdf"
    pdf: Union[Unset, "PdfOptions"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto_set_depth = self.auto_set_depth

        pdf_filename = self.pdf_filename

        pdf: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pdf, Unset):
            pdf = self.pdf.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auto_set_depth is not UNSET:
            field_dict["auto_set_depth"] = auto_set_depth
        if pdf_filename is not UNSET:
            field_dict["pdf_filename"] = pdf_filename
        if pdf is not UNSET:
            field_dict["pdf"] = pdf

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pdf_options import PdfOptions

        d = dict(src_dict)
        auto_set_depth = d.pop("auto_set_depth", UNSET)

        pdf_filename = d.pop("pdf_filename", UNSET)

        _pdf = d.pop("pdf", UNSET)
        pdf: Union[Unset, PdfOptions]
        if isinstance(_pdf, Unset):
            pdf = UNSET
        else:
            pdf = PdfOptions.from_dict(_pdf)

        plot_sequence_options = cls(
            auto_set_depth=auto_set_depth,
            pdf_filename=pdf_filename,
            pdf=pdf,
        )

        plot_sequence_options.additional_properties = d
        return plot_sequence_options

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
