# micropython_lib/network.py
"""
MicroPython network module stub.
Provides basic API signatures for Wi-Fi, LAN, and other interfaces.
On TI‑84: networking is not supported — all functions are no‑ops.
"""

STA_IF = 0
AP_IF = 1

class WLAN:
    def __init__(self, interface_id):
        """Create a WLAN interface object."""
        self.interface_id = interface_id
        self._active = False

    def active(self, is_active=None):
        """Get or set interface active state."""
        if is_active is None:
            return self._active
        self._active = bool(is_active)

    def connect(self, ssid=None, key=None):
        """Connect to a network (stub: no-op)."""
        pass

    def disconnect(self):
        """Disconnect from the network."""
        pass

    def isconnected(self):
        """Return True if connected to a network."""
        return False

    def ifconfig(self, config_tuple=None):
        """Get or set IP configuration."""
        if config_tuple is None:
            return ("0.0.0.0", "0.0.0.0", "0.0.0.0", "0.0.0.0")
        pass

def LAN(*args, **kwargs):
    """Stub for LAN interface."""
    return None