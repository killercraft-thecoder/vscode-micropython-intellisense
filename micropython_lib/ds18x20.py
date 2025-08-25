# micropython_lib/ds18x20.py
"""
MicroPython ds18x20 module stub.
Driver for DS18B20 temperature sensors (uses onewire).
"""

class DS18X20:
    def __init__(self, onewire):
        self.ow = onewire

    def scan(self):
        return []

    def convert_temp(self):
        pass

    def read_temp(self, rom):
        return 25.0