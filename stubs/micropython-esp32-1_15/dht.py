"""
Module: 'dht' on micropython-esp32-1.15
"""
# MCU: {'ver': '1.15', 'port': 'esp32', 'arch': 'xtensawin', 'sysname': 'esp32', 'release': '1.15.0', 'name': 'micropython', 'mpy': 10757, 'version': '1.15.0', 'machine': 'ESP32 module (spiram) with ESP32', 'build': '', 'nodename': 'esp32', 'platform': 'esp32', 'family': 'micropython'}
# Stubber: 1.3.11
from typing import Any


class DHT11:
    ''
    def humidity(self) -> Any:
        pass

    def measure(self) -> Any:
        pass

    def temperature(self) -> Any:
        pass


class DHT22:
    ''
    def humidity(self) -> Any:
        pass

    def measure(self) -> Any:
        pass

    def temperature(self) -> Any:
        pass


class DHTBase:
    ''
    def measure(self) -> Any:
        pass

def dht_readinto() -> Any:
    pass

