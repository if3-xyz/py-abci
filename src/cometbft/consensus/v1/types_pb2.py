# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cometbft/consensus/v1/types.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cometbft.libs.bits.v1 import types_pb2 as cometbft_dot_libs_dot_bits_dot_v1_dot_types__pb2
from cometbft.types.v1 import types_pb2 as cometbft_dot_types_dot_v1_dot_types__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cometbft/consensus/v1/types.proto',
  package='cometbft.consensus.v1',
  syntax='proto3',
  serialized_options=b'Z6github.com/cometbft/cometbft/api/cometbft/consensus/v1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n!cometbft/consensus/v1/types.proto\x12\x15\x63ometbft.consensus.v1\x1a\x14gogoproto/gogo.proto\x1a!cometbft/libs/bits/v1/types.proto\x1a\x1d\x63ometbft/types/v1/types.proto\"x\n\x0cNewRoundStep\x12\x0e\n\x06height\x18\x01 \x01(\x03\x12\r\n\x05round\x18\x02 \x01(\x05\x12\x0c\n\x04step\x18\x03 \x01(\r\x12 \n\x18seconds_since_start_time\x18\x04 \x01(\x03\x12\x19\n\x11last_commit_round\x18\x05 \x01(\x05\"\xbe\x01\n\rNewValidBlock\x12\x0e\n\x06height\x18\x01 \x01(\x03\x12\r\n\x05round\x18\x02 \x01(\x05\x12\x45\n\x15\x62lock_part_set_header\x18\x03 \x01(\x0b\x32 .cometbft.types.v1.PartSetHeaderB\x04\xc8\xde\x1f\x00\x12\x34\n\x0b\x62lock_parts\x18\x04 \x01(\x0b\x32\x1f.cometbft.libs.bits.v1.BitArray\x12\x11\n\tis_commit\x18\x05 \x01(\x08\"?\n\x08Proposal\x12\x33\n\x08proposal\x18\x01 \x01(\x0b\x32\x1b.cometbft.types.v1.ProposalB\x04\xc8\xde\x1f\x00\"v\n\x0bProposalPOL\x12\x0e\n\x06height\x18\x01 \x01(\x03\x12\x1a\n\x12proposal_pol_round\x18\x02 \x01(\x05\x12;\n\x0cproposal_pol\x18\x03 \x01(\x0b\x32\x1f.cometbft.libs.bits.v1.BitArrayB\x04\xc8\xde\x1f\x00\"W\n\tBlockPart\x12\x0e\n\x06height\x18\x01 \x01(\x03\x12\r\n\x05round\x18\x02 \x01(\x05\x12+\n\x04part\x18\x03 \x01(\x0b\x32\x17.cometbft.types.v1.PartB\x04\xc8\xde\x1f\x00\"-\n\x04Vote\x12%\n\x04vote\x18\x01 \x01(\x0b\x32\x17.cometbft.types.v1.Vote\"g\n\x07HasVote\x12\x0e\n\x06height\x18\x01 \x01(\x03\x12\r\n\x05round\x18\x02 \x01(\x05\x12.\n\x04type\x18\x03 \x01(\x0e\x32 .cometbft.types.v1.SignedMsgType\x12\r\n\x05index\x18\x04 \x01(\x05\"\x9c\x01\n\x0cVoteSetMaj23\x12\x0e\n\x06height\x18\x01 \x01(\x03\x12\r\n\x05round\x18\x02 \x01(\x05\x12.\n\x04type\x18\x03 \x01(\x0e\x32 .cometbft.types.v1.SignedMsgType\x12=\n\x08\x62lock_id\x18\x04 \x01(\x0b\x32\x1a.cometbft.types.v1.BlockIDB\x0f\xe2\xde\x1f\x07\x42lockID\xc8\xde\x1f\x00\"\xd1\x01\n\x0bVoteSetBits\x12\x0e\n\x06height\x18\x01 \x01(\x03\x12\r\n\x05round\x18\x02 \x01(\x05\x12.\n\x04type\x18\x03 \x01(\x0e\x32 .cometbft.types.v1.SignedMsgType\x12=\n\x08\x62lock_id\x18\x04 \x01(\x0b\x32\x1a.cometbft.types.v1.BlockIDB\x0f\xe2\xde\x1f\x07\x42lockID\xc8\xde\x1f\x00\x12\x34\n\x05votes\x18\x05 \x01(\x0b\x32\x1f.cometbft.libs.bits.v1.BitArrayB\x04\xc8\xde\x1f\x00\"D\n\x14HasProposalBlockPart\x12\x0e\n\x06height\x18\x01 \x01(\x03\x12\r\n\x05round\x18\x02 \x01(\x05\x12\r\n\x05index\x18\x03 \x01(\x05\"\xe6\x04\n\x07Message\x12=\n\x0enew_round_step\x18\x01 \x01(\x0b\x32#.cometbft.consensus.v1.NewRoundStepH\x00\x12?\n\x0fnew_valid_block\x18\x02 \x01(\x0b\x32$.cometbft.consensus.v1.NewValidBlockH\x00\x12\x33\n\x08proposal\x18\x03 \x01(\x0b\x32\x1f.cometbft.consensus.v1.ProposalH\x00\x12:\n\x0cproposal_pol\x18\x04 \x01(\x0b\x32\".cometbft.consensus.v1.ProposalPOLH\x00\x12\x36\n\nblock_part\x18\x05 \x01(\x0b\x32 .cometbft.consensus.v1.BlockPartH\x00\x12+\n\x04vote\x18\x06 \x01(\x0b\x32\x1b.cometbft.consensus.v1.VoteH\x00\x12\x32\n\x08has_vote\x18\x07 \x01(\x0b\x32\x1e.cometbft.consensus.v1.HasVoteH\x00\x12=\n\x0evote_set_maj23\x18\x08 \x01(\x0b\x32#.cometbft.consensus.v1.VoteSetMaj23H\x00\x12;\n\rvote_set_bits\x18\t \x01(\x0b\x32\".cometbft.consensus.v1.VoteSetBitsH\x00\x12N\n\x17has_proposal_block_part\x18\n \x01(\x0b\x32+.cometbft.consensus.v1.HasProposalBlockPartH\x00\x42\x05\n\x03sumB8Z6github.com/cometbft/cometbft/api/cometbft/consensus/v1b\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,cometbft_dot_libs_dot_bits_dot_v1_dot_types__pb2.DESCRIPTOR,cometbft_dot_types_dot_v1_dot_types__pb2.DESCRIPTOR,])




