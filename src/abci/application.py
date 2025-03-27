"""
Base ABCI Application class that defines the interface between CometBFT and the application.

CometBFT creates 4 ABCI connections to the application:

1. Query Connection - For querying application state
   - info(): Get application info and sync status
   - query(): Query application state

2. Mempool Connection - For transaction validation 
   - check_tx(): Validate transactions before adding to mempool

3. Consensus Connection - For block execution
   - init_chain(): Initialize chain with genesis state
   - prepare_proposal(): Prepare block proposal
   - process_proposal(): Process block proposal
   - finalize_block(): Execute block transactions
   - commit(): Persist state changes
   - extend_vote(): Add vote extensions
   - verify_vote_extension(): Verify vote extensions

4. State Sync Connection - For state synchronization
   - list_snapshots(): Get available state snapshots
   - offer_snapshot(): Offer snapshot to application
   - load_snapshot_chunk(): Load snapshot chunk
   - apply_snapshot_chunk(): Apply snapshot chunk

Applications should inherit from BaseApplication and override methods as needed.
"""

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

# Common response code
# All is good
OkCode = 0
# There was a problem...
ErrorCode = 1


class BaseApplication:
    """
    Base ABCI Application that defines the interface between CometBFT and applications.
    
    Applications should inherit from this class and override methods as needed.
    Default implementations provide no-op responses.
    """

    def info(self, request: InfoRequest) -> InfoResponse:
        """
        Called by ABCI when the app first starts. A stateful application
        should alway return the last blockhash and blockheight to prevent Tendermint
        from replaying the transaction log from the beginning.  These values are used
        to help Tendermint determine how to synch the node.
        If blockheight == 0, Tendermint will call ``init_chain()``
        """
        return InfoResponse()

    def check_tx(self, request: CheckTxRequest) -> CheckTxResponse:
        """
        Use to validate incoming transactions.  If the returned resp.code is 0 (OK),
        the tx will be added to Tendermint's mempool for consideration in a block.
        A non-zero response code implies an error and the transaction will be rejected
        """
        return CheckTxResponse(code=OkCode)

    def commit(self, request: CommitRequest) -> CommitResponse:
        """
        Called after ``end_block``.  This should return a compact ``fingerprint``
        of the current state of the application. This is usually the root hash
        of a merkletree.  The returned data is used as part of the consensus process.
        """
        return CommitResponse(retain_height=1)

    def query(self, request: QueryRequest) -> QueryResponse:
        """
        This is commonly used to query the state of the application.
        A non-zero 'code' in the response is used to indicate an error.
        """
        return QueryResponse(code=OkCode)

    def init_chain(self, request: InitChainRequest) -> InitChainResponse:
        """
        Called once, after ``info()`` during startup.  This is where you
        can load initial ``genesis`` data, etc....
        See ``info()``
        """
        return InitChainResponse()

    def list_snapshots(self, request: ListSnapshotsRequest) -> ListSnapshotsResponse:
        """
        State sync: return state snapshots
        """
        return ListSnapshotsResponse()

    def offer_snapshot(self, request: OfferSnapshotRequest) -> OfferSnapshotResponse:
        """
        State sync: Offer a snapshot to the application
        """
        return OfferSnapshotResponse()

    def load_snapshot_chunk(self, request: LoadSnapshotChunkRequest) -> LoadSnapshotChunkResponse:
        """
        State sync: Load a snapshot
        """
        return LoadSnapshotChunkResponse()

    def apply_snapshot_chunk(self, request: ApplySnapshotChunkRequest) -> ApplySnapshotChunkResponse:
        """
        State sync: Apply a snapshot to state
        """
        return ApplySnapshotChunkResponse()

    def prepare_proposal(self, request: PrepareProposalRequest) -> PrepareProposalResponse:
        """
        Prepare a block proposal by selecting and ordering transactions.
        """
        txs = []
        total_bytes = 0
        for tx in request.txs:
            total_bytes += len(tx)
            if total_bytes > request.max_tx_bytes:
                break
            txs.append(tx)
        return PrepareProposalResponse(txs=txs)

    def process_proposal(self, request: ProcessProposalRequest) -> ProcessProposalResponse:
        """
        Consensus: Process a proposal
        """
        return ProcessProposalResponse(status=1)

    def extend_vote(self, request: ExtendVoteRequest) -> ExtendVoteResponse:
        """
        Consensus: Extend a vote
        """
        return ExtendVoteResponse(vote_extension=b"")

    def verify_vote_extension(self, request: VerifyVoteExtensionRequest) -> VerifyVoteExtensionResponse:
        """
        Consensus: Verify a vote extension
        """
        return VerifyVoteExtensionResponse(status=1)

    def finalize_block(self, request: FinalizeBlockRequest) -> FinalizeBlockResponse:
        """
        Consensus: Finalize a block
        """
        tx_results = []
        for _ in request.txs:
            tx_results.append(ExecTxResult(code=OkCode))
        return FinalizeBlockResponse(tx_results=tx_results)

    def flush(self, request: FlushRequest) -> FlushResponse:
        """
        Flush the mempool
        """
        return FlushResponse()
