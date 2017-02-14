# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: get_updates_caller_info.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='get_updates_caller_info.proto',
  package='sync_pb',
  syntax='proto2',
  serialized_pb=_b('\n\x1dget_updates_caller_info.proto\x12\x07sync_pb\"\xf6\x02\n\x14GetUpdatesCallerInfo\x12>\n\x06source\x18\x01 \x02(\x0e\x32..sync_pb.GetUpdatesCallerInfo.GetUpdatesSource\x12\x1d\n\x15notifications_enabled\x18\x02 \x01(\x08\"\xfe\x01\n\x10GetUpdatesSource\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x10\n\x0c\x46IRST_UPDATE\x10\x01\x12\t\n\x05LOCAL\x10\x02\x12\x10\n\x0cNOTIFICATION\x10\x03\x12\x0c\n\x08PERIODIC\x10\x04\x12\x1b\n\x17SYNC_CYCLE_CONTINUATION\x10\x05\x12\x1c\n\x18NEWLY_SUPPORTED_DATATYPE\x10\x07\x12\r\n\tMIGRATION\x10\x08\x12\x0e\n\nNEW_CLIENT\x10\t\x12\x13\n\x0fRECONFIGURATION\x10\n\x12\x14\n\x10\x44\x41TATYPE_REFRESH\x10\x0b\x12\t\n\x05RETRY\x10\r\x12\x10\n\x0cPROGRAMMATIC\x10\x0e\x42\x02H\x03')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_GETUPDATESCALLERINFO_GETUPDATESSOURCE = _descriptor.EnumDescriptor(
  name='GetUpdatesSource',
  full_name='sync_pb.GetUpdatesCallerInfo.GetUpdatesSource',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FIRST_UPDATE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOCAL', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOTIFICATION', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PERIODIC', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYNC_CYCLE_CONTINUATION', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NEWLY_SUPPORTED_DATATYPE', index=6, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MIGRATION', index=7, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NEW_CLIENT', index=8, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RECONFIGURATION', index=9, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DATATYPE_REFRESH', index=10, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RETRY', index=11, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROGRAMMATIC', index=12, number=14,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=163,
  serialized_end=417,
)
_sym_db.RegisterEnumDescriptor(_GETUPDATESCALLERINFO_GETUPDATESSOURCE)


_GETUPDATESCALLERINFO = _descriptor.Descriptor(
  name='GetUpdatesCallerInfo',
  full_name='sync_pb.GetUpdatesCallerInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='source', full_name='sync_pb.GetUpdatesCallerInfo.source', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='notifications_enabled', full_name='sync_pb.GetUpdatesCallerInfo.notifications_enabled', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GETUPDATESCALLERINFO_GETUPDATESSOURCE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=43,
  serialized_end=417,
)

_GETUPDATESCALLERINFO.fields_by_name['source'].enum_type = _GETUPDATESCALLERINFO_GETUPDATESSOURCE
_GETUPDATESCALLERINFO_GETUPDATESSOURCE.containing_type = _GETUPDATESCALLERINFO
DESCRIPTOR.message_types_by_name['GetUpdatesCallerInfo'] = _GETUPDATESCALLERINFO

GetUpdatesCallerInfo = _reflection.GeneratedProtocolMessageType('GetUpdatesCallerInfo', (_message.Message,), dict(
  DESCRIPTOR = _GETUPDATESCALLERINFO,
  __module__ = 'get_updates_caller_info_pb2'
  # @@protoc_insertion_point(class_scope:sync_pb.GetUpdatesCallerInfo)
  ))
_sym_db.RegisterMessage(GetUpdatesCallerInfo)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('H\003'))
# @@protoc_insertion_point(module_scope)
