"""
Type stub file for the pyb module used in MicroPython for the DXM Controller.
Based on "MicroPython for the DXM Controller Instruction Manual" (b_51151351 Rev. A, 21 September 2021)
https://info.bannerengineering.com/cs/groups/public/documents/literature/b_51151351.pdf
"""

from __future__ import annotations
from typing import List, Union

def api(cmd: int) -> str:
    """
    Access features of the DXM API.

    Args:
        cmd: Command value as integer
            6: Register push - Invoke cellular register push
            8: Clear HTTP Log - Clear HTTP log (no return)
            16: Get Default IP - returns string value of IP address
            18: Get Default Gateway - Returns string value of gateway
            28: Get Modbus Server SLID - returns string value of Modbus server ID
            102: Get RTC Value - returns string value of current time
            103: Get Firmware version - returns string value of firmware version
            112: Get MAC Address - Returns string value of device MAC address
            113: Get Model Number - Returns string value of device model number
            114: Get Serial Number - Returns string value of device serial number
            200: Reboot - Restarts the device
            212: Update Cell Firmware - Cellular FOTA

    Returns:
        Command API response in string format, or "INVALID PA" on error.
    """
    ...

def filein(fileindex: int, maxlen: int = 200) -> str:
    """
    Read bytes from UART, file, TCP socket, or UDP socket.

    Args:
        fileindex: Target file/device index
            1: UART (generally serial console)
            2: Email
            3: SMS
            4: TCP Server
            5: TCP Client
            6: UDP socket
            10: File 1
            11: File 2
            12: File 3
            13: File 4
            14: File 5
        maxlen: Maximum number of characters to read (default 200)

    Returns:
        Content read as a string
    """
    ...

def fileout(
    fileindex: int, length: int, flags: int, content: str, content2: str = ""
) -> int:
    """
    Write a string to a serial port, email, TCP Socket, UDP socket, or file.

    Args:
        fileindex: Target file/device index
            1: UART (generally serial console)
            2: Email
            3: SMS
            4: TCP Server
            5: TCP Client
            6: UDP socket
            10: File 1
            11: File 2
            12: File 3
            13: File 4
            14: File 5
        length: Length of content to write (use 0 for auto-detect)
        flags: File operation flag
            0: append file
            1: Overwrite the file, if it exists
        content: The content to write
        content2: Optional string; only used for email and SMS
                 (SMS is not supported on the DXM700 models)

    Returns:
        0 on success or an error code on failure
    """
    ...

def filepeek(fileindex: int) -> int:
    """
    Reads the number of bytes waiting in a network socket,
    the number of bytes in the serial port read buffer,
    or the size of a file on disc.

    Args:
        fileindex: Target file/device index
            1: UART (generally serial console) - Number of bytes in serial out buffer
            2: Email
            3: SMS
            4: TCP Server - Number of bytes in TCP server buffer
            5: TCP Client - Number of bytes in TCP client buffer
            6: UDP socket - Number of bytes in UDP buffer
            10: File 1
            11: File 2
            12: File 3
            13: File 4
            14: File 5

    Returns:
        Size of file in bytes, or number of bytes in buffer
    """
    ...

def getreg(reg: int, sid: int, mbtype: int = 0) -> Union[int, float]:
    """
    Returns a register value.

    Args:
        reg: The register address
        sid: The Modbus Slave ID
            0-198: External Modbus slave devices
            199: Internal Local Registers
            200: I/O board registers
            201: Display board registers
            203: On-board I/O
        mbtype: The Modbus Register Type (ignored but reserved for future use)
            0: holding register (all DXM local registers are holding registers)
            3: coil
            4: input
            5: input register
            6: single coil
            7: single register

    Returns:
        Register value (integer or float depending on register type)

    Notes:
        The data type of the register (integer or floating point) is determined by
        the register address and Modbus Slave ID (sid). For example, if reading from
        internal floating-point registers (register IDs 1001 through 5000, inclusive)
        from SID 199, the result is a float. Otherwise the result is a 16-bit integer.
    """
    ...

def multiget(
    reg: int, count: int, sid: int, mbtype: int = 0
) -> Union[List[int], List[float]]:
    """
    Returns a list of register values.

    Args:
        reg: The starting register address
        count: The number of registers to get [1,100]
        sid: The Modbus Slave ID
            0-198: External Modbus slave devices
            199: Internal Local Registers
            200: I/O board registers
            201: Display board registers
            203: On-board I/O
        mbtype: The Modbus Register Type (ignored but reserved for future use)
            0: holding register (all DXM local registers are holding registers)
            3: coil
            4: input
            5: input register
            6: single coil
            7: single register

    Returns:
        List of register values (length will be equal to count)

    Notes:
        This call may take some time due to networking delays when external devices are polled.
        If more than 100 registers are requested, the contents of indices beyond 100
        of the returned list will likely be 0.
    """
    ...

def multiset(
    reg: int, values: Union[List[int], List[float]], sid: int, mbtype: int = 0
) -> int:
    """
    Set multiple register values.

    Args:
        reg: The starting register address
        values: The list of register values to set (length must be 1 to 100 values)
               Values must match the register type: Uint16 for offboard Modbus registers,
               int32/uint32 for SID 199 internal registers, and SEM32 format for
               SID 199 floating point registers.
        sid: The Modbus Slave ID
            0-198: External Modbus slave devices
            199: Internal Local Registers
            200: I/O board registers
            201: Display board registers
            203: On-board I/O
        mbtype: The Modbus Register Type (ignored but reserved for future use)
            0: holding register (all DXM local registers are holding registers)
            3: coil
            4: input
            5: input register
            6: single coil
            7: single register

    Returns:
        0 on success or an error code on failure

    Notes:
        This call may take some time due to networking delays when external devices are polled.
    """
    ...

def setreg(reg: int, value: Union[int, float], sid: int, mbtype: int = 0) -> int:
    """
    Set a register value.

    Args:
        reg: The register address
        value: The value to set. Integer values can be written to any register;
               floating point values can only be written to floating point registers.
        sid: The Modbus Slave ID
            0-198: External Modbus slave devices
            199: Internal Local Registers
            200: I/O board registers
            201: Display board registers
            203: On-board I/O
        mbtype: The Modbus Register Type (ignored but reserved for future use)
            0: holding register (all DXM local registers are holding registers)
            3: coil
            4: input
            5: input register
            6: single coil
            7: single register

    Returns:
        0 on success or an error code on failure
        (even on invalid register set, for example, non-writeable registers)

    Notes:
        This call may take some time due to networking delays when external devices are polled.
    """
    ...
