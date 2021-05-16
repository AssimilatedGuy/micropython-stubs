"""
Module: 'esp32' on micropython-esp32-1.15
"""
# MCU: {'ver': '1.15', 'port': 'esp32', 'arch': 'xtensawin', 'sysname': 'esp32', 'release': '1.15.0', 'name': 'micropython', 'mpy': 10757, 'version': '1.15.0', 'machine': 'ESP32 module (spiram) with ESP32', 'build': '', 'nodename': 'esp32', 'platform': 'esp32', 'family': 'micropython'}
# Stubber: 1.3.11
from typing import Any

HEAP_DATA = 4
HEAP_EXEC = 1

class NVS:
    ''
    def commit(self) -> Any:
        pass

    def erase_key(self) -> Any:
        pass

    def get_blob(self) -> Any:
        pass

    def get_i32(self) -> Any:
        pass

    def set_blob(self) -> Any:
        pass

    def set_i32(self) -> Any:
        pass


class Partition:
    ''
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


class RMT:
    ''
    def clock_div(self) -> Any:
        pass

    def deinit(self) -> Any:
        pass

    def loop(self) -> Any:
        pass

    def source_freq(self) -> Any:
        pass

    def wait_done(self) -> Any:
        pass

    def write_pulses(self) -> Any:
        pass


class ULP:
    ''
    RESERVE_MEM = 512
    def load_binary(self) -> Any:
        pass

    def run(self) -> Any:
        pass

    def set_wakeup_period(self) -> Any:
        pass

WAKEUP_ALL_LOW = Any
WAKEUP_ANY_HIGH = Any
def hall_sensor() -> Any:
    pass

def idf_heap_info() -> Any:
    pass

def raw_temperature() -> Any:
    pass

def wake_on_ext0() -> Any:
    pass

def wake_on_ext1() -> Any:
    pass

def wake_on_touch() -> Any:
    pass

