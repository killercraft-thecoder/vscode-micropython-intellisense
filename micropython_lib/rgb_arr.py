class RGBArray:
    def __init__(self):
        """Initialize RGB LED array."""
        ...

    def set(self, led_position: int, r: int, g: int, b: int):
        """Set color of a single LED."""
        ...

    def set_all(self, r: int, g: int, b: int):
        """Set all LEDs to the same color."""
        ...

    def all_off(self):
        """Turn off all LEDs."""
        ...

    def pattern(self, val: int, r: int = None, g: int = None, b: int = None):
        """Set LED pattern. If RGB provided, apply color."""
        ...

    def measurement(self) -> float:
        """Return current draw in mA."""
        ...

    def set_led_list(self, led_list: list[int], r: int, g: int, b: int):
        """Set multiple LEDs by list of positions."""
        ...

def rgb_array() -> RGBArray:
    """Create an RGBArray object."""
    return RGBArray()