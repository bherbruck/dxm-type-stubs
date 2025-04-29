from __future__ import annotations
from typing import List, Union


def api(cmd: int) -> str:
    return "INVALID PA"


def filein(fileindex: int, maxlen: int = 200) -> str:
    return ""


def fileout(
    fileindex: int, length: int, flags: int, content: str, content2: str = ""
) -> int:
    return 0


def filepeek(fileindex: int) -> int:
    return 0


def getreg(reg: int, sid: int, mbtype: int = 0) -> Union[int, float]:
    if sid == 199 and 1001 <= reg <= 5000:
        return 0.0
    return 0


def multiget(
    reg: int, count: int, sid: int, mbtype: int = 0
) -> Union[List[int], List[float]]:
    if sid == 199 and 1001 <= reg <= 5000:
        return [0.0] * min(count, 100)
    return [0] * min(count, 100)


def multiset(
    reg: int, values: Union[List[int], List[float]], sid: int, mbtype: int = 0
) -> int:
    return 0


def setreg(reg: int, value: Union[int, float], sid: int, mbtype: int = 0) -> int:
    return 0
