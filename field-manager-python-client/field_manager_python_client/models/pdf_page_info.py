from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PDFPageInfo")


@_attrs_define
class PDFPageInfo:
    """
    Attributes:
        project_name (Union[None, Unset, str]):  Default: ''.
        client (Union[None, Unset, str]):  Default: ''.
        report_number (Union[None, Unset, str]):  Default: ''.
        revision (Union[None, Unset, str]):  Default: ''.
        date (Union[None, Unset, str]):  Default: ''.
        page_number (Union[None, Unset, list[str], str]):  Default: ''.
        info_table (Union[None, Unset, list[Any], str]):
        drawn_by (Union[None, Unset, str]):  Default: ''.
        controlled_by (Union[None, Unset, str]):  Default: ''.
        approved_by (Union[None, Unset, str]):  Default: ''.
        split_page_info (Union[None, Unset, str]):
    """

    project_name: Union[None, Unset, str] = ""
    client: Union[None, Unset, str] = ""
    report_number: Union[None, Unset, str] = ""
    revision: Union[None, Unset, str] = ""
    date: Union[None, Unset, str] = ""
    page_number: Union[None, Unset, list[str], str] = ""
    info_table: Union[None, Unset, list[Any], str] = UNSET
    drawn_by: Union[None, Unset, str] = ""
    controlled_by: Union[None, Unset, str] = ""
    approved_by: Union[None, Unset, str] = ""
    split_page_info: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_name: Union[None, Unset, str]
        if isinstance(self.project_name, Unset):
            project_name = UNSET
        else:
            project_name = self.project_name

        client: Union[None, Unset, str]
        if isinstance(self.client, Unset):
            client = UNSET
        else:
            client = self.client

        report_number: Union[None, Unset, str]
        if isinstance(self.report_number, Unset):
            report_number = UNSET
        else:
            report_number = self.report_number

        revision: Union[None, Unset, str]
        if isinstance(self.revision, Unset):
            revision = UNSET
        else:
            revision = self.revision

        date: Union[None, Unset, str]
        if isinstance(self.date, Unset):
            date = UNSET
        else:
            date = self.date

        page_number: Union[None, Unset, list[str], str]
        if isinstance(self.page_number, Unset):
            page_number = UNSET
        elif isinstance(self.page_number, list):
            page_number = self.page_number

        else:
            page_number = self.page_number

        info_table: Union[None, Unset, list[Any], str]
        if isinstance(self.info_table, Unset):
            info_table = UNSET
        elif isinstance(self.info_table, list):
            info_table = self.info_table

        else:
            info_table = self.info_table

        drawn_by: Union[None, Unset, str]
        if isinstance(self.drawn_by, Unset):
            drawn_by = UNSET
        else:
            drawn_by = self.drawn_by

        controlled_by: Union[None, Unset, str]
        if isinstance(self.controlled_by, Unset):
            controlled_by = UNSET
        else:
            controlled_by = self.controlled_by

        approved_by: Union[None, Unset, str]
        if isinstance(self.approved_by, Unset):
            approved_by = UNSET
        else:
            approved_by = self.approved_by

        split_page_info: Union[None, Unset, str]
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
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_project_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        project_name = _parse_project_name(d.pop("project_name", UNSET))

        def _parse_client(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        client = _parse_client(d.pop("client", UNSET))

        def _parse_report_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        report_number = _parse_report_number(d.pop("report_number", UNSET))

        def _parse_revision(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        revision = _parse_revision(d.pop("revision", UNSET))

        def _parse_date(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        date = _parse_date(d.pop("date", UNSET))

        def _parse_page_number(data: object) -> Union[None, Unset, list[str], str]:
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
            return cast(Union[None, Unset, list[str], str], data)

        page_number = _parse_page_number(d.pop("page_number", UNSET))

        def _parse_info_table(data: object) -> Union[None, Unset, list[Any], str]:
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
            return cast(Union[None, Unset, list[Any], str], data)

        info_table = _parse_info_table(d.pop("info_table", UNSET))

        def _parse_drawn_by(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        drawn_by = _parse_drawn_by(d.pop("drawn_by", UNSET))

        def _parse_controlled_by(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        controlled_by = _parse_controlled_by(d.pop("controlled_by", UNSET))

        def _parse_approved_by(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        approved_by = _parse_approved_by(d.pop("approved_by", UNSET))

        def _parse_split_page_info(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

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
