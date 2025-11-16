"""
MicroPython uio module stub.
Provides stream (I/O) classes and functions.
On TI‑84: not available — this is for IntelliSense and optional emulation.
"""

class IOBase:
    """Base class for stream objects."""
    def read(self, n=-1):
        return b""
    def readinto(self, buf):
        return 0
    def readline(self):
        return b""
    def write(self, buf):
        return len(buf)
    def flush(self):
        pass
    def close(self):
        pass

class StringIO:
    """In-memory text stream."""
    def __init__(self, initial_value="", newline="\n"):
        self._buf = str(initial_value)
    def write(self, s):
        self._buf += str(s)
        return len(s)
    def read(self, n=-1):
        if n == -1:
            return self._buf
        out, self._buf = self._buf[:n], self._buf[n:]
        return out
    def getvalue(self):
        return self._buf
    def seek(self, pos):
        # Simple stub: ignore pos
        pass
    def close(self):
        pass

class BytesIO:
    """In-memory bytes stream."""
    def __init__(self, initial_bytes=b""):
        self._buf = bytearray(initial_bytes)
    def write(self, b):
        self._buf.extend(b)
        return len(b)
    def read(self, n=-1):
        if n == -1:
            return bytes(self._buf)
        out = bytes(self._buf[:n])
        del self._buf[:n]
        return out
    def getvalue(self):
        return bytes(self._buf)
    def seek(self, pos):
        # Simple stub: ignore pos
        pass
    def close(self):
        pass