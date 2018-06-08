# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chat-server-grpc.proto

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
  name='chat-server-grpc.proto',
  package='chat_server_grpc',
  syntax='proto3',
  serialized_pb=_b('\n\x16\x63hat-server-grpc.proto\x12\x10\x63hat_server_grpc\"-\n\x07Request\x12\x11\n\tclient_id\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\"\x1b\n\x08Response\x12\x0f\n\x07message\x18\x01 \x01(\t2V\n\nChatServer\x12H\n\x0b\x43ommunicate\x12\x19.chat_server_grpc.Request\x1a\x1a.chat_server_grpc.Response(\x01\x30\x01\x62\x06proto3')
)




_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='chat_server_grpc.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_id', full_name='chat_server_grpc.Request.client_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='chat_server_grpc.Request.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=44,
  serialized_end=89,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='chat_server_grpc.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='chat_server_grpc.Response.message', index=0,
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
  serialized_start=91,
  serialized_end=118,
)

DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'chat_server_grpc_pb2'
  # @@protoc_insertion_point(class_scope:chat_server_grpc.Request)
  ))
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'chat_server_grpc_pb2'
  # @@protoc_insertion_point(class_scope:chat_server_grpc.Response)
  ))
_sym_db.RegisterMessage(Response)



_CHATSERVER = _descriptor.ServiceDescriptor(
  name='ChatServer',
  full_name='chat_server_grpc.ChatServer',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=120,
  serialized_end=206,
  methods=[
  _descriptor.MethodDescriptor(
    name='Communicate',
    full_name='chat_server_grpc.ChatServer.Communicate',
    index=0,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CHATSERVER)

DESCRIPTOR.services_by_name['ChatServer'] = _CHATSERVER

# @@protoc_insertion_point(module_scope)
