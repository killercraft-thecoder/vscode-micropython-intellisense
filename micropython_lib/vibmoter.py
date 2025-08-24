class VibrationMotor:
    def __init__(self, port: str):
        """Initialize vibration motor on given port."""
        ...

    def set(self, val: int):
        """
        Set vibration intensity.
        val: 0–255
        """
        ...

    def off(self):
        """Turn vibration motor off."""
        ...

    def on(self):
        """Turn vibration motor on at full power."""
        ...

def vibration_motor(port: str) -> VibrationMotor:
    """Create a VibrationMotor object for the given port."""
    return VibrationMotor(port)