"""
Module: 'uasyncio.__init__' on micropython-esp32-1.15
"""
# MCU: {'ver': '1.15', 'port': 'esp32', 'arch': 'xtensawin', 'sysname': 'esp32', 'release': '1.15.0', 'name': 'micropython', 'mpy': 10757, 'version': '1.15.0', 'machine': 'ESP32 module (spiram) with ESP32', 'build': '', 'nodename': 'esp32', 'platform': 'esp32', 'family': 'micropython'}
# Stubber: 1.3.11
from typing import Any


class CancelledError:
    ''

class Event:
    ''
    def clear(self) -> Any:
        pass

    def is_set(self) -> Any:
        pass

    def set(self) -> Any:
        pass

    wait = Any

class IOQueue:
    ''
    def _dequeue(self) -> Any:
        pass

    def _enqueue(self) -> Any:
        pass

    def queue_read(self) -> Any:
        pass

    def queue_write(self) -> Any:
        pass

    def remove(self) -> Any:
        pass

    def wait_io_event(self) -> Any:
        pass


class Lock:
    ''
    acquire = Any
    def locked(self) -> Any:
        pass

    def release(self) -> Any:
        pass


class Loop:
    ''
    _exc_handler = Any
    def call_exception_handler(self) -> Any:
        pass

    def close(self) -> Any:
        pass

    def create_task(self) -> Any:
        pass

    def default_exception_handler(self) -> Any:
        pass

    def get_exception_handler(self) -> Any:
        pass

    def run_forever(self) -> Any:
        pass

    def run_until_complete(self) -> Any:
        pass

    def set_exception_handler(self) -> Any:
        pass

    def stop(self) -> Any:
        pass


class SingletonGenerator:
    ''

class StreamReader:
    ''
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
    ''
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


class Task:
    ''

class TaskQueue:
    ''
    def peek(self) -> Any:
        pass

    def pop_head(self) -> Any:
        pass

    def push_head(self) -> Any:
        pass

    def push_sorted(self) -> Any:
        pass

    def remove(self) -> Any:
        pass


class ThreadSafeFlag:
    ''
    def ioctl(self) -> Any:
        pass

    def set(self) -> Any:
        pass

    wait = Any

class TimeoutError:
    ''
_attrs = Any
def create_task() -> Any:
    pass

def current_task() -> Any:
    pass

gather = Any
def get_event_loop() -> Any:
    pass

def new_event_loop() -> Any:
    pass

open_connection = Any
def run() -> Any:
    pass

def run_until_complete() -> Any:
    pass

select = Any
def sleep() -> Any:
    pass

def sleep_ms() -> Any:
    pass

start_server = Any
sys = Any
def ticks() -> Any:
    pass

def ticks_add() -> Any:
    pass

def ticks_diff() -> Any:
    pass

wait_for = Any
def wait_for_ms() -> Any:
    pass

