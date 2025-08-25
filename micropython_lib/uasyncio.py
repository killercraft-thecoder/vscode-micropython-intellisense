# micropython_lib/uasyncio.py
"""
MicroPython uasyncio module stub.
Uses host Python's asyncio for emulation.
"""

import asyncio as _asyncio

def run(coro):
    """Run a coroutine until complete."""
    return _asyncio.run(coro)

def create_task(coro):
    """Schedule a coroutine object as a Task."""
    return _asyncio.create_task(coro)

sleep = _asyncio.sleep

class Event:
    def __init__(self):
        self._event = _asyncio.Event()
    async def wait(self):
        await self._event.wait()
    def set(self):
        self._event.set()
    def clear(self):
        self._event.clear()
    def is_set(self):
        return self._event.is_set()