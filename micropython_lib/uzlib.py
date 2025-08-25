# micropython_lib/uzlib.py
"""
MicroPython uzlib module stub.
Uses host Python's zlib for emulation.
"""

import zlib as _zlib

class DecompIO:
    def __init__(self, stream, wbits=0):
        """Create a stream wrapper that decompresses zlib data."""
        self._data = _zlib.decompress(stream.read())
    def read(self, size=-1):
        if size == -1:
            return self._data
        return self._data[:size]

def decompress(data, wbits=0, bufsize=0):
    """Decompress zlib-compressed data."""
    return _zlib.decompress(data)