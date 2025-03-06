"""
TCP Server that communicates with Tendermint
"""
import asyncio
import signal
import platform
from .utils import read_messages, write_message, get_logger
from io import BytesIO
from .types import Request, Response, ExceptionResponse
from .application import BaseApplication

DefaultABCIPort = 26658
MaxReadInBytes = 64 * 1024  # Max we'll consume on a read stream

log = get_logger("abci.server")


class ProtocolHandler:
    """
    Internal handler called by the server to process requests from
    Tendermint.  The handler delegates calls to your application
    """

    app: BaseApplication

    def __init__(self, app):
        self.app = app

    def process(self, req_type: str, req) -> bytes:
        handler = getattr(self, req_type, self.no_match)
        return handler(req)

    def info(self, req) -> bytes:
        result = self.app.Info(req.info)
        response = Response(info=result)
        return write_message(response)

    def check_tx(self, req) -> bytes:
        result = self.app.CheckTx(req.check_tx)
        response = Response(check_tx=result)
        return write_message(response)

    def commit(self, req) -> bytes:
        result = self.app.Commit(req.commit)
        response = Response(commit=result)
        return write_message(response)

    def query(self, req) -> bytes:
        result = self.app.Query(req.query)
        response = Response(query=result)
        return write_message(response)

    def init_chain(self, req) -> bytes:
        result = self.app.InitChain(req.init_chain)
        response = Response(init_chain=result)
        return write_message(response)

    def list_snapshots(self, req) -> bytes:
        result = self.app.ListSnapshots(req.list_snapshots)
        response = Response(list_snapshots=result)
        return write_message(response)

    def offer_snapshot(self, req) -> bytes:
        result = self.app.OfferSnapshot(req.offer_snapshot)
        response = Response(offer_snapshot=result)
        return write_message(response)

    def load_snapshot_chunk(self, req) -> bytes:
        result = self.app.LoadSnapshotChunk(req.load_snapshot_chunk)
        response = Response(load_snapshot_chunk=result)
        return write_message(response)

    def apply_snapshot_chunk(self, req) -> bytes:
        result = self.app.ApplySnapshotChunk(req.apply_snapshot_chunk)
        response = Response(apply_snapshot_chunk=result)
        return write_message(response)

    def prepare_proposal(self, req) -> bytes:
        result = self.app.PrepareProposal(req.prepare_proposal)
        response = Response(prepare_proposal=result)
        return write_message(response)

    def process_proposal(self, req) -> bytes:
        result = self.app.ProcessProposal(req.process_proposal)
        response = Response(process_proposal=result)
        return write_message(response)

    def extend_vote(self, req) -> bytes:
        result = self.app.ExtendVote(req.extend_vote)
        response = Response(extend_vote=result)
        return write_message(response)

    def verify_vote_extension(self, req) -> bytes:
        result = self.app.VerifyVoteExtension(req.verify_vote_extension)
        response = Response(verify_vote_extension=result)
        return write_message(response)

    def finalize_block(self, req) -> bytes:
        result = self.app.FinalizeBlock(req.finalize_block)
        response = Response(finalize_block=result)
        return write_message(response)
 
    def no_match(self, req) -> bytes:
        response = Response(
            exception=ExceptionResponse(error="ABCI request not found")
        )
        return write_message(response)


class ABCIServer:
    """
    Async TCP server
    """

    port: int
    protocol: ProtocolHandler

    def __init__(self, app: BaseApplication, port=DefaultABCIPort) -> None:
        """
        Requires App and an optional port if you changed the ABCI port on
        Tendermint
        """
        if not app or not isinstance(app, BaseApplication):
            raise TypeError(
                "Application missing or not an instance of ABCI Base Application"
            )
        self.port = port
        self.protocol = ProtocolHandler(app)

    def run(self) -> None:
        """
        Run the application
        """
        # Check OS to handle signals appropriately
        on_windows = platform.system() == "Windows"

        loop = asyncio.get_event_loop()
        if not on_windows:
            # Unix...register signal handlers
            loop.add_signal_handler(
                signal.SIGINT, lambda: asyncio.create_task(_stop())
            )
            loop.add_signal_handler(
                signal.SIGTERM, lambda: asyncio.create_task(_stop())
            )
        try:
            log.info(" ~ running app - press CTRL-C to stop ~")
            loop.run_until_complete(self._start())
        except:
            log.warn(" ... shutting down")
            if on_windows:
                loop.run_until_complete(_stop())
        finally:
            loop.stop()

    async def _start(self) -> None:
        self.server = await asyncio.start_server(
            self._handler,
            host="0.0.0.0",
            port=self.port,
        )
        await self.server.serve_forever()

    async def _handler(
        self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter
    ) -> None:
        ip, socket, *_ = writer.get_extra_info("peername")
        log.info(f" ... connection @ {ip}:{socket}")

        data = BytesIO()
        last_pos = 0

        while True:
            if last_pos == data.tell():
                data = BytesIO()
                last_pos = 0

            bits = await reader.read(MaxReadInBytes)
            if len(bits) == 0:
                log.error(" ... tendermint closed connection")
                # break to the _stop if the connection stops
                break

            data.write(bits)
            data.seek(last_pos)

            ## Tendermint prefixes each serialized protobuf message
            ## with varint encoded length. We use the 'data' buffer to
            ## keep track of where we are in the byte stream and progress
            ## based on the length encoding
            for message in read_messages(data, Request):
                req_type = message.WhichOneof("value")
                response = self.protocol.process(req_type, message)
                writer.write(response)
                last_pos = data.tell()

        # Any connection fails and we shut the whole thing down
        await _stop()


async def _stop() -> None:
    """
    Clean up all async tasks.  Called on a signal or a connection closed by
    tendermint
    """
    log.warn(" ... received exit signal")
    tasks = [t for t in asyncio.all_tasks() if t is not asyncio.current_task()]
    for task in tasks:
        task.cancel()
    await asyncio.gather(*tasks, return_exceptions=True)
