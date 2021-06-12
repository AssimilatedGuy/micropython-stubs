from typing import Any

class JSONDecoder:
    def __init__(self, *args: Any) -> None: ...
    def decode() -> None: ...
    def raw_decode() -> None: ...

class JSONEncoder:
    def __init__(self, *args: Any) -> None: ...
    def default() -> None: ...
    def encode() -> None: ...
    item_separator: str = ...
    def iterencode() -> None: ...
    key_separator: str = ...

_default_decoder: Any
_default_encoder: Any
decoder: Any

def dump() -> None: ...
def dumps() -> None: ...

encoder: Any

def load() -> None: ...
def loads() -> None: ...

scanner: Any
