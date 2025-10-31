from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.iogp_type_enum import IOGPTypeEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.method_ad_create import MethodADCreate
    from ..models.method_cd_create import MethodCDCreate
    from ..models.method_cpt_create import MethodCPTCreate
    from ..models.method_def_create import MethodDEFCreate
    from ..models.method_dp_create import MethodDPCreate
    from ..models.method_dt_create import MethodDTCreate
    from ..models.method_esa_create import MethodESACreate
    from ..models.method_inc_create import MethodINCCreate
    from ..models.method_iw_create import MethodIWCreate
    from ..models.method_other_create import MethodOTHERCreate
    from ..models.method_pt_create import MethodPTCreate
    from ..models.method_pz_create import MethodPZCreate
    from ..models.method_rcd_create import MethodRCDCreate
    from ..models.method_ro_create import MethodROCreate
    from ..models.method_rp_create import MethodRPCreate
    from ..models.method_rs_create import MethodRSCreate
    from ..models.method_rws_create import MethodRWSCreate
    from ..models.method_sa_create import MethodSACreate
    from ..models.method_slb_create import MethodSLBCreate
    from ..models.method_spt_create import MethodSPTCreate
    from ..models.method_srs_create import MethodSRSCreate
    from ..models.method_ss_create import MethodSSCreate
    from ..models.method_sti_create import MethodSTICreate
    from ..models.method_svt_create import MethodSVTCreate
    from ..models.method_tot_create import MethodTOTCreate
    from ..models.method_tp_create import MethodTPCreate
    from ..models.method_tr_create import MethodTRCreate
    from ..models.method_wst_create import MethodWSTCreate


T = TypeVar("T", bound="LocationCreate")


