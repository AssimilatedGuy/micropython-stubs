"""
Module: 'machine' on micropython-esp32-1.15
"""
# MCU: {'ver': '1.15', 'port': 'esp32', 'arch': 'xtensawin', 'sysname': 'esp32', 'release': '1.15.0', 'name': 'micropython', 'mpy': 10757, 'version': '1.15.0', 'machine': 'ESP32 module (spiram) with ESP32', 'build': '', 'nodename': 'esp32', 'platform': 'esp32', 'family': 'micropython'}
# Stubber: 1.3.11
from typing import Any


class ADC:
    def __init__(self, *args):
        ''
        pass

    ATTN_0DB = 0
    ATTN_11DB = 3
    ATTN_2_5DB = 1
    ATTN_6DB = 2
    WIDTH_10BIT = 1
    WIDTH_11BIT = 2
    WIDTH_12BIT = 3
    WIDTH_9BIT = 0
    def atten(self) -> Any:
        pass

    def read(self) -> Any:
        pass

    def read_u16(self) -> Any:
        pass

    def width(self) -> Any:
        pass


class DAC:
    def __init__(self, *args):
        ''
        pass

    def write(self) -> Any:
        pass

DEEPSLEEP = 4
DEEPSLEEP_RESET = 4
EXT0_WAKE = 2
EXT1_WAKE = 3
HARD_RESET = 2

class I2C:
    def __init__(self, *args):
        ''
        pass

    def init(self) -> Any:
        pass

    def readfrom(self) -> Any:
        pass

    def readfrom_into(self) -> Any:
        pass

    def readfrom_mem(self) -> Any:
        pass

    def readfrom_mem_into(self) -> Any:
        pass

    def readinto(self) -> Any:
        pass

    def scan(self) -> Any:
        pass

    def start(self) -> Any:
        pass

    def stop(self) -> Any:
        pass

    def write(self) -> Any:
        pass

    def writeto(self) -> Any:
        pass

    def writeto_mem(self) -> Any:
        pass

    def writevto(self) -> Any:
        pass

PIN_WAKE = 2

class PWM:
    def __init__(self, *args):
        ''
        pass

    def deinit(self) -> Any:
        pass

    def duty(self) -> Any:
        pass

    def freq(self) -> Any:
        pass

    def init(self) -> Any:
        pass

PWRON_RESET = 1

class Pin:
    def __init__(self, *args):
        ''
        pass

    IN = 1
    IRQ_FALLING = 2
    IRQ_RISING = 1
    OPEN_DRAIN = 7
    OUT = 3
    PULL_DOWN = 1
    PULL_HOLD = 4
    PULL_UP = 2
    WAKE_HIGH = 5
    WAKE_LOW = 4
    def init(self) -> Any:
        pass

    def irq(self) -> Any:
        pass

    def off(self) -> Any:
        pass

    def on(self) -> Any:
        pass

    def value(self) -> Any:
        pass


class RTC:
    def __init__(self, *args):
        ''
        pass

    def datetime(self) -> Any:
        pass

    def init(self) -> Any:
        pass

    def memory(self) -> Any:
        pass


class SDCard:
    def __init__(self, *args):
        ''
        pass

    def deinit(self) -> Any:
        pass

    def info(self) -> Any:
        pass

    def ioctl(self) -> Any:
        pass

    def readblocks(self) -> Any:
        pass

    def writeblocks(self) -> Any:
        pass

SLEEP = 2
SOFT_RESET = 5

class SPI:
    def __init__(self, *args):
        ''
        pass

    LSB = 1
    MSB = 0
    def deinit(self) -> Any:
        pass

    def init(self) -> Any:
        pass

    def read(self) -> Any:
        pass

    def readinto(self) -> Any:
        pass

    def write(self) -> Any:
        pass

    def write_readinto(self) -> Any:
        pass


class Signal:
    def __init__(self, *args):
        ''
        pass

    def off(self) -> Any:
        pass

    def on(self) -> Any:
        pass

    def value(self) -> Any:
        pass


class SoftI2C:
    def __init__(self, *args):
        ''
        pass

    def init(self) -> Any:
        pass

    def readfrom(self) -> Any:
        pass

    def readfrom_into(self) -> Any:
        pass

    def readfrom_mem(self) -> Any:
        pass

    def readfrom_mem_into(self) -> Any:
        pass

    def readinto(self) -> Any:
        pass

    def scan(self) -> Any:
        pass

    def start(self) -> Any:
        pass

    def stop(self) -> Any:
        pass

    def write(self) -> Any:
        pass

    def writeto(self) -> Any:
        pass

    def writeto_mem(self) -> Any:
        pass

    def writevto(self) -> Any:
        pass


class SoftSPI:
    def __init__(self, *args):
        ''
        pass

    LSB = 1
    MSB = 0
    def deinit(self) -> Any:
        pass

    def init(self) -> Any:
        pass

    def read(self) -> Any:
        pass

    def readinto(self) -> Any:
        pass

    def write(self) -> Any:
        pass

    def write_readinto(self) -> Any:
        pass

TIMER_WAKE = 4
TOUCHPAD_WAKE = 5

class Timer:
    def __init__(self, *args):
        ''
        pass

    ONE_SHOT = 0
    PERIODIC = 1
    def deinit(self) -> Any:
        pass

    def init(self) -> Any:
        pass

    def value(self) -> Any:
        pass


class TouchPad:
    def __init__(self, *args):
        ''
        pass

    def config(self) -> Any:
        pass

    def read(self) -> Any:
        pass


class UART:
    def __init__(self, *args):
        ''
        pass

    INV_CTS = 8
    INV_RTS = 64
    INV_RX = 4
    INV_TX = 32
    def any(self) -> Any:
        pass

    def deinit(self) -> Any:
        pass

    def init(self) -> Any:
        pass

    def read(self) -> Any:
        pass

    def readinto(self) -> Any:
        pass

    def readline(self) -> Any:
        pass

    def sendbreak(self) -> Any:
        pass

    def write(self) -> Any:
        pass

ULP_WAKE = 6

class WDT:
    def __init__(self, *args):
        ''
        pass

    def feed(self) -> Any:
        pass

WDT_RESET = 3
def deepsleep() -> Any:
    pass

def disable_irq() -> Any:
    pass

def enable_irq() -> Any:
    pass

def freq() -> Any:
    pass

def idle() -> Any:
    pass

def lightsleep() -> Any:
    pass

mem16 = Any
mem32 = Any
mem8 = Any
def reset() -> Any:
    pass

def reset_cause() -> Any:
    pass

def sleep() -> Any:
    pass

def soft_reset() -> Any:
    pass

def time_pulse_us() -> Any:
    pass

def unique_id() -> Any:
    pass

def wake_reason() -> Any:
    pass

