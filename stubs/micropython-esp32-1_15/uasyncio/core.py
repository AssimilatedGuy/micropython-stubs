"""
Module: 'uasyncio.core' on micropython-esp32-1.15
"""
# MCU: {'ver': '1.15', 'port': 'esp32', 'arch': 'xtensawin', 'sysname': 'esp32', 'release': '1.15.0', 'name': 'micropython', 'mpy': 10757, 'version': '1.15.0', 'machine': 'ESP32 module (spiram) with ESP32', 'build': '', 'nodename': 'esp32', 'platform': 'esp32', 'family': 'micropython'}
# Stubber: 1.3.11
from typing import Any


class CancelledError:
    ''

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


class TimeoutError:
    ''
_exc_context = Any
_io_queue = Any
def _promote_to_task() -> Any:
    pass

_stop_task = Any
_stopper = Any
_task_queue = Any
def create_task() -> Any:
    pass

def current_task() -> Any:
    pass

def get_event_loop() -> Any:
    pass

def new_event_loop() -> Any:
    pass

def run() -> Any:
    pass

def run_until_complete() -> Any:
    pass

select = Any
def sleep() -> Any:
    pass

def sleep_ms() -> Any:
    pass

sys = Any
def ticks() -> Any:
    pass

def ticks_add() -> Any:
    pass

def ticks_diff() -> Any:
    pass

