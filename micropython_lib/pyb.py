"""
MicroPython pyb module stub.
This module provides access to Pyboard-specific hardware functions.
On TI‑84: not available — this is for IntelliSense and optional emulation.
"""

# Constants
USB_VCP = 0
USB_HID = 1

# Classes
class LED:
    def __init__(self, id):
        """Create an LED object for the given LED id (1-4 on Pyboard)."""
        self.id = id
        self._state = False

    def on(self):
        """Turn the LED on."""
        self._state = True

    def off(self):
        """Turn the LED off."""
        self._state = False

    def toggle(self):
        """Toggle the LED state."""
        self._state = not self._state

    def intensity(self, value=None):
        """
        Get or set LED intensity (0-255).
        If value is None, return current intensity.
        """
        if value is None:
            return 255 if self._state else 0
        return None

class Switch:
    def __init__(self):
        """Create a Switch object."""
        self._pressed = False

    def value(self):
        """Return True if the switch is pressed."""
        return self._pressed

    def callback(self, func):
        """Set a callback for when the switch is pressed."""
        pass

class Pin:
    IN = 0
    OUT_PP = 1
    OUT_OD = 2
    AF_PP = 3
    AF_OD = 4
    PULL_NONE = 0
    PULL_UP = 1
    PULL_DOWN = 2

    def __init__(self, id, mode=-1, pull=-1):
        """Create a Pin object."""
        self.id = id
        self.mode = mode
        self.pull = pull
        self._value = 0

    def value(self, x=None):
        """Get or set the pin value."""
        if x is None:
            return self._value
        self._value = 1 if x else 0

class Timer:
    def __init__(self, id, **kwargs):
        """Create a Timer object."""
        self.id = id

    def init(self, **kwargs):
        """Initialize the timer."""
        pass

    def deinit(self):
        """Deinitialize the timer."""
        pass

class UART:
    def __init__(self, id, baudrate=9600, **kwargs):
        """Create a UART object."""
        self.id = id
        self.baudrate = baudrate

    def write(self, data):
        """Write data to the UART."""
        return len(data)

    def read(self, nbytes=None):
        """Read data from the UART."""
        return b""

class USB_VCP:
    def __init__(self):
        """Create a USB_VCP object."""
        pass

    def isconnected(self):
        """Return True if USB is connected."""
        return False

    def read(self, nbytes=None):
        """Read data from USB VCP."""
        return b""

    def write(self, data):
        """Write data to USB VCP."""
        return len(data)

# Functions
def delay(ms):
    """Delay for the given number of milliseconds."""
    import time
    time.sleep(ms / 1000)

def millis():
    """Return the number of milliseconds since reset."""
    import time
    return int(time.time() * 1000)

def micros():
    """Return the number of microseconds since reset."""
    import time
    return int(time.time() * 1_000_000)

def elapsed_millis(start):
    """Return milliseconds elapsed since start."""
    return millis() - start

def elapsed_micros(start):
    """Return microseconds elapsed since start."""
    return micros() - start

def hard_reset():
    """Perform a hard reset of the board (stub: no-op)."""
    pass

def bootloader():
    """Enter bootloader mode (stub: no-op)."""
    pass

def mount(device, mountpoint, readonly=False):
    """Mount a filesystem (stub: no-op)."""
    pass

def repl_info(val=None):
    """Get or set REPL info display."""
    return 0

def unique_id():
    """Return a unique ID for the board."""
    return b"PYB-STUB-0001"