from typing import Any

ACCESS_COPY: int
ACCESS_READ: int
ACCESS_WRITE: int
MAP_PRIVATE: int
MAP_SHARED: int
PROT_EXEC: int
PROT_READ: int
PROT_WRITE: int

class mmap:
    def __init__(self, *args: Any) -> None: ...
    def close() -> None: ...
    def read() -> None: ...
    def seek() -> None: ...
    def write() -> None: ...
