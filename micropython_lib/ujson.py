# micropython_lib/ujson.py
"""
MicroPython ujson module stub.
Uses host Python's json for emulation.
"""

import json as _json

def dumps(obj):
    """Serialize obj to a JSON string."""
    return _json.dumps(obj)

def loads(s):
    """Deserialize s (a str, bytes, or bytearray) to a Python object."""
    return _json.loads(s)