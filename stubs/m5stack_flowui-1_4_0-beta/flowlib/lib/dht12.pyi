from typing import Any

class DHT12:
    def __init__(self, *args: Any) -> None: ...
    def humidity() -> None: ...
    def measure() -> None: ...
    def temperature() -> None: ...

class DHTBaseI2C:
    def __init__(self, *args: Any) -> None: ...
    def measure() -> None: ...
