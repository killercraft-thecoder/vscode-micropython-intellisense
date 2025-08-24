class ColorInput:
    def __init__(self, port: str):
        """Initialize color sensor on given I2C port."""
        ...

    def color_number(self) -> int:
        """Return detected color number."""
        ...

    def red(self) -> int:
        """Return red component."""
        ...

    def green(self) -> int:
        """Return green component."""
        ...

    def blue(self) -> int:
        """Return blue component."""
        ...

    def gray(self) -> int:
        """Return grayscale value."""
        ...

def color_input(port: str) -> ColorInput:
    """Create a ColorInput object."""
    return ColorInput(port)