from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.file_type import FileType
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import cast, List
from typing import cast, Union
from typing import Dict
from typing import Union
from uuid import UUID
import datetime

if TYPE_CHECKING:
  from ..models.bff_method import BFFMethod
  from ..models.bff_location import BFFLocation





T = TypeVar("T", bound="BFFFile")


@_attrs_define
class BFFFile:
    """ 
        Attributes:
            file_id (UUID):
            name (str):
            file_type (FileType):
            created_at (datetime.datetime):
            comment (Union[None, Unset, str]):
            size (Union[None, Unset, int]):
            created_by (Union[None, Unset, str]):
            locations (Union[Unset, List['BFFLocation']]):
            methods (Union[Unset, List['BFFMethod']]):
     """

    file_id: UUID
    name: str
    file_type: FileType
    created_at: datetime.datetime
    comment: Union[None, Unset, str] = UNSET
    size: Union[None, Unset, int] = UNSET
    created_by: Union[None, Unset, str] = UNSET
    locations: Union[Unset, List['BFFLocation']] = UNSET
    methods: Union[Unset, List['BFFMethod']] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.bff_method import BFFMethod
        from ..models.bff_location import BFFLocation
        file_id = str(self.file_id)

        name = self.name

        file_type = self.file_type.value

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

        locations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.locations, Unset):
            locations = []
            for locations_item_data in self.locations:
                locations_item = locations_item_data.to_dict()
                locations.append(locations_item)



        methods: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.methods, Unset):
            methods = []
            for methods_item_data in self.methods:
                methods_item = methods_item_data.to_dict()
                methods.append(methods_item)




        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "file_id": file_id,
            "name": name,
            "file_type": file_type,
            "created_at": created_at,
        })
        if comment is not UNSET:
            field_dict["comment"] = comment
        if size is not UNSET:
            field_dict["size"] = size
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if locations is not UNSET:
            field_dict["locations"] = locations
        if methods is not UNSET:
            field_dict["methods"] = methods

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.bff_method import BFFMethod
        from ..models.bff_location import BFFLocation
        d = src_dict.copy()
        file_id = UUID(d.pop("file_id"))




        name = d.pop("name")

        file_type = FileType(d.pop("file_type"))




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


        locations = []
        _locations = d.pop("locations", UNSET)
        for locations_item_data in (_locations or []):
            locations_item = BFFLocation.from_dict(locations_item_data)



            locations.append(locations_item)


        methods = []
        _methods = d.pop("methods", UNSET)
        for methods_item_data in (_methods or []):
            methods_item = BFFMethod.from_dict(methods_item_data)



            methods.append(methods_item)


        bff_file = cls(
            file_id=file_id,
            name=name,
            file_type=file_type,
            created_at=created_at,
            comment=comment,
            size=size,
            created_by=created_by,
            locations=locations,
            methods=methods,
        )


        bff_file.additional_properties = d
        return bff_file

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
