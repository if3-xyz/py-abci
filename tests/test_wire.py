from io import BytesIO

from abci.utils import write_message, read_messages

from cometbft.abci.v1.types_pb2 import (
    Request,
    FinalizeBlockRequest,
    EchoRequest,
    InfoRequest,
)


def test_raw_decoding():
    from io import BytesIO

    # info request
    inbound = b"\x0f\x1a\r\n\x070.34.24\x10\x0b\x18\x08"
    data = BytesIO(inbound)

    req_type = next(read_messages(data, Request))
    assert "info" == req_type.WhichOneof("value")

    assert data.read() == b""


def test_encoding_decoding():
    echo = Request(echo=EchoRequest(message="hello"))
    raw = write_message(echo)
    buffer = BytesIO(raw)
    req = next(read_messages(buffer, Request))
    assert "echo" == req.WhichOneof("value")

    info = Request(info=InfoRequest(version="18.0"))
    raw1 = write_message(info)
    buffer1 = BytesIO(raw1)
    req = next(read_messages(buffer1, Request))
    assert "info" == req.WhichOneof("value")


def test_check_reading_batch():
    bits = b""
    for i in range(20):
        tx = (i).to_bytes(2, byteorder="big")
        bits += write_message(FinalizeBlockRequest(txs=[tx]))

    result = [m.txs[0] for m in read_messages(BytesIO(bits), FinalizeBlockRequest)]
    assert len(result) == 20


if __name__ == "__main__":
    test_raw_decoding()
    test_encoding_decoding()
    test_check_reading_batch()
    print("All tests passed!")
