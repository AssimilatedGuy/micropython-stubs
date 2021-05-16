"""
Module: '_thread' on micropython-esp32-1.15
"""
# MCU: {'ver': '1.15', 'port': 'esp32', 'arch': 'xtensawin', 'sysname': 'esp32', 'release': '1.15.0', 'name': 'micropython', 'mpy': 10757, 'version': '1.15.0', 'machine': 'ESP32 module (spiram) with ESP32', 'build': '', 'nodename': 'esp32', 'platform': 'esp32', 'family': 'micropython'}
# Stubber: 1.3.11
from typing import Any


class LockType:
    ''
    def acquire(self) -> Any:
        pass

    def locked(self) -> Any:
        pass

    def release(self) -> Any:
        pass

def allocate_lock() -> Any:
    pass

def exit() -> Any:
    pass

def get_ident() -> Any:
    pass

def stack_size() -> Any:
    pass

def start_new_thread() -> Any:
    pass

