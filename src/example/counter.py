"""
Simple counting app.  It only accepts values sent to it in correct order.  The
state maintains the current count. For example, if starting at state 0, sending:
-> 0x01 = OK!
-> 0x03 = Will fail! (expects 2)

To run it:
- make a clean new directory for tendermint
- start this server: python counter.py
- start tendermint: tendermint --home "YOUR DIR HERE" node
- The send transactions to the app:


curl http://localhost:26657/broadcast_tx_commit?tx=0x01
curl http://localhost:26657/broadcast_tx_commit?tx=0x02
...

To see the latest count:
curl http://localhost:26657/abci_query

The way the app state is structured, you can also see the current state value
in the tendermint console output (see app_hash).
"""
import struct
from cometbft.abci.v1.types_pb2 import (
    InfoResponse,
    InitChainResponse,
    CheckTxResponse,
    FinalizeBlockResponse,
    CommitResponse,
    QueryResponse,
    CommitResponse,
)

from abci.application import BaseApplication, OkCode, ErrorCode
from cometbft.abci.v1beta3.types_pb2 import ExecTxResult


# Tx encoding/decoding


def encode_number(value):
    return struct.pack(">I", value)


def decode_number(raw):
    return int.from_bytes(raw, byteorder="big")


class SimpleCounter(BaseApplication):
    def info(self, req) -> InfoResponse:
        """
        Since this will always respond with height=0, Tendermint
        will resync this app from the begining
        """
        r = InfoResponse()
        r.version = req.version
        r.last_block_height = 0
        r.last_block_app_hash = b""
        return r

    def init_chain(self, req) -> InitChainResponse:
        """Set initial state on first run"""
        self.txCount = 0
        self.nextTxCount = 0
        self.last_block_height = 0
        return InitChainResponse()

    def check_tx(self, tx) -> CheckTxResponse:
        """
        Validate the Tx before entry into the mempool
        Checks the txs are submitted in order 1,2,3...
        If not an order, a non-zero code is returned and the tx
        will be dropped.
        """
        value = decode_number(tx)
        if not value == (self.txCount + 1):
            return CheckTxResponse(code=ErrorCode)
        return CheckTxResponse(code=OkCode)

    def finalize_block(self, request: FinalizeBlockRequest) -> FinalizeBlockResponse:
        # Collect transactions but do NOT store them yet
        tx_results = []
        self.pending_txs = request.txs  # Store pending transactions

        for tx in request.txs:
            self.nextTxCount += 1
            tx_results.append(ExecTxResult(code=OkCode))

        return FinalizeBlockResponse(tx_results=tx_results)

    def commit(self) -> CommitResponse:
        """Return the current encode state value to tendermint"""
        self.txCount = self.nextTxCount
        hash = struct.pack(">Q", self.txCount)
        return CommitResponse(data=hash)

    def query(self, req) -> QueryResponse:
        """Return the last tx count"""
        v = encode_number(self.txCount)
        return QueryResponse(
            code=OkCode, value=v, height=self.last_block_height
        )

    def commit(self) -> CommitResponse:
        """Return the current encode state value to tendermint"""
        hash = struct.pack(">Q", self.txCount)
        return CommitResponse(data=hash)
