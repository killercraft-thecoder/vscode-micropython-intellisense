# micropython_lib/machine.py

class Pin:
    IN = 0
    OUT = 1
    PULL_UP = 2
    PULL_DOWN = 3

    def __init__(self, id, mode=-1, pull=-1):
        """Create a new Pin object."""
        self.id = id
        self.mode = mode
        self.pull = pull
        self._value = 0

    def value(self, x=None):
        """Get or set the pin value."""
        if x is None:
            return self._value
        self._value = 1 if x else 0

class I2C:
    def __init__(self, id=-1, *, scl=None, sda=None, freq=400000):
        """Create an I2C object."""
    def scan(self):
        """Scan for devices on the bus."""
        return []
    def readfrom(self, addr, nbytes):
        return b"\x00" * nbytes
    def writeto(self, addr, buf):
        return len(buf)

class SPI:
    def __init__(self, id=-1, *, baudrate=1000000, polarity=0, phase=0):
        """Create an SPI object."""
    def read(self, nbytes):
        return b"\x00" * nbytes
    def write(self, buf):
        return len(buf)

def reset():
    """Reset the device (stub: no-op)."""
    print("[machine] Reset called (stub mode)")

def freq():
    """Return CPU frequency in Hz."""
    return 48000000

def unique_id():
    """Return a unique ID for the device."""
    return b"PC-STUB-0001"