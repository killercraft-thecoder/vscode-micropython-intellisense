# micropython_lib/micropython.py
"""
MicroPython internal control functions stub.
On TI‑84: most of these are not exposed.
"""

def const(x):
    """Declare a constant value."""
    return x

def opt_level(level=None):
    """Get or set the compiler optimisation level."""
    if level is None:
        return 0
    return None

def mem_info(verbose=False):
    """Print memory info (stub: no-op)."""
    print("[micropython] mem_info (stub)")

def qstr_info(verbose=False):
    """Print qstr info (stub: no-op)."""
    print("[micropython] qstr_info (stub)")

def stack_use():
    """Return current stack usage (stub: returns 0)."""
    return 0

def schedule(func, arg):
    """Schedule a function to run later (stub: calls immediately)."""
    func(arg)