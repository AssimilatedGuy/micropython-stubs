"""
Module: 'onewire' on micropython-esp32-1.15
"""
# MCU: {'ver': '1.15', 'port': 'esp32', 'arch': 'xtensawin', 'sysname': 'esp32', 'release': '1.15.0', 'name': 'micropython', 'mpy': 10757, 'version': '1.15.0', 'machine': 'ESP32 module (spiram) with ESP32', 'build': '', 'nodename': 'esp32', 'platform': 'esp32', 'family': 'micropython'}
# Stubber: 1.3.11
from typing import Any


class OneWire:
    def __init__(self, *args):
        ''
        pass

    MATCH_ROM = 85
    SEARCH_ROM = 240
    SKIP_ROM = 204
    def _search_rom(self) -> Any:
        pass

    def crc8(self) -> Any:
        pass

    def readbit(self) -> Any:
        pass

    def readbyte(self) -> Any:
        pass

    def readinto(self) -> Any:
        pass

    def reset(self) -> Any:
        pass

    def scan(self) -> Any:
        pass

    def select_rom(self) -> Any:
        pass

    def write(self) -> Any:
        pass

    def writebit(self) -> Any:
        pass

    def writebyte(self) -> Any:
        pass


class OneWireError:
    ''
_ow = Any
