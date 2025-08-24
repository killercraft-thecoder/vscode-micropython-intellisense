class Loudness:
    def __init__(self, port: str):
        """Initialize loudness sensor on given port."""
        ...

    def measurement(self) -> int:
        """Return current loudness measurement."""
        ...

    def range(self, min_val: int, max_val: int):
        """Set loudness measurement range."""
        ...

def loudness(port: str) -> Loudness:
    """Create a Loudness object for the given port."""
    return Loudness(port)