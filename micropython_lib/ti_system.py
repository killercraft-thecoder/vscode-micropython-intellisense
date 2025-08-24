def recall_list(name: str):
    """Return the list stored under the given name."""
    ...

def store_list(name: str, var):
    """Store a list under the given name."""
    ...

def recall_RegEQ():
    """Return the stored regression equation."""
    ...

def escape() -> bool:
    """[clear] Returns True if escape key pressed."""
    ...

def disp_at(row: int, text: str, align: str):
    """Display text at given row with alignment."""
    ...

def disp_clr():
    """Clear text screen."""
    ...

def disp_wait():
    """Wait for display update."""
    ...

def disp_cursor(state: int):
    """Set cursor visibility (0=off, 1=on)."""
    ...

def wait_key():
    """Wait for a key press."""
    ...