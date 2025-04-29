from typing import Optional, Tuple, Any
import time as py_time


def gmtime(secs: Optional[Any] = None) -> Tuple:
    return py_time.gmtime(secs)


def localtime(secs: Optional[Any] = None) -> Tuple:
    return py_time.localtime(secs)


def mktime(t: Tuple) -> int:
    return int(py_time.mktime(t))


def sleep(seconds) -> Any:
    return py_time.sleep(seconds)


def sleep_ms(ms) -> None:
    py_time.sleep(ms / 1000)


def sleep_us(us) -> None:
    py_time.sleep(us / 1000000)


def ticks_ms() -> int:
    return int(py_time.time() * 1000) & 0x3FFFFFFF


def ticks_us() -> Any:
    return int(py_time.time() * 1000000) & 0x3FFFFFFF


def ticks_cpu() -> Any:
    return ticks_us()


def ticks_add(ticks, delta) -> Any:
    return (ticks + delta) & 0x3FFFFFFF


def ticks_diff(ticks1, ticks2) -> int:
    diff = (ticks1 - ticks2) & 0x3FFFFFFF
    if diff & 0x20000000:
        diff -= 0x40000000
    return diff


class time:
    def __init__(self) -> None:
        pass

    def __call__(self) -> int:
        return int(py_time.time())


time = time()  # type: ignore


def time_ns() -> int:
    return int(py_time.time_ns())
