import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.file_type import FileType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.location_min import LocationMin
    from ..models.method_min import MethodMin


T = TypeVar("T", bound="FileExtended")


@_attrs_define
class FileExtended:
    """
    Attributes:
        file_id (UUID):
        name (str):
        blob_url (str):
        original_filename (str):
        file_type (FileType):
        mime_type (str):
        created_at (datetime.datetime):
        comment (Union[None, Unset, str]):
        size (Union[None, Unset, int]):
        created_by (Union[None, Unset, str]):
        image_size_width (Union[None, Unset, int]):
        image_size_height (Union[None, Unset, int]):
        image_taken (Union[None, Unset, datetime.datetime]):
        image_point_latitude (Union[None, Unset, float]):
        image_point_longitude (Union[None, Unset, float]):
        image_point_z (Union[None, Unset, float]):
        locations (Union[Unset, list['LocationMin']]):
        methods (Union[Unset, list['MethodMin']]):
    """

    file_id: UUID
    name: str
    blob_url: str
    original_filename: str
    file_type: FileType
    mime_type: str
    created_at: datetime.datetime
    comment: Union[None, Unset, str] = UNSET
    size: Union[None, Unset, int] = UNSET
    created_by: Union[None, Unset, str] = UNSET
    image_size_width: Union[None, Unset, int] = UNSET
    image_size_height: Union[None, Unset, int] = UNSET
    image_taken: Union[None, Unset, datetime.datetime] = UNSET
    image_point_latitude: Union[None, Unset, float] = UNSET
    image_point_longitude: Union[None, Unset, float] = UNSET
    image_point_z: Union[None, Unset, float] = UNSET
    locations: Union[Unset, list["LocationMin"]] = UNSET
    methods: Union[Unset, list["MethodMin"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_id = str(self.file_id)

        name = self.name

        blob_url = self.blob_url

        original_filename = self.original_filename

        file_type = self.file_type.value

        mime_type = self.mime_type

        created_at = self.created_at.isoformat()

        comment: Union[None, Unset, str]
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

        size: Union[None, Unset, int]
        if isinstance(self.size, Unset):
            size = UNSET
        else:
            size = self.size

        created_by: Union[None, Unset, str]
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        else:
            created_by = self.created_by

        image_size_width: Union[None, Unset, int]
        if isinstance(self.image_size_width, Unset):
            image_size_width = UNSET
        else:
            image_size_width = self.image_size_width

        image_size_height: Union[None, Unset, int]
        if isinstance(self.image_size_height, Unset):
            image_size_height = UNSET
        else:
            image_size_height = self.image_size_height

        image_taken: Union[None, Unset, str]
        if isinstance(self.image_taken, Unset):
            image_taken = UNSET
        elif isinstance(self.image_taken, datetime.datetime):
            image_taken = self.image_taken.isoformat()
        else:
            image_taken = self.image_taken

        image_point_latitude: Union[None, Unset, float]
        if isinstance(self.image_point_latitude, Unset):
            image_point_latitude = UNSET
        else:
            image_point_latitude = self.image_point_latitude

        image_point_longitude: Union[None, Unset, float]
        if isinstance(self.image_point_longitude, Unset):
            image_point_longitude = UNSET
        else:
            image_point_longitude = self.image_point_longitude

        image_point_z: Union[None, Unset, float]
        if isinstance(self.image_point_z, Unset):
            image_point_z = UNSET
        else:
            image_point_z = self.image_point_z

        locations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.locations, Unset):
            locations = []
            for locations_item_data in self.locations:
                locations_item = locations_item_data.to_dict()
                locations.append(locations_item)

        methods: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.methods, Unset):
            methods = []
            for methods_item_data in self.methods:
                methods_item = methods_item_data.to_dict()
                methods.append(methods_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file_id": file_id,
                "name": name,
                "blob_url": blob_url,
                "original_filename": original_filename,
                "file_type": file_type,
                "mime_type": mime_type,
                "created_at": created_at,
            }
        )
        if comment is not UNSET:
            field_dict["comment"] = comment
        if size is not UNSET:
            field_dict["size"] = size
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if image_size_width is not UNSET:
            field_dict["image_size_width"] = image_size_width
        if image_size_height is not UNSET:
            field_dict["image_size_height"] = image_size_height
        if image_taken is not UNSET:
            field_dict["image_taken"] = image_taken
        if image_point_latitude is not UNSET:
            field_dict["image_point_latitude"] = image_point_latitude
        if image_point_longitude is not UNSET:
            field_dict["image_point_longitude"] = image_point_longitude
        if image_point_z is not UNSET:
            field_dict["image_point_z"] = image_point_z
        if locations is not UNSET:
            field_dict["locations"] = locations
        if methods is not UNSET:
            field_dict["methods"] = methods

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.location_min import LocationMin
        from ..models.method_min import MethodMin

        d = dict(src_dict)
        file_id = UUID(d.pop("file_id"))

        name = d.pop("name")

        blob_url = d.pop("blob_url")

        original_filename = d.pop("original_filename")

        file_type = FileType(d.pop("file_type"))

        mime_type = d.pop("mime_type")

        created_at = isoparse(d.pop("created_at"))

        def _parse_comment(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        comment = _parse_comment(d.pop("comment", UNSET))

        def _parse_size(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        size = _parse_size(d.pop("size", UNSET))

        def _parse_created_by(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        created_by = _parse_created_by(d.pop("created_by", UNSET))

        def _parse_image_size_width(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        image_size_width = _parse_image_size_width(d.pop("image_size_width", UNSET))

        def _parse_image_size_height(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        image_size_height = _parse_image_size_height(d.pop("image_size_height", UNSET))

        def _parse_image_taken(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                image_taken_type_0 = isoparse(data)

                return image_taken_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        image_taken = _parse_image_taken(d.pop("image_taken", UNSET))

        def _parse_image_point_latitude(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        image_point_latitude = _parse_image_point_latitude(d.pop("image_point_latitude", UNSET))

        def _parse_image_point_longitude(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        image_point_longitude = _parse_image_point_longitude(d.pop("image_point_longitude", UNSET))

        def _parse_image_point_z(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        image_point_z = _parse_image_point_z(d.pop("image_point_z", UNSET))

        locations = []
        _locations = d.pop("locations", UNSET)
        for locations_item_data in _locations or []:
            locations_item = LocationMin.from_dict(locations_item_data)

            locations.append(locations_item)

        methods = []
        _methods = d.pop("methods", UNSET)
        for methods_item_data in _methods or []:
            methods_item = MethodMin.from_dict(methods_item_data)

            methods.append(methods_item)

        file_extended = cls(
            file_id=file_id,
            name=name,
            blob_url=blob_url,
            original_filename=original_filename,
            file_type=file_type,
            mime_type=mime_type,
            created_at=created_at,
            comment=comment,
            size=size,
            created_by=created_by,
            image_size_width=image_size_width,
            image_size_height=image_size_height,
            image_taken=image_taken,
            image_point_latitude=image_point_latitude,
            image_point_longitude=image_point_longitude,
            image_point_z=image_point_z,
            locations=locations,
            methods=methods,
        )

        file_extended.additional_properties = d
        return file_extended

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
