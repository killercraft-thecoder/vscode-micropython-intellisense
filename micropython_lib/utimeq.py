# micropython_lib/utimeq.py
"""
MicroPython utimeq module stub.
Implements a time‑ordered queue for scheduling.
"""

class utimeq:
    def __init__(self, maxlen):
        self.q = []

    def push(self, time, id, data):
        self.q.append((time, id, data))
        self.q.sort()

    def pop(self):
        return self.q.pop(0) if self.q else None

    def peektime(self):
        return self.q[0][0] if self.q else None

    def __len__(self):
        return len(self.q)