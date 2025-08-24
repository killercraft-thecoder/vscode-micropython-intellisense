class RGB:
    def __init__(self, r: str, g: str, b: str):
        """Initialize RGB light with given pin names."""
        ...

    def rgb(self, r: int, g: int, b: int):
        """Set RGB color."""
        ...

    def blink(self, freq: int, time: int):
        """Blink RGB light at given frequency for given time."""
        ...

    def off(self):
        """Turn off RGB light."""
        ...

def rgb(r: str, g: str, b: str) -> RGB:
    """Create an RGB object."""
    return RGB(r, g, b)