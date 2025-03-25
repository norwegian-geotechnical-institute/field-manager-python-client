from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrganizationInformation")


@_attrs_define
class OrganizationInformation:
    """
    Attributes:
        external_id (Union[None, Unset, str]):
        name (Union[None, Unset, str]):
        logo (Union[None, Unset, str]):
        logo_mime_type (Union[None, Unset, str]):
        authentication_alias (Union[None, Unset, str]):
    """

    external_id: Union[None, Unset, str] = UNSET
    name: Union[None, Unset, str] = UNSET
    logo: Union[None, Unset, str] = UNSET
    logo_mime_type: Union[None, Unset, str] = UNSET
    authentication_alias: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        external_id: Union[None, Unset, str]
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        logo: Union[None, Unset, str]
        if isinstance(self.logo, Unset):
            logo = UNSET
        else:
            logo = self.logo

        logo_mime_type: Union[None, Unset, str]
        if isinstance(self.logo_mime_type, Unset):
            logo_mime_type = UNSET
        else:
            logo_mime_type = self.logo_mime_type

        authentication_alias: Union[None, Unset, str]
        if isinstance(self.authentication_alias, Unset):
            authentication_alias = UNSET
        else:
            authentication_alias = self.authentication_alias

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if name is not UNSET:
            field_dict["name"] = name
        if logo is not UNSET:
            field_dict["logo"] = logo
        if logo_mime_type is not UNSET:
            field_dict["logo_mime_type"] = logo_mime_type
        if authentication_alias is not UNSET:
            field_dict["authentication_alias"] = authentication_alias

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id = _parse_external_id(d.pop("external_id", UNSET))

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_logo(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        logo = _parse_logo(d.pop("logo", UNSET))

        def _parse_logo_mime_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        logo_mime_type = _parse_logo_mime_type(d.pop("logo_mime_type", UNSET))

        def _parse_authentication_alias(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        authentication_alias = _parse_authentication_alias(d.pop("authentication_alias", UNSET))

        organization_information = cls(
            external_id=external_id,
            name=name,
            logo=logo,
            logo_mime_type=logo_mime_type,
            authentication_alias=authentication_alias,
        )

        organization_information.additional_properties = d
        return organization_information

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
