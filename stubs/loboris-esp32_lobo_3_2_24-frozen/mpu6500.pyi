from typing import Any, Optional

__version__: str
_GYRO_CONFIG: Any
_ACCEL_CONFIG: Any
_ACCEL_CONFIG2: Any
_INT_PIN_CFG: Any
_ACCEL_XOUT_H: Any
_ACCEL_XOUT_L: Any
_ACCEL_YOUT_H: Any
_ACCEL_YOUT_L: Any
_ACCEL_ZOUT_H: Any
_ACCEL_ZOUT_L: Any
_TEMP_OUT_H: Any
_TEMP_OUT_L: Any
_GYRO_XOUT_H: Any
_GYRO_XOUT_L: Any
_GYRO_YOUT_H: Any
_GYRO_YOUT_L: Any
_GYRO_ZOUT_H: Any
_GYRO_ZOUT_L: Any
_WHO_AM_I: Any
ACCEL_FS_SEL_2G: Any
ACCEL_FS_SEL_4G: Any
ACCEL_FS_SEL_8G: Any
ACCEL_FS_SEL_16G: Any
_ACCEL_SO_2G: int
_ACCEL_SO_4G: int
_ACCEL_SO_8G: int
_ACCEL_SO_16G: int
GYRO_FS_SEL_250DPS: Any
GYRO_FS_SEL_500DPS: Any
GYRO_FS_SEL_1000DPS: Any
GYRO_FS_SEL_2000DPS: Any
_GYRO_SO_250DPS: int
_GYRO_SO_500DPS: float
_GYRO_SO_1000DPS: float
_GYRO_SO_2000DPS: float
_I2C_BYPASS_MASK: Any
_I2C_BYPASS_EN: Any
_I2C_BYPASS_DIS: Any
SF_G: int
SF_M_S2: float
SF_DEG_S: int
SF_RAD_S: float

class MPU6500:
    i2c: Any = ...
    address: Any = ...
    _accel_so: Any = ...
    _gyro_so: Any = ...
    _accel_sf: Any = ...
    _gyro_sf: Any = ...
    def __init__(self, i2c: Any, address: int=..., accel_fs: Any=..., gyro_fs: Any=..., accel_sf: Any=..., gyro_sf: Any=...) -> None: ...
    @property
    def acceleration(self) -> None: ...
    @property
    def gyro(self) -> None: ...
    @property
    def whoami(self) -> None: ...
    def _register_short(self, register: Any, value: Optional[Any]=..., buf: Any=...) -> Any: ...
    def _register_three_shorts(self, register: Any, buf: Any=...) -> Any: ...
    def _register_char(self, register: Any, value: Optional[Any]=..., buf: Any=...) -> Any: ...
    def _accel_fs(self, value: Any) -> Any: ...
    def _gyro_fs(self, value: Any) -> Any: ...
    def __enter__(self) -> None: ...
    def __exit__(self, exception_type: Any, exception_value: Any, traceback: Any) -> None: ...
