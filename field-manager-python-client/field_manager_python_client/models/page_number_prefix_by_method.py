from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PageNumberPrefixByMethod")


@_attrs_define
class PageNumberPrefixByMethod:
    """
    Attributes:
        cpt (None | str | Unset):  Default: ''.
        pz (None | str | Unset):  Default: ''.
        ss (None | str | Unset):  Default: ''.
        svt (None | str | Unset):  Default: ''.
        rp (None | str | Unset):  Default: ''.
        tot (None | str | Unset):  Default: ''.
        rcd (None | str | Unset):  Default: ''.
        dp (None | str | Unset):  Default: ''.
        srs (None | str | Unset):  Default: ''.
        wst (None | str | Unset):  Default: ''.
    """

    cpt: None | str | Unset = ""
    pz: None | str | Unset = ""
    ss: None | str | Unset = ""
    svt: None | str | Unset = ""
    rp: None | str | Unset = ""
    tot: None | str | Unset = ""
    rcd: None | str | Unset = ""
    dp: None | str | Unset = ""
    srs: None | str | Unset = ""
    wst: None | str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cpt: None | str | Unset
        if isinstance(self.cpt, Unset):
            cpt = UNSET
        else:
            cpt = self.cpt

        pz: None | str | Unset
        if isinstance(self.pz, Unset):
            pz = UNSET
        else:
            pz = self.pz

        ss: None | str | Unset
        if isinstance(self.ss, Unset):
            ss = UNSET
        else:
            ss = self.ss

        svt: None | str | Unset
        if isinstance(self.svt, Unset):
            svt = UNSET
        else:
            svt = self.svt

        rp: None | str | Unset
        if isinstance(self.rp, Unset):
            rp = UNSET
        else:
            rp = self.rp

        tot: None | str | Unset
        if isinstance(self.tot, Unset):
            tot = UNSET
        else:
            tot = self.tot

        rcd: None | str | Unset
        if isinstance(self.rcd, Unset):
            rcd = UNSET
        else:
            rcd = self.rcd

        dp: None | str | Unset
        if isinstance(self.dp, Unset):
            dp = UNSET
        else:
            dp = self.dp

        srs: None | str | Unset
        if isinstance(self.srs, Unset):
            srs = UNSET
        else:
            srs = self.srs

        wst: None | str | Unset
        if isinstance(self.wst, Unset):
            wst = UNSET
        else:
            wst = self.wst

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cpt is not UNSET:
            field_dict["CPT"] = cpt
        if pz is not UNSET:
            field_dict["PZ"] = pz
        if ss is not UNSET:
            field_dict["SS"] = ss
        if svt is not UNSET:
            field_dict["SVT"] = svt
        if rp is not UNSET:
            field_dict["RP"] = rp
        if tot is not UNSET:
            field_dict["TOT"] = tot
        if rcd is not UNSET:
            field_dict["RCD"] = rcd
        if dp is not UNSET:
            field_dict["DP"] = dp
        if srs is not UNSET:
            field_dict["SRS"] = srs
        if wst is not UNSET:
            field_dict["WST"] = wst

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_cpt(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cpt = _parse_cpt(d.pop("CPT", UNSET))

        def _parse_pz(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pz = _parse_pz(d.pop("PZ", UNSET))

        def _parse_ss(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ss = _parse_ss(d.pop("SS", UNSET))

        def _parse_svt(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        svt = _parse_svt(d.pop("SVT", UNSET))

        def _parse_rp(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rp = _parse_rp(d.pop("RP", UNSET))

        def _parse_tot(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tot = _parse_tot(d.pop("TOT", UNSET))

        def _parse_rcd(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rcd = _parse_rcd(d.pop("RCD", UNSET))

        def _parse_dp(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dp = _parse_dp(d.pop("DP", UNSET))

        def _parse_srs(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        srs = _parse_srs(d.pop("SRS", UNSET))

        def _parse_wst(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        wst = _parse_wst(d.pop("WST", UNSET))

        page_number_prefix_by_method = cls(
            cpt=cpt,
            pz=pz,
            ss=ss,
            svt=svt,
            rp=rp,
            tot=tot,
            rcd=rcd,
            dp=dp,
            srs=srs,
            wst=wst,
        )

        page_number_prefix_by_method.additional_properties = d
        return page_number_prefix_by_method

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
