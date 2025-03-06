from .types import (
    InfoResponse,
    InfoRequest,
    CheckTxRequest,
    CheckTxResponse,
    CommitRequest,
    CommitResponse,
    QueryRequest,
    QueryResponse,
    InitChainRequest,
    InitChainResponse,
    ListSnapshotsRequest,
    ListSnapshotsResponse,
    OfferSnapshotRequest,
    OfferSnapshotResponse,
    LoadSnapshotChunkRequest,
    LoadSnapshotChunkResponse,
    ApplySnapshotChunkRequest,
    ApplySnapshotChunkResponse,
    PrepareProposalRequest,
    PrepareProposalResponse,
    ProcessProposalRequest,
    ProcessProposalResponse,
    ExtendVoteRequest,
    ExtendVoteResponse,
    VerifyVoteExtensionRequest,
    VerifyVoteExtensionResponse,
    FinalizeBlockRequest,
    FinalizeBlockResponse,
    ExecTxResult,
    FlushRequest,
    FlushResponse,
)

# All is good
OkCode = 0
# There was a problem...
ErrorCode = 1


class BaseApplication:

    def info(self, request: InfoRequest) -> InfoResponse:
        return InfoResponse()

    def check_tx(self, request: CheckTxRequest) -> CheckTxResponse:
        return CheckTxResponse(code=OkCode)

    def commit(self, request: CommitRequest) -> CommitResponse:
        return CommitResponse(retain_height=1)

    def query(self, request: QueryRequest) -> QueryResponse:
        return QueryResponse(code=OkCode)

    def init_chain(self, request: InitChainRequest) -> InitChainResponse:
        return InitChainResponse()

    def list_snapshots(self, request: ListSnapshotsRequest) -> ListSnapshotsResponse:
        return ListSnapshotsResponse()

    def offer_snapshot(self, request: OfferSnapshotRequest) -> OfferSnapshotResponse:
        return OfferSnapshotResponse()

    def load_snapshot_chunk(self, request: LoadSnapshotChunkRequest) -> LoadSnapshotChunkResponse:
        return LoadSnapshotChunkResponse()

    def apply_snapshot_chunk(self, request: ApplySnapshotChunkRequest) -> ApplySnapshotChunkResponse:
        return ApplySnapshotChunkResponse()

    def prepare_proposal(self, request: PrepareProposalRequest) -> PrepareProposalResponse:
        txs = []
        total_bytes = 0
        for tx in request.txs:
            total_bytes += len(tx)
            if total_bytes > request.max_tx_bytes:
                break
            txs.append(tx)
        return PrepareProposalResponse(txs=txs)

    def process_proposal(self, request: ProcessProposalRequest) -> ProcessProposalResponse:
        return ProcessProposalResponse(status=1)

    def extend_vote(self, request: ExtendVoteRequest) -> ExtendVoteResponse:
        return ExtendVoteResponse(vote_extension=b"")

    def verify_vote_extension(self, request: VerifyVoteExtensionRequest) -> VerifyVoteExtensionResponse:
        return VerifyVoteExtensionResponse(status=1)

    def finalize_block(self, request: FinalizeBlockRequest) -> FinalizeBlockResponse:
        tx_results = []
        for _ in request.txs:
            tx_results.append(ExecTxResult(code=OkCode))
        return FinalizeBlockResponse(tx_results=tx_results)

    def Flush(self, request: FlushRequest) -> FlushResponse:
        return FlushResponse()