# micropython_lib/utime.py
"""
MicroPython utime module stub.
Provides timing functions. Uses host time for emulation.
"""

import time as _time

def sleep(seconds):
    """Sleep for the given number of seconds."""
    _time.sleep(seconds)

def sleep_ms(ms):
    """Sleep for the given number of milliseconds."""
    _time.sleep(ms / 1000)

def sleep_us(us):
    """Sleep for the given number of microseconds."""
    _time.sleep(us / 1_000_000)

def ticks_ms():
    """Return milliseconds since an arbitrary point."""
    return int(_time.time() * 1000)

def ticks_us():
    """Return microseconds since an arbitrary point."""
    return int(_time.time() * 1_000_000)

def ticks_diff(t1, t2):
    """Compute the signed difference between two ticks values."""
    return t1 - t2

def time():
    """Return the current time in seconds since the Epoch."""
    return int(_time.time())