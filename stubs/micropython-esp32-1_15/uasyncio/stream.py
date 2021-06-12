"""
Module: 'uasyncio.stream' on micropython-esp32-1.15
"""
# MCU: {'ver': '1.15', 'port': 'esp32', 'arch': 'xtensawin', 'sysname': 'esp32', 'release': '1.15.0', 'name': 'micropython', 'mpy': 10757, 'version': '1.15.0', 'machine': 'ESP32 module (spiram) with ESP32', 'build': '', 'nodename': 'esp32', 'platform': 'esp32', 'family': 'micropython'}
# Stubber: 1.3.11
from typing import Any


class Server:
    def __init__(self, *args):
        ''
        pass

    _serve = Any
    def close(self) -> Any:
        pass

    wait_closed = Any

class Stream:
    def __init__(self, *args):
        ''
        pass

    aclose = Any
    awrite = Any
    awritestr = Any
    def close(self) -> Any:
        pass

    drain = Any
    def get_extra_info(self) -> Any:
        pass

    read = Any
    readexactly = Any
    readline = Any
    wait_closed = Any
    def write(self) -> Any:
        pass


class StreamReader:
    def __init__(self, *args):
        ''
        pass

    aclose = Any
    awrite = Any
    awritestr = Any
    def close(self) -> Any:
        pass

    drain = Any
    def get_extra_info(self) -> Any:
        pass

    read = Any
    readexactly = Any
    readline = Any
    wait_closed = Any
    def write(self) -> Any:
        pass


class StreamWriter:
    def __init__(self, *args):
        ''
        pass

    aclose = Any
    awrite = Any
    awritestr = Any
    def close(self) -> Any:
        pass

    drain = Any
    def get_extra_info(self) -> Any:
        pass

    read = Any
    readexactly = Any
    readline = Any
    wait_closed = Any
    def write(self) -> Any:
        pass

core = Any
open_connection = Any
start_server = Any
stream_awrite = Any
