from typing import Any

Node = Any

def allowsuspend() -> None: ...
def getReplID() -> None: ...
def getSelfName() -> None: ...
def getThreadName() -> None: ...
def getmsg() -> None: ...
def getnotification() -> None: ...
def isnotified() -> None: ...
def list() -> None: ...
def lock() -> None: ...
def notify() -> None: ...
def replAcceptMsg() -> None: ...
def resume() -> None: ...
def sendmsg() -> None: ...
def stack_size() -> None: ...
def start_new_thread() -> None: ...
def status() -> None: ...
def stop() -> None: ...
def suspend() -> None: ...
def unlock() -> None: ...
def wait() -> None: ...