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
    from ..models.file import File
    from ..models.method_ad import MethodAD
    from ..models.method_cd import MethodCD
    from ..models.method_cpt import MethodCPT
    from ..models.method_def import MethodDEF
    from ..models.method_dp import MethodDP
    from ..models.method_dt import MethodDT
    from ..models.method_esa import MethodESA
    from ..models.method_inc import MethodINC
    from ..models.method_iw import MethodIW
    from ..models.method_other import MethodOTHER
    from ..models.method_pt import MethodPT
    from ..models.method_pz import MethodPZ
    from ..models.method_rcd import MethodRCD
    from ..models.method_ro import MethodRO
    from ..models.method_rp import MethodRP
    from ..models.method_rs import MethodRS
    from ..models.method_rws import MethodRWS
    from ..models.method_sa import MethodSA
    from ..models.method_slb import MethodSLB
    from ..models.method_spt import MethodSPT
    from ..models.method_srs import MethodSRS
    from ..models.method_ss import MethodSS
    from ..models.method_sti import MethodSTI
    from ..models.method_svt import MethodSVT
    from ..models.method_tot import MethodTOT
    from ..models.method_tp import MethodTP
    from ..models.method_tr import MethodTR
    from ..models.method_wst import MethodWST


T = TypeVar("T", bound="Location")


