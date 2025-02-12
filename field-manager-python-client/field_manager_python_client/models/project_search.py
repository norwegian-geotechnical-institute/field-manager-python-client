from typing import Any, Dict, List, Type, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectSearch")


@_attrs_define
class ProjectSearch:
    """
    Attributes:
        project_ids (Union[List[UUID], None, Unset]):
    """

    project_ids: Union[List[UUID], None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        project_ids: Union[List[str], None, Unset]
        if isinstance(self.project_ids, Unset):
            project_ids = UNSET
        elif isinstance(self.project_ids, list):
            project_ids = []
            for project_ids_type_0_item_data in self.project_ids:
                project_ids_type_0_item = str(project_ids_type_0_item_data)
                project_ids.append(project_ids_type_0_item)

        else:
            project_ids = self.project_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if project_ids is not UNSET:
            field_dict["project_ids"] = project_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_project_ids(data: object) -> Union[List[UUID], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                project_ids_type_0 = []
                _project_ids_type_0 = data
                for project_ids_type_0_item_data in _project_ids_type_0:
                    project_ids_type_0_item = UUID(project_ids_type_0_item_data)

                    project_ids_type_0.append(project_ids_type_0_item)

                return project_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[UUID], None, Unset], data)

        project_ids = _parse_project_ids(d.pop("project_ids", UNSET))

        project_search = cls(
            project_ids=project_ids,
        )

        project_search.additional_properties = d
        return project_search

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
