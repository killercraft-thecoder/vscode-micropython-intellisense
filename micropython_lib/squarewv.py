class SquareWave:
    def __init__(self, port: str):
        """Initialize square wave output on given port."""
        ...

    def set(self, freq: int, duty: int, time: float):
        """
        Set square wave parameters.
        freq: 1–500 Hz
        duty: % power
        time: seconds
        """
        ...

    def off(self):
        """Stop square wave output."""
        ...

def squarewave(port: str) -> SquareWave:
    """Create a SquareWave object for the given port."""
    return SquareWave(port)