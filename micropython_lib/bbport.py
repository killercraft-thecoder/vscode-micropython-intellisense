class BBPort:
    def __init__(self, mask: int = None):
        """Initialize breadboard port with optional mask."""
        ...

    def read_port(self, mask: int = None) -> int:
        """Read port value, optionally masked."""
        ...

    def write_port(self, val: int, mask: int = None):
        """Write value to port, optionally masked."""
        ...

def bb_port(mask: int = None) -> BBPort:
    """Create a BBPort object with optional mask."""
    return BBPort(mask)