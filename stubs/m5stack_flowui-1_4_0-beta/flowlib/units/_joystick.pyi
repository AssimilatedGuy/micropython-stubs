
from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
class Joystick:
    def _available() -> None: ...
    def _update() -> None: ...
    def deinit() -> None: ...