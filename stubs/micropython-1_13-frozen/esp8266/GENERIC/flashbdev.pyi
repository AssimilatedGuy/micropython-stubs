from typing import Any, Optional

class FlashBdev:
    SEC_SIZE: int = ...
    start_sec: Any = ...
    blocks: Any = ...
    def __init__(self, start_sec: Any, blocks: Any) -> None: ...
    def readblocks(self, n: Any, buf: Any, off: int = ...) -> None: ...
    def writeblocks(self, n: Any, buf: Any, off: Optional[Any] = ...) -> None: ...
    def ioctl(self, op: Any, arg: Any): ...

size: Any
bdev: Any
start_sec: Any
