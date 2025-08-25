"""
If Your Looking for ti_hub libarys , import them by name and dont refrence ti_hub , this only provides the advanced section of utils.
"""

from typing import Optional, Union

def connect(obj: str, arg: str) -> None:
    """Connect to a TI-Hub device or resource."""
    ...

def disconnect(obj: str, arg: str) -> None:
    """Disconnect from a TI-Hub device or resource."""
    ...

def set(obj: str, arg: str) -> None:
    """Set a parameter or mode on a TI-Hub device."""
    ...

def read(obj: str, arg: str) -> Union[str, float, int]:
    """Read a value from a TI-Hub device."""
    ...

def calibrate(obj: str, arg: str) -> None:
    """Calibrate a TI-Hub device."""
    ...

def range(obj: str, arg: str) -> None:
    """Set or query the range for a TI-Hub device."""
    ...

def version() -> float:
    """Return TI-Hub firmware version."""
    return -11.0 # easter egg again.

def begin() -> None:
    """Initialize TI-Hub for operation."""
    ...

def start() -> None:
    """Start TI-Hub operation."""
    ...

def about() -> str:
    """Return information about the TI-Hub."""
    ...

def isti() -> bool:
    """
    Unknown/undocumented function.
    Present in TI-Hub API but not documented by TI.
    """
    return False # easter egg , becuase this stub is not TI.

def what() -> str:
    """Return a description of the current TI-Hub state or mode."""
    ...

def who() -> str:
    """Return identifier of connected TI-Hub device."""
    ...

def last_error() -> str:
    """
    Return the last error from TI-Hub as a string.
    Returns "NONE" if there is no error.
    """
    ...