@_attrs_define
class Location:
    """
    Example:
        {'location_id': '22be3639-4271-4c5b-9d51-86268159e976', 'name': 'Loc01', 'point_easting': 1194547,
            'point_northing': 8388298, 'point_z': 0.0, 'project_id': '85244111-4374-413e-aad1-d20be1d32f53', 'srid': 3857}

    Attributes:
        name (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        location_id (UUID):
        project_id (UUID):
        is_deleted (bool):
        last_updated (datetime.datetime):
        iogp_type_id (Union[Unset, IOGPTypeEnum]): For offshore locations, an IOGP type is required
        created_by (Union[None, Unset, str]):
        updated_by (Union[None, Unset, str]):
        point_easting (Union[None, Unset, float]):
        point_northing (Union[None, Unset, float]):
        point_z (Union[None, Unset, float]):
        srid (Union[None, Unset, int]):
        point_x_wgs84_pseudo (Union[None, Unset, float]):
        point_y_wgs84_pseudo (Union[None, Unset, float]):
        point_x_wgs84_web (Union[None, Unset, float]):
        point_y_wgs84_web (Union[None, Unset, float]):
        tags (Union[None, Unset, list[str]]):
        methods (Union[Unset, list[Union['MethodAD', 'MethodCD', 'MethodCPT', 'MethodDEF', 'MethodDP', 'MethodDT',
            'MethodESA', 'MethodINC', 'MethodIW', 'MethodOTHER', 'MethodPT', 'MethodPZ', 'MethodRCD', 'MethodRO',
            'MethodRP', 'MethodRS', 'MethodRWS', 'MethodSA', 'MethodSLB', 'MethodSPT', 'MethodSRS', 'MethodSS', 'MethodSTI',
            'MethodSVT', 'MethodTOT', 'MethodTP', 'MethodTR', 'MethodWST']]]):
        files (Union[Unset, list['File']]):
    """

    name: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    location_id: UUID
    project_id: UUID
    is_deleted: bool
    last_updated: datetime.datetime
    iogp_type_id: Union[Unset, IOGPTypeEnum] = UNSET
    created_by: Union[None, Unset, str] = UNSET
    updated_by: Union[None, Unset, str] = UNSET
    point_easting: Union[None, Unset, float] = UNSET
    point_northing: Union[None, Unset, float] = UNSET
    point_z: Union[None, Unset, float] = UNSET
    srid: Union[None, Unset, int] = UNSET
    point_x_wgs84_pseudo: Union[None, Unset, float] = UNSET
    point_y_wgs84_pseudo: Union[None, Unset, float] = UNSET
    point_x_wgs84_web: Union[None, Unset, float] = UNSET
    point_y_wgs84_web: Union[None, Unset, float] = UNSET
    tags: Union[None, Unset, list[str]] = UNSET
    methods: Union[
        Unset,
        list[
            Union[
                "MethodAD",
                "MethodCD",
                "MethodCPT",
                "MethodDEF",
                "MethodDP",
                "MethodDT",
                "MethodESA",
                "MethodINC",
                "MethodIW",
                "MethodOTHER",
                "MethodPT",
                "MethodPZ",
                "MethodRCD",
                "MethodRO",
                "MethodRP",
                "MethodRS",
                "MethodRWS",
                "MethodSA",
                "MethodSLB",
                "MethodSPT",
                "MethodSRS",
                "MethodSS",
                "MethodSTI",
                "MethodSVT",
                "MethodTOT",
                "MethodTP",
                "MethodTR",
                "MethodWST",
            ]
        ],
    ] = UNSET
    files: Union[Unset, list["File"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.method_ad import MethodAD
        from ..models.method_cd import MethodCD
        from ..models.method_cpt import MethodCPT
        from ..models.method_def import MethodDEF
        from ..models.method_dp import MethodDP
        from ..models.method_dt import MethodDT
        from ..models.method_esa import MethodESA
        from ..models.method_inc import MethodINC
        from ..models.method_iw import MethodIW
        from ..models.method_other import MethodOTHER
        from ..models.method_pt import MethodPT
        from ..models.method_pz import MethodPZ
        from ..models.method_rcd import MethodRCD
        from ..models.method_ro import MethodRO
        from ..models.method_rp import MethodRP
        from ..models.method_rs import MethodRS
        from ..models.method_rws import MethodRWS
        from ..models.method_sa import MethodSA
        from ..models.method_slb import MethodSLB
        from ..models.method_spt import MethodSPT
        from ..models.method_srs import MethodSRS
        from ..models.method_ss import MethodSS
        from ..models.method_svt import MethodSVT
        from ..models.method_tot import MethodTOT
        from ..models.method_tp import MethodTP
        from ..models.method_tr import MethodTR
        from ..models.method_wst import MethodWST

        name = self.name

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        location_id = str(self.location_id)

        project_id = str(self.project_id)

        is_deleted = self.is_deleted

        last_updated = self.last_updated.isoformat()

        iogp_type_id: Union[Unset, str] = UNSET
        if not isinstance(self.iogp_type_id, Unset):
            iogp_type_id = self.iogp_type_id.value

        created_by: Union[None, Unset, str]
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        else:
            created_by = self.created_by

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
                if isinstance(methods_item_data, MethodCPT):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodTOT):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodRP):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodSA):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodPZ):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodSS):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodRWS):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodRCD):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodRS):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodSVT):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodSPT):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodCD):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodTP):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodPT):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodESA):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodTR):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodAD):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodRO):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodINC):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodDEF):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodIW):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodDT):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodOTHER):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodSRS):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodDP):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodWST):
                    methods_item = methods_item_data.to_dict()
                elif isinstance(methods_item_data, MethodSLB):
                    methods_item = methods_item_data.to_dict()
                else:
                    methods_item = methods_item_data.to_dict()

                methods.append(methods_item)

        files: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.files, Unset):
            files = []
            for files_item_data in self.files:
                files_item = files_item_data.to_dict()
                files.append(files_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "created_at": created_at,
                "updated_at": updated_at,
                "location_id": location_id,
                "project_id": project_id,
                "is_deleted": is_deleted,
                "last_updated": last_updated,
            }
        )
        if iogp_type_id is not UNSET:
            field_dict["iogp_type_id"] = iogp_type_id
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
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
        if methods is not UNSET:
            field_dict["methods"] = methods
        if files is not UNSET:
            field_dict["files"] = files

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file import File
        from ..models.method_ad import MethodAD
        from ..models.method_cd import MethodCD
        from ..models.method_cpt import MethodCPT
        from ..models.method_def import MethodDEF
        from ..models.method_dp import MethodDP
        from ..models.method_dt import MethodDT
        from ..models.method_esa import MethodESA
        from ..models.method_inc import MethodINC
        from ..models.method_iw import MethodIW
        from ..models.method_other import MethodOTHER
        from ..models.method_pt import MethodPT
        from ..models.method_pz import MethodPZ
        from ..models.method_rcd import MethodRCD
        from ..models.method_ro import MethodRO
        from ..models.method_rp import MethodRP
        from ..models.method_rs import MethodRS
        from ..models.method_rws import MethodRWS
        from ..models.method_sa import MethodSA
        from ..models.method_slb import MethodSLB
        from ..models.method_spt import MethodSPT
        from ..models.method_srs import MethodSRS
        from ..models.method_ss import MethodSS
        from ..models.method_sti import MethodSTI
        from ..models.method_svt import MethodSVT
        from ..models.method_tot import MethodTOT
        from ..models.method_tp import MethodTP
        from ..models.method_tr import MethodTR
        from ..models.method_wst import MethodWST

        d = dict(src_dict)
        name = d.pop("name")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        location_id = UUID(d.pop("location_id"))

        project_id = UUID(d.pop("project_id"))

        is_deleted = d.pop("is_deleted")

        last_updated = isoparse(d.pop("last_updated"))

        _iogp_type_id = d.pop("iogp_type_id", UNSET)
        iogp_type_id: Union[Unset, IOGPTypeEnum]
        if isinstance(_iogp_type_id, Unset):
            iogp_type_id = UNSET
        else:
            iogp_type_id = IOGPTypeEnum(_iogp_type_id)

        def _parse_created_by(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        created_by = _parse_created_by(d.pop("created_by", UNSET))

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
                "MethodAD",
                "MethodCD",
                "MethodCPT",
                "MethodDEF",
                "MethodDP",
                "MethodDT",
                "MethodESA",
                "MethodINC",
                "MethodIW",
                "MethodOTHER",
                "MethodPT",
                "MethodPZ",
                "MethodRCD",
                "MethodRO",
                "MethodRP",
                "MethodRS",
                "MethodRWS",
                "MethodSA",
                "MethodSLB",
                "MethodSPT",
                "MethodSRS",
                "MethodSS",
                "MethodSTI",
                "MethodSVT",
                "MethodTOT",
                "MethodTP",
                "MethodTR",
                "MethodWST",
            ]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_0 = MethodCPT.from_dict(data)

                    return methods_item_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_1 = MethodTOT.from_dict(data)

                    return methods_item_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_2 = MethodRP.from_dict(data)

                    return methods_item_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_3 = MethodSA.from_dict(data)

                    return methods_item_type_3
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_4 = MethodPZ.from_dict(data)

                    return methods_item_type_4
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_5 = MethodSS.from_dict(data)

                    return methods_item_type_5
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_6 = MethodRWS.from_dict(data)

                    return methods_item_type_6
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_7 = MethodRCD.from_dict(data)

                    return methods_item_type_7
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_8 = MethodRS.from_dict(data)

                    return methods_item_type_8
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_9 = MethodSVT.from_dict(data)

                    return methods_item_type_9
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_10 = MethodSPT.from_dict(data)

                    return methods_item_type_10
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_11 = MethodCD.from_dict(data)

                    return methods_item_type_11
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_12 = MethodTP.from_dict(data)

                    return methods_item_type_12
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_13 = MethodPT.from_dict(data)

                    return methods_item_type_13
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_14 = MethodESA.from_dict(data)

                    return methods_item_type_14
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_15 = MethodTR.from_dict(data)

                    return methods_item_type_15
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_16 = MethodAD.from_dict(data)

                    return methods_item_type_16
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_17 = MethodRO.from_dict(data)

                    return methods_item_type_17
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_18 = MethodINC.from_dict(data)

                    return methods_item_type_18
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_19 = MethodDEF.from_dict(data)

                    return methods_item_type_19
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_20 = MethodIW.from_dict(data)

                    return methods_item_type_20
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_21 = MethodDT.from_dict(data)

                    return methods_item_type_21
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_22 = MethodOTHER.from_dict(data)

                    return methods_item_type_22
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_23 = MethodSRS.from_dict(data)

                    return methods_item_type_23
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_24 = MethodDP.from_dict(data)

                    return methods_item_type_24
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_25 = MethodWST.from_dict(data)

                    return methods_item_type_25
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    methods_item_type_26 = MethodSLB.from_dict(data)

                    return methods_item_type_26
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                methods_item_type_27 = MethodSTI.from_dict(data)

                return methods_item_type_27

            methods_item = _parse_methods_item(methods_item_data)

            methods.append(methods_item)

        files = []
        _files = d.pop("files", UNSET)
        for files_item_data in _files or []:
            files_item = File.from_dict(files_item_data)

            files.append(files_item)

        location = cls(
            name=name,
            created_at=created_at,
            updated_at=updated_at,
            location_id=location_id,
            project_id=project_id,
            is_deleted=is_deleted,
            last_updated=last_updated,
            iogp_type_id=iogp_type_id,
            created_by=created_by,
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
            methods=methods,
            files=files,
        )

        location.additional_properties = d
        return location

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
