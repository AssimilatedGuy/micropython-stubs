from typing import Any

BAT_VOLTAGE: Any
BAT_CHARGE: Any
DOTSTAR_CLK: Any
DOTSTAR_DATA: Any
DOTSTAR_PWR: Any
SPI_MOSI: Any
SPI_CLK: Any
SPI_MISO: Any
I2C_SDA: Any
I2C_SCL: Any
DAC1: Any
DAC2: Any

def get_battery_voltage() -> None: ...
def get_battery_charging() -> None: ...
def set_dotstar_power(state: Any) -> None: ...
def dotstar_color_wheel(wheel_pos: Any) -> Any: ...
def go_deepsleep(t: Any) -> None: ...
