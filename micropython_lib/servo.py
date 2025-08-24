class Servo:
    def __init__(self, port: str):
        """Initialize servo on given port."""
        ...

    def set_position(self, pos: float):
        """Set servo position (e.g., 90.0)."""
        ...

    def zero(self):
        """Reset servo to zero position."""
        ...

def servo(port: str) -> Servo:
    """Create a Servo object."""
    return Servo(port)