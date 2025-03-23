import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.iogp_type_enum import IOGPTypeEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.method_ad_create import MethodADCreate
    from ..models.method_ad_update import MethodADUpdate
    from ..models.method_cd_create import MethodCDCreate
    from ..models.method_cd_update import MethodCDUpdate
    from ..models.method_cpt_create import MethodCPTCreate
    from ..models.method_cpt_update import MethodCPTUpdate
    from ..models.method_def_create import MethodDEFCreate
    from ..models.method_def_update import MethodDEFUpdate
    from ..models.method_dp_create import MethodDPCreate
    from ..models.method_dp_update import MethodDPUpdate
    from ..models.method_dt_create import MethodDTCreate
    from ..models.method_dt_update import MethodDTUpdate
    from ..models.method_esa_create import MethodESACreate
    from ..models.method_esa_update import MethodESAUpdate
    from ..models.method_inc_create import MethodINCCreate
    from ..models.method_inc_update import MethodINCUpdate
    from ..models.method_iw_create import MethodIWCreate
    from ..models.method_iw_update import MethodIWUpdate
    from ..models.method_other_create import MethodOTHERCreate
    from ..models.method_other_update import MethodOTHERUpdate
    from ..models.method_pt_create import MethodPTCreate
    from ..models.method_pt_update import MethodPTUpdate
    from ..models.method_pz_create import MethodPZCreate
    from ..models.method_pz_update import MethodPZUpdate
    from ..models.method_rcd_create import MethodRCDCreate
    from ..models.method_rcd_update import MethodRCDUpdate
    from ..models.method_ro_create import MethodROCreate
    from ..models.method_ro_update import MethodROUpdate
    from ..models.method_rp_create import MethodRPCreate
    from ..models.method_rp_update import MethodRPUpdate
    from ..models.method_rs_create import MethodRSCreate
    from ..models.method_rs_update import MethodRSUpdate
    from ..models.method_rws_create import MethodRWSCreate
    from ..models.method_rws_update import MethodRWSUpdate
    from ..models.method_sa_create import MethodSACreate
    from ..models.method_sa_update import MethodSAUpdate
    from ..models.method_slb_create import MethodSLBCreate
    from ..models.method_slb_update import MethodSLBUpdate
    from ..models.method_spt_create import MethodSPTCreate
    from ..models.method_spt_update import MethodSPTUpdate
    from ..models.method_srs_create import MethodSRSCreate
    from ..models.method_srs_update import MethodSRSUpdate
    from ..models.method_ss_create import MethodSSCreate
    from ..models.method_ss_update import MethodSSUpdate
    from ..models.method_sti_create import MethodSTICreate
    from ..models.method_sti_update import MethodSTIUpdate
    from ..models.method_svt_create import MethodSVTCreate
    from ..models.method_svt_update import MethodSVTUpdate
    from ..models.method_tot_create import MethodTOTCreate
    from ..models.method_tot_update import MethodTOTUpdate
    from ..models.method_tp_create import MethodTPCreate
    from ..models.method_tp_update import MethodTPUpdate
    from ..models.method_tr_create import MethodTRCreate
    from ..models.method_tr_update import MethodTRUpdate
    from ..models.method_wst_create import MethodWSTCreate
    from ..models.method_wst_update import MethodWSTUpdate


T = TypeVar("T", bound="LocationUpdate")