@_attrs_define
class LocationCreate:
    """
    Example:
        {'methods': [{'method_type_id': 1}, {'method_type_id': 2}], 'name': 'Loc01', 'point_easting': 1194547,
            'point_northing': 8388298, 'point_z': 0, 'srid': 3857}

    Attributes:
        name (str):
        iogp_type_id (IOGPTypeEnum | Unset): For offshore locations, an IOGP type is required
        created_at (datetime.datetime | None | Unset):
        created_by (None | str | Unset):
        updated_at (datetime.datetime | None | Unset):
        updated_by (None | str | Unset):
        point_easting (float | None | Unset):
        point_northing (float | None | Unset):
        point_z (float | None | Unset):
        srid (int | None | Unset):
        point_x_wgs84_pseudo (float | None | Unset):
        point_y_wgs84_pseudo (float | None | Unset):
        point_x_wgs84_web (float | None | Unset):
        point_y_wgs84_web (float | None | Unset):
        tags (list[str] | Unset):
        project_id (None | Unset | UUID):
        methods (list[MethodADCreate | MethodCDCreate | MethodCPTCreate | MethodDEFCreate | MethodDPCreate |
            MethodDTCreate | MethodESACreate | MethodINCCreate | MethodIWCreate | MethodOTHERCreate | MethodPTCreate |
            MethodPZCreate | MethodRCDCreate | MethodROCreate | MethodRPCreate | MethodRSCreate | MethodRWSCreate |
            MethodSACreate | MethodSLBCreate | MethodSPTCreate | MethodSRSCreate | MethodSSCreate | MethodSTICreate |
            MethodSVTCreate | MethodTOTCreate | MethodTPCreate | MethodTRCreate | MethodWSTCreate] | Unset):
    """

    name: str
    iogp_type_id: IOGPTypeEnum | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    created_by: None | str | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    updated_by: None | str | Unset = UNSET
    point_easting: float | None | Unset = UNSET
    point_northing: float | None | Unset = UNSET
    point_z: float | None | Unset = UNSET
    srid: int | None | Unset = UNSET
    point_x_wgs84_pseudo: float | None | Unset = UNSET
    point_y_wgs84_pseudo: float | None | Unset = UNSET
    point_x_wgs84_web: float | None | Unset = UNSET
    point_y_wgs84_web: float | None | Unset = UNSET
    tags: list[str] | Unset = UNSET
    project_id: None | Unset | UUID = UNSET
    methods: (
        list[
            MethodADCreate
            | MethodCDCreate
            | MethodCPTCreate
            | MethodDEFCreate
            | MethodDPCreate
            | MethodDTCreate
            | MethodESACreate
            | MethodINCCreate
            | MethodIWCreate
            | MethodOTHERCreate
            | MethodPTCreate
            | MethodPZCreate
            | MethodRCDCreate
            | MethodROCreate
            | MethodRPCreate
            | MethodRSCreate
            | MethodRWSCreate
            | MethodSACreate
            | MethodSLBCreate
            | MethodSPTCreate
            | MethodSRSCreate
            | MethodSSCreate
            | MethodSTICreate
            | MethodSVTCreate
            | MethodTOTCreate
            | MethodTPCreate
            | MethodTRCreate
            | MethodWSTCreate
        ]
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.method_ad_create import MethodADCreate
        from ..models.method_cd_create import MethodCDCreate
        from ..models.method_cpt_create import MethodCPTCreate
        from ..models.method_def_create import MethodDEFCreate
        from ..models.method_dp_create import MethodDPCreate
        from ..models.method_dt_create import MethodDTCreate
        from ..models.method_esa_create import MethodESACreate
        from ..models.method_inc_create import MethodINCCreate
        from ..models.method_iw_create import MethodIWCreate
        from ..models.method_other_create import MethodOTHERCreate
        from ..models.method_pt_create import MethodPTCreate
        from ..models.method_pz_create import MethodPZCreate
        from ..models.method_rcd_create import MethodRCDCreate
        from ..models.method_ro_create import MethodROCreate
        from ..models.method_rp_create import MethodRPCreate
        from ..models.method_rs_create import MethodRSCreate
        from ..models.method_rws_create import MethodRWSCreate
        from ..models.method_sa_create import MethodSACreate
        from ..models.method_slb_create import MethodSLBCreate
        from ..models.method_spt_create import MethodSPTCreate
        from ..models.method_srs_create import MethodSRSCreate
        from ..models.method_ss_create import MethodSSCreate
        from ..models.method_sti_create import MethodSTICreate
        from ..models.method_svt_create import MethodSVTCreate
        from ..models.method_tot_create import MethodTOTCreate
        from ..models.method_tp_create import MethodTPCreate
        from ..models.method_tr_create import MethodTRCreate

        name = self.name

        iogp_type_id: str | Unset = UNSET
        if not isinstance(self.iogp_type_id, Unset):
            iogp_type_id = self.iogp_type_id.value

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        created_by: None | str | Unset
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        else:
            created_by = self.created_by

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        updated_by: None | str | Unset
        if isinstance(self.updated_by, Unset):
            updated_by = UNSET
        else:
            updated_by = self.updated_by

        point_easting: float | None | Unset
        if isinstance(self.point_easting, Unset):
            point_easting = UNSET
        else:
            point_easting = self.point_easting

        point_northing: float | None | Unset
        if isinstance(self.point_northing, Unset):
            point_northing = UNSET
        else:
            point_northing = self.point_northing

        point_z: float | None | Unset
        if isinstance(self.point_z, Unset):
            point_z = UNSET
        else:
            point_z = self.point_z

        srid: int | None | Unset
        if isinstance(self.srid, Unset):
            srid = UNSET
        else:
            srid = self.srid

        point_x_wgs84_pseudo: float | None | Unset
        if isinstance(self.point_x_wgs84_pseudo, Unset):
            point_x_wgs84_pseudo = UNSET
        else:
            point_x_wgs84_pseudo = self.point_x_wgs84_pseudo

        point_y_wgs84_pseudo: float | None | Unset
        if isinstance(self.point_y_wgs84_pseudo, Unset):
            point_y_wgs84_pseudo = UNSET
        else:
            point_y_wgs84_pseudo = self.point_y_wgs84_pseudo

        point_x_wgs84_web: float | None | Unset
        if isinstance(self.point_x_wgs84_web, Unset):
            point_x_wgs84_web = UNSET
        else:
            point_x_wgs84_web = self.point_x_wgs84_web

        point_y_wgs84_web: float | None | Unset
        if isinstance(self.point_y_wgs84_web, Unset):
            point_y_wgs84_web = UNSET
        else:
            point_y_wgs84_web = self.point_y_wgs84_web

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        project_id: None | str | Unset
        if isinstance(self.project_id, Unset):
            project_id = UNSET
        elif isinstance(self.project_id, UUID):
            project_id = str(self.project_id)
        else:
            project_id = self.project_id

        methods: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.methods, Unset):
            methods = []
            for methods_item_data in self.methods:
                methods_item: dict[str, Any]
                if isinstance(methods_item_data, MethodADCreate):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodCDCreate):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodCPTCreate):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodDPCreate):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodDTCreate):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodESACreate):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodINCCreate):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodIWCreate):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodOTHERCreate):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodPTCreate):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodPZCreate):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodRCDCreate):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodROCreate):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodRPCreate):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodRSCreate):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodRWSCreate):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodSACreate):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodSLBCreate):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodSPTCreate):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodDEFCreate):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodSRSCreate):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodSSCreate):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodSTICreate):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodSVTCreate):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodTOTCreate):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodTPCreate):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodTRCreate):
                    methods_item = methods_item_data.to_dict()
                else:
                    methods_item = methods_item_data.to_dict()

                methods.append(methods_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if iogp_type_id is not UNSET:
            field_dict["iogp_type_id"] = iogp_type_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if updated_by is not UNSET:
            field_dict["updated_by"] = updated_by
        if point_easting is not UNSET:
            field_dict["point_easting"] = point_easting
        if point_northing is not UNSET:
            field_dict["point_northing"] = point_northing
        if point_z is not UNSET:
            field_dict["point_z"] = point_z
        if srid is not UNSET:
            field_dict["srid"] = srid
        if point_x_wgs84_pseudo is not UNSET:
            field_dict["point_x_wgs84_pseudo"] = point_x_wgs84_pseudo
        if point_y_wgs84_pseudo is not UNSET:
            field_dict["point_y_wgs84_pseudo"] = point_y_wgs84_pseudo
        if point_x_wgs84_web is not UNSET:
            field_dict["point_x_wgs84_web"] = point_x_wgs84_web
        if point_y_wgs84_web is not UNSET:
            field_dict["point_y_wgs84_web"] = point_y_wgs84_web
        if tags is not UNSET:
            field_dict["tags"] = tags
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if methods is not UNSET:
            field_dict["methods"] = methods

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.method_ad_create import MethodADCreate
        from ..models.method_cd_create import MethodCDCreate
        from ..models.method_cpt_create import MethodCPTCreate
        from ..models.method_def_create import MethodDEFCreate
        from ..models.method_dp_create import MethodDPCreate
        from ..models.method_dt_create import MethodDTCreate
        from ..models.method_esa_create import MethodESACreate
        from ..models.method_inc_create import MethodINCCreate
        from ..models.method_iw_create import MethodIWCreate
        from ..models.method_other_create import MethodOTHERCreate
        from ..models.method_pt_create import MethodPTCreate
        from ..models.method_pz_create import MethodPZCreate
        from ..models.method_rcd_create import MethodRCDCreate
        from ..models.method_ro_create import MethodROCreate
        from ..models.method_rp_create import MethodRPCreate
        from ..models.method_rs_create import MethodRSCreate
        from ..models.method_rws_create import MethodRWSCreate
        from ..models.method_sa_create import MethodSACreate
        from ..models.method_slb_create import MethodSLBCreate
        from ..models.method_spt_create import MethodSPTCreate
        from ..models.method_srs_create import MethodSRSCreate
        from ..models.method_ss_create import MethodSSCreate
        from ..models.method_sti_create import MethodSTICreate
        from ..models.method_svt_create import MethodSVTCreate
        from ..models.method_tot_create import MethodTOTCreate
        from ..models.method_tp_create import MethodTPCreate
        from ..models.method_tr_create import MethodTRCreate
        from ..models.method_wst_create import MethodWSTCreate

        d = dict(src_dict)
        name = d.pop("name")

        _iogp_type_id = d.pop("iogp_type_id", UNSET)
        iogp_type_id: IOGPTypeEnum | Unset
        if isinstance(_iogp_type_id, Unset):
            iogp_type_id = UNSET
        else:
            iogp_type_id = IOGPTypeEnum(_iogp_type_id)

        def _parse_created_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = isoparse(data)

                return created_at_type_0
            except:  # noqa: E722
                pass
            return cast(datetime.datetime | None | Unset, data)

        created_at = _parse_created_at(d.pop("created_at", UNSET))

        def _parse_created_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_by = _parse_created_by(d.pop("created_by", UNSET))

        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = isoparse(data)

                return updated_at_type_0
            except:  # noqa: E722
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))

        def _parse_updated_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        updated_by = _parse_updated_by(d.pop("updated_by", UNSET))

        def _parse_point_easting(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        point_easting = _parse_point_easting(d.pop("point_easting", UNSET))

        def _parse_point_northing(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        point_northing = _parse_point_northing(d.pop("point_northing", UNSET))

        def _parse_point_z(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        point_z = _parse_point_z(d.pop("point_z", UNSET))

        def _parse_srid(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        srid = _parse_srid(d.pop("srid", UNSET))

        def _parse_point_x_wgs84_pseudo(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        point_x_wgs84_pseudo = _parse_point_x_wgs84_pseudo(d.pop("point_x_wgs84_pseudo", UNSET))

        def _parse_point_y_wgs84_pseudo(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        point_y_wgs84_pseudo = _parse_point_y_wgs84_pseudo(d.pop("point_y_wgs84_pseudo", UNSET))

        def _parse_point_x_wgs84_web(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        point_x_wgs84_web = _parse_point_x_wgs84_web(d.pop("point_x_wgs84_web", UNSET))

        def _parse_point_y_wgs84_web(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        point_y_wgs84_web = _parse_point_y_wgs84_web(d.pop("point_y_wgs84_web", UNSET))

        tags = cast(list[str], d.pop("tags", UNSET))

        def _parse_project_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                project_id_type_0 = UUID(data)

                return project_id_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | UUID, data)

        project_id = _parse_project_id(d.pop("project_id", UNSET))

        methods = []
        _methods = d.pop("methods", UNSET)
        for methods_item_data in _methods or []:

            def _parse_methods_item(
                data: object,
            ) -> (
                MethodADCreate
                | MethodCDCreate
                | MethodCPTCreate
                | MethodDEFCreate
                | MethodDPCreate
                | MethodDTCreate
                | MethodESACreate
                | MethodINCCreate
                | MethodIWCreate
                | MethodOTHERCreate
                | MethodPTCreate
                | MethodPZCreate
                | MethodRCDCreate
                | MethodROCreate
                | MethodRPCreate
                | MethodRSCreate
                | MethodRWSCreate
                | MethodSACreate
                | MethodSLBCreate
                | MethodSPTCreate
                | MethodSRSCreate
                | MethodSSCreate
                | MethodSTICreate
                | MethodSVTCreate
                | MethodTOTCreate
                | MethodTPCreate
                | MethodTRCreate
                | MethodWSTCreate
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_0 = MethodADCreate.from_dict(data)

                    return methods_item_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_1 = MethodCDCreate.from_dict(data)

                    return methods_item_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_2 = MethodCPTCreate.from_dict(data)

                    return methods_item_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_3 = MethodDPCreate.from_dict(data)

                    return methods_item_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_4 = MethodDTCreate.from_dict(data)

                    return methods_item_type_4
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_5 = MethodESACreate.from_dict(data)

                    return methods_item_type_5
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_6 = MethodINCCreate.from_dict(data)

                    return methods_item_type_6
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_7 = MethodIWCreate.from_dict(data)

                    return methods_item_type_7
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_8 = MethodOTHERCreate.from_dict(data)

                    return methods_item_type_8
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_9 = MethodPTCreate.from_dict(data)

                    return methods_item_type_9
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_10 = MethodPZCreate.from_dict(data)

                    return methods_item_type_10
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_11 = MethodRCDCreate.from_dict(data)

                    return methods_item_type_11
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_12 = MethodROCreate.from_dict(data)

                    return methods_item_type_12
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_13 = MethodRPCreate.from_dict(data)

                    return methods_item_type_13
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_14 = MethodRSCreate.from_dict(data)

                    return methods_item_type_14
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_15 = MethodRWSCreate.from_dict(data)

                    return methods_item_type_15
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_16 = MethodSACreate.from_dict(data)

                    return methods_item_type_16
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_17 = MethodSLBCreate.from_dict(data)

                    return methods_item_type_17
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_18 = MethodSPTCreate.from_dict(data)

                    return methods_item_type_18
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_19 = MethodDEFCreate.from_dict(data)

                    return methods_item_type_19
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_20 = MethodSRSCreate.from_dict(data)

                    return methods_item_type_20
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_21 = MethodSSCreate.from_dict(data)

                    return methods_item_type_21
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_22 = MethodSTICreate.from_dict(data)

                    return methods_item_type_22
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_23 = MethodSVTCreate.from_dict(data)

                    return methods_item_type_23
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_24 = MethodTOTCreate.from_dict(data)

                    return methods_item_type_24
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_25 = MethodTPCreate.from_dict(data)

                    return methods_item_type_25
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_26 = MethodTRCreate.from_dict(data)

                    return methods_item_type_26
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                methods_item_type_27 = MethodWSTCreate.from_dict(data)

                return methods_item_type_27

            methods_item = _parse_methods_item(methods_item_data)

            methods.append(methods_item)

        location_create = cls(
            name=name,
            iogp_type_id=iogp_type_id,
            created_at=created_at,
            created_by=created_by,
            updated_at=updated_at,
            updated_by=updated_by,
            point_easting=point_easting,
            point_northing=point_northing,
            point_z=point_z,
            srid=srid,
            point_x_wgs84_pseudo=point_x_wgs84_pseudo,
            point_y_wgs84_pseudo=point_y_wgs84_pseudo,
            point_x_wgs84_web=point_x_wgs84_web,
            point_y_wgs84_web=point_y_wgs84_web,
            tags=tags,
            project_id=project_id,
            methods=methods,
        )

        location_create.additional_properties = d
        return location_create

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
