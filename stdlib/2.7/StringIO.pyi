# Stubs for StringIO (Python 2)

from typing import Any, IO, AnyStr, Iterator, Iterable, Generic, List

class StringIO(IO[AnyStr], Generic[AnyStr]):
    closed = ... # type: bool
    softspace = ... # type: int
    len = ... # type: int
    def __init__(self, buf: AnyStr = ...) -> None: ...
    def __iter__(self) -> Iterator[AnyStr]: ...
    def next(self) -> AnyStr: ...
    def close(self) -> None: ...
    def isatty(self) -> bool: ...
    def seek(self, pos: int, mode: int = ...) -> None: ...
    def tell(self) -> int: ...
    def read(self, n: int = ...) -> AnyStr: ...
    def readline(self, length: int = ...) -> AnyStr: ...
    def readlines(self, sizehint: int = ...) -> List[AnyStr]: ...
    def truncate(self, size: int = ...) -> int: ...
    def write(self, s: AnyStr) -> None: ...
    def writelines(self, iterable: Iterable[AnyStr]) -> None: ...
    def flush(self) -> None: ...
    def getvalue(self) -> AnyStr: ...
    def __enter__(self) -> Any: ...
    def __exit__(self, type: Any, value: Any, traceback: Any) -> Any: ...
    def fileno(self) -> int: ...
    def readable(self) -> bool: ...
    def seekable(self) -> bool: ...
    def writable(self) -> bool: ...
