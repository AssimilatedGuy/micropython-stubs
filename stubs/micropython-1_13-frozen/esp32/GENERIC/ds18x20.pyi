from typing import Any

_CONVERT: Any
_RD_SCRATCH: Any
_WR_SCRATCH: Any

class DS18X20:
    ow: Any = ...
    buf: Any = ...
    def __init__(self, onewire: Any) -> None: ...
    def scan(self) -> None: ...
    def convert_temp(self) -> None: ...
    def read_scratch(self, rom: Any) -> Any: ...
    def write_scratch(self, rom: Any, buf: Any) -> None: ...
    def read_temp(self, rom: Any) -> Any: ...
