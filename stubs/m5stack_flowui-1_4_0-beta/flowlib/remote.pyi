from typing import Any

class Btn:
    def __init__(self, *args: Any) -> None: ...
    def attach() -> None: ...
    def deinit() -> None: ...
    def detach() -> None: ...
    def multiBtnCb() -> None: ...
    def restart() -> None: ...
    def timerCb() -> None: ...

class BtnChild:
    def __init__(self, *args: Any) -> None: ...
    def deinit() -> None: ...
    def isPressed() -> None: ...
    def isReleased() -> None: ...
    def pressFor() -> None: ...
    def restart() -> None: ...
    def upDate() -> None: ...
    def wasDoublePress() -> None: ...
    def wasPressed() -> None: ...
    def wasReleased() -> None: ...

class IP5306:
    def __init__(self, *args: Any) -> None: ...
    def getBatteryLevel() -> None: ...
    def init() -> None: ...
    def isChargeFull() -> None: ...
    def isCharging() -> None: ...
    def setCharge() -> None: ...
    def setChargeVolt() -> None: ...
    def setVinMaxCurrent() -> None: ...

class MQTTClient:
    def __init__(self, *args: Any) -> None: ...
    def _clean_sock_buffer() -> None: ...
    def _recv_len() -> None: ...
    def _send_str() -> None: ...
    def check_msg() -> None: ...
    def connect() -> None: ...
    def disconnect() -> None: ...
    def lock_msg_rec() -> None: ...
    def ping() -> None: ...
    def publish() -> None: ...
    def set_block() -> None: ...
    def set_callback() -> None: ...
    def set_last_will() -> None: ...
    def socket_connect() -> None: ...
    def subscribe() -> None: ...
    def topic_get() -> None: ...
    def topic_msg_get() -> None: ...
    def unlock_msg_rec() -> None: ...
    def wait_msg() -> None: ...

class Rgb_multi:
    def __init__(self, *args: Any) -> None: ...
    def deinit() -> None: ...
    def setBrightness() -> None: ...
    def setColor() -> None: ...
    def setColorAll() -> None: ...
    def setColorFrom() -> None: ...
    def setShowLock() -> None: ...
    def show() -> None: ...

class Speaker:
    def __init__(self, *args: Any) -> None: ...
    def _timeout_cb() -> None: ...
    def checkInit() -> None: ...
    def setBeat() -> None: ...
    def setVolume() -> None: ...
    def sing() -> None: ...
    def tone() -> None: ...

_thread: Any
apikey: str
binascii: Any
btn: Any
btnA: Any
btnB: Any
btnC: Any

def btnText() -> None: ...
def const() -> None: ...

display: Any
gc: Any

def get_sd_state() -> None: ...
def hwDeinit() -> None: ...

json: Any
lcd: Any
m5base: Any
machine: Any
node_id: str
os: Any
power: Any
rgb: Any

def sd_mount() -> None: ...
def sd_umount() -> None: ...

speaker: Any
timEx: Any
time: Any
timeSchedule: Any
time_ex: Any
timerSch: Any
ubinascii: Any
