# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nigori_specifics.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import encryption_pb2 as encryption__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='nigori_specifics.proto',
  package='sync_pb',
  syntax='proto2',
  serialized_pb=_b('\n\x16nigori_specifics.proto\x12\x07sync_pb\x1a\x10\x65ncryption.proto\"T\n\tNigoriKey\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08user_key\x18\x02 \x01(\x0c\x12\x16\n\x0e\x65ncryption_key\x18\x03 \x01(\x0c\x12\x0f\n\x07mac_key\x18\x04 \x01(\x0c\"/\n\x0cNigoriKeyBag\x12\x1f\n\x03key\x18\x02 \x03(\x0b\x32\x12.sync_pb.NigoriKey\"\xb3\t\n\x0fNigoriSpecifics\x12\x31\n\x11\x65ncryption_keybag\x18\x01 \x01(\x0b\x32\x16.sync_pb.EncryptedData\x12\x18\n\x10keybag_is_frozen\x18\x02 \x01(\x08\x12\x19\n\x11\x65ncrypt_bookmarks\x18\r \x01(\x08\x12\x1b\n\x13\x65ncrypt_preferences\x18\x0e \x01(\x08\x12 \n\x18\x65ncrypt_autofill_profile\x18\x0f \x01(\x08\x12\x18\n\x10\x65ncrypt_autofill\x18\x10 \x01(\x08\x12\x16\n\x0e\x65ncrypt_themes\x18\x11 \x01(\x08\x12\x1a\n\x12\x65ncrypt_typed_urls\x18\x12 \x01(\x08\x12\x1a\n\x12\x65ncrypt_extensions\x18\x13 \x01(\x08\x12\x18\n\x10\x65ncrypt_sessions\x18\x14 \x01(\x08\x12\x14\n\x0c\x65ncrypt_apps\x18\x15 \x01(\x08\x12\x1e\n\x16\x65ncrypt_search_engines\x18\x16 \x01(\x08\x12\x1a\n\x12\x65ncrypt_everything\x18\x18 \x01(\x08\x12\"\n\x1a\x65ncrypt_extension_settings\x18\x19 \x01(\x08\x12!\n\x19\x65ncrypt_app_notifications\x18\x1a \x01(\x08\x12\x1c\n\x14\x65ncrypt_app_settings\x18\x1b \x01(\x08\x12\x19\n\x11sync_tab_favicons\x18\x1d \x01(\x08\x12U\n\x0fpassphrase_type\x18\x1e \x01(\x0e\x32\'.sync_pb.NigoriSpecifics.PassphraseType:\x13IMPLICIT_PASSPHRASE\x12\x38\n\x18keystore_decryptor_token\x18\x1f \x01(\x0b\x32\x16.sync_pb.EncryptedData\x12\x1f\n\x17keystore_migration_time\x18  \x01(\x03\x12\x1e\n\x16\x63ustom_passphrase_time\x18! \x01(\x03\x12\x1a\n\x12\x65ncrypt_dictionary\x18\" \x01(\x08\x12\x1e\n\x16\x65ncrypt_favicon_images\x18# \x01(\x08\x12 \n\x18\x65ncrypt_favicon_tracking\x18$ \x01(\x08\x12\x18\n\x10\x65ncrypt_articles\x18% \x01(\x08\x12\x18\n\x10\x65ncrypt_app_list\x18& \x01(\x08\x12(\n encrypt_autofill_wallet_metadata\x18\' \x01(\x08\x12\x37\n/server_only_was_missing_keystore_migration_time\x18( \x01(\x08\x12\x1b\n\x13\x65ncrypt_arc_package\x18) \x01(\x08\x12\x18\n\x10\x65ncrypt_printers\x18* \x01(\x08\x12\x1c\n\x14\x65ncrypt_reading_list\x18+ \x01(\x08\"\x86\x01\n\x0ePassphraseType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x17\n\x13IMPLICIT_PASSPHRASE\x10\x01\x12\x17\n\x13KEYSTORE_PASSPHRASE\x10\x02\x12\x1e\n\x1a\x46ROZEN_IMPLICIT_PASSPHRASE\x10\x03\x12\x15\n\x11\x43USTOM_PASSPHRASE\x10\x04\x42\x02H\x03')
  ,
  dependencies=[encryption__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_NIGORISPECIFICS_PASSPHRASETYPE = _descriptor.EnumDescriptor(
  name='PassphraseType',
  full_name='sync_pb.NigoriSpecifics.PassphraseType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IMPLICIT_PASSPHRASE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KEYSTORE_PASSPHRASE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FROZEN_IMPLICIT_PASSPHRASE', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CUSTOM_PASSPHRASE', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1258,
  serialized_end=1392,
)
_sym_db.RegisterEnumDescriptor(_NIGORISPECIFICS_PASSPHRASETYPE)


_NIGORIKEY = _descriptor.Descriptor(
  name='NigoriKey',
  full_name='sync_pb.NigoriKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='sync_pb.NigoriKey.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_key', full_name='sync_pb.NigoriKey.user_key', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='encryption_key', full_name='sync_pb.NigoriKey.encryption_key', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mac_key', full_name='sync_pb.NigoriKey.mac_key', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=53,
  serialized_end=137,
)


_NIGORIKEYBAG = _descriptor.Descriptor(
  name='NigoriKeyBag',
  full_name='sync_pb.NigoriKeyBag',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='sync_pb.NigoriKeyBag.key', index=0,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=139,
  serialized_end=186,
)


_NIGORISPECIFICS = _descriptor.Descriptor(
  name='NigoriSpecifics',
  full_name='sync_pb.NigoriSpecifics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='encryption_keybag', full_name='sync_pb.NigoriSpecifics.encryption_keybag', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='keybag_is_frozen', full_name='sync_pb.NigoriSpecifics.keybag_is_frozen', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='encrypt_bookmarks', full_name='sync_pb.NigoriSpecifics.encrypt_bookmarks', index=2,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='encrypt_preferences', full_name='sync_pb.NigoriSpecifics.encrypt_preferences', index=3,
      number=14, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='encrypt_autofill_profile', full_name='sync_pb.NigoriSpecifics.encrypt_autofill_profile', index=4,
      number=15, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='encrypt_autofill', full_name='sync_pb.NigoriSpecifics.encrypt_autofill', index=5,
      number=16, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='encrypt_themes', full_name='sync_pb.NigoriSpecifics.encrypt_themes', index=6,
      number=17, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='encrypt_typed_urls', full_name='sync_pb.NigoriSpecifics.encrypt_typed_urls', index=7,
      number=18, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='encrypt_extensions', full_name='sync_pb.NigoriSpecifics.encrypt_extensions', index=8,
      number=19, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='encrypt_sessions', full_name='sync_pb.NigoriSpecifics.encrypt_sessions', index=9,
      number=20, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='encrypt_apps', full_name='sync_pb.NigoriSpecifics.encrypt_apps', index=10,
      number=21, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='encrypt_search_engines', full_name='sync_pb.NigoriSpecifics.encrypt_search_engines', index=11,
      number=22, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='encrypt_everything', full_name='sync_pb.NigoriSpecifics.encrypt_everything', index=12,
      number=24, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='encrypt_extension_settings', full_name='sync_pb.NigoriSpecifics.encrypt_extension_settings', index=13,
      number=25, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='encrypt_app_notifications', full_name='sync_pb.NigoriSpecifics.encrypt_app_notifications', index=14,
      number=26, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='encrypt_app_settings', full_name='sync_pb.NigoriSpecifics.encrypt_app_settings', index=15,
      number=27, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sync_tab_favicons', full_name='sync_pb.NigoriSpecifics.sync_tab_favicons', index=16,
      number=29, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='passphrase_type', full_name='sync_pb.NigoriSpecifics.passphrase_type', index=17,
      number=30, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='keystore_decryptor_token', full_name='sync_pb.NigoriSpecifics.keystore_decryptor_token', index=18,
      number=31, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='keystore_migration_time', full_name='sync_pb.NigoriSpecifics.keystore_migration_time', index=19,
      number=32, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='custom_passphrase_time', full_name='sync_pb.NigoriSpecifics.custom_passphrase_time', index=20,
      number=33, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='encrypt_dictionary', full_name='sync_pb.NigoriSpecifics.encrypt_dictionary', index=21,
      number=34, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='encrypt_favicon_images', full_name='sync_pb.NigoriSpecifics.encrypt_favicon_images', index=22,
      number=35, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='encrypt_favicon_tracking', full_name='sync_pb.NigoriSpecifics.encrypt_favicon_tracking', index=23,
      number=36, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='encrypt_articles', full_name='sync_pb.NigoriSpecifics.encrypt_articles', index=24,
      number=37, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='encrypt_app_list', full_name='sync_pb.NigoriSpecifics.encrypt_app_list', index=25,
      number=38, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='encrypt_autofill_wallet_metadata', full_name='sync_pb.NigoriSpecifics.encrypt_autofill_wallet_metadata', index=26,
      number=39, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='server_only_was_missing_keystore_migration_time', full_name='sync_pb.NigoriSpecifics.server_only_was_missing_keystore_migration_time', index=27,
      number=40, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='encrypt_arc_package', full_name='sync_pb.NigoriSpecifics.encrypt_arc_package', index=28,
      number=41, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='encrypt_printers', full_name='sync_pb.NigoriSpecifics.encrypt_printers', index=29,
      number=42, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='encrypt_reading_list', full_name='sync_pb.NigoriSpecifics.encrypt_reading_list', index=30,
      number=43, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _NIGORISPECIFICS_PASSPHRASETYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=189,
  serialized_end=1392,
)

_NIGORIKEYBAG.fields_by_name['key'].message_type = _NIGORIKEY
_NIGORISPECIFICS.fields_by_name['encryption_keybag'].message_type = encryption__pb2._ENCRYPTEDDATA
_NIGORISPECIFICS.fields_by_name['passphrase_type'].enum_type = _NIGORISPECIFICS_PASSPHRASETYPE
_NIGORISPECIFICS.fields_by_name['keystore_decryptor_token'].message_type = encryption__pb2._ENCRYPTEDDATA
_NIGORISPECIFICS_PASSPHRASETYPE.containing_type = _NIGORISPECIFICS
DESCRIPTOR.message_types_by_name['NigoriKey'] = _NIGORIKEY
DESCRIPTOR.message_types_by_name['NigoriKeyBag'] = _NIGORIKEYBAG
DESCRIPTOR.message_types_by_name['NigoriSpecifics'] = _NIGORISPECIFICS

NigoriKey = _reflection.GeneratedProtocolMessageType('NigoriKey', (_message.Message,), dict(
  DESCRIPTOR = _NIGORIKEY,
  __module__ = 'nigori_specifics_pb2'
  # @@protoc_insertion_point(class_scope:sync_pb.NigoriKey)
  ))
_sym_db.RegisterMessage(NigoriKey)

NigoriKeyBag = _reflection.GeneratedProtocolMessageType('NigoriKeyBag', (_message.Message,), dict(
  DESCRIPTOR = _NIGORIKEYBAG,
  __module__ = 'nigori_specifics_pb2'
  # @@protoc_insertion_point(class_scope:sync_pb.NigoriKeyBag)
  ))
_sym_db.RegisterMessage(NigoriKeyBag)

NigoriSpecifics = _reflection.GeneratedProtocolMessageType('NigoriSpecifics', (_message.Message,), dict(
  DESCRIPTOR = _NIGORISPECIFICS,
  __module__ = 'nigori_specifics_pb2'
  # @@protoc_insertion_point(class_scope:sync_pb.NigoriSpecifics)
  ))
_sym_db.RegisterMessage(NigoriSpecifics)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('H\003'))
# @@protoc_insertion_point(module_scope)