@_attrs_define
class LocationUpdate:
    """
    Attributes:
        project_id (Union[None, UUID, Unset]):
        location_id (Union[None, UUID, Unset]):
        iogp_type_id (Union[IOGPTypeEnum, None, Unset]):
        name (Union[None, Unset, str]):
        updated_at (Union[None, Unset, datetime.datetime]):
        updated_by (Union[None, Unset, str]):
        point_easting (Union[None, Unset, float]):
        point_northing (Union[None, Unset, float]):
        point_z (Union[None, Unset, float]):
        srid (Union[None, Unset, int]):
        tags (Union[None, Unset, list[str]]):
        methods (Union[Unset, list[Union['MethodADCreate', 'MethodADUpdate', 'MethodCDCreate', 'MethodCDUpdate',
            'MethodCPTCreate', 'MethodCPTUpdate', 'MethodDEFCreate', 'MethodDEFUpdate', 'MethodDPCreate', 'MethodDPUpdate',
            'MethodDTCreate', 'MethodDTUpdate', 'MethodESACreate', 'MethodESAUpdate', 'MethodINCCreate', 'MethodINCUpdate',
            'MethodIWCreate', 'MethodIWUpdate', 'MethodOTHERCreate', 'MethodOTHERUpdate', 'MethodPTCreate',
            'MethodPTUpdate', 'MethodPZCreate', 'MethodPZUpdate', 'MethodRCDCreate', 'MethodRCDUpdate', 'MethodROCreate',
            'MethodROUpdate', 'MethodRPCreate', 'MethodRPUpdate', 'MethodRSCreate', 'MethodRSUpdate', 'MethodRWSCreate',
            'MethodRWSUpdate', 'MethodSACreate', 'MethodSAUpdate', 'MethodSLBCreate', 'MethodSLBUpdate', 'MethodSPTCreate',
            'MethodSPTUpdate', 'MethodSRSCreate', 'MethodSRSUpdate', 'MethodSSCreate', 'MethodSSUpdate', 'MethodSTICreate',
            'MethodSTIUpdate', 'MethodSVTCreate', 'MethodSVTUpdate', 'MethodTOTCreate', 'MethodTOTUpdate', 'MethodTPCreate',
            'MethodTPUpdate', 'MethodTRCreate', 'MethodTRUpdate', 'MethodWSTCreate', 'MethodWSTUpdate']]]):
    """

    project_id: Union[None, UUID, Unset] = UNSET
    location_id: Union[None, UUID, Unset] = UNSET
    iogp_type_id: Union[IOGPTypeEnum, None, Unset] = UNSET
    name: Union[None, Unset, str] = UNSET
    updated_at: Union[None, Unset, datetime.datetime] = UNSET
    updated_by: Union[None, Unset, str] = UNSET
    point_easting: Union[None, Unset, float] = UNSET
    point_northing: Union[None, Unset, float] = UNSET
    point_z: Union[None, Unset, float] = UNSET
    srid: Union[None, Unset, int] = UNSET
    tags: Union[None, Unset, list[str]] = UNSET
    methods: Union[
        Unset,
        list[
            Union[
                "MethodADCreate",
                "MethodADUpdate",
                "MethodCDCreate",
                "MethodCDUpdate",
                "MethodCPTCreate",
                "MethodCPTUpdate",
                "MethodDEFCreate",
                "MethodDEFUpdate",
                "MethodDPCreate",
                "MethodDPUpdate",
                "MethodDTCreate",
                "MethodDTUpdate",
                "MethodESACreate",
                "MethodESAUpdate",
                "MethodINCCreate",
                "MethodINCUpdate",
                "MethodIWCreate",
                "MethodIWUpdate",
                "MethodOTHERCreate",
                "MethodOTHERUpdate",
                "MethodPTCreate",
                "MethodPTUpdate",
                "MethodPZCreate",
                "MethodPZUpdate",
                "MethodRCDCreate",
                "MethodRCDUpdate",
                "MethodROCreate",
                "MethodROUpdate",
                "MethodRPCreate",
                "MethodRPUpdate",
                "MethodRSCreate",
                "MethodRSUpdate",
                "MethodRWSCreate",
                "MethodRWSUpdate",
                "MethodSACreate",
                "MethodSAUpdate",
                "MethodSLBCreate",
                "MethodSLBUpdate",
                "MethodSPTCreate",
                "MethodSPTUpdate",
                "MethodSRSCreate",
                "MethodSRSUpdate",
                "MethodSSCreate",
                "MethodSSUpdate",
                "MethodSTICreate",
                "MethodSTIUpdate",
                "MethodSVTCreate",
                "MethodSVTUpdate",
                "MethodTOTCreate",
                "MethodTOTUpdate",
                "MethodTPCreate",
                "MethodTPUpdate",
                "MethodTRCreate",
                "MethodTRUpdate",
                "MethodWSTCreate",
                "MethodWSTUpdate",
            ]
        ],
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.method_ad_create import MethodADCreate
        from ..models.method_ad_update import MethodADUpdate
        from ..models.method_cd_create import MethodCDCreate
        from ..models.method_cd_update import MethodCDUpdate
        from ..models.method_cpt_create import MethodCPTCreate
        from ..models.method_cpt_update import MethodCPTUpdate
        from ..models.method_def_create import MethodDEFCreate
        from ..models.method_def_update import MethodDEFUpdate
        from ..models.method_dp_create import MethodDPCreate
        from ..models.method_dp_update import MethodDPUpdate
        from ..models.method_dt_create import MethodDTCreate
        from ..models.method_dt_update import MethodDTUpdate
        from ..models.method_esa_create import MethodESACreate
        from ..models.method_esa_update import MethodESAUpdate
        from ..models.method_inc_create import MethodINCCreate
        from ..models.method_inc_update import MethodINCUpdate
        from ..models.method_iw_create import MethodIWCreate
        from ..models.method_iw_update import MethodIWUpdate
        from ..models.method_other_create import MethodOTHERCreate
        from ..models.method_other_update import MethodOTHERUpdate
        from ..models.method_pt_create import MethodPTCreate
        from ..models.method_pt_update import MethodPTUpdate
        from ..models.method_pz_create import MethodPZCreate
        from ..models.method_pz_update import MethodPZUpdate
        from ..models.method_rcd_create import MethodRCDCreate
        from ..models.method_rcd_update import MethodRCDUpdate
        from ..models.method_ro_create import MethodROCreate
        from ..models.method_ro_update import MethodROUpdate
        from ..models.method_rp_create import MethodRPCreate
        from ..models.method_rp_update import MethodRPUpdate
        from ..models.method_rs_create import MethodRSCreate
        from ..models.method_rs_update import MethodRSUpdate
        from ..models.method_rws_create import MethodRWSCreate
        from ..models.method_rws_update import MethodRWSUpdate
        from ..models.method_sa_create import MethodSACreate
        from ..models.method_sa_update import MethodSAUpdate
        from ..models.method_slb_create import MethodSLBCreate
        from ..models.method_slb_update import MethodSLBUpdate
        from ..models.method_spt_create import MethodSPTCreate
        from ..models.method_spt_update import MethodSPTUpdate
        from ..models.method_srs_create import MethodSRSCreate
        from ..models.method_srs_update import MethodSRSUpdate
        from ..models.method_ss_create import MethodSSCreate
        from ..models.method_ss_update import MethodSSUpdate
        from ..models.method_sti_create import MethodSTICreate
        from ..models.method_svt_create import MethodSVTCreate
        from ..models.method_svt_update import MethodSVTUpdate
        from ..models.method_tot_create import MethodTOTCreate
        from ..models.method_tot_update import MethodTOTUpdate
        from ..models.method_tp_create import MethodTPCreate
        from ..models.method_tp_update import MethodTPUpdate
        from ..models.method_tr_create import MethodTRCreate
        from ..models.method_tr_update import MethodTRUpdate
        from ..models.method_wst_create import MethodWSTCreate
        from ..models.method_wst_update import MethodWSTUpdate

        project_id: Union[None, Unset, str]
        if isinstance(self.project_id, Unset):
            project_id = UNSET
        elif isinstance(self.project_id, UUID):
            project_id = str(self.project_id)
        else:
            project_id = self.project_id

        location_id: Union[None, Unset, str]
        if isinstance(self.location_id, Unset):
            location_id = UNSET
        elif isinstance(self.location_id, UUID):
            location_id = str(self.location_id)
        else:
            location_id = self.location_id

        iogp_type_id: Union[None, Unset, str]
        if isinstance(self.iogp_type_id, Unset):
            iogp_type_id = UNSET
        elif isinstance(self.iogp_type_id, IOGPTypeEnum):
            iogp_type_id = self.iogp_type_id.value
        else:
            iogp_type_id = self.iogp_type_id

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        updated_at: Union[None, Unset, str]
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        updated_by: Union[None, Unset, str]
        if isinstance(self.updated_by, Unset):
            updated_by = UNSET
        else:
            updated_by = self.updated_by

        point_easting: Union[None, Unset, float]
        if isinstance(self.point_easting, Unset):
            point_easting = UNSET
        else:
            point_easting = self.point_easting

        point_northing: Union[None, Unset, float]
        if isinstance(self.point_northing, Unset):
            point_northing = UNSET
        else:
            point_northing = self.point_northing

        point_z: Union[None, Unset, float]
        if isinstance(self.point_z, Unset):
            point_z = UNSET
        else:
            point_z = self.point_z

        srid: Union[None, Unset, int]
        if isinstance(self.srid, Unset):
            srid = UNSET
        else:
            srid = self.srid

        tags: Union[None, Unset, list[str]]
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        methods: Union[Unset, list[dict[str, Any]]] = UNSET
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
                elif isinstance(methods_item_data, MethodWSTCreate):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodCPTUpdate):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodTOTUpdate):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodRPUpdate):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodSAUpdate):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodPZUpdate):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodSSUpdate):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodRWSUpdate):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodRCDUpdate):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodRSUpdate):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodSVTUpdate):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodSPTUpdate):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodCDUpdate):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodTPUpdate):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodPTUpdate):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodESAUpdate):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodTRUpdate):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodADUpdate):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodROUpdate):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodINCUpdate):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodDEFUpdate):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodIWUpdate):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodDTUpdate):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodOTHERUpdate):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodSRSUpdate):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodDPUpdate):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodWSTUpdate):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodSLBUpdate):
                    methods_item = methods_item_data.to_dict()
                else:
                    methods_item = methods_item_data.to_dict()

                methods.append(methods_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if location_id is not UNSET:
            field_dict["location_id"] = location_id
        if iogp_type_id is not UNSET:
            field_dict["iogp_type_id"] = iogp_type_id
        if name is not UNSET:
            field_dict["name"] = name
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
        if tags is not UNSET:
            field_dict["tags"] = tags
        if methods is not UNSET:
            field_dict["methods"] = methods

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.method_ad_create import MethodADCreate
        from ..models.method_ad_update import MethodADUpdate
        from ..models.method_cd_create import MethodCDCreate
        from ..models.method_cd_update import MethodCDUpdate
        from ..models.method_cpt_create import MethodCPTCreate
        from ..models.method_cpt_update import MethodCPTUpdate
        from ..models.method_def_create import MethodDEFCreate
        from ..models.method_def_update import MethodDEFUpdate
        from ..models.method_dp_create import MethodDPCreate
        from ..models.method_dp_update import MethodDPUpdate
        from ..models.method_dt_create import MethodDTCreate
        from ..models.method_dt_update import MethodDTUpdate
        from ..models.method_esa_create import MethodESACreate
        from ..models.method_esa_update import MethodESAUpdate
        from ..models.method_inc_create import MethodINCCreate
        from ..models.method_inc_update import MethodINCUpdate
        from ..models.method_iw_create import MethodIWCreate
        from ..models.method_iw_update import MethodIWUpdate
        from ..models.method_other_create import MethodOTHERCreate
        from ..models.method_other_update import MethodOTHERUpdate
        from ..models.method_pt_create import MethodPTCreate
        from ..models.method_pt_update import MethodPTUpdate
        from ..models.method_pz_create import MethodPZCreate
        from ..models.method_pz_update import MethodPZUpdate
        from ..models.method_rcd_create import MethodRCDCreate
        from ..models.method_rcd_update import MethodRCDUpdate
        from ..models.method_ro_create import MethodROCreate
        from ..models.method_ro_update import MethodROUpdate
        from ..models.method_rp_create import MethodRPCreate
        from ..models.method_rp_update import MethodRPUpdate
        from ..models.method_rs_create import MethodRSCreate
        from ..models.method_rs_update import MethodRSUpdate
        from ..models.method_rws_create import MethodRWSCreate
        from ..models.method_rws_update import MethodRWSUpdate
        from ..models.method_sa_create import MethodSACreate
        from ..models.method_sa_update import MethodSAUpdate
        from ..models.method_slb_create import MethodSLBCreate
        from ..models.method_slb_update import MethodSLBUpdate
        from ..models.method_spt_create import MethodSPTCreate
        from ..models.method_spt_update import MethodSPTUpdate
        from ..models.method_srs_create import MethodSRSCreate
        from ..models.method_srs_update import MethodSRSUpdate
        from ..models.method_ss_create import MethodSSCreate
        from ..models.method_ss_update import MethodSSUpdate
        from ..models.method_sti_create import MethodSTICreate
        from ..models.method_sti_update import MethodSTIUpdate
        from ..models.method_svt_create import MethodSVTCreate
        from ..models.method_svt_update import MethodSVTUpdate
        from ..models.method_tot_create import MethodTOTCreate
        from ..models.method_tot_update import MethodTOTUpdate
        from ..models.method_tp_create import MethodTPCreate
        from ..models.method_tp_update import MethodTPUpdate
        from ..models.method_tr_create import MethodTRCreate
        from ..models.method_tr_update import MethodTRUpdate
        from ..models.method_wst_create import MethodWSTCreate
        from ..models.method_wst_update import MethodWSTUpdate

        d = dict(src_dict)

        def _parse_project_id(data: object) -> Union[None, UUID, Unset]:
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
            return cast(Union[None, UUID, Unset], data)

        project_id = _parse_project_id(d.pop("project_id", UNSET))

        def _parse_location_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                location_id_type_0 = UUID(data)

                return location_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        location_id = _parse_location_id(d.pop("location_id", UNSET))

        def _parse_iogp_type_id(data: object) -> Union[IOGPTypeEnum, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                iogp_type_id_type_0 = IOGPTypeEnum(data)

                return iogp_type_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[IOGPTypeEnum, None, Unset], data)

        iogp_type_id = _parse_iogp_type_id(d.pop("iogp_type_id", UNSET))

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_updated_at(data: object) -> Union[None, Unset, datetime.datetime]:
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
            return cast(Union[None, Unset, datetime.datetime], data)

        updated_at = _parse_updated_at(d.pop("updated_at", UNSET))

        def _parse_updated_by(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        updated_by = _parse_updated_by(d.pop("updated_by", UNSET))

        def _parse_point_easting(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        point_easting = _parse_point_easting(d.pop("point_easting", UNSET))

        def _parse_point_northing(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        point_northing = _parse_point_northing(d.pop("point_northing", UNSET))

        def _parse_point_z(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        point_z = _parse_point_z(d.pop("point_z", UNSET))

        def _parse_srid(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        srid = _parse_srid(d.pop("srid", UNSET))

        def _parse_tags(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = cast(list[str], data)

                return tags_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        tags = _parse_tags(d.pop("tags", UNSET))

        methods = []
        _methods = d.pop("methods", UNSET)
        for methods_item_data in _methods or []:

            def _parse_methods_item(
                data: object,
            ) -> Union[
                "MethodADCreate",
                "MethodADUpdate",
                "MethodCDCreate",
                "MethodCDUpdate",
                "MethodCPTCreate",
                "MethodCPTUpdate",
                "MethodDEFCreate",
                "MethodDEFUpdate",
                "MethodDPCreate",
                "MethodDPUpdate",
                "MethodDTCreate",
                "MethodDTUpdate",
                "MethodESACreate",
                "MethodESAUpdate",
                "MethodINCCreate",
                "MethodINCUpdate",
                "MethodIWCreate",
                "MethodIWUpdate",
                "MethodOTHERCreate",
                "MethodOTHERUpdate",
                "MethodPTCreate",
                "MethodPTUpdate",
                "MethodPZCreate",
                "MethodPZUpdate",
                "MethodRCDCreate",
                "MethodRCDUpdate",
                "MethodROCreate",
                "MethodROUpdate",
                "MethodRPCreate",
                "MethodRPUpdate",
                "MethodRSCreate",
                "MethodRSUpdate",
                "MethodRWSCreate",
                "MethodRWSUpdate",
                "MethodSACreate",
                "MethodSAUpdate",
                "MethodSLBCreate",
                "MethodSLBUpdate",
                "MethodSPTCreate",
                "MethodSPTUpdate",
                "MethodSRSCreate",
                "MethodSRSUpdate",
                "MethodSSCreate",
                "MethodSSUpdate",
                "MethodSTICreate",
                "MethodSTIUpdate",
                "MethodSVTCreate",
                "MethodSVTUpdate",
                "MethodTOTCreate",
                "MethodTOTUpdate",
                "MethodTPCreate",
                "MethodTPUpdate",
                "MethodTRCreate",
                "MethodTRUpdate",
                "MethodWSTCreate",
                "MethodWSTUpdate",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_0_type_0 = MethodADCreate.from_dict(data)

                    return methods_item_type_0_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_0_type_1 = MethodCDCreate.from_dict(data)

                    return methods_item_type_0_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_0_type_2 = MethodCPTCreate.from_dict(data)

                    return methods_item_type_0_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_0_type_3 = MethodDPCreate.from_dict(data)

                    return methods_item_type_0_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_0_type_4 = MethodDTCreate.from_dict(data)

                    return methods_item_type_0_type_4
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_0_type_5 = MethodESACreate.from_dict(data)

                    return methods_item_type_0_type_5
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_0_type_6 = MethodINCCreate.from_dict(data)

                    return methods_item_type_0_type_6
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_0_type_7 = MethodIWCreate.from_dict(data)

                    return methods_item_type_0_type_7
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_0_type_8 = MethodOTHERCreate.from_dict(data)

                    return methods_item_type_0_type_8
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_0_type_9 = MethodPTCreate.from_dict(data)

                    return methods_item_type_0_type_9
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_0_type_10 = MethodPZCreate.from_dict(data)

                    return methods_item_type_0_type_10
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_0_type_11 = MethodRCDCreate.from_dict(data)

                    return methods_item_type_0_type_11
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_0_type_12 = MethodROCreate.from_dict(data)

                    return methods_item_type_0_type_12
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_0_type_13 = MethodRPCreate.from_dict(data)

                    return methods_item_type_0_type_13
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_0_type_14 = MethodRSCreate.from_dict(data)

                    return methods_item_type_0_type_14
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_0_type_15 = MethodRWSCreate.from_dict(data)

                    return methods_item_type_0_type_15
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_0_type_16 = MethodSACreate.from_dict(data)

                    return methods_item_type_0_type_16
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_0_type_17 = MethodSLBCreate.from_dict(data)

                    return methods_item_type_0_type_17
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_0_type_18 = MethodSPTCreate.from_dict(data)

                    return methods_item_type_0_type_18
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_0_type_19 = MethodDEFCreate.from_dict(data)

                    return methods_item_type_0_type_19
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_0_type_20 = MethodSRSCreate.from_dict(data)

                    return methods_item_type_0_type_20
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_0_type_21 = MethodSSCreate.from_dict(data)

                    return methods_item_type_0_type_21
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_0_type_22 = MethodSTICreate.from_dict(data)

                    return methods_item_type_0_type_22
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_0_type_23 = MethodSVTCreate.from_dict(data)

                    return methods_item_type_0_type_23
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_0_type_24 = MethodTOTCreate.from_dict(data)

                    return methods_item_type_0_type_24
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_0_type_25 = MethodTPCreate.from_dict(data)

                    return methods_item_type_0_type_25
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_0_type_26 = MethodTRCreate.from_dict(data)

                    return methods_item_type_0_type_26
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_0_type_27 = MethodWSTCreate.from_dict(data)

                    return methods_item_type_0_type_27
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_1_type_0 = MethodCPTUpdate.from_dict(data)

                    return methods_item_type_1_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_1_type_1 = MethodTOTUpdate.from_dict(data)

                    return methods_item_type_1_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_1_type_2 = MethodRPUpdate.from_dict(data)

                    return methods_item_type_1_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_1_type_3 = MethodSAUpdate.from_dict(data)

                    return methods_item_type_1_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_1_type_4 = MethodPZUpdate.from_dict(data)

                    return methods_item_type_1_type_4
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_1_type_5 = MethodSSUpdate.from_dict(data)

                    return methods_item_type_1_type_5
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_1_type_6 = MethodRWSUpdate.from_dict(data)

                    return methods_item_type_1_type_6
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_1_type_7 = MethodRCDUpdate.from_dict(data)

                    return methods_item_type_1_type_7
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_1_type_8 = MethodRSUpdate.from_dict(data)

                    return methods_item_type_1_type_8
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_1_type_9 = MethodSVTUpdate.from_dict(data)

                    return methods_item_type_1_type_9
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_1_type_10 = MethodSPTUpdate.from_dict(data)

                    return methods_item_type_1_type_10
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_1_type_11 = MethodCDUpdate.from_dict(data)

                    return methods_item_type_1_type_11
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_1_type_12 = MethodTPUpdate.from_dict(data)

                    return methods_item_type_1_type_12
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_1_type_13 = MethodPTUpdate.from_dict(data)

                    return methods_item_type_1_type_13
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_1_type_14 = MethodESAUpdate.from_dict(data)

                    return methods_item_type_1_type_14
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_1_type_15 = MethodTRUpdate.from_dict(data)

                    return methods_item_type_1_type_15
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_1_type_16 = MethodADUpdate.from_dict(data)

                    return methods_item_type_1_type_16
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_1_type_17 = MethodROUpdate.from_dict(data)

                    return methods_item_type_1_type_17
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_1_type_18 = MethodINCUpdate.from_dict(data)

                    return methods_item_type_1_type_18
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_1_type_19 = MethodDEFUpdate.from_dict(data)

                    return methods_item_type_1_type_19
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_1_type_20 = MethodIWUpdate.from_dict(data)

                    return methods_item_type_1_type_20
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_1_type_21 = MethodDTUpdate.from_dict(data)

                    return methods_item_type_1_type_21
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_1_type_22 = MethodOTHERUpdate.from_dict(data)

                    return methods_item_type_1_type_22
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_1_type_23 = MethodSRSUpdate.from_dict(data)

                    return methods_item_type_1_type_23
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_1_type_24 = MethodDPUpdate.from_dict(data)

                    return methods_item_type_1_type_24
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_1_type_25 = MethodWSTUpdate.from_dict(data)

                    return methods_item_type_1_type_25
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_1_type_26 = MethodSLBUpdate.from_dict(data)

                    return methods_item_type_1_type_26
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                methods_item_type_1_type_27 = MethodSTIUpdate.from_dict(data)

                return methods_item_type_1_type_27

            methods_item = _parse_methods_item(methods_item_data)

            methods.append(methods_item)

        location_update = cls(
            project_id=project_id,
            location_id=location_id,
            iogp_type_id=iogp_type_id,
            name=name,
            updated_at=updated_at,
            updated_by=updated_by,
            point_easting=point_easting,
            point_northing=point_northing,
            point_z=point_z,
            srid=srid,
            tags=tags,
            methods=methods,
        )

        location_update.additional_properties = d
        return location_update

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
