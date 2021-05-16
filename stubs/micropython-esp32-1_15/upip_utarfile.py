"""
Module: 'upip_utarfile' on micropython-esp32-1.15
"""
# MCU: {'ver': '1.15', 'port': 'esp32', 'arch': 'xtensawin', 'sysname': 'esp32', 'release': '1.15.0', 'name': 'micropython', 'mpy': 10757, 'version': '1.15.0', 'machine': 'ESP32 module (spiram) with ESP32', 'build': '', 'nodename': 'esp32', 'platform': 'esp32', 'family': 'micropython'}
# Stubber: 1.3.11
from typing import Any

DIRTYPE = 'dir'

class FileSection:
    ''
    def read(self) -> Any:
        pass

    def readinto(self) -> Any:
        pass

    def skip(self) -> Any:
        pass

REGTYPE = 'file'
TAR_HEADER = Any

class TarFile:
    ''
    def extractfile(self) -> Any:
        pass

    def next(self) -> Any:
        pass


class TarInfo:
    ''
def roundup() -> Any:
    pass

uctypes = Any
