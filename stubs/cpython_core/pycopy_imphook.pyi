import importlib
from typing import Any

_import_hook: Any
_import_exts: Any

class ImphookFileLoader(importlib._bootstrap_external.FileLoader):
    def create_module(self, spec: Any) -> Any: ...
    def exec_module(self, mod: Any) -> None: ...

def setimphook(hook: Any, exts: Any) -> Any: ...
