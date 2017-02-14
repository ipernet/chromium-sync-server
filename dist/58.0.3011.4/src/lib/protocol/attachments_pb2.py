# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: attachments.proto

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
  name='attachments.proto',
  package='sync_pb',
  syntax='proto2',
  serialized_pb=_b('\n\x11\x61ttachments.proto\x12\x07sync_pb\"J\n\x11\x41ttachmentIdProto\x12\x11\n\tunique_id\x18\x01 \x01(\t\x12\x12\n\nsize_bytes\x18\x02 \x01(\x04\x12\x0e\n\x06\x63rc32c\x18\x03 \x01(\r\"X\n\x18\x41ttachmentMetadataRecord\x12&\n\x02id\x18\x01 \x01(\x0b\x32\x1a.sync_pb.AttachmentIdProto\x12\x14\n\x0cis_on_server\x18\x02 \x01(\x08\"G\n\x12\x41ttachmentMetadata\x12\x31\n\x06record\x18\x01 \x03(\x0b\x32!.sync_pb.AttachmentMetadataRecordB\x02H\x03')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ATTACHMENTIDPROTO = _descriptor.Descriptor(
  name='AttachmentIdProto',
  full_name='sync_pb.AttachmentIdProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unique_id', full_name='sync_pb.AttachmentIdProto.unique_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='size_bytes', full_name='sync_pb.AttachmentIdProto.size_bytes', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='crc32c', full_name='sync_pb.AttachmentIdProto.crc32c', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=30,
  serialized_end=104,
)


_ATTACHMENTMETADATARECORD = _descriptor.Descriptor(
  name='AttachmentMetadataRecord',
  full_name='sync_pb.AttachmentMetadataRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='sync_pb.AttachmentMetadataRecord.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_on_server', full_name='sync_pb.AttachmentMetadataRecord.is_on_server', index=1,
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
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=106,
  serialized_end=194,
)


_ATTACHMENTMETADATA = _descriptor.Descriptor(
  name='AttachmentMetadata',
  full_name='sync_pb.AttachmentMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='record', full_name='sync_pb.AttachmentMetadata.record', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=196,
  serialized_end=267,
)

_ATTACHMENTMETADATARECORD.fields_by_name['id'].message_type = _ATTACHMENTIDPROTO
_ATTACHMENTMETADATA.fields_by_name['record'].message_type = _ATTACHMENTMETADATARECORD
DESCRIPTOR.message_types_by_name['AttachmentIdProto'] = _ATTACHMENTIDPROTO
DESCRIPTOR.message_types_by_name['AttachmentMetadataRecord'] = _ATTACHMENTMETADATARECORD
DESCRIPTOR.message_types_by_name['AttachmentMetadata'] = _ATTACHMENTMETADATA

AttachmentIdProto = _reflection.GeneratedProtocolMessageType('AttachmentIdProto', (_message.Message,), dict(
  DESCRIPTOR = _ATTACHMENTIDPROTO,
  __module__ = 'attachments_pb2'
  # @@protoc_insertion_point(class_scope:sync_pb.AttachmentIdProto)
  ))
_sym_db.RegisterMessage(AttachmentIdProto)

AttachmentMetadataRecord = _reflection.GeneratedProtocolMessageType('AttachmentMetadataRecord', (_message.Message,), dict(
  DESCRIPTOR = _ATTACHMENTMETADATARECORD,
  __module__ = 'attachments_pb2'
  # @@protoc_insertion_point(class_scope:sync_pb.AttachmentMetadataRecord)
  ))
_sym_db.RegisterMessage(AttachmentMetadataRecord)

AttachmentMetadata = _reflection.GeneratedProtocolMessageType('AttachmentMetadata', (_message.Message,), dict(
  DESCRIPTOR = _ATTACHMENTMETADATA,
  __module__ = 'attachments_pb2'
  # @@protoc_insertion_point(class_scope:sync_pb.AttachmentMetadata)
  ))
_sym_db.RegisterMessage(AttachmentMetadata)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('H\003'))
# @@protoc_insertion_point(module_scope)
