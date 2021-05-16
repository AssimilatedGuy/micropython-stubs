from typing import Any

ENCODER_ADDR: int

class Lego:
    def deinit() -> None: ...

class Lego_Motor:
    def _available() -> None: ...
    def _read_encoder() -> None: ...
    def deinit() -> None: ...
    def position_update() -> None: ...
    def read_encoder() -> None: ...
    def run_distance() -> None: ...
    def run_to() -> None: ...
    def set_pwm() -> None: ...
    def stop() -> None: ...

M5GO_WHEEL_ADDR: int
MOTOR_CTRL_ADDR: int

def const() -> None: ...
def constrain() -> None: ...
def dead_area() -> None: ...

i2c_bus: Any
machine: Any
module: Any
motor1_pwm: int
motor2_pwm: int
os: Any
time: Any
ustruct: Any
