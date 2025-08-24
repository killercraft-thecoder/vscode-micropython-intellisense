class Pin:
    IN = 0
    OUT = 1
    PULL_UP = 2
    PULL_DOWN = 3

    def __init__(self, id: int, mode: int = None, pull: int = None): # type: ignore
        """Initialize a pin."""
        pass

    def value(self, x: int = None) -> int: # type: ignore
        """Get or set the pin value."""
        return 0

def reset():
    """Reset the device."""
    pass