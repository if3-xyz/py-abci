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

    def Info(self, request: InfoRequest) -> InfoResponse:
        return InfoResponse()

    def CheckTx(self, request: CheckTxRequest) -> CheckTxResponse:
        return CheckTxResponse(code=OkCode)

    def Commit(self, request: CommitRequest) -> CommitResponse:
        return CommitResponse(retain_height=1)

    def Query(self, request: QueryRequest) -> QueryResponse:
        return QueryResponse(code=OkCode)

    def InitChain(self, request: InitChainRequest) -> InitChainResponse:
        return InitChainResponse()

    def ListSnapshots(self, request: ListSnapshotsRequest) -> ListSnapshotsResponse:
        return ListSnapshotsResponse()

    def OfferSnapshot(self, request: OfferSnapshotRequest) -> OfferSnapshotResponse:
        return OfferSnapshotResponse()

    def LoadSnapshotChunk(self, request: LoadSnapshotChunkRequest) -> LoadSnapshotChunkResponse:
        return LoadSnapshotChunkResponse()

    def ApplySnapshotChunk(self, request: ApplySnapshotChunkRequest) -> ApplySnapshotChunkResponse:
        return ApplySnapshotChunkResponse()

    def PrepareProposal(self, request: PrepareProposalRequest) -> PrepareProposalResponse:
        txs = []
        total_bytes = 0
        for tx in request.txs:
            total_bytes += len(tx)
            if total_bytes > request.max_tx_bytes:
                break
            txs.append(tx)
        return PrepareProposalResponse(txs=txs)

    def ProcessProposal(self, request: ProcessProposalRequest) -> ProcessProposalResponse:
        return ProcessProposalResponse(status=1)

    def ExtendVote(self, request: ExtendVoteRequest) -> ExtendVoteResponse:
        return ExtendVoteResponse(vote_extension=b"")

    def VerifyVoteExtension(self, request: VerifyVoteExtensionRequest) -> VerifyVoteExtensionResponse:
        return VerifyVoteExtensionResponse(status=1)

    def FinalizeBlock(self, request: FinalizeBlockRequest) -> FinalizeBlockResponse:
        tx_results = []
        for _ in request.txs:
            tx_results.append(ExecTxResult(code=OkCode))
        return FinalizeBlockResponse(tx_results=tx_results)