_NEWROUNDSTEP = _descriptor.Descriptor(
  name='NewRoundStep',
  full_name='cometbft.consensus.v1.NewRoundStep',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='height', full_name='cometbft.consensus.v1.NewRoundStep.height', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='round', full_name='cometbft.consensus.v1.NewRoundStep.round', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='step', full_name='cometbft.consensus.v1.NewRoundStep.step', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='seconds_since_start_time', full_name='cometbft.consensus.v1.NewRoundStep.seconds_since_start_time', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_commit_round', full_name='cometbft.consensus.v1.NewRoundStep.last_commit_round', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=148,
  serialized_end=268,
)


_NEWVALIDBLOCK = _descriptor.Descriptor(
  name='NewValidBlock',
  full_name='cometbft.consensus.v1.NewValidBlock',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='height', full_name='cometbft.consensus.v1.NewValidBlock.height', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='round', full_name='cometbft.consensus.v1.NewValidBlock.round', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='block_part_set_header', full_name='cometbft.consensus.v1.NewValidBlock.block_part_set_header', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='block_parts', full_name='cometbft.consensus.v1.NewValidBlock.block_parts', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_commit', full_name='cometbft.consensus.v1.NewValidBlock.is_commit', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=271,
  serialized_end=461,
)


_PROPOSAL = _descriptor.Descriptor(
  name='Proposal',
  full_name='cometbft.consensus.v1.Proposal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='proposal', full_name='cometbft.consensus.v1.Proposal.proposal', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=463,
  serialized_end=526,
)


_PROPOSALPOL = _descriptor.Descriptor(
  name='ProposalPOL',
  full_name='cometbft.consensus.v1.ProposalPOL',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='height', full_name='cometbft.consensus.v1.ProposalPOL.height', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='proposal_pol_round', full_name='cometbft.consensus.v1.ProposalPOL.proposal_pol_round', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='proposal_pol', full_name='cometbft.consensus.v1.ProposalPOL.proposal_pol', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=528,
  serialized_end=646,
)


_BLOCKPART = _descriptor.Descriptor(
  name='BlockPart',
  full_name='cometbft.consensus.v1.BlockPart',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='height', full_name='cometbft.consensus.v1.BlockPart.height', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='round', full_name='cometbft.consensus.v1.BlockPart.round', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='part', full_name='cometbft.consensus.v1.BlockPart.part', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=648,
  serialized_end=735,
)


_VOTE = _descriptor.Descriptor(
  name='Vote',
  full_name='cometbft.consensus.v1.Vote',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='vote', full_name='cometbft.consensus.v1.Vote.vote', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=737,
  serialized_end=782,
)


_HASVOTE = _descriptor.Descriptor(
  name='HasVote',
  full_name='cometbft.consensus.v1.HasVote',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='height', full_name='cometbft.consensus.v1.HasVote.height', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='round', full_name='cometbft.consensus.v1.HasVote.round', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='cometbft.consensus.v1.HasVote.type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='index', full_name='cometbft.consensus.v1.HasVote.index', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=784,
  serialized_end=887,
)


_VOTESETMAJ23 = _descriptor.Descriptor(
  name='VoteSetMaj23',
  full_name='cometbft.consensus.v1.VoteSetMaj23',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='height', full_name='cometbft.consensus.v1.VoteSetMaj23.height', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='round', full_name='cometbft.consensus.v1.VoteSetMaj23.round', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='cometbft.consensus.v1.VoteSetMaj23.type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='block_id', full_name='cometbft.consensus.v1.VoteSetMaj23.block_id', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342\336\037\007BlockID\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=890,
  serialized_end=1046,
)


_VOTESETBITS = _descriptor.Descriptor(
  name='VoteSetBits',
  full_name='cometbft.consensus.v1.VoteSetBits',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='height', full_name='cometbft.consensus.v1.VoteSetBits.height', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='round', full_name='cometbft.consensus.v1.VoteSetBits.round', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='cometbft.consensus.v1.VoteSetBits.type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='block_id', full_name='cometbft.consensus.v1.VoteSetBits.block_id', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342\336\037\007BlockID\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='votes', full_name='cometbft.consensus.v1.VoteSetBits.votes', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1049,
  serialized_end=1258,
)


_HASPROPOSALBLOCKPART = _descriptor.Descriptor(
  name='HasProposalBlockPart',
  full_name='cometbft.consensus.v1.HasProposalBlockPart',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='height', full_name='cometbft.consensus.v1.HasProposalBlockPart.height', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='round', full_name='cometbft.consensus.v1.HasProposalBlockPart.round', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='index', full_name='cometbft.consensus.v1.HasProposalBlockPart.index', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1260,
  serialized_end=1328,
)


