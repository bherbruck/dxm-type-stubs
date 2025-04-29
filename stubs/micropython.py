from typing import Any, Callable, Optional, Tuple, TypeVar, Union

from _typeshed import Incomplete

Const_T = TypeVar("Const_T", int, float, str, bytes, Tuple)  # constant


def const(expr: Const_T) -> Const_T:
    return expr


def opt_level(level) -> Incomplete:
    pass


def alloc_emergency_exception_buf(size) -> Incomplete:
    """
    Allocate *size* bytes of RAM for the emergency exception buffer (a good
    size is around 100 bytes).  The buffer is used to create exceptions in cases
    when normal RAM allocation would fail (eg within an interrupt handler) and
    therefore give useful traceback information in these situations.

    A good way to use this function is to put it at the start of your main script
    (eg ``boot.py`` or ``main.py``) and then the emergency exception buffer will be active
    for all the code following it.
    """
    ...


def mem_info(verbose: Optional[Any] = None) -> None:
    return None


def qstr_info(verbose: Optional[Any] = None) -> None:
    return None


def stack_use() -> int:
    return 0


def heap_lock() -> int:
    return 0


def heap_unlock() -> int:
    return 0


def heap_locked() -> bool:
    return False


def kbd_intr(chr) -> None:
    return None


def schedule(func, arg) -> Incomplete:
    pass


def viper(func: Callable) -> Callable:
    return func


def native(func: Callable) -> Callable:
    return func
