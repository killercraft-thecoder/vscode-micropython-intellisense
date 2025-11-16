"""
MicroPython errno module stub.

Provides symbolic error codes for OSError and related exceptions.
Not all constants are available on all ports.
"""

from typing import Dict

# Common error codes (POSIX subset)
EPERM: int        # Operation not permitted
ENOENT: int       # No such file or directory
ESRCH: int        # No such process
EINTR: int        # Interrupted system call
EIO: int          # I/O error
ENXIO: int        # No such device or address
E2BIG: int        # Argument list too long
ENOEXEC: int      # Exec format error
EBADF: int        # Bad file number
ECHILD: int       # No child processes
EAGAIN: int       # Try again
ENOMEM: int       # Out of memory
EACCES: int       # Permission denied
EFAULT: int       # Bad address
ENOTBLK: int      # Block device required
EBUSY: int        # Device or resource busy
EEXIST: int       # File exists
EXDEV: int        # Cross-device link
ENODEV: int       # No such device
ENOTDIR: int      # Not a directory
EISDIR: int       # Is a directory
EINVAL: int       # Invalid argument
ENFILE: int       # File table overflow
EMFILE: int       # Too many open files
ENOTTY: int       # Not a typewriter
ETXTBSY: int      # Text file busy
EFBIG: int        # File too large
ENOSPC: int       # No space left on device
ESPIPE: int       # Illegal seek
EROFS: int        # Read-only file system
EMLINK: int       # Too many links
EPIPE: int        # Broken pipe
EDOM: int         # Math argument out of domain of func
ERANGE: int       # Math result not representable

# Networking-related
EADDRINUSE: int   # Address already in use
EADDRNOTAVAIL: int # Cannot assign requested address
ENETDOWN: int     # Network is down
ENETUNREACH: int  # Network is unreachable
ENETRESET: int    # Network dropped connection
ECONNABORTED: int # Software caused connection abort
ECONNRESET: int   # Connection reset by peer
ENOBUFS: int      # No buffer space available
EISCONN: int      # Transport endpoint is already connected
ENOTCONN: int     # Transport endpoint is not connected
ETIMEDOUT: int    # Connection timed out
ECONNREFUSED: int # Connection refused
EHOSTUNREACH: int # No route to host

# Dictionary mapping error numbers to names
errorcode: Dict[int, str]