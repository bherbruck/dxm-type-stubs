from __future__ import annotations
from typing import List, Union, Dict, Optional
import threading

# Use dictionaries instead of lists for sparse register maps
_register_map: Dict[int, Dict[int, Union[float, int]]] = {
    199: {},  # Internal Local Registers
    200: {},  # I/O board registers
    201: {},  # Display board registers
    203: {},  # On-board I/O
}

# File storage simulation
_files: Dict[int, str] = {}
_file_locks = {}
_register_lock = threading.RLock()


def _ensure_sid_exists(sid: int) -> None:
    with _register_lock:
        if sid not in _register_map:
            _register_map[sid] = {}


def _ensure_file_exists(fileindex: int) -> None:
    if fileindex not in _files:
        _files[fileindex] = ""
    if fileindex not in _file_locks:
        _file_locks[fileindex] = threading.RLock()


def api(cmd: int) -> str:
    api_responses = {
        16: "192.168.1.100",
        18: "192.168.1.1",
        28: "DXM100",
        102: "2023-04-29 12:00:00",
        103: "1.0.0",
        112: "00:11:22:33:44:55",
        113: "DXM100-B1R1",
        114: "12345-67890",
    }
    return api_responses.get(cmd, "INVALID PA")


def filein(fileindex: int, maxlen: int = 200) -> str:
    _ensure_file_exists(fileindex)
    with _file_locks.get(fileindex, threading.RLock()):
        return _files.get(fileindex, "")[:maxlen]


def fileout(
    fileindex: int, length: int, flags: int, content: str, content2: str = ""
) -> int:
    _ensure_file_exists(fileindex)
    with _file_locks.get(fileindex, threading.RLock()):
        if flags == 1:  # Overwrite
            _files[fileindex] = content
        else:  # Append
            _files[fileindex] += content
    return 0


def filepeek(fileindex: int) -> int:
    _ensure_file_exists(fileindex)
    with _file_locks.get(fileindex, threading.RLock()):
        return len(_files.get(fileindex, ""))


def getreg(reg: int, sid: int, mbtype: int) -> Union[int, float]:
    _ensure_sid_exists(sid)
    with _register_lock:
        # If it's a floating point register for internal registers
        if sid == 199 and 1001 <= reg <= 5000:
            return float(_register_map[sid].get(reg, 0.0))
        # Otherwise return an integer
        return int(_register_map[sid].get(reg, 0))


def setreg(reg: int, value: Union[int, float], sid: int, mbtype: int) -> int:
    _ensure_sid_exists(sid)
    with _register_lock:
        try:
            # Convert to appropriate type based on register range
            if sid == 199 and 1001 <= reg <= 5000:
                _register_map[sid][reg] = float(value)
            else:
                _register_map[sid][reg] = (
                    int(value) & 0xFFFF
                )  # 16-bit integer for Modbus
            return 0
        except (ValueError, TypeError):
            return -1


def multiget(
    reg: int, count: int, sid: int, mbtype: int
) -> Union[List[int], List[float]]:
    count = min(count, 100)  # Limit to 100 registers as per spec
    _ensure_sid_exists(sid)
    result = []

    # Determine if we're dealing with floating point registers
    is_float = sid == 199 and 1001 <= reg <= 5000

    with _register_lock:
        for i in range(count):
            current_reg = reg + i
            # Add the value if it exists, otherwise add default
            if current_reg in _register_map[sid]:
                result.append(_register_map[sid][current_reg])
            else:
                result.append(0.0 if is_float else 0)

    # Ensure consistent type for the entire result list
    if is_float:
        return [float(v) for v in result]
    return [int(v) for v in result]


def multiset(
    reg: int, values: Union[List[int], List[float]], sid: int, mbtype: int
) -> int:
    if not values or len(values) > 100:
        return -1  # Invalid length

    _ensure_sid_exists(sid)
    success = True

    with _register_lock:
        for i, value in enumerate(values):
            current_reg = reg + i
            try:
                if sid == 199 and 1001 <= current_reg <= 5000:
                    _register_map[sid][current_reg] = float(value)
                else:
                    _register_map[sid][current_reg] = int(value) & 0xFFFF
            except (ValueError, TypeError):
                # Continue processing remaining values even if one fails
                success = False

    return 0 if success else -1
