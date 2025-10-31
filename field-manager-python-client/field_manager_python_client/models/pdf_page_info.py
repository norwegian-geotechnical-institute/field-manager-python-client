from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PDFPageInfo")


@_attrs_define
class PDFPageInfo:
    """
    Attributes:
        project_name (None | str | Unset):  Default: ''.
        client (None | str | Unset):  Default: ''.
        report_number (None | str | Unset):  Default: ''.
        revision (None | str | Unset):  Default: ''.
        date (None | str | Unset):  Default: ''.
        page_number (list[str] | None | str | Unset):  Default: ''.
        info_table (list[Any] | None | str | Unset):
        drawn_by (None | str | Unset):  Default: ''.
        controlled_by (None | str | Unset):  Default: ''.
        approved_by (None | str | Unset):  Default: ''.
        split_page_info (None | str | Unset):
    """

    project_name: None | str | Unset = ""
    client: None | str | Unset = ""
    report_number: None | str | Unset = ""
    revision: None | str | Unset = ""
    date: None | str | Unset = ""
    page_number: list[str] | None | str | Unset = ""
    info_table: list[Any] | None | str | Unset = UNSET
    drawn_by: None | str | Unset = ""
    controlled_by: None | str | Unset = ""
    approved_by: None | str | Unset = ""
    split_page_info: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_name: None | str | Unset
        if isinstance(self.project_name, Unset):
            project_name = UNSET
        else:
            project_name = self.project_name

        client: None | str | Unset
        if isinstance(self.client, Unset):
            client = UNSET
        else:
            client = self.client

        report_number: None | str | Unset
        if isinstance(self.report_number, Unset):
            report_number = UNSET
        else:
            report_number = self.report_number

        revision: None | str | Unset
        if isinstance(self.revision, Unset):
            revision = UNSET
        else:
            revision = self.revision

        date: None | str | Unset
        if isinstance(self.date, Unset):
            date = UNSET
        else:
            date = self.date

        page_number: list[str] | None | str | Unset
        if isinstance(self.page_number, Unset):
            page_number = UNSET
        elif isinstance(self.page_number, list):
            page_number = self.page_number

        else:
            page_number = self.page_number

        info_table: list[Any] | None | str | Unset
        if isinstance(self.info_table, Unset):
            info_table = UNSET
        elif isinstance(self.info_table, list):
            info_table = self.info_table

        else:
            info_table = self.info_table

        drawn_by: None | str | Unset
        if isinstance(self.drawn_by, Unset):
            drawn_by = UNSET
        else:
            drawn_by = self.drawn_by

        controlled_by: None | str | Unset
        if isinstance(self.controlled_by, Unset):
            controlled_by = UNSET
        else:
            controlled_by = self.controlled_by

        approved_by: None | str | Unset
        if isinstance(self.approved_by, Unset):
            approved_by = UNSET
        else:
            approved_by = self.approved_by

        split_page_info: None | str | Unset
        if isinstance(self.split_page_info, Unset):
            split_page_info = UNSET
        else:
            split_page_info = self.split_page_info

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if project_name is not UNSET:
            field_dict["project_name"] = project_name
        if client is not UNSET:
            field_dict["client"] = client
        if report_number is not UNSET:
            field_dict["report_number"] = report_number
        if revision is not UNSET:
            field_dict["revision"] = revision
        if date is not UNSET:
            field_dict["date"] = date
        if page_number is not UNSET:
            field_dict["page_number"] = page_number
        if info_table is not UNSET:
            field_dict["info_table"] = info_table
        if drawn_by is not UNSET:
            field_dict["drawn_by"] = drawn_by
        if controlled_by is not UNSET:
            field_dict["controlled_by"] = controlled_by
        if approved_by is not UNSET:
            field_dict["approved_by"] = approved_by
        if split_page_info is not UNSET:
            field_dict["split_page_info"] = split_page_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_project_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_name = _parse_project_name(d.pop("project_name", UNSET))

        def _parse_client(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        client = _parse_client(d.pop("client", UNSET))

        def _parse_report_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        report_number = _parse_report_number(d.pop("report_number", UNSET))

        def _parse_revision(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        revision = _parse_revision(d.pop("revision", UNSET))

        def _parse_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date = _parse_date(d.pop("date", UNSET))

        def _parse_page_number(data: object) -> list[str] | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                page_number_type_1 = cast(list[str], data)

                return page_number_type_1
            except:  # noqa: E722
                pass
            return cast(list[str] | None | str | Unset, data)

        page_number = _parse_page_number(d.pop("page_number", UNSET))

        def _parse_info_table(data: object) -> list[Any] | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                info_table_type_0 = cast(list[Any], data)

                return info_table_type_0
            except:  # noqa: E722
                pass
            return cast(list[Any] | None | str | Unset, data)

        info_table = _parse_info_table(d.pop("info_table", UNSET))

        def _parse_drawn_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        drawn_by = _parse_drawn_by(d.pop("drawn_by", UNSET))

        def _parse_controlled_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        controlled_by = _parse_controlled_by(d.pop("controlled_by", UNSET))

        def _parse_approved_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        approved_by = _parse_approved_by(d.pop("approved_by", UNSET))

        def _parse_split_page_info(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        split_page_info = _parse_split_page_info(d.pop("split_page_info", UNSET))

        pdf_page_info = cls(
            project_name=project_name,
            client=client,
            report_number=report_number,
            revision=revision,
            date=date,
            page_number=page_number,
            info_table=info_table,
            drawn_by=drawn_by,
            controlled_by=controlled_by,
            approved_by=approved_by,
            split_page_info=split_page_info,
        )

        pdf_page_info.additional_properties = d
        return pdf_page_info

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
