from typing import overload,Union


# --- Setup Section ---

def cls() -> None:
    """Clear the plot screen."""
    ...

def grid(xscl: float, yscl: float, style: str) -> None:
    """Set grid scale and style."""
    ...

def window(xmin: float, xmax: float, ymin: float, ymax: float) -> None:
    """Set plot window boundaries."""
    ...

def auto_window(xlist: list[float], ylist: list[float]) -> None:
    """Automatically set window to fit given data lists."""
    ...

def axes(mode: str) -> None:
    """Set axes display mode."""
    ...

def labels(xlabel: str, ylabel: str, x: float, y: float) -> None:
    """Set axis labels and their positions."""
    ...

def title(title: str) -> None:
    """Set plot title."""
    ...

def show_plot() -> None:
    """Display the plot."""
    ...

# --- Draw Section ---

def color(r: int, g: int, b: int) -> None:
    """Set drawing color."""
    ...

def scatter(xlist: list[float], ylist: list[float], mark: str) -> None:
    """Draw scatter plot with given mark style."""
    ...

@overload
def plot(x: list[float], y: list[float], mark: str) -> None: ...
@overload
def plot(x: float, y: float, mark: str) -> None: ...
def plot(x: Union[list[float], float],
         y: Union[list[float], float],
         mark: str) -> None:
    """
    Plot data.
    - If x and y are lists, plots a series of points.
    - If x and y are floats, plots a single point.
    mark: marker style string.
    """
    ...


# Note: On‑calc both are `plot()`, but we split for IntelliSense clarity.

def line(x1: float, y1: float, x2: float, y2: float, mode: str) -> None:
    """Draw a line between two points."""
    ...

def lin_reg(xlist: list[float], ylist: list[float], disp: str) -> None:
    """Perform linear regression and optionally display results."""
    ...

def pen(size: str, style: str) -> None:
    """Set pen size and style."""
    ...

def text_at(row: int, text: str, align: str) -> None:
    """Draw text at given row with alignment."""
    ...

# --- Properties Section ---

xmin: float = -10.0
"""Minimum X value of the plot window."""

xmax: float = 10.0
"""Maximum X value of the plot window."""

ymin: float = -6.56
"""Minimum Y value of the plot window."""

ymax: float = 6.56
"""Maximum Y value of the plot window."""

a: float = 0.0
"""Gradient (slope) from regression."""

b: float = 0.0
"""Y-intercept from regression."""