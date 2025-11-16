class ColorInput:
    def __init__(self, port: str):
        """Initialize color sensor on given I2C port."""
        pass

    def color_number(self) -> int:
        """Return detected color number."""
        return 0

    def red(self) -> int:
        """Return red component."""
        return 0 

    def green(self) -> int:
        """Return green component."""
        return 0

    def blue(self) -> int:
        """Return blue component."""
        return 0

    def gray(self) -> int:
        """Return grayscale value."""
        return 0

def color_input(port: str) -> ColorInput:
    """Create a ColorInput object."""
    return ColorInput(port)