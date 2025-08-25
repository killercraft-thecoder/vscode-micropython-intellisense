# micropython_lib/ubluetooth.py
"""
MicroPython ubluetooth module stub.
Provides Bluetooth Low Energy (BLE) support.
On TI‑84: not available — this is for IntelliSense and optional emulation.
"""

FLAG_READ = 0x0002
FLAG_WRITE = 0x0008
FLAG_NOTIFY = 0x0010

class BLE:
    def __init__(self):
        self.active_state = False

    def active(self, state=None):
        """Get or set BLE active state."""
        if state is None:
            return self.active_state
        self.active_state = bool(state)

    def gap_advertise(self, interval_us, adv_data=None):
        """Start advertising."""
        pass

    def gap_scan(self, duration_ms, interval_us=1280000, window_us=11250):
        """Start scanning for devices."""
        pass

    def gatt_register_services(self, services):
        """Register GATT services."""
        pass