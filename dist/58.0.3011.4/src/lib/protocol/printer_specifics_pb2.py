# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: printer_specifics.proto

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
  name='printer_specifics.proto',
  package='sync_pb',
  syntax='proto2',
  serialized_pb=_b('\n\x17printer_specifics.proto\x12\x07sync_pb\"\x97\x01\n\x13PrinterPPDReference\x12\x1d\n\x15user_supplied_ppd_url\x18\x01 \x01(\t\x12\"\n\x16\x65\x66\x66\x65\x63tive_manufacturer\x18\x02 \x01(\tB\x02\x18\x01\x12\x1b\n\x0f\x65\x66\x66\x65\x63tive_model\x18\x03 \x01(\tB\x02\x18\x01\x12 \n\x18\x65\x66\x66\x65\x63tive_make_and_model\x18\x04 \x01(\t\"\xea\x01\n\x10PrinterSpecifics\x12\n\n\x02id\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x14\n\x0cmanufacturer\x18\x04 \x01(\t\x12\r\n\x05model\x18\x05 \x01(\t\x12\x0b\n\x03uri\x18\x06 \x01(\t\x12\x0c\n\x04uuid\x18\x07 \x01(\t\x12\x0f\n\x03ppd\x18\x08 \x01(\x0c\x42\x02\x18\x01\x12\x33\n\rppd_reference\x18\t \x01(\x0b\x32\x1c.sync_pb.PrinterPPDReference\x12\x19\n\x11updated_timestamp\x18\n \x01(\x03\x42\x02H\x03')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PRINTERPPDREFERENCE = _descriptor.Descriptor(
  name='PrinterPPDReference',
  full_name='sync_pb.PrinterPPDReference',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_supplied_ppd_url', full_name='sync_pb.PrinterPPDReference.user_supplied_ppd_url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='effective_manufacturer', full_name='sync_pb.PrinterPPDReference.effective_manufacturer', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001'))),
    _descriptor.FieldDescriptor(
      name='effective_model', full_name='sync_pb.PrinterPPDReference.effective_model', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001'))),
    _descriptor.FieldDescriptor(
      name='effective_make_and_model', full_name='sync_pb.PrinterPPDReference.effective_make_and_model', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=37,
  serialized_end=188,
)


_PRINTERSPECIFICS = _descriptor.Descriptor(
  name='PrinterSpecifics',
  full_name='sync_pb.PrinterSpecifics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='sync_pb.PrinterSpecifics.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='display_name', full_name='sync_pb.PrinterSpecifics.display_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='sync_pb.PrinterSpecifics.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='manufacturer', full_name='sync_pb.PrinterSpecifics.manufacturer', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='model', full_name='sync_pb.PrinterSpecifics.model', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uri', full_name='sync_pb.PrinterSpecifics.uri', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uuid', full_name='sync_pb.PrinterSpecifics.uuid', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ppd', full_name='sync_pb.PrinterSpecifics.ppd', index=7,
      number=8, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001'))),
    _descriptor.FieldDescriptor(
      name='ppd_reference', full_name='sync_pb.PrinterSpecifics.ppd_reference', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='updated_timestamp', full_name='sync_pb.PrinterSpecifics.updated_timestamp', index=9,
      number=10, type=3, cpp_type=2, label=1,
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
  serialized_start=191,
  serialized_end=425,
)

_PRINTERSPECIFICS.fields_by_name['ppd_reference'].message_type = _PRINTERPPDREFERENCE
DESCRIPTOR.message_types_by_name['PrinterPPDReference'] = _PRINTERPPDREFERENCE
DESCRIPTOR.message_types_by_name['PrinterSpecifics'] = _PRINTERSPECIFICS

PrinterPPDReference = _reflection.GeneratedProtocolMessageType('PrinterPPDReference', (_message.Message,), dict(
  DESCRIPTOR = _PRINTERPPDREFERENCE,
  __module__ = 'printer_specifics_pb2'
  # @@protoc_insertion_point(class_scope:sync_pb.PrinterPPDReference)
  ))
_sym_db.RegisterMessage(PrinterPPDReference)

PrinterSpecifics = _reflection.GeneratedProtocolMessageType('PrinterSpecifics', (_message.Message,), dict(
  DESCRIPTOR = _PRINTERSPECIFICS,
  __module__ = 'printer_specifics_pb2'
  # @@protoc_insertion_point(class_scope:sync_pb.PrinterSpecifics)
  ))
_sym_db.RegisterMessage(PrinterSpecifics)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('H\003'))
_PRINTERPPDREFERENCE.fields_by_name['effective_manufacturer'].has_options = True
_PRINTERPPDREFERENCE.fields_by_name['effective_manufacturer']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001'))
_PRINTERPPDREFERENCE.fields_by_name['effective_model'].has_options = True
_PRINTERPPDREFERENCE.fields_by_name['effective_model']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001'))
_PRINTERSPECIFICS.fields_by_name['ppd'].has_options = True
_PRINTERSPECIFICS.fields_by_name['ppd']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001'))
# @@protoc_insertion_point(module_scope)
