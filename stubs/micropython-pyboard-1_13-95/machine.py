"""
Module: 'machine' on pyboard 1.13.0-95
"""
# MCU: (sysname='pyboard', nodename='pyboard', release='1.13.0', version='v1.13-95-g0fff2e03f on 2020-10-03', machine='PYBv1.1 with STM32F405RG')
# Stubber: 1.3.4

class ADC:
    def __init__(self, *args):
        ''
        pass

    CORE_TEMP = 16
    CORE_VBAT = 18
    CORE_VREF = 17
    VREF = 65535
    def read_u16():
        pass

DEEPSLEEP_RESET = 4
HARD_RESET = 2

class I2C:
    def __init__(self, *args):
        ''
        pass

    def init():
        pass

    def readfrom():
        pass

    def readfrom_into():
        pass

    def readfrom_mem():
        pass

    def readfrom_mem_into():
        pass

    def readinto():
        pass

    def scan():
        pass

    def start():
        pass

    def stop():
        pass

    def write():
        pass

    def writeto():
        pass

    def writeto_mem():
        pass

    def writevto():
        pass

PWRON_RESET = 1

class Pin:
    def __init__(self, *args):
        ''
        pass

    AF1_TIM1 = 1
    AF1_TIM2 = 1
    AF2_TIM3 = 2
    AF2_TIM4 = 2
    AF2_TIM5 = 2
    AF3_TIM10 = 3
    AF3_TIM11 = 3
    AF3_TIM8 = 3
    AF3_TIM9 = 3
    AF4_I2C1 = 4
    AF4_I2C2 = 4
    AF5_SPI1 = 5
    AF5_SPI2 = 5
    AF7_USART1 = 7
    AF7_USART2 = 7
    AF7_USART3 = 7
    AF8_UART4 = 8
    AF8_USART6 = 8
    AF9_CAN1 = 9
    AF9_CAN2 = 9
    AF9_TIM12 = 9
    AF9_TIM13 = 9
    AF9_TIM14 = 9
    AF_OD = 18
    AF_PP = 2
    ALT = 2
    ALT_OPEN_DRAIN = 18
    ANALOG = 3
    IN = 0
    IRQ_FALLING = 270598144
    IRQ_RISING = 269549568
    OPEN_DRAIN = 17
    OUT = 1
    OUT_OD = 17
    OUT_PP = 1
    PULL_DOWN = 2
    PULL_NONE = 0
    PULL_UP = 1
    def af():
        pass

    def af_list():
        pass

    board = None
    cpu = None
    def debug():
        pass

    def dict():
        pass

    def gpio():
        pass

    def high():
        pass

    def init():
        pass

    def irq():
        pass

    def low():
        pass

    def mapper():
        pass

    def mode():
        pass

    def name():
        pass

    def names():
        pass

    def off():
        pass

    def on():
        pass

    def pin():
        pass

    def port():
        pass

    def pull():
        pass

    def value():
        pass


class RTC:
    def __init__(self, *args):
        ''
        pass

    def calibration():
        pass

    def datetime():
        pass

    def info():
        pass

    def init():
        pass

    def wakeup():
        pass

SOFT_RESET = 0

class SPI:
    def __init__(self, *args):
        ''
        pass

    LSB = 128
    MSB = 0
    def deinit():
        pass

    def init():
        pass

    def read():
        pass

    def readinto():
        pass

    def write():
        pass

    def write_readinto():
        pass


class Signal:
    def __init__(self, *args):
        ''
        pass

    def off():
        pass

    def on():
        pass

    def value():
        pass


class SoftI2C:
    def __init__(self, *args):
        ''
        pass

    def init():
        pass

    def readfrom():
        pass

    def readfrom_into():
        pass

    def readfrom_mem():
        pass

    def readfrom_mem_into():
        pass

    def readinto():
        pass

    def scan():
        pass

    def start():
        pass

    def stop():
        pass

    def write():
        pass

    def writeto():
        pass

    def writeto_mem():
        pass

    def writevto():
        pass


class SoftSPI:
    def __init__(self, *args):
        ''
        pass

    LSB = 128
    MSB = 0
    def deinit():
        pass

    def init():
        pass

    def read():
        pass

    def readinto():
        pass

    def write():
        pass

    def write_readinto():
        pass


class Timer:
    def __init__(self, *args):
        ''
        pass

    ONE_SHOT = 1
    PERIODIC = 2
    def deinit():
        pass

    def init():
        pass


class UART:
    def __init__(self, *args):
        ''
        pass

    CTS = 512
    IRQ_RXIDLE = 16
    RTS = 256
    def any():
        pass

    def deinit():
        pass

    def init():
        pass

    def irq():
        pass

    def read():
        pass

    def readchar():
        pass

    def readinto():
        pass

    def readline():
        pass

    def sendbreak():
        pass

    def write():
        pass

    def writechar():
        pass


class WDT:
    def __init__(self, *args):
        ''
        pass

    def feed():
        pass

WDT_RESET = 3
def bootloader():
    pass

def deepsleep():
    pass

def disable_irq():
    pass

def enable_irq():
    pass

def freq():
    pass

def idle():
    pass

def info():
    pass

def lightsleep():
    pass

mem16 = None
mem32 = None
mem8 = None
def reset():
    pass

def reset_cause():
    pass

def rng():
    pass

def sleep():
    pass

def soft_reset():
    pass

def time_pulse_us():
    pass

def unique_id():
    pass

