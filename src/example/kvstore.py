from src.abci.application import BaseApplication, OkCode, ErrorCode
from src.abci.types import (
    CheckTxRequest,
    CheckTxResponse,
    CommitRequest,
    CommitResponse,
    QueryRequest,
    QueryResponse,
    FinalizeBlockRequest,
    FinalizeBlockResponse,
    ExecTxResult,
)


class KVStoreApplication(BaseApplication):
    def __init__(self):
        super().__init__()
        self.store = {}  # Persistent key-value store
        self.pending_txs = []  # Store uncommitted transactions

    def check_tx(self, request: CheckTxRequest) -> CheckTxResponse:
        # Ensure the transaction is in the form of "key=value"
        tx = request.tx.decode("utf-8")
        if "=" not in tx:
            return CheckTxResponse(code=ErrorCode)
        return CheckTxResponse(code=OkCode)

    def finalize_block(self, request: FinalizeBlockRequest) -> FinalizeBlockResponse:
        # Collect transactions but do NOT store them yet
        tx_results = []
        self.pending_txs = request.txs  # Store pending transactions

        for tx in request.txs:
            tx_results.append(ExecTxResult(code=OkCode))

        return FinalizeBlockResponse(tx_results=tx_results)

    def commit(self, request: CommitRequest) -> CommitResponse:
        # Apply pending transactions to the store
        for tx in self.pending_txs:
            tx_str = tx.decode("utf-8")
            key, value = tx_str.split("=", 1)
            self.store[key] = value  # Store the key-value pair

        self.pending_txs = []  # Clear pending transactions after commit
        return CommitResponse(retain_height=1)

    def query(self, request: QueryRequest) -> QueryResponse:
        key = request.data.decode("utf-8")
        value = self.store.get(key)
        if value is None:
            return QueryResponse(code=ErrorCode)
        return QueryResponse(code=OkCode, value=value.encode("utf-8"))
