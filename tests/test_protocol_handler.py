from io import BytesIO

from abci.application import BaseApplication, OkCode
from abci.server import ProtocolHandler
from abci.utils import read_messages

from cometbft.abci.v1.types_pb2 import (
    Request,
    Response,
    FlushRequest,
    FlushResponse,
    InitChainRequest,
    InitChainResponse,
    InfoRequest,
    InfoResponse,
    CheckTxRequest,
    CheckTxResponse,
    QueryRequest,
    QueryResponse,
    FinalizeBlockRequest,
    FinalizeBlockResponse,
    CommitRequest,
    CommitResponse,
    ValidatorUpdate,
    ExecTxResult,
)

from cometbft.crypto.v1.keys_pb2 import PublicKey



class ExampleApp(BaseApplication):
    def __init__(self):
        self.validators = []

    def Info(self, req):
        v = req.version
        r = InfoResponse(
            version=v,
            data="hello",
            last_block_height=0,
            last_block_app_hash=b"0x12",
        )
        return r

    def InitChain(self, req):
        self.validators = req.validators
        return InitChainResponse()

    def CheckTx(self, req):
        return CheckTxResponse(code=OkCode, data=req.tx, log="bueno")

    def Query(self, req):
        d = req.data
        return QueryResponse(code=OkCode, value=d)

    def FinalizeBlock(self, req):
        # Create a TxResult for the transaction
        tx_result = ExecTxResult(
            code=OkCode,
            data=req.txs[0] if req.txs else b"",
            log="bueno"
        )
        
        return FinalizeBlockResponse(
            events=[],
            tx_results=[tx_result],
            validator_updates=[],
            consensus_param_updates=None,
            app_hash=b"hash"
        )

    def Commit(self, req):
        # CommitResponse doesn't have a data field in the current protobuf definition
        # It only has retain_height field according to the error
        return CommitResponse(retain_height=0)


def __deserialze(raw: bytes) -> Request:
    resp = next(read_messages(BytesIO(raw), Response))
    return resp


def test_handler():
    app = ExampleApp()
    p = ProtocolHandler(app)

    # Flush
    req = Request(flush=FlushRequest())
    raw = p.process("flush", req)
    resp = __deserialze(raw)
    assert isinstance(resp.flush, FlushResponse)

    # Echo
    # req = Request(echo=RequestEcho(message="hello"))
    # raw = p.process("echo", req)
    # resp = __deserialze(raw)
    # assert resp.echo.message == "hello"

    # Info
    req = Request(info=InfoRequest(version="16"))
    raw = p.process("info", req)
    resp = __deserialze(raw)
    assert resp.info.version == "16"
    assert resp.info.data == "hello"
    assert resp.info.last_block_height == 0
    assert resp.info.last_block_app_hash == b"0x12"

    # init_chain
    val_a = ValidatorUpdate(power=10, pub_key_type="ed25519", pub_key_bytes=b"a_pub_key")
    val_b = ValidatorUpdate(power=10, pub_key_type="ed25519", pub_key_bytes=b"b_pub_key")

    v = [val_a, val_b]
    req = Request(init_chain=InitChainRequest(validators=v))
    raw = p.process("init_chain", req)
    resp = __deserialze(raw)
    assert isinstance(resp.init_chain, InitChainResponse)

    # check_tx
    req = Request(check_tx=CheckTxRequest(tx=b"helloworld"))
    raw = p.process("check_tx", req)
    resp = __deserialze(raw)
    assert resp.check_tx.code == OkCode
    assert resp.check_tx.data == b"helloworld"
    assert resp.check_tx.log == "bueno"

    # finalize_block
    req = Request(finalize_block=FinalizeBlockRequest(txs=[b"helloworld"]))
    raw = p.process("finalize_block", req)
    resp = __deserialze(raw)
    assert resp.finalize_block.tx_results[0].code == OkCode
    assert resp.finalize_block.tx_results[0].data == b"helloworld"
    assert resp.finalize_block.tx_results[0].log == "bueno"

    # query
    req = Request(query=QueryRequest(path="/dave", data=b"0x12"))
    raw = p.process("query", req)
    resp = __deserialze(raw)
    assert resp.query.code == OkCode
    assert resp.query.value == b"0x12"

    # Commit
    req = Request(commit=CommitRequest())
    raw = p.process("commit", req)
    resp = __deserialze(raw)
    assert isinstance(resp.commit, CommitResponse)
    assert resp.commit.retain_height == 0

    # No match
    raw = p.process("whatever", None)
    resp = __deserialze(raw)
    assert resp.exception.error == "ABCI request not found"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_handler()