_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='cometbft.consensus.v1.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='new_round_step', full_name='cometbft.consensus.v1.Message.new_round_step', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='new_valid_block', full_name='cometbft.consensus.v1.Message.new_valid_block', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='proposal', full_name='cometbft.consensus.v1.Message.proposal', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='proposal_pol', full_name='cometbft.consensus.v1.Message.proposal_pol', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='block_part', full_name='cometbft.consensus.v1.Message.block_part', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='vote', full_name='cometbft.consensus.v1.Message.vote', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='has_vote', full_name='cometbft.consensus.v1.Message.has_vote', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='vote_set_maj23', full_name='cometbft.consensus.v1.Message.vote_set_maj23', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='vote_set_bits', full_name='cometbft.consensus.v1.Message.vote_set_bits', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='has_proposal_block_part', full_name='cometbft.consensus.v1.Message.has_proposal_block_part', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='sum', full_name='cometbft.consensus.v1.Message.sum',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=1331,
  serialized_end=1945,
)

_NEWVALIDBLOCK.fields_by_name['block_part_set_header'].message_type = cometbft_dot_types_dot_v1_dot_types__pb2._PARTSETHEADER
_NEWVALIDBLOCK.fields_by_name['block_parts'].message_type = cometbft_dot_libs_dot_bits_dot_v1_dot_types__pb2._BITARRAY
_PROPOSAL.fields_by_name['proposal'].message_type = cometbft_dot_types_dot_v1_dot_types__pb2._PROPOSAL
_PROPOSALPOL.fields_by_name['proposal_pol'].message_type = cometbft_dot_libs_dot_bits_dot_v1_dot_types__pb2._BITARRAY
_BLOCKPART.fields_by_name['part'].message_type = cometbft_dot_types_dot_v1_dot_types__pb2._PART
_VOTE.fields_by_name['vote'].message_type = cometbft_dot_types_dot_v1_dot_types__pb2._VOTE
_HASVOTE.fields_by_name['type'].enum_type = cometbft_dot_types_dot_v1_dot_types__pb2._SIGNEDMSGTYPE
_VOTESETMAJ23.fields_by_name['type'].enum_type = cometbft_dot_types_dot_v1_dot_types__pb2._SIGNEDMSGTYPE
_VOTESETMAJ23.fields_by_name['block_id'].message_type = cometbft_dot_types_dot_v1_dot_types__pb2._BLOCKID
_VOTESETBITS.fields_by_name['type'].enum_type = cometbft_dot_types_dot_v1_dot_types__pb2._SIGNEDMSGTYPE
_VOTESETBITS.fields_by_name['block_id'].message_type = cometbft_dot_types_dot_v1_dot_types__pb2._BLOCKID
_VOTESETBITS.fields_by_name['votes'].message_type = cometbft_dot_libs_dot_bits_dot_v1_dot_types__pb2._BITARRAY
_MESSAGE.fields_by_name['new_round_step'].message_type = _NEWROUNDSTEP
_MESSAGE.fields_by_name['new_valid_block'].message_type = _NEWVALIDBLOCK
_MESSAGE.fields_by_name['proposal'].message_type = _PROPOSAL
_MESSAGE.fields_by_name['proposal_pol'].message_type = _PROPOSALPOL
_MESSAGE.fields_by_name['block_part'].message_type = _BLOCKPART
_MESSAGE.fields_by_name['vote'].message_type = _VOTE
_MESSAGE.fields_by_name['has_vote'].message_type = _HASVOTE
_MESSAGE.fields_by_name['vote_set_maj23'].message_type = _VOTESETMAJ23
_MESSAGE.fields_by_name['vote_set_bits'].message_type = _VOTESETBITS
_MESSAGE.fields_by_name['has_proposal_block_part'].message_type = _HASPROPOSALBLOCKPART
_MESSAGE.oneofs_by_name['sum'].fields.append(
  _MESSAGE.fields_by_name['new_round_step'])
_MESSAGE.fields_by_name['new_round_step'].containing_oneof = _MESSAGE.oneofs_by_name['sum']
_MESSAGE.oneofs_by_name['sum'].fields.append(
  _MESSAGE.fields_by_name['new_valid_block'])
_MESSAGE.fields_by_name['new_valid_block'].containing_oneof = _MESSAGE.oneofs_by_name['sum']
_MESSAGE.oneofs_by_name['sum'].fields.append(
  _MESSAGE.fields_by_name['proposal'])
