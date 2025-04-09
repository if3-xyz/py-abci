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
        Query Connection: Provide information about the application state.
        
        Called during startup to synchronize CometBFT with the application.
        A stateful application should return the last block height and app hash
        to prevent CometBFT from replaying the transaction log from the beginning.
        These values help CometBFT determine how to synchronize the node.
        
        If block height is 0, CometBFT will call init_chain().
        """
        return InfoResponse()

    def check_tx(self, request: CheckTxRequest) -> CheckTxResponse:
        """
        Mempool Connection: Validate transactions before they enter the mempool.
        
        Called when a new transaction is added to the mempool.
        Validates transactions before they are broadcasted to other peers.
        Applications can perform stateful or stateless checks.
        
        If response code is 0 (OK), the tx is added to the mempool for consideration in a block.
        A non-zero response code indicates an error and the transaction will be rejected.
        """
        return CheckTxResponse(code=OkCode)

    def commit(self, request: CommitRequest) -> CommitResponse:
        """
        Consensus Connection: Commit the current application state.
        
        Called after finalize_block. Applications should persist their state at this point.
        Should return a deterministic commitment of the current application state.
        Typically a cryptographic commitment to the state (e.g., Merkle root hash).
        
        The returned data is included in the header of the next block.
        Can also return a retain_height to indicate to CometBFT which heights can be pruned.
        """
        return CommitResponse(retain_height=1)

    def query(self, request: QueryRequest) -> QueryResponse:
        """
        Query Connection: Query the application state.
        
        Main method for clients to query the application state directly.
        Can be used for both public and private data with appropriate authentication.
        Queries do not affect the blockchain state and are not broadcasted to other nodes.
        
        A non-zero 'code' in the response indicates an error.
        Applications may implement domain-specific queries by path/data parsing.
        """
        return QueryResponse(code=OkCode)

    def init_chain(self, request: InitChainRequest) -> InitChainResponse:
        """
        Consensus Connection: Initialize chain with genesis state.
        
        Called once upon genesis (when block height is 0).
        Contains information from the genesis file.
        Applications should validate and initialize chain state from the genesis parameters,
        including consensus parameters, validators, and application-specific genesis state.
        
        May return consensus parameters updates and initial validator set updates.
        """
        return InitChainResponse()

    def list_snapshots(self, request: ListSnapshotsRequest) -> ListSnapshotsResponse:
        """
        State Sync Connection: Return available application state snapshots.
        
        Allows CometBFT to discover available snapshots for state synchronization.
        Applications should return metadata about available snapshots.
        Used by new nodes to catch up quickly without replaying all historical blocks.
        
        Returns a list of snapshots, each with height, format, chunks, hash, and metadata.
        """
        return ListSnapshotsResponse()

    def offer_snapshot(self, request: OfferSnapshotRequest) -> OfferSnapshotResponse:
        """
        State Sync Connection: Offer a snapshot to the application.
        
        Called when CometBFT has discovered a snapshot from peers.
        Applications should determine if they can and want to restore from the offered snapshot.
        
        Can accept or reject the snapshot, with various rejection reasons available.
        Applications may choose to accept a snapshot but abort if chunks fail to apply.
        """
        return OfferSnapshotResponse()

    def load_snapshot_chunk(self, request: LoadSnapshotChunkRequest) -> LoadSnapshotChunkResponse:
        """
        State Sync Connection: Load a snapshot chunk.
        
        Called when a peer requests a specific chunk of a snapshot.
        Applications should return the requested binary chunk data.
        
        Used by other nodes to retrieve snapshot data for state synchronization.
        """
        return LoadSnapshotChunkResponse()

    def apply_snapshot_chunk(self, request: ApplySnapshotChunkRequest) -> ApplySnapshotChunkResponse:
        """
        State Sync Connection: Apply a snapshot chunk to the application state.
        
        Called with chunks of an accepted snapshot in sequential order.
        Applications should apply each chunk to restore application state incrementally.
        
        Can reject chunks that are invalid or indicate progress through the chunks.
        Rejecting a chunk will cause CometBFT to try a different snapshot.
        """
        return ApplySnapshotChunkResponse()

    def prepare_proposal(self, request: PrepareProposalRequest) -> PrepareProposalResponse:
        """
        Consensus Connection: Prepare a new block proposal.
        
        Called when a validator is selected as the proposer for a block.
        Applications can modify the raw transaction bytes from the mempool.
        Can reorder, remove, or modify transactions before they are proposed in a block.
        
        Allows application-level customization of block proposals, such as:
        - Transaction ordering/prioritization
        - Censorship resistance mechanisms
        - Specialized transaction handling
        - Validation of dependent transactions
        
        Must respect max_tx_bytes limit for total size of transactions.
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
        Consensus Connection: Process and validate a block proposal.
        
        Called on validator nodes when they receive a proposal from the designated proposer.
        Allows the application to validate the block proposal as a whole.
        Applications can perform stateful validation of the entire transaction set.
        
        Returns a status indicating whether the proposal is valid.
        Rejecting proposals is a mechanism for application-determined fork choice.
        """
        return ProcessProposalResponse(status=1)

    def extend_vote(self, request: ExtendVoteRequest) -> ExtendVoteResponse:
        """
        Consensus Connection: Add application-specific information to a consensus vote.
        
        Called when a validator is about to sign a consensus vote.
        Applications can attach custom data (extensions) to votes.
        These extensions can be used to implement application-level voting rules.
        
        Extensions are opaque to CometBFT but are included in vote messages.
        Can be used for various application-layer consensus features.
        """
        return ExtendVoteResponse(vote_extension=b"")

    def verify_vote_extension(self, request: VerifyVoteExtensionRequest) -> VerifyVoteExtensionResponse:
        """
        Consensus Connection: Verify vote extensions received from other validators.
        
        Called when a node receives a vote from another validator.
        Applications can validate the extension data attached to votes.
        Allows implementing application-specific validation rules for vote extensions.
        
        Returns a status indicating if the extension is valid.
        Invalid extensions may influence how votes are counted in some applications.
        """
        return VerifyVoteExtensionResponse(status=1)

    def finalize_block(self, request: FinalizeBlockRequest) -> FinalizeBlockResponse:
        """
        Consensus Connection: Execute transactions and update application state.
        
        Called after a block has been decided in consensus but before committing.
        Applications should execute all transactions in the block and update their state.
        Transactions must be executed deterministically in the specified order.
        
        Returns execution results for each transaction.
        Can also return validator set updates, consensus parameter updates, and events.
        The resulting state is not yet considered committed until commit() is called.
        """
        tx_results = []
        for _ in request.txs:
            tx_results.append(ExecTxResult(code=OkCode))
        return FinalizeBlockResponse(tx_results=tx_results)

    def flush(self, request: FlushRequest) -> FlushResponse:
        """
        Signals the application to flush any pending operations.
        
        Called by CometBFT to ensure all pending operations are written.
        Applications should ensure any buffered data is persisted.
        Part of CometBFT's synchronization mechanism with the application.
        """
        return FlushResponse()
