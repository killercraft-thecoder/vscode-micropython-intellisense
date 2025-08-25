# micropython_lib/random.py
"""
MicroPython random module stub.
Uses host Python's random for emulation.
"""

import random as _random

def getrandbits(k):
    return _random.getrandbits(k)

def seed(x=None):
    _random.seed(x)

def randrange(start, stop=None, step=1):
    return _random.randrange(start, stop, step)

def randint(a, b):
    return _random.randint(a, b)

def choice(seq):
    return _random.choice(seq)

def random():
    return _random.random()

def uniform(a, b):
    return _random.uniform(a, b)