# micropython_lib/sys.py
"""
MicroPython sys module stub.
"""

version = "3.4.0"  # Example: TI‑84 MicroPython version
platform = "TI84-Stub"
implementation = ("micropython", (3, 4, 0))

def exit(code=0):
    """Exit the interpreter."""
    raise SystemExit(code)

def print_exception(exc, file=None):
    """Print exception with traceback."""
    import traceback
    traceback.print_exception(type(exc), exc, exc.__traceback__, file=file)