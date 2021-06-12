from typing import Any

class PinBase:
    def __init__(self, *args: Any) -> None: ...

class Signal:
    def __init__(self, *args: Any) -> None: ...
    def off() -> None: ...
    def on() -> None: ...
    def value() -> None: ...

mem16: Any
mem32: Any
mem8: Any

def time_pulse_us() -> None: ...
