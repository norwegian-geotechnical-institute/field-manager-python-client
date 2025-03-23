from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bedrock_type import BedrockType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BedrockInfo")


@_attrs_define
class BedrockInfo:
    """
    Attributes:
        depth (Union[None, Unset, float]):
        bedrock_type (Union[BedrockType, None, Unset]):
    """

    depth: Union[None, Unset, float] = UNSET
    bedrock_type: Union[BedrockType, None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        depth: Union[None, Unset, float]
        if isinstance(self.depth, Unset):
            depth = UNSET
        else:
            depth = self.depth

        bedrock_type: Union[None, Unset, str]
        if isinstance(self.bedrock_type, Unset):
            bedrock_type = UNSET
        elif isinstance(self.bedrock_type, BedrockType):
            bedrock_type = self.bedrock_type.value
        else:
            bedrock_type = self.bedrock_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if depth is not UNSET:
            field_dict["depth"] = depth
        if bedrock_type is not UNSET:
            field_dict["bedrock_type"] = bedrock_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_depth(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        depth = _parse_depth(d.pop("depth", UNSET))

        def _parse_bedrock_type(data: object) -> Union[BedrockType, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                bedrock_type_type_0 = BedrockType(data)

                return bedrock_type_type_0
            except:  # noqa: E722
                pass
            return cast(Union[BedrockType, None, Unset], data)

        bedrock_type = _parse_bedrock_type(d.pop("bedrock_type", UNSET))

        bedrock_info = cls(
            depth=depth,
            bedrock_type=bedrock_type,
        )

        bedrock_info.additional_properties = d
        return bedrock_info

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
