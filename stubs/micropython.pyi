from typing import Any, Callable, Optional, Tuple, TypeVar, Union
from functools import wraps

Const_T = TypeVar("Const_T", int, float, str, bytes, Tuple)

def const(expr: Const_T) -> Const_T:
    return expr

def opt_level(level: Optional[Any] = None):
    if level is not None:
        return None
    return 0

def alloc_emergency_exception_buf(size):
    pass

def mem_info(verbose: Optional[Any] = None) -> None:
    import sys
    import gc

    print(f"Memory usage: {sys.getsizeof(0)} bytes per integer")
    print(f"Number of objects tracked by GC: {len(gc.get_objects())}")

    if verbose:
        print("Collecting garbage...")
        collected = gc.collect()
        print(f"Collected {collected} objects")

def qstr_info(verbose: Optional[Any] = None) -> None:
    print("qstr information not available in standard Python")
    if verbose:
        print("Verbose output not available")

def stack_use() -> int:
    import sys

    return sys.getsizeof(sys._getframe())

def heap_lock() -> int:
    return 1

def heap_unlock() -> int:
    return 0

def heap_locked() -> bool:
    return False

def kbd_intr(chr) -> None:
    pass

def schedule(func, arg):
    func(arg)

def viper(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

def native(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
