from typing import Any

AUTHENT1A: int
AUTHENT1B: int
ERR: int
NOTAGERR: int
OK: int
REQALL: int
REQIDL: int

class Rfid:
    def _antenna_on() -> None: ...
    def _anticoll() -> None: ...
    def _auth() -> None: ...
    def _available() -> None: ...
    def _cflags() -> None: ...
    def _crc() -> None: ...
    def _get_access() -> None: ...
    def _read() -> None: ...
    def _request() -> None: ...
    def _reset() -> None: ...
    def _rreg() -> None: ...
    def _selectTag() -> None: ...
    def _sflags() -> None: ...
    def _stop_crypto1() -> None: ...
    def _tocard() -> None: ...
    def _wreg() -> None: ...
    def _write() -> None: ...
    def deinit() -> None: ...
    def init() -> None: ...
    def isCardOn() -> None: ...
    def readBlock() -> None: ...
    def readBlockStr() -> None: ...
    def readUid() -> None: ...
    def writeBlock() -> None: ...

def const() -> None: ...

i2c_bus: Any
time: Any
unit: Any
