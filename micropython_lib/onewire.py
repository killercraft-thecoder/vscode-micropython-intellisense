# micropython_lib/onewire.py
"""
MicroPython onewire module stub.
Implements the 1-Wire bus protocol.
"""

class OneWire:
    def __init__(self, pin):
        self.pin = pin

    def reset(self):
        return True

    def readbit(self):
        return 0

    def writebit(self, value):
        pass

    def readbyte(self):
        return 0

    def writebyte(self, value):
        pass

    def select_rom(self, rom):
        pass

    def scan(self):
        return []