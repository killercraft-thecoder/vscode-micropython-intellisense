# micropython_lib/framebuf.py
"""
MicroPython framebuf module stub.
Provides a FrameBuffer class for drawing graphics into a buffer.
"""

MONO_HLSB = 0
MONO_VLSB = 1
MONO_HMSB = 2
RGB565 = 3
GS4_HMSB = 4

class FrameBuffer:
    def __init__(self, buffer, width, height, format):
        self.buffer = buffer
        self.width = width
        self.height = height
        self.format = format

    def fill(self, c):
        pass

    def pixel(self, x, y, c=None):
        if c is None:
            return 0
        pass

    def hline(self, x, y, w, c):
        pass

    def vline(self, x, y, h, c):
        pass

    def rect(self, x, y, w, h, c):
        pass

    def fill_rect(self, x, y, w, h, c):
        pass

    def text(self, s, x, y, c=1):
        pass

    def scroll(self, dx, dy):
        pass