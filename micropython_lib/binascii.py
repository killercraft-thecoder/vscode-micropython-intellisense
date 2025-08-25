# micropython_lib/binascii.py
"""
MicroPython binascii module stub.
Uses host Python's binascii for emulation.
"""

import binascii as _binascii

hexlify = _binascii.hexlify
unhexlify = _binascii.unhexlify
b2a_base64 = _binascii.b2a_base64
a2b_base64 = _binascii.a2b_base64