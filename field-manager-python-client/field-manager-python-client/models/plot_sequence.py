from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import cast, List
from typing import Dict
from typing import Union

if TYPE_CHECKING:
  from ..models.plot_info_object import PlotInfoObject
  from ..models.plot_sequence_options import PlotSequenceOptions





T = TypeVar("T", bound="PlotSequence")


@_attrs_define
class PlotSequence:
    """ 
        Attributes:
            sequence (List['PlotInfoObject']):
            options (Union[Unset, PlotSequenceOptions]):
     """

    sequence: List['PlotInfoObject']
    options: Union[Unset, 'PlotSequenceOptions'] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.plot_info_object import PlotInfoObject
        from ..models.plot_sequence_options import PlotSequenceOptions
        sequence = []
        for sequence_item_data in self.sequence:
            sequence_item = sequence_item_data.to_dict()
            sequence.append(sequence_item)



        options: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "sequence": sequence,
        })
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.plot_info_object import PlotInfoObject
        from ..models.plot_sequence_options import PlotSequenceOptions
        d = src_dict.copy()
        sequence = []
        _sequence = d.pop("sequence")
        for sequence_item_data in (_sequence):
            sequence_item = PlotInfoObject.from_dict(sequence_item_data)



            sequence.append(sequence_item)


        _options = d.pop("options", UNSET)
        options: Union[Unset, PlotSequenceOptions]
        if isinstance(_options,  Unset):
            options = UNSET
        else:
            options = PlotSequenceOptions.from_dict(_options)




        plot_sequence = cls(
            sequence=sequence,
            options=options,
        )


        plot_sequence.additional_properties = d
        return plot_sequence

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
