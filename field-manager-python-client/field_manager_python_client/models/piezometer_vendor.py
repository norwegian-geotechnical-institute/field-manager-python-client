from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PiezometerVendor")


@_attrs_define
class PiezometerVendor:
    """
    Attributes:
        vendor_id (UUID):
        name (str):
        organization_id (Union[None, UUID, Unset]):
        sort_order (Union[None, Unset, int]):
    """

    vendor_id: UUID
    name: str
    organization_id: Union[None, UUID, Unset] = UNSET
    sort_order: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vendor_id = str(self.vendor_id)

        name = self.name

        organization_id: Union[None, Unset, str]
        if isinstance(self.organization_id, Unset):
            organization_id = UNSET
        elif isinstance(self.organization_id, UUID):
            organization_id = str(self.organization_id)
        else:
            organization_id = self.organization_id

        sort_order: Union[None, Unset, int]
        if isinstance(self.sort_order, Unset):
            sort_order = UNSET
        else:
            sort_order = self.sort_order

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "vendor_id": vendor_id,
                "name": name,
            }
        )
        if organization_id is not UNSET:
            field_dict["organization_id"] = organization_id
        if sort_order is not UNSET:
            field_dict["sort_order"] = sort_order

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        vendor_id = UUID(d.pop("vendor_id"))

        name = d.pop("name")

        def _parse_organization_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                organization_id_type_0 = UUID(data)

                return organization_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        organization_id = _parse_organization_id(d.pop("organization_id", UNSET))

        def _parse_sort_order(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        sort_order = _parse_sort_order(d.pop("sort_order", UNSET))

        piezometer_vendor = cls(
            vendor_id=vendor_id,
            name=name,
            organization_id=organization_id,
            sort_order=sort_order,
        )

        piezometer_vendor.additional_properties = d
        return piezometer_vendor

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
