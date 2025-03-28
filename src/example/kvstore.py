import json
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
import plyvel


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

    def _commit(self, request: CommitRequest):
        for tx in self.pending_txs:
            tx_str = tx.decode("utf-8")
            key, value = tx_str.split("=", 1)
            self.store[key] = value  # Store the key-value pair

        self.pending_txs = []  # Clear pending transactions after commit

    def commit(self, request: CommitRequest) -> CommitResponse:
        # Apply pending transactions to the store
        self._commit(request)
        return CommitResponse(retain_height=1)

    def query(self, request: QueryRequest) -> QueryResponse:
        key = request.data.decode("utf-8")
        value = self.store.get(key)
        if value is None:
            return QueryResponse(code=ErrorCode)
        return QueryResponse(code=OkCode, value=value.encode("utf-8"))


class PersistentKVStoreApplication:
    def __init__(self, db_path: str):
        super().__init__()
        self.db = plyvel.DB(db_path)
        self.store = self.load_store()

    def load_store(self):
        store = self.db.get("store")
        if store is None:
            return {}
        return json.loads(store.decode("utf-8"))

    def save_store(self):
        self.db.put("store", json.dumps(self.store).encode("utf-8"))

    def commit(self, request: CommitRequest):
        self._commit(request)
        self.save_store()
        return CommitResponse(retain_height=1)
