from typing import Any

class NeoPixel:
    ORDER: Any = ...
    pin: Any = ...
    n: Any = ...
    bpp: Any = ...
    buf: Any = ...
    def __init__(self, pin: Any, n: Any, bpp: int = ...) -> None: ...
    def __setitem__(self, index: Any, val: Any) -> None: ...
    def __getitem__(self, index: Any): ...
    def fill(self, color: Any) -> None: ...
    def write(self) -> None: ...
