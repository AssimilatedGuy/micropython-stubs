from neopixel import NeoPixel
from typing import Any

class APA102(NeoPixel):
    ORDER: Any = ...
    clock_pin: Any = ...
    def __init__(self, clock_pin: Any, data_pin: Any, n: Any, bpp: int=...) -> None: ...
    def write(self) -> None: ...
