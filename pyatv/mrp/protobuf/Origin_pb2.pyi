# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from pyatv.mrp.protobuf.DeviceInfoMessage_pb2 import (
    DeviceInfoMessage as pyatv___mrp___protobuf___DeviceInfoMessage_pb2___DeviceInfoMessage,
)

from typing import (
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class Origin(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    type = ... # type: int
    displayName = ... # type: typing___Text
    identifier = ... # type: int

    @property
    def deviceInfo(self) -> pyatv___mrp___protobuf___DeviceInfoMessage_pb2___DeviceInfoMessage: ...

    def __init__(self,
        *,
        type : typing___Optional[int] = None,
        displayName : typing___Optional[typing___Text] = None,
        identifier : typing___Optional[int] = None,
        deviceInfo : typing___Optional[pyatv___mrp___protobuf___DeviceInfoMessage_pb2___DeviceInfoMessage] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> Origin: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"deviceInfo",u"displayName",u"identifier",u"type"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"deviceInfo",u"displayName",u"identifier",u"type"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"deviceInfo",b"deviceInfo",u"displayName",b"displayName",u"identifier",b"identifier",u"type",b"type"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"deviceInfo",b"deviceInfo",u"displayName",b"displayName",u"identifier",b"identifier",u"type",b"type"]) -> None: ...