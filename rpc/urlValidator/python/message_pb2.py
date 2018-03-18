# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: message.proto

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
  name='message.proto',
  package='api',
  syntax='proto3',
  serialized_pb=_b('\n\rmessage.proto\x12\x03\x61pi\"\x19\n\nUrlRequest\x12\x0b\n\x03url\x18\x01 \x01(\t\"\x1c\n\x0bUrlResponse\x12\r\n\x05valid\x18\x01 \x01(\x08\x32\x36\n\x03URL\x12/\n\x08register\x12\x0f.api.UrlRequest\x1a\x10.api.UrlResponse\"\x00\x62\x06proto3')
)




_URLREQUEST = _descriptor.Descriptor(
  name='UrlRequest',
  full_name='api.UrlRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='api.UrlRequest.url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=47,
)


_URLRESPONSE = _descriptor.Descriptor(
  name='UrlResponse',
  full_name='api.UrlResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='valid', full_name='api.UrlResponse.valid', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=49,
  serialized_end=77,
)

DESCRIPTOR.message_types_by_name['UrlRequest'] = _URLREQUEST
DESCRIPTOR.message_types_by_name['UrlResponse'] = _URLRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UrlRequest = _reflection.GeneratedProtocolMessageType('UrlRequest', (_message.Message,), dict(
  DESCRIPTOR = _URLREQUEST,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:api.UrlRequest)
  ))
_sym_db.RegisterMessage(UrlRequest)

UrlResponse = _reflection.GeneratedProtocolMessageType('UrlResponse', (_message.Message,), dict(
  DESCRIPTOR = _URLRESPONSE,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:api.UrlResponse)
  ))
_sym_db.RegisterMessage(UrlResponse)



_URL = _descriptor.ServiceDescriptor(
  name='URL',
  full_name='api.URL',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=79,
  serialized_end=133,
  methods=[
  _descriptor.MethodDescriptor(
    name='register',
    full_name='api.URL.register',
    index=0,
    containing_service=None,
    input_type=_URLREQUEST,
    output_type=_URLRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_URL)

DESCRIPTOR.services_by_name['URL'] = _URL

# @@protoc_insertion_point(module_scope)
