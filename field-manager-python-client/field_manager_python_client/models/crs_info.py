from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CRSInfo")


@_attrs_define
class CRSInfo:
    """
    Attributes:
        auth_name (str):
        srid (int): EPSG code
        name (str):
        unit (str): Unit of measurement for coordinate axes (e.g., meter, degree, foot)
        wkt (None | str): Well-Known Text representation of the CRS
        proj4 (None | str): Proj4 representation of the CRS
        proj_json (None | str): JSON representation of the CRS
    """

    auth_name: str
    srid: int
    name: str
    unit: str
    wkt: None | str
    proj4: None | str
    proj_json: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auth_name = self.auth_name

        srid = self.srid

        name = self.name

        unit = self.unit

        wkt: None | str
        wkt = self.wkt

        proj4: None | str
        proj4 = self.proj4

        proj_json: None | str
        proj_json = self.proj_json

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "auth_name": auth_name,
                "srid": srid,
                "name": name,
                "unit": unit,
                "wkt": wkt,
                "proj4": proj4,
                "proj_json": proj_json,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        auth_name = d.pop("auth_name")

        srid = d.pop("srid")

        name = d.pop("name")

        unit = d.pop("unit")

        def _parse_wkt(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        wkt = _parse_wkt(d.pop("wkt"))

        def _parse_proj4(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        proj4 = _parse_proj4(d.pop("proj4"))

        def _parse_proj_json(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        proj_json = _parse_proj_json(d.pop("proj_json"))

        crs_info = cls(
            auth_name=auth_name,
            srid=srid,
            name=name,
            unit=unit,
            wkt=wkt,
            proj4=proj4,
            proj_json=proj_json,
        )

        crs_info.additional_properties = d
        return crs_info

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
