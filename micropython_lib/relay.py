class Relay:
    def __init__(self, port: str):
        """Initialize relay on given port."""
        ...

    def on(self):
        """Turn relay on."""
        ...

    def off(self):
        """Turn relay off."""
        ...

def relay(port: str) -> Relay:
    """Create a Relay object for the given port."""
    return Relay(port)