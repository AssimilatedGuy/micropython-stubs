from typing import Any

CRITICAL: int
DEBUG: int
ERROR: int
INFO: int

class Logger:
    def _level_str() -> None: ...
    def critical() -> None: ...
    def debug() -> None: ...
    def error() -> None: ...
    def exc() -> None: ...
    def exception() -> None: ...
    def info() -> None: ...
    def isEnabledFor() -> None: ...
    level: int = ...
    def log() -> None: ...
    def setLevel() -> None: ...
    def warning() -> None: ...

NOTSET: int
WARNING: int
_level: int
_level_dict: Any
_loggers: Any
_stream: Any

def basicConfig() -> None: ...
def debug() -> None: ...
def getLogger() -> None: ...
def info() -> None: ...

sys: Any
