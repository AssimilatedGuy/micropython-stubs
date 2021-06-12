"""
Module: 'uasyncio.__init__' on pyboard 1.13.0-95
"""
# MCU: (sysname='pyboard', nodename='pyboard', release='1.13.0', version='v1.13-95-g0fff2e03f on 2020-10-03', machine='PYBv1.1 with STM32F405RG')
# Stubber: 1.3.4

class CancelledError:
    ''

class Event:
    def __init__(self, *args):
        ''
        pass

    def clear():
        pass

    def is_set():
        pass

    def set():
        pass

    wait = None

class IOQueue:
    def __init__(self, *args):
        ''
        pass

    def _dequeue():
        pass

    def _enqueue():
        pass

    def queue_read():
        pass

    def queue_write():
        pass

    def remove():
        pass

    def wait_io_event():
        pass


class Lock:
    def __init__(self, *args):
        ''
        pass

    acquire = None
    def locked():
        pass

    def release():
        pass


class Loop:
    def __init__(self, *args):
        ''
        pass

    _exc_handler = None
    def call_exception_handler():
        pass

    def close():
        pass

    def create_task():
        pass

    def default_exception_handler():
        pass

    def get_exception_handler():
        pass

    def run_forever():
        pass

    def run_until_complete():
        pass

    def set_exception_handler():
        pass

    def stop():
        pass


class SingletonGenerator:
    def __init__(self, *args):
        ''
        pass


class StreamReader:
    def __init__(self, *args):
        ''
        pass

    aclose = None
    awrite = None
    awritestr = None
    def close():
        pass

    drain = None
    def get_extra_info():
        pass

    read = None
    readexactly = None
    readline = None
    wait_closed = None
    def write():
        pass


class StreamWriter:
    def __init__(self, *args):
        ''
        pass

    aclose = None
    awrite = None
    awritestr = None
    def close():
        pass

    drain = None
    def get_extra_info():
        pass

    read = None
    readexactly = None
    readline = None
    wait_closed = None
    def write():
        pass


class Task:
    def __init__(self, *args):
        ''
        pass

