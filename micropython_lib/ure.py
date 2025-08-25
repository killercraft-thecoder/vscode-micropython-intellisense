# micropython_lib/ure.py
"""
MicroPython ure module stub.
Lightweight regular expression engine.
Uses host Python's re for emulation.
"""

import re as _re

DEBUG = 0

def compile(pattern, flags=0):
    """Compile a regex pattern."""
    return _re.compile(pattern, flags)

def match(pattern, string):
    """Try to apply the pattern at the start of the string."""
    return _re.match(pattern, string)

def search(pattern, string):
    """Search the string for the first location where the pattern matches."""
    return _re.search(pattern, string)

def sub(pattern, repl, string, count=0):
    """Return the string with all occurrences of pattern replaced by repl."""
    return _re.sub(pattern, repl, string, count)