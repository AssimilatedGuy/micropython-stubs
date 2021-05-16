from typing import Any

class Calibrate:
    tft: Any = ...
    rx: Any = ...
    ry: Any = ...
    def __init__(self, tft: Any) -> None: ...
    def drawCrossHair(self, x: Any, y: Any, clr: Any) -> None: ...
    def readCoordinates(self) -> None: ...
    def calibrate(self, x: Any, y: Any, i: Any) -> Any: ...
    def calibError(self) -> None: ...
    def tpcalib(self, save: bool=...) -> Any: ...
