"""
Module: 'logging' on micropython-esp32-1.15
"""
# MCU: {'ver': '1.15', 'port': 'esp32', 'arch': 'xtensawin', 'sysname': 'esp32', 'release': '1.15.0', 'name': 'micropython', 'mpy': 10757, 'version': '1.15.0', 'machine': 'ESP32 module (spiram) with ESP32', 'build': '', 'nodename': 'esp32', 'platform': 'esp32', 'family': 'micropython'}
# Stubber: 1.3.11
from typing import Any

CRITICAL = 50
DEBUG = 10
ERROR = 40
INFO = 20

class Logger:
    ''
    def _level_str(self) -> Any:
        pass

    def critical(self) -> Any:
        pass

    def debug(self) -> Any:
        pass

    def error(self) -> Any:
        pass

    def exc(self) -> Any:
        pass

    def exception(self) -> Any:
        pass

    def info(self) -> Any:
        pass

    def isEnabledFor(self) -> Any:
        pass

    level = 0
    def log(self) -> Any:
        pass

    def setLevel(self) -> Any:
        pass

    def warning(self) -> Any:
        pass

NOTSET = 0
WARNING = 30
_level = 20
_level_dict = Any
_loggers = Any
_stream = Any
def basicConfig() -> Any:
    pass

def debug() -> Any:
    pass

def getLogger() -> Any:
    pass

def info() -> Any:
    pass

sys = Any
