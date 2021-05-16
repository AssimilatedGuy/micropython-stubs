from typing import Any

POLLERR: int
POLLHUP: int
POLLIN: int
POLLOUT: int

def poll() -> Any: ...
def select() -> Any: ...
