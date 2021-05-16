"""
Module: 'usocket' on micropython-esp32-1.15
"""
# MCU: {'ver': '1.15', 'port': 'esp32', 'arch': 'xtensawin', 'sysname': 'esp32', 'release': '1.15.0', 'name': 'micropython', 'mpy': 10757, 'version': '1.15.0', 'machine': 'ESP32 module (spiram) with ESP32', 'build': '', 'nodename': 'esp32', 'platform': 'esp32', 'family': 'micropython'}
# Stubber: 1.3.11
from typing import Any

AF_INET = 2
AF_INET6 = 10
IPPROTO_IP = 0
IPPROTO_TCP = 6
IPPROTO_UDP = 17
IP_ADD_MEMBERSHIP = 3
SOCK_DGRAM = 2
SOCK_RAW = 3
SOCK_STREAM = 1
SOL_SOCKET = 4095
SO_REUSEADDR = 4
def getaddrinfo() -> Any:
    pass


class socket:
    ''
    def accept(self) -> Any:
        pass

    def bind(self) -> Any:
        pass

    def close(self) -> Any:
        pass

    def connect(self) -> Any:
        pass

    def fileno(self) -> Any:
        pass

    def listen(self) -> Any:
        pass

    def makefile(self) -> Any:
        pass

    def read(self) -> Any:
        pass

    def readinto(self) -> Any:
        pass

    def readline(self) -> Any:
        pass

    def recv(self) -> Any:
        pass

    def recvfrom(self) -> Any:
        pass

    def send(self) -> Any:
        pass

    def sendall(self) -> Any:
        pass

    def sendto(self) -> Any:
        pass

    def setblocking(self) -> Any:
        pass

    def setsockopt(self) -> Any:
        pass

    def settimeout(self) -> Any:
        pass

    def write(self) -> Any:
        pass

