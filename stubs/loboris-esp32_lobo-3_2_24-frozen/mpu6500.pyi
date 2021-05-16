from typing import Any, Tuple

Node = Any

class MPU6500:
    def __init__(self, i2c: Any, address: Any=..., accel_fs: Any=..., gyro_fs: Any=..., accel_sf: Any=..., gyro_sf: Any=...) -> None: ...
    def acceleration(self) -> Tuple[Any]: ...
    def gyro(self) -> Tuple[Any]: ...
    def whoami(self) -> Any: ...
    def _register_short(self, register: Any, value: Any=..., buf: Any=...) -> Any: ...
    def _register_three_shorts(self, register: Any, buf: Any=...) -> Any: ...
    def _register_char(self, register: Any, value: Any=..., buf: Any=...) -> Any: ...
    def _accel_fs(self, value: Any) -> Any: ...
    def _gyro_fs(self, value: Any) -> Any: ...
    def __enter__(self) -> Any: ...
    def __exit__(self, exception_type: Any, exception_value: Any, traceback: Any) -> None: ...