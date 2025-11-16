class BBPort:
    def __init__(self, mask: int = None): # type:ignore
        """Initialize breadboard port with optional mask."""
        pass

    def read_port(self, mask: int = None) -> int: # type:ignore
        """Read port value, optionally masked."""
        return 0

    def write_port(self, val: int, mask: int = None): # type:ignore
        """Write value to port, optionally masked."""
        return 0

def bb_port(mask: int = None) -> BBPort: # type:ignore
    """Create a BBPort object with optional mask."""
    return BBPort(mask)