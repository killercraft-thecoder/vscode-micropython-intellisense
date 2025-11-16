class VibrationMotor:
    def __init__(self, port: str):
        """Initialize vibration motor on given port."""
        self._enabled = False
        self._vib = 0

    def set(self, val: int):
        """
        Set vibration intensity.
        val: 0–255
        """
        if (self._enabled == False):
            return
        self._vib = val
        print(f"[MICROPYTHON-EMU] VIB MOTER VIBRATION START WITH INTENSITY:{val}")
    def off(self):
        """Turn vibration motor off."""
        self._vib = 0
        self._enabled = False
        print("[MICROPYTHON-EMU] VIB MOTER OFF")

    def on(self):
        """Turn vibration motor on at full power."""
        self._enabled = True
        print("[MICROPYTHON-EMU] VIB MOTER ON")

def vibration_motor(port: str) -> VibrationMotor:
    """Create a VibrationMotor object for the given port."""
    return VibrationMotor(port)