# micropython_lib/uos.py
"""
MicroPython uos module stub.
Provides basic filesystem access. Maps to host OS for emulation.
"""

import os as _os

def listdir(path="."):
    """List directory contents."""
    return _os.listdir(path)

def mkdir(path):
    """Create a new directory."""
    _os.mkdir(path)

def remove(path):
    """Remove a file."""
    _os.remove(path)

def rmdir(path):
    """Remove a directory."""
    _os.rmdir(path)

def rename(old_path, new_path):
    """Rename a file or directory."""
    _os.rename(old_path, new_path)

def stat(path):
    """Get the status of a file or directory."""
    return _os.stat(path)

def getcwd():
    """Get the current working directory."""
    return _os.getcwd()

def chdir(path):
    """Change the current working directory."""
    _os.chdir(path)

def uname():
    """Return system information (stubbed)."""
    return ("MicroPython", "PC-Stub", "0.0.1", "stub", "x86_64")