"""Contains all the data models used in inputs/outputs"""

from .application_class_enum import ApplicationClassEnum
from .background_map_layer import BackgroundMapLayer
from .bedrock_info import BedrockInfo
from .bedrock_type import BedrockType
from .bff_file import BFFFile
from .bff_location import BFFLocation
from .bff_location_summary import BFFLocationSummary
from .bff_method import BFFMethod
from .bff_method_summary import BFFMethodSummary
from .bff_project_summary import BFFProjectSummary
from .body_queue_locations_to_project_projects_project_id_locations_queue_post import (
    BodyQueueLocationsToProjectProjectsProjectIdLocationsQueuePost,
)
from .body_upload_file_projects_project_id_locations_location_id_methods_method_id_upload_post import (
    BodyUploadFileProjectsProjectIdLocationsLocationIdMethodsMethodIdUploadPost,
)
from .body_upload_file_to_location_projects_project_id_locations_location_id_upload_post import (
    BodyUploadFileToLocationProjectsProjectIdLocationsLocationIdUploadPost,
)
from .body_upload_file_to_organization_organizations_organization_id_upload_post import (
    BodyUploadFileToOrganizationOrganizationsOrganizationIdUploadPost,
)
from .body_upload_file_to_project_projects_project_id_upload_post import (
    BodyUploadFileToProjectProjectsProjectIdUploadPost,
)
from .body_upload_locations_to_project_projects_project_id_locations_upload_post import (
    BodyUploadLocationsToProjectProjectsProjectIdLocationsUploadPost,
)
from .color_mode import ColorMode
from .comment import Comment
from .comment_create import CommentCreate
from .comment_update import CommentUpdate
from .cpt_options import CPTOptions
from .date_format import DateFormat
from .dp_type import DPType
from .export import Export
from .export_type import ExportType
from .file import File
from .file_extended import FileExtended
from .file_extension import FileExtension
from .file_type import FileType
from .file_update import FileUpdate
from .fm_plot_options import FMPlotOptions
from .height_reference import HeightReference
from .http_validation_error import HTTPValidationError
from .image_size import ImageSize
from .iogp_type import IOGPType
from .iogp_type_enum import IOGPTypeEnum
from .language import Language
from .like import Like
from .linked_project_info import LinkedProjectInfo
from .location import Location
from .location_coordinates import LocationCoordinates
from .location_create import LocationCreate
from .location_gis import LocationGis
from .location_info import LocationInfo
from .location_min import LocationMin
from .location_summary import LocationSummary
from .location_type import LocationType
from .location_type_enum import LocationTypeEnum
from .location_update import LocationUpdate
from .map_layout import MapLayout
from .map_layout_create import MapLayoutCreate
from .map_layout_update import MapLayoutUpdate
from .map_layout_version import MapLayoutVersion
from .map_layout_version_create import MapLayoutVersionCreate
from .map_layout_version_update import MapLayoutVersionUpdate
from .map_scale import MapScale
from .method_ad import MethodAD
from .method_ad_create import MethodADCreate
from .method_ad_create_method_type_id import MethodADCreateMethodTypeId
from .method_ad_method_type_id import MethodADMethodTypeId
from .method_ad_update import MethodADUpdate
from .method_ad_update_method_type_id import MethodADUpdateMethodTypeId
from .method_cd import MethodCD
from .method_cd_create import MethodCDCreate
from .method_cd_create_method_type_id import MethodCDCreateMethodTypeId
from .method_cd_method_type_id import MethodCDMethodTypeId
from .method_cd_update import MethodCDUpdate
from .method_cd_update_method_type_id import MethodCDUpdateMethodTypeId
from .method_cpt import MethodCPT
from .method_cpt_create import MethodCPTCreate
from .method_cpt_create_method_type_id import MethodCPTCreateMethodTypeId
from .method_cpt_data import MethodCPTData
from .method_cpt_data_create import MethodCPTDataCreate
from .method_cpt_data_create_method_type_id import MethodCPTDataCreateMethodTypeId
from .method_cpt_data_method_type_id import MethodCPTDataMethodTypeId
from .method_cpt_data_update import MethodCPTDataUpdate
from .method_cpt_data_update_method_type_id import MethodCPTDataUpdateMethodTypeId
from .method_cpt_method_type_id import MethodCPTMethodTypeId
from .method_cpt_update import MethodCPTUpdate
from .method_cpt_update_method_type_id import MethodCPTUpdateMethodTypeId
from .method_dp import MethodDP
from .method_dp_create import MethodDPCreate
from .method_dp_create_method_type_id import MethodDPCreateMethodTypeId
from .method_dp_data import MethodDPData
from .method_dp_data_create import MethodDPDataCreate
from .method_dp_data_create_method_type_id import MethodDPDataCreateMethodTypeId
from .method_dp_data_method_type_id import MethodDPDataMethodTypeId
from .method_dp_method_type_id import MethodDPMethodTypeId
from .method_dp_update import MethodDPUpdate
from .method_dp_update_method_type_id import MethodDPUpdateMethodTypeId
from .method_dt import MethodDT
from .method_dt_create import MethodDTCreate
from .method_dt_create_method_type_id import MethodDTCreateMethodTypeId
from .method_dt_data import MethodDTData
from .method_dt_data_create import MethodDTDataCreate
from .method_dt_data_create_method_type_id import MethodDTDataCreateMethodTypeId
from .method_dt_data_method_type_id import MethodDTDataMethodTypeId
from .method_dt_data_update import MethodDTDataUpdate
from .method_dt_data_update_method_type_id import MethodDTDataUpdateMethodTypeId
from .method_dt_method_type_id import MethodDTMethodTypeId
from .method_dt_update import MethodDTUpdate
from .method_dt_update_method_type_id import MethodDTUpdateMethodTypeId
from .method_esa import MethodESA
from .method_esa_create import MethodESACreate
from .method_esa_create_method_type_id import MethodESACreateMethodTypeId
from .method_esa_method_type_id import MethodESAMethodTypeId
from .method_esa_update import MethodESAUpdate
from .method_esa_update_method_type_id import MethodESAUpdateMethodTypeId
from .method_export_type import MethodExportType
from .method_inc import MethodINC
from .method_inc_create import MethodINCCreate
from .method_inc_create_method_type_id import MethodINCCreateMethodTypeId
from .method_inc_method_type_id import MethodINCMethodTypeId
from .method_inc_update import MethodINCUpdate
from .method_inc_update_method_type_id import MethodINCUpdateMethodTypeId
from .method_info import MethodInfo
from .method_iw import MethodIW
from .method_iw_create import MethodIWCreate
from .method_iw_create_method_type_id import MethodIWCreateMethodTypeId
from .method_iw_method_type_id import MethodIWMethodTypeId
from .method_iw_update import MethodIWUpdate
from .method_iw_update_method_type_id import MethodIWUpdateMethodTypeId
from .method_min import MethodMin
from .method_other import MethodOTHER
from .method_other_create import MethodOTHERCreate
from .method_other_create_method_type_id import MethodOTHERCreateMethodTypeId
from .method_other_method_type_id import MethodOTHERMethodTypeId
from .method_other_update import MethodOTHERUpdate
from .method_other_update_method_type_id import MethodOTHERUpdateMethodTypeId
from .method_pt import MethodPT
from .method_pt_create import MethodPTCreate
from .method_pt_create_method_type_id import MethodPTCreateMethodTypeId
from .method_pt_method_type_id import MethodPTMethodTypeId
from .method_pt_update import MethodPTUpdate
from .method_pt_update_method_type_id import MethodPTUpdateMethodTypeId
from .method_pz import MethodPZ
from .method_pz_create import MethodPZCreate
from .method_pz_create_method_type_id import MethodPZCreateMethodTypeId
from .method_pz_data import MethodPZData
from .method_pz_data_create import MethodPZDataCreate
from .method_pz_data_create_method_type_id import MethodPZDataCreateMethodTypeId
from .method_pz_data_method_type_id import MethodPZDataMethodTypeId
from .method_pz_data_update import MethodPZDataUpdate
from .method_pz_data_update_method_type_id import MethodPZDataUpdateMethodTypeId
from .method_pz_method_type_id import MethodPZMethodTypeId
from .method_pz_update import MethodPZUpdate
from .method_pz_update_method_type_id import MethodPZUpdateMethodTypeId
from .method_rcd import MethodRCD
from .method_rcd_create import MethodRCDCreate
from .method_rcd_create_method_type_id import MethodRCDCreateMethodTypeId
from .method_rcd_data import MethodRCDData
from .method_rcd_data_create import MethodRCDDataCreate
from .method_rcd_data_create_method_type_id import MethodRCDDataCreateMethodTypeId
from .method_rcd_data_method_type_id import MethodRCDDataMethodTypeId
from .method_rcd_data_update import MethodRCDDataUpdate
from .method_rcd_data_update_method_type_id import MethodRCDDataUpdateMethodTypeId
from .method_rcd_method_type_id import MethodRCDMethodTypeId
from .method_rcd_update import MethodRCDUpdate
from .method_rcd_update_method_type_id import MethodRCDUpdateMethodTypeId
from .method_ro import MethodRO
from .method_ro_create import MethodROCreate
from .method_ro_create_method_type_id import MethodROCreateMethodTypeId
from .method_ro_method_type_id import MethodROMethodTypeId
from .method_ro_update import MethodROUpdate
from .method_ro_update_method_type_id import MethodROUpdateMethodTypeId
from .method_rp import MethodRP
from .method_rp_create import MethodRPCreate
from .method_rp_create_method_type_id import MethodRPCreateMethodTypeId
from .method_rp_data import MethodRPData
from .method_rp_data_create import MethodRPDataCreate
from .method_rp_data_create_method_type_id import MethodRPDataCreateMethodTypeId
from .method_rp_data_method_type_id import MethodRPDataMethodTypeId
from .method_rp_data_update import MethodRPDataUpdate
from .method_rp_data_update_method_type_id import MethodRPDataUpdateMethodTypeId
from .method_rp_method_type_id import MethodRPMethodTypeId
from .method_rp_update import MethodRPUpdate
from .method_rp_update_method_type_id import MethodRPUpdateMethodTypeId
from .method_rs import MethodRS
from .method_rs_create import MethodRSCreate
from .method_rs_create_method_type_id import MethodRSCreateMethodTypeId
from .method_rs_method_type_id import MethodRSMethodTypeId
from .method_rs_update import MethodRSUpdate
from .method_rs_update_method_type_id import MethodRSUpdateMethodTypeId
from .method_rws import MethodRWS
from .method_rws_create import MethodRWSCreate
from .method_rws_create_method_type_id import MethodRWSCreateMethodTypeId
from .method_rws_method_type_id import MethodRWSMethodTypeId
from .method_rws_update import MethodRWSUpdate
from .method_rws_update_method_type_id import MethodRWSUpdateMethodTypeId
from .method_sa import MethodSA
from .method_sa_create import MethodSACreate
from .method_sa_create_method_type_id import MethodSACreateMethodTypeId
from .method_sa_method_type_id import MethodSAMethodTypeId
from .method_sa_update import MethodSAUpdate
from .method_sa_update_method_type_id import MethodSAUpdateMethodTypeId
from .method_spt import MethodSPT
from .method_spt_create import MethodSPTCreate
from .method_spt_create_method_type_id import MethodSPTCreateMethodTypeId
from .method_spt_method_type_id import MethodSPTMethodTypeId
from .method_spt_update import MethodSPTUpdate
from .method_spt_update_method_type_id import MethodSPTUpdateMethodTypeId
from .method_sr import MethodSR
from .method_sr_create import MethodSRCreate
from .method_sr_create_method_type_id import MethodSRCreateMethodTypeId
from .method_sr_method_type_id import MethodSRMethodTypeId
from .method_sr_update import MethodSRUpdate
from .method_sr_update_method_type_id import MethodSRUpdateMethodTypeId
from .method_srs import MethodSRS
from .method_srs_create import MethodSRSCreate
from .method_srs_create_method_type_id import MethodSRSCreateMethodTypeId
from .method_srs_data import MethodSRSData
from .method_srs_data_create import MethodSRSDataCreate
from .method_srs_data_create_method_type_id import MethodSRSDataCreateMethodTypeId
from .method_srs_data_method_type_id import MethodSRSDataMethodTypeId
from .method_srs_data_update import MethodSRSDataUpdate
from .method_srs_data_update_method_type_id import MethodSRSDataUpdateMethodTypeId
from .method_srs_method_type_id import MethodSRSMethodTypeId
from .method_srs_update import MethodSRSUpdate
from .method_srs_update_method_type_id import MethodSRSUpdateMethodTypeId
from .method_ss import MethodSS
from .method_ss_create import MethodSSCreate
from .method_ss_create_method_type_id import MethodSSCreateMethodTypeId
from .method_ss_data import MethodSSData
from .method_ss_data_create import MethodSSDataCreate
from .method_ss_data_create_method_type_id import MethodSSDataCreateMethodTypeId
from .method_ss_data_method_type_id import MethodSSDataMethodTypeId
from .method_ss_data_update import MethodSSDataUpdate
from .method_ss_data_update_method_type_id import MethodSSDataUpdateMethodTypeId
from .method_ss_method_type_id import MethodSSMethodTypeId
from .method_ss_update import MethodSSUpdate
from .method_ss_update_method_type_id import MethodSSUpdateMethodTypeId
from .method_status_enum import MethodStatusEnum
from .method_summary import MethodSummary
from .method_svt import MethodSVT
from .method_svt_create import MethodSVTCreate
from .method_svt_create_method_type_id import MethodSVTCreateMethodTypeId
from .method_svt_data import MethodSVTData
from .method_svt_data_create import MethodSVTDataCreate
from .method_svt_data_create_method_type_id import MethodSVTDataCreateMethodTypeId
from .method_svt_data_method_type_id import MethodSVTDataMethodTypeId
from .method_svt_data_update import MethodSVTDataUpdate
from .method_svt_data_update_method_type_id import MethodSVTDataUpdateMethodTypeId
from .method_svt_method_type_id import MethodSVTMethodTypeId
from .method_svt_update import MethodSVTUpdate
from .method_svt_update_method_type_id import MethodSVTUpdateMethodTypeId
from .method_tot import MethodTOT
from .method_tot_create import MethodTOTCreate
from .method_tot_create_method_type_id import MethodTOTCreateMethodTypeId
from .method_tot_data import MethodTOTData
from .method_tot_data_create import MethodTOTDataCreate
from .method_tot_data_create_method_type_id import MethodTOTDataCreateMethodTypeId
from .method_tot_data_method_type_id import MethodTOTDataMethodTypeId
from .method_tot_data_update import MethodTOTDataUpdate
from .method_tot_data_update_method_type_id import MethodTOTDataUpdateMethodTypeId
from .method_tot_method_type_id import MethodTOTMethodTypeId
from .method_tot_update import MethodTOTUpdate
from .method_tot_update_method_type_id import MethodTOTUpdateMethodTypeId
from .method_tp import MethodTP
from .method_tp_create import MethodTPCreate
from .method_tp_create_method_type_id import MethodTPCreateMethodTypeId
from .method_tp_method_type_id import MethodTPMethodTypeId
from .method_tp_update import MethodTPUpdate
from .method_tp_update_method_type_id import MethodTPUpdateMethodTypeId
from .method_type import MethodType
from .method_type_enum import MethodTypeEnum
from .method_type_enum_str import MethodTypeEnumStr
from .method_wst import MethodWST
from .method_wst_create import MethodWSTCreate
from .method_wst_create_method_type_id import MethodWSTCreateMethodTypeId
from .method_wst_data import MethodWSTData
from .method_wst_data_create import MethodWSTDataCreate
from .method_wst_data_create_method_type_id import MethodWSTDataCreateMethodTypeId
from .method_wst_data_method_type_id import MethodWSTDataMethodTypeId
from .method_wst_data_update import MethodWSTDataUpdate
from .method_wst_data_update_method_type_id import MethodWSTDataUpdateMethodTypeId
from .method_wst_method_type_id import MethodWSTMethodTypeId
from .method_wst_update import MethodWSTUpdate
from .method_wst_update_method_type_id import MethodWSTUpdateMethodTypeId
from .operation import Operation
from .options import Options
from .organization import Organization
from .organization_create import OrganizationCreate
from .organization_information import OrganizationInformation
from .organization_min import OrganizationMin
from .organization_update import OrganizationUpdate
from .orientation import Orientation
from .page_number_prefix_by_method import PageNumberPrefixByMethod
from .page_number_start_per_method import PageNumberStartPerMethod
from .paper_size import PaperSize
from .pdf_options import PdfOptions
from .pdf_options_date_format import PdfOptionsDateFormat
from .pdf_options_lang import PdfOptionsLang
from .pdf_options_paper_size import PdfOptionsPaperSize
from .pdf_options_sort_figures_by import PdfOptionsSortFiguresBy
from .pdf_page_info import PDFPageInfo
from .piezometer_model import PiezometerModel
from .piezometer_model_create import PiezometerModelCreate
from .piezometer_model_update import PiezometerModelUpdate
from .piezometer_type import PiezometerType
from .piezometer_vendor import PiezometerVendor
from .pizeometer_units import PizeometerUnits
from .plot_data_stats import PlotDataStats
from .plot_data_stats_percentiles import PlotDataStatsPercentiles
from .plot_format import PlotFormat
from .plot_info_object import PlotInfoObject
from .plot_info_object_stats_type_0 import PlotInfoObjectStatsType0
from .plot_sequence import PlotSequence
from .plot_sequence_options import PlotSequenceOptions
from .plot_type import PlotType
from .project import Project
from .project_create import ProjectCreate
from .project_info import ProjectInfo
from .project_location_method_types import ProjectLocationMethodTypes
from .project_search import ProjectSearch
from .project_summary import ProjectSummary
from .project_update import ProjectUpdate
from .reading_type import ReadingType
from .role import Role
from .role_entity_enum import RoleEntityEnum
from .role_enum import RoleEnum
from .sample_container_type import SampleContainerType
from .sample_material import SampleMaterial
from .sampler_type import SamplerType
from .sampling_technique import SamplingTechnique
from .scales import Scales
from .scaling_mode import ScalingMode
from .sounding_class import SoundingClass
from .standard import Standard
from .standard_type import StandardType
from .transformation_type import TransformationType
from .user import User
from .validation_error import ValidationError

__all__ = (
    "ApplicationClassEnum",
    "BackgroundMapLayer",
    "BedrockInfo",
    "BedrockType",
    "BFFFile",
    "BFFLocation",
    "BFFLocationSummary",
    "BFFMethod",
    "BFFMethodSummary",
    "BFFProjectSummary",
    "BodyQueueLocationsToProjectProjectsProjectIdLocationsQueuePost",
    "BodyUploadFileProjectsProjectIdLocationsLocationIdMethodsMethodIdUploadPost",
    "BodyUploadFileToLocationProjectsProjectIdLocationsLocationIdUploadPost",
    "BodyUploadFileToOrganizationOrganizationsOrganizationIdUploadPost",
    "BodyUploadFileToProjectProjectsProjectIdUploadPost",
    "BodyUploadLocationsToProjectProjectsProjectIdLocationsUploadPost",
    "ColorMode",
    "Comment",
    "CommentCreate",
    "CommentUpdate",
    "CPTOptions",
    "DateFormat",
    "DPType",
    "Export",
    "ExportType",
    "File",
    "FileExtended",
    "FileExtension",
    "FileType",
    "FileUpdate",
    "FMPlotOptions",
    "HeightReference",
    "HTTPValidationError",
    "ImageSize",
    "IOGPType",
    "IOGPTypeEnum",
    "Language",
    "Like",
    "LinkedProjectInfo",
    "Location",
    "LocationCoordinates",
    "LocationCreate",
    "LocationGis",
    "LocationInfo",
    "LocationMin",
    "LocationSummary",
    "LocationType",
    "LocationTypeEnum",
    "LocationUpdate",
    "MapLayout",
    "MapLayoutCreate",
    "MapLayoutUpdate",
    "MapLayoutVersion",
    "MapLayoutVersionCreate",
    "MapLayoutVersionUpdate",
    "MapScale",
    "MethodAD",
    "MethodADCreate",
    "MethodADCreateMethodTypeId",
    "MethodADMethodTypeId",
    "MethodADUpdate",
    "MethodADUpdateMethodTypeId",
    "MethodCD",
    "MethodCDCreate",
    "MethodCDCreateMethodTypeId",
    "MethodCDMethodTypeId",
    "MethodCDUpdate",
    "MethodCDUpdateMethodTypeId",
    "MethodCPT",
    "MethodCPTCreate",
    "MethodCPTCreateMethodTypeId",
    "MethodCPTData",
    "MethodCPTDataCreate",
    "MethodCPTDataCreateMethodTypeId",
    "MethodCPTDataMethodTypeId",
    "MethodCPTDataUpdate",
    "MethodCPTDataUpdateMethodTypeId",
    "MethodCPTMethodTypeId",
    "MethodCPTUpdate",
    "MethodCPTUpdateMethodTypeId",
    "MethodDP",
    "MethodDPCreate",
    "MethodDPCreateMethodTypeId",
    "MethodDPData",
    "MethodDPDataCreate",
    "MethodDPDataCreateMethodTypeId",
    "MethodDPDataMethodTypeId",
    "MethodDPMethodTypeId",
    "MethodDPUpdate",
    "MethodDPUpdateMethodTypeId",
    "MethodDT",
    "MethodDTCreate",
    "MethodDTCreateMethodTypeId",
    "MethodDTData",
    "MethodDTDataCreate",
    "MethodDTDataCreateMethodTypeId",
    "MethodDTDataMethodTypeId",
    "MethodDTDataUpdate",
    "MethodDTDataUpdateMethodTypeId",
    "MethodDTMethodTypeId",
    "MethodDTUpdate",
    "MethodDTUpdateMethodTypeId",
    "MethodESA",
    "MethodESACreate",
    "MethodESACreateMethodTypeId",
    "MethodESAMethodTypeId",
    "MethodESAUpdate",
    "MethodESAUpdateMethodTypeId",
    "MethodExportType",
    "MethodINC",
    "MethodINCCreate",
    "MethodINCCreateMethodTypeId",
    "MethodINCMethodTypeId",
    "MethodINCUpdate",
    "MethodINCUpdateMethodTypeId",
    "MethodInfo",
    "MethodIW",
    "MethodIWCreate",
    "MethodIWCreateMethodTypeId",
    "MethodIWMethodTypeId",
    "MethodIWUpdate",
    "MethodIWUpdateMethodTypeId",
    "MethodMin",
    "MethodOTHER",
    "MethodOTHERCreate",
    "MethodOTHERCreateMethodTypeId",
    "MethodOTHERMethodTypeId",
    "MethodOTHERUpdate",
    "MethodOTHERUpdateMethodTypeId",
    "MethodPT",
    "MethodPTCreate",
    "MethodPTCreateMethodTypeId",
    "MethodPTMethodTypeId",
    "MethodPTUpdate",
    "MethodPTUpdateMethodTypeId",
    "MethodPZ",
    "MethodPZCreate",
    "MethodPZCreateMethodTypeId",
    "MethodPZData",
    "MethodPZDataCreate",
    "MethodPZDataCreateMethodTypeId",
    "MethodPZDataMethodTypeId",
    "MethodPZDataUpdate",
    "MethodPZDataUpdateMethodTypeId",
    "MethodPZMethodTypeId",
    "MethodPZUpdate",
    "MethodPZUpdateMethodTypeId",
    "MethodRCD",
    "MethodRCDCreate",
    "MethodRCDCreateMethodTypeId",
    "MethodRCDData",
    "MethodRCDDataCreate",
    "MethodRCDDataCreateMethodTypeId",
    "MethodRCDDataMethodTypeId",
    "MethodRCDDataUpdate",
    "MethodRCDDataUpdateMethodTypeId",
    "MethodRCDMethodTypeId",
    "MethodRCDUpdate",
    "MethodRCDUpdateMethodTypeId",
    "MethodRO",
    "MethodROCreate",
    "MethodROCreateMethodTypeId",
    "MethodROMethodTypeId",
    "MethodROUpdate",
    "MethodROUpdateMethodTypeId",
    "MethodRP",
    "MethodRPCreate",
    "MethodRPCreateMethodTypeId",
    "MethodRPData",
    "MethodRPDataCreate",
    "MethodRPDataCreateMethodTypeId",
    "MethodRPDataMethodTypeId",
    "MethodRPDataUpdate",
    "MethodRPDataUpdateMethodTypeId",
    "MethodRPMethodTypeId",
    "MethodRPUpdate",
    "MethodRPUpdateMethodTypeId",
    "MethodRS",
    "MethodRSCreate",
    "MethodRSCreateMethodTypeId",
    "MethodRSMethodTypeId",
    "MethodRSUpdate",
    "MethodRSUpdateMethodTypeId",
    "MethodRWS",
    "MethodRWSCreate",
    "MethodRWSCreateMethodTypeId",
    "MethodRWSMethodTypeId",
    "MethodRWSUpdate",
    "MethodRWSUpdateMethodTypeId",
    "MethodSA",
    "MethodSACreate",
    "MethodSACreateMethodTypeId",
    "MethodSAMethodTypeId",
    "MethodSAUpdate",
    "MethodSAUpdateMethodTypeId",
    "MethodSPT",
    "MethodSPTCreate",
    "MethodSPTCreateMethodTypeId",
    "MethodSPTMethodTypeId",
    "MethodSPTUpdate",
    "MethodSPTUpdateMethodTypeId",
    "MethodSR",
    "MethodSRCreate",
    "MethodSRCreateMethodTypeId",
    "MethodSRMethodTypeId",
    "MethodSRS",
    "MethodSRSCreate",
    "MethodSRSCreateMethodTypeId",
    "MethodSRSData",
    "MethodSRSDataCreate",
    "MethodSRSDataCreateMethodTypeId",
    "MethodSRSDataMethodTypeId",
    "MethodSRSDataUpdate",
    "MethodSRSDataUpdateMethodTypeId",
    "MethodSRSMethodTypeId",
    "MethodSRSUpdate",
    "MethodSRSUpdateMethodTypeId",
    "MethodSRUpdate",
    "MethodSRUpdateMethodTypeId",
    "MethodSS",
    "MethodSSCreate",
    "MethodSSCreateMethodTypeId",
    "MethodSSData",
    "MethodSSDataCreate",
    "MethodSSDataCreateMethodTypeId",
    "MethodSSDataMethodTypeId",
    "MethodSSDataUpdate",
    "MethodSSDataUpdateMethodTypeId",
    "MethodSSMethodTypeId",
    "MethodSSUpdate",
    "MethodSSUpdateMethodTypeId",
    "MethodStatusEnum",
    "MethodSummary",
    "MethodSVT",
    "MethodSVTCreate",
    "MethodSVTCreateMethodTypeId",
    "MethodSVTData",
    "MethodSVTDataCreate",
    "MethodSVTDataCreateMethodTypeId",
    "MethodSVTDataMethodTypeId",
    "MethodSVTDataUpdate",
    "MethodSVTDataUpdateMethodTypeId",
    "MethodSVTMethodTypeId",
    "MethodSVTUpdate",
    "MethodSVTUpdateMethodTypeId",
    "MethodTOT",
    "MethodTOTCreate",
    "MethodTOTCreateMethodTypeId",
    "MethodTOTData",
    "MethodTOTDataCreate",
    "MethodTOTDataCreateMethodTypeId",
    "MethodTOTDataMethodTypeId",
    "MethodTOTDataUpdate",
    "MethodTOTDataUpdateMethodTypeId",
    "MethodTOTMethodTypeId",
    "MethodTOTUpdate",
    "MethodTOTUpdateMethodTypeId",
    "MethodTP",
    "MethodTPCreate",
    "MethodTPCreateMethodTypeId",
    "MethodTPMethodTypeId",
    "MethodTPUpdate",
    "MethodTPUpdateMethodTypeId",
    "MethodType",
    "MethodTypeEnum",
    "MethodTypeEnumStr",
    "MethodWST",
    "MethodWSTCreate",
    "MethodWSTCreateMethodTypeId",
    "MethodWSTData",
    "MethodWSTDataCreate",
    "MethodWSTDataCreateMethodTypeId",
    "MethodWSTDataMethodTypeId",
    "MethodWSTDataUpdate",
    "MethodWSTDataUpdateMethodTypeId",
    "MethodWSTMethodTypeId",
    "MethodWSTUpdate",
    "MethodWSTUpdateMethodTypeId",
    "Operation",
    "Options",
    "Organization",
    "OrganizationCreate",
    "OrganizationInformation",
    "OrganizationMin",
    "OrganizationUpdate",
    "Orientation",
    "PageNumberPrefixByMethod",
    "PageNumberStartPerMethod",
    "PaperSize",
    "PdfOptions",
    "PdfOptionsDateFormat",
    "PdfOptionsLang",
    "PdfOptionsPaperSize",
    "PdfOptionsSortFiguresBy",
    "PDFPageInfo",
    "PiezometerModel",
    "PiezometerModelCreate",
    "PiezometerModelUpdate",
    "PiezometerType",
    "PiezometerVendor",
    "PizeometerUnits",
    "PlotDataStats",
    "PlotDataStatsPercentiles",
    "PlotFormat",
    "PlotInfoObject",
    "PlotInfoObjectStatsType0",
    "PlotSequence",
    "PlotSequenceOptions",
    "PlotType",
    "Project",
    "ProjectCreate",
    "ProjectInfo",
    "ProjectLocationMethodTypes",
    "ProjectSearch",
    "ProjectSummary",
    "ProjectUpdate",
    "ReadingType",
    "Role",
    "RoleEntityEnum",
    "RoleEnum",
    "SampleContainerType",
    "SampleMaterial",
    "SamplerType",
    "SamplingTechnique",
    "Scales",
    "ScalingMode",
    "SoundingClass",
    "Standard",
    "StandardType",
    "TransformationType",
    "User",
    "ValidationError",
)
