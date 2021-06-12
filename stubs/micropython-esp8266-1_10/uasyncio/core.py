"""
Module: 'uasyncio.core' on esp8266 v1.10
"""
# MCU: (sysname='esp8266', nodename='esp8266', release='2.2.0-dev(9422289)', version='v1.10-8-g8b7039d7d on 2019-01-26', machine='ESP module with ESP8266')
# Stubber: 1.1.0

class CancelledError:
    ''
DEBUG = 0

class EventLoop:
    def __init__(self, *args):
        ''
        pass

    def call_at_():
        pass

    def call_later():
        pass

    def call_later_ms():
        pass

    def call_soon():
        pass

    def close():
        pass

    def create_task():
        pass

    def run_forever():
        pass

    def run_until_complete():
        pass

    def stop():
        pass

    def time():
        pass

    def wait():
        pass


class IORead:
    def __init__(self, *args):
        ''
        pass

    def handle():
        pass


class IOReadDone:
    def __init__(self, *args):
        ''
        pass

    def handle():
        pass


class IOWrite:
    def __init__(self, *args):
        ''
        pass

    def handle():
        pass


class IOWriteDone:
    def __init__(self, *args):
        ''
        pass

    def handle():
        pass


class PollEventLoop:
    def __init__(self, *args):
        ''
        pass

    def add_reader():
        pass

    def add_writer():
        pass

    def call_at_():
        pass

    def call_later():
        pass

    def call_later_ms():
        pass

    def call_soon():
        pass

    def close():
        pass

    def create_task():
        pass

    def remove_reader():
        pass

    def remove_writer():
        pass

    def run_forever():
        pass

    def run_until_complete():
        pass

    def stop():
        pass

    def time():
        pass

    def wait():
        pass


class SleepMs:
    def __init__(self, *args):
        ''
        pass

    def handle():
        pass


class StopLoop:
    def __init__(self, *args):
        ''
        pass

    def handle():
        pass


class StreamReader:
    def __init__(self, *args):
        ''
        pass

    aclose = None
    read = None
    readexactly = None
    readline = None

class StreamWriter:
    def __init__(self, *args):
        ''
        pass

    aclose = None
    awrite = None
    awriteiter = None
    def get_extra_info():
        pass


class SysCall:
    def __init__(self, *args):
        ''
        pass

    def handle():
        pass


class SysCall1:
    def __init__(self, *args):
        ''
        pass

    def handle():
        pass

def Task():
    pass


class TimeoutError:
    ''

class TimeoutObj:
    def __init__(self, *args):
        ''
        pass

_socket = None
def cancel():
    pass

core = None
def coroutine():
    pass

def ensure_future():
    pass

def get_event_loop():
    pass

log = None
open_connection = None
select = None
def set_debug():
    pass

sleep = None
sleep_ms = None
start_server = None
time = None

class type_gen:
    def __init__(self, *args):
        ''
        pass

    def close():
        pass

    def pend_throw():
        pass

    def send():
        pass

    def throw():
        pass

uasyncio = None
ucollections = None
uerrno = None
utimeq = None
def wait_for():
    pass

wait_for_ms = None
