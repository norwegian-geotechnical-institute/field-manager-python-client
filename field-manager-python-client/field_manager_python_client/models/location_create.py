import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
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
        iogp_type_id (Union[Unset, IOGPTypeEnum]): For offshore locations, an IOGP type is required
        created_at (Union[None, Unset, datetime.datetime]):
        created_by (Union[None, Unset, str]):
        updated_at (Union[None, Unset, datetime.datetime]):
        updated_by (Union[None, Unset, str]):
        point_easting (Union[None, Unset, float]):
        point_northing (Union[None, Unset, float]):
        point_z (Union[None, Unset, float]):
        srid (Union[None, Unset, int]):
        point_x_wgs84_pseudo (Union[None, Unset, float]):
        point_y_wgs84_pseudo (Union[None, Unset, float]):
        point_x_wgs84_web (Union[None, Unset, float]):
        point_y_wgs84_web (Union[None, Unset, float]):
        tags (Union[Unset, list[str]]):
        project_id (Union[None, UUID, Unset]):
        methods (Union[Unset, list[Union['MethodADCreate', 'MethodCDCreate', 'MethodCPTCreate', 'MethodDEFCreate',
            'MethodDPCreate', 'MethodDTCreate', 'MethodESACreate', 'MethodINCCreate', 'MethodIWCreate', 'MethodOTHERCreate',
            'MethodPTCreate', 'MethodPZCreate', 'MethodRCDCreate', 'MethodROCreate', 'MethodRPCreate', 'MethodRSCreate',
            'MethodRWSCreate', 'MethodSACreate', 'MethodSLBCreate', 'MethodSPTCreate', 'MethodSRSCreate', 'MethodSSCreate',
            'MethodSTICreate', 'MethodSVTCreate', 'MethodTOTCreate', 'MethodTPCreate', 'MethodTRCreate',
            'MethodWSTCreate']]]):
    """

    name: str
    iogp_type_id: Union[Unset, IOGPTypeEnum] = UNSET
    created_at: Union[None, Unset, datetime.datetime] = UNSET
    created_by: Union[None, Unset, str] = UNSET
    updated_at: Union[None, Unset, datetime.datetime] = UNSET
    updated_by: Union[None, Unset, str] = UNSET
    point_easting: Union[None, Unset, float] = UNSET
    point_northing: Union[None, Unset, float] = UNSET
    point_z: Union[None, Unset, float] = UNSET
    srid: Union[None, Unset, int] = UNSET
    point_x_wgs84_pseudo: Union[None, Unset, float] = UNSET
    point_y_wgs84_pseudo: Union[None, Unset, float] = UNSET
    point_x_wgs84_web: Union[None, Unset, float] = UNSET
    point_y_wgs84_web: Union[None, Unset, float] = UNSET
    tags: Union[Unset, list[str]] = UNSET
    project_id: Union[None, UUID, Unset] = UNSET
    methods: Union[
        Unset,
        list[
            Union[
                "MethodADCreate",
                "MethodCDCreate",
                "MethodCPTCreate",
                "MethodDEFCreate",
                "MethodDPCreate",
                "MethodDTCreate",
                "MethodESACreate",
                "MethodINCCreate",
                "MethodIWCreate",
                "MethodOTHERCreate",
                "MethodPTCreate",
                "MethodPZCreate",
                "MethodRCDCreate",
                "MethodROCreate",
                "MethodRPCreate",
                "MethodRSCreate",
                "MethodRWSCreate",
                "MethodSACreate",
                "MethodSLBCreate",
                "MethodSPTCreate",
                "MethodSRSCreate",
                "MethodSSCreate",
                "MethodSTICreate",
                "MethodSVTCreate",
                "MethodTOTCreate",
                "MethodTPCreate",
                "MethodTRCreate",
                "MethodWSTCreate",
            ]
        ],
    ] = UNSET
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

        iogp_type_id: Union[Unset, str] = UNSET
        if not isinstance(self.iogp_type_id, Unset):
            iogp_type_id = self.iogp_type_id.value

        created_at: Union[None, Unset, str]
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        created_by: Union[None, Unset, str]
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        else:
            created_by = self.created_by

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

        point_x_wgs84_pseudo: Union[None, Unset, float]
        if isinstance(self.point_x_wgs84_pseudo, Unset):
            point_x_wgs84_pseudo = UNSET
        else:
            point_x_wgs84_pseudo = self.point_x_wgs84_pseudo

        point_y_wgs84_pseudo: Union[None, Unset, float]
        if isinstance(self.point_y_wgs84_pseudo, Unset):
            point_y_wgs84_pseudo = UNSET
        else:
            point_y_wgs84_pseudo = self.point_y_wgs84_pseudo

        point_x_wgs84_web: Union[None, Unset, float]
        if isinstance(self.point_x_wgs84_web, Unset):
            point_x_wgs84_web = UNSET
        else:
            point_x_wgs84_web = self.point_x_wgs84_web

        point_y_wgs84_web: Union[None, Unset, float]
        if isinstance(self.point_y_wgs84_web, Unset):
            point_y_wgs84_web = UNSET
        else:
            point_y_wgs84_web = self.point_y_wgs84_web

        tags: Union[Unset, list[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        project_id: Union[None, Unset, str]
        if isinstance(self.project_id, Unset):
            project_id = UNSET
        elif isinstance(self.project_id, UUID):
            project_id = str(self.project_id)
        else:
            project_id = self.project_id

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
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
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

        d = src_dict.copy()
        name = d.pop("name")

        _iogp_type_id = d.pop("iogp_type_id", UNSET)
        iogp_type_id: Union[Unset, IOGPTypeEnum]
        if isinstance(_iogp_type_id, Unset):
            iogp_type_id = UNSET
        else:
            iogp_type_id = IOGPTypeEnum(_iogp_type_id)

        def _parse_created_at(data: object) -> Union[None, Unset, datetime.datetime]:
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
            return cast(Union[None, Unset, datetime.datetime], data)

        created_at = _parse_created_at(d.pop("created_at", UNSET))

        def _parse_created_by(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        created_by = _parse_created_by(d.pop("created_by", UNSET))

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

        def _parse_point_x_wgs84_pseudo(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        point_x_wgs84_pseudo = _parse_point_x_wgs84_pseudo(d.pop("point_x_wgs84_pseudo", UNSET))

        def _parse_point_y_wgs84_pseudo(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        point_y_wgs84_pseudo = _parse_point_y_wgs84_pseudo(d.pop("point_y_wgs84_pseudo", UNSET))

        def _parse_point_x_wgs84_web(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        point_x_wgs84_web = _parse_point_x_wgs84_web(d.pop("point_x_wgs84_web", UNSET))

        def _parse_point_y_wgs84_web(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        point_y_wgs84_web = _parse_point_y_wgs84_web(d.pop("point_y_wgs84_web", UNSET))

        tags = cast(list[str], d.pop("tags", UNSET))

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

        methods = []
        _methods = d.pop("methods", UNSET)
        for methods_item_data in _methods or []:

            def _parse_methods_item(
                data: object,
            ) -> Union[
                "MethodADCreate",
                "MethodCDCreate",
                "MethodCPTCreate",
                "MethodDEFCreate",
                "MethodDPCreate",
                "MethodDTCreate",
                "MethodESACreate",
                "MethodINCCreate",
                "MethodIWCreate",
                "MethodOTHERCreate",
                "MethodPTCreate",
                "MethodPZCreate",
                "MethodRCDCreate",
                "MethodROCreate",
                "MethodRPCreate",
                "MethodRSCreate",
                "MethodRWSCreate",
                "MethodSACreate",
                "MethodSLBCreate",
                "MethodSPTCreate",
                "MethodSRSCreate",
                "MethodSSCreate",
                "MethodSTICreate",
                "MethodSVTCreate",
                "MethodTOTCreate",
                "MethodTPCreate",
                "MethodTRCreate",
                "MethodWSTCreate",
            ]:
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
