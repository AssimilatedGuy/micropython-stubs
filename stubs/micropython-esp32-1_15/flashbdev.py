"""
Module: 'flashbdev' on micropython-esp32-1.15
"""
# MCU: {'ver': '1.15', 'port': 'esp32', 'arch': 'xtensawin', 'sysname': 'esp32', 'release': '1.15.0', 'name': 'micropython', 'mpy': 10757, 'version': '1.15.0', 'machine': 'ESP32 module (spiram) with ESP32', 'build': '', 'nodename': 'esp32', 'platform': 'esp32', 'family': 'micropython'}
# Stubber: 1.3.11
from typing import Any


class Partition:
    def __init__(self, *args):
        ''
        pass

    BOOT = 0
    RUNNING = 1
    TYPE_APP = 0
    TYPE_DATA = 1
    def find(self) -> Any:
        pass

    def get_next_update(self) -> Any:
        pass

    def info(self) -> Any:
        pass

    def ioctl(self) -> Any:
        pass

    def mark_app_valid_cancel_rollback(self) -> Any:
        pass

    def readblocks(self) -> Any:
        pass

    def set_boot(self) -> Any:
        pass

    def writeblocks(self) -> Any:
        pass

bdev = Any