_MESSAGE.fields_by_name['proposal'].containing_oneof = _MESSAGE.oneofs_by_name['sum']
_MESSAGE.oneofs_by_name['sum'].fields.append(
  _MESSAGE.fields_by_name['proposal_pol'])
_MESSAGE.fields_by_name['proposal_pol'].containing_oneof = _MESSAGE.oneofs_by_name['sum']
_MESSAGE.oneofs_by_name['sum'].fields.append(
  _MESSAGE.fields_by_name['block_part'])
_MESSAGE.fields_by_name['block_part'].containing_oneof = _MESSAGE.oneofs_by_name['sum']
_MESSAGE.oneofs_by_name['sum'].fields.append(
  _MESSAGE.fields_by_name['vote'])
_MESSAGE.fields_by_name['vote'].containing_oneof = _MESSAGE.oneofs_by_name['sum']
_MESSAGE.oneofs_by_name['sum'].fields.append(
  _MESSAGE.fields_by_name['has_vote'])
_MESSAGE.fields_by_name['has_vote'].containing_oneof = _MESSAGE.oneofs_by_name['sum']
_MESSAGE.oneofs_by_name['sum'].fields.append(
  _MESSAGE.fields_by_name['vote_set_maj23'])
_MESSAGE.fields_by_name['vote_set_maj23'].containing_oneof = _MESSAGE.oneofs_by_name['sum']
_MESSAGE.oneofs_by_name['sum'].fields.append(
  _MESSAGE.fields_by_name['vote_set_bits'])
_MESSAGE.fields_by_name['vote_set_bits'].containing_oneof = _MESSAGE.oneofs_by_name['sum']
_MESSAGE.oneofs_by_name['sum'].fields.append(
  _MESSAGE.fields_by_name['has_proposal_block_part'])
_MESSAGE.fields_by_name['has_proposal_block_part'].containing_oneof = _MESSAGE.oneofs_by_name['sum']
DESCRIPTOR.message_types_by_name['NewRoundStep'] = _NEWROUNDSTEP
DESCRIPTOR.message_types_by_name['NewValidBlock'] = _NEWVALIDBLOCK
DESCRIPTOR.message_types_by_name['Proposal'] = _PROPOSAL
DESCRIPTOR.message_types_by_name['ProposalPOL'] = _PROPOSALPOL
DESCRIPTOR.message_types_by_name['BlockPart'] = _BLOCKPART
DESCRIPTOR.message_types_by_name['Vote'] = _VOTE
DESCRIPTOR.message_types_by_name['HasVote'] = _HASVOTE
DESCRIPTOR.message_types_by_name['VoteSetMaj23'] = _VOTESETMAJ23
DESCRIPTOR.message_types_by_name['VoteSetBits'] = _VOTESETBITS
DESCRIPTOR.message_types_by_name['HasProposalBlockPart'] = _HASPROPOSALBLOCKPART
DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NewRoundStep = _reflection.GeneratedProtocolMessageType('NewRoundStep', (_message.Message,), {
  'DESCRIPTOR' : _NEWROUNDSTEP,
  '__module__' : 'cometbft.consensus.v1.types_pb2'
  # @@protoc_insertion_point(class_scope:cometbft.consensus.v1.NewRoundStep)
  })
_sym_db.RegisterMessage(NewRoundStep)

NewValidBlock = _reflection.GeneratedProtocolMessageType('NewValidBlock', (_message.Message,), {
  'DESCRIPTOR' : _NEWVALIDBLOCK,
  '__module__' : 'cometbft.consensus.v1.types_pb2'
  # @@protoc_insertion_point(class_scope:cometbft.consensus.v1.NewValidBlock)
  })
_sym_db.RegisterMessage(NewValidBlock)

