from typing import Any

Node = Any

class LS:
    def __repr__(self) -> str: ...
    def __call__(self, path: Any=...) -> None: ...

class PWD:
    def __repr__(self) -> Any: ...
    def __call__(self) -> Any: ...

class CLEAR:
    def __repr__(self) -> str: ...
    def __call__(self) -> Any: ...

class CP:
    def __repr__(self) -> str: ...
    def __call__(self, srcf: Any, destf: Any) -> None: ...

def head(f: Any, n: int=...) -> None: ...
def cat(f: Any) -> None: ...
def newfile(path: Any) -> None: ...

class Man:
    def __repr__(self) -> str: ...