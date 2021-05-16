"""
Module: 'ubluetooth' on micropython-esp32-1.15
"""
# MCU: {'ver': '1.15', 'port': 'esp32', 'arch': 'xtensawin', 'sysname': 'esp32', 'release': '1.15.0', 'name': 'micropython', 'mpy': 10757, 'version': '1.15.0', 'machine': 'ESP32 module (spiram) with ESP32', 'build': '', 'nodename': 'esp32', 'platform': 'esp32', 'family': 'micropython'}
# Stubber: 1.3.11
from typing import Any


class BLE:
    ''
    def active(self) -> Any:
        pass

    def config(self) -> Any:
        pass

    def gap_advertise(self) -> Any:
        pass

    def gap_connect(self) -> Any:
        pass

    def gap_disconnect(self) -> Any:
        pass

    def gap_scan(self) -> Any:
        pass

    def gattc_discover_characteristics(self) -> Any:
        pass

    def gattc_discover_descriptors(self) -> Any:
        pass

    def gattc_discover_services(self) -> Any:
        pass

    def gattc_exchange_mtu(self) -> Any:
        pass

    def gattc_read(self) -> Any:
        pass

    def gattc_write(self) -> Any:
        pass

    def gatts_indicate(self) -> Any:
        pass

    def gatts_notify(self) -> Any:
        pass

    def gatts_read(self) -> Any:
        pass

    def gatts_register_services(self) -> Any:
        pass

    def gatts_set_buffer(self) -> Any:
        pass

    def gatts_write(self) -> Any:
        pass

    def irq(self) -> Any:
        pass

FLAG_INDICATE = 32
FLAG_NOTIFY = 16
FLAG_READ = 2
FLAG_WRITE = 8
FLAG_WRITE_NO_RESPONSE = 4

class UUID:
    ''