Proposal = _reflection.GeneratedProtocolMessageType('Proposal', (_message.Message,), {
  'DESCRIPTOR' : _PROPOSAL,
  '__module__' : 'cometbft.consensus.v1.types_pb2'
  # @@protoc_insertion_point(class_scope:cometbft.consensus.v1.Proposal)
  })
_sym_db.RegisterMessage(Proposal)

ProposalPOL = _reflection.GeneratedProtocolMessageType('ProposalPOL', (_message.Message,), {
  'DESCRIPTOR' : _PROPOSALPOL,
  '__module__' : 'cometbft.consensus.v1.types_pb2'
  # @@protoc_insertion_point(class_scope:cometbft.consensus.v1.ProposalPOL)
  })
_sym_db.RegisterMessage(ProposalPOL)

BlockPart = _reflection.GeneratedProtocolMessageType('BlockPart', (_message.Message,), {
  'DESCRIPTOR' : _BLOCKPART,
  '__module__' : 'cometbft.consensus.v1.types_pb2'
  # @@protoc_insertion_point(class_scope:cometbft.consensus.v1.BlockPart)
  })
_sym_db.RegisterMessage(BlockPart)

Vote = _reflection.GeneratedProtocolMessageType('Vote', (_message.Message,), {
  'DESCRIPTOR' : _VOTE,
  '__module__' : 'cometbft.consensus.v1.types_pb2'
  # @@protoc_insertion_point(class_scope:cometbft.consensus.v1.Vote)
  })
_sym_db.RegisterMessage(Vote)

HasVote = _reflection.GeneratedProtocolMessageType('HasVote', (_message.Message,), {
  'DESCRIPTOR' : _HASVOTE,
  '__module__' : 'cometbft.consensus.v1.types_pb2'
  # @@protoc_insertion_point(class_scope:cometbft.consensus.v1.HasVote)
  })
_sym_db.RegisterMessage(HasVote)

VoteSetMaj23 = _reflection.GeneratedProtocolMessageType('VoteSetMaj23', (_message.Message,), {
  'DESCRIPTOR' : _VOTESETMAJ23,
  '__module__' : 'cometbft.consensus.v1.types_pb2'
  # @@protoc_insertion_point(class_scope:cometbft.consensus.v1.VoteSetMaj23)
  })
_sym_db.RegisterMessage(VoteSetMaj23)

VoteSetBits = _reflection.GeneratedProtocolMessageType('VoteSetBits', (_message.Message,), {
  'DESCRIPTOR' : _VOTESETBITS,
  '__module__' : 'cometbft.consensus.v1.types_pb2'
  # @@protoc_insertion_point(class_scope:cometbft.consensus.v1.VoteSetBits)
  })
_sym_db.RegisterMessage(VoteSetBits)

HasProposalBlockPart = _reflection.GeneratedProtocolMessageType('HasProposalBlockPart', (_message.Message,), {
  'DESCRIPTOR' : _HASPROPOSALBLOCKPART,
  '__module__' : 'cometbft.consensus.v1.types_pb2'
  # @@protoc_insertion_point(class_scope:cometbft.consensus.v1.HasProposalBlockPart)
  })
_sym_db.RegisterMessage(HasProposalBlockPart)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGE,
  '__module__' : 'cometbft.consensus.v1.types_pb2'
  # @@protoc_insertion_point(class_scope:cometbft.consensus.v1.Message)
  })
_sym_db.RegisterMessage(Message)


DESCRIPTOR._options = None
_NEWVALIDBLOCK.fields_by_name['block_part_set_header']._options = None
_PROPOSAL.fields_by_name['proposal']._options = None
_PROPOSALPOL.fields_by_name['proposal_pol']._options = None
_BLOCKPART.fields_by_name['part']._options = None
_VOTESETMAJ23.fields_by_name['block_id']._options = None
_VOTESETBITS.fields_by_name['block_id']._options = None
_VOTESETBITS.fields_by_name['votes']._options = None
# @@protoc_insertion_point(module_scope)
