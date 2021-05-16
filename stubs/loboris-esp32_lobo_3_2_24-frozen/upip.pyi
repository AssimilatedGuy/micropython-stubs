from typing import Any, Optional

debug: bool
install_path: Any
cleanup_files: Any
gzdict_sz: Any
file_buf: Any

class NotFoundError(Exception): ...

def op_split(path: Any) -> Any: ...
def op_basename(path: Any) -> Any: ...
def _makedirs(name: Any, mode: int=...) -> Any: ...
def save_file(fname: Any, subf: Any) -> None: ...
def install_tar(f: Any, prefix: Any) -> Any: ...
def expandhome(s: Any) -> Any: ...

warn_ussl: bool

def url_open(url: Any) -> Any: ...
def get_pkg_metadata(name: Any) -> Any: ...
def fatal(msg: Any, exc: Optional[Any]=...) -> None: ...
def install_pkg(pkg_spec: Any, install_path: Any) -> Any: ...
def install(to_install: Any, install_path: Optional[Any]=...) -> None: ...
def get_install_path() -> None: ...
def cleanup() -> None: ...
def help() -> None: ...
def main() -> None: ...