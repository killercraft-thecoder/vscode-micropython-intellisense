# micropython_lib/uheapq.py
"""
MicroPython uheapq module stub.
Implements a heap queue algorithm.
"""

def heappush(heap, item):
    heap.append(item)
    heap.sort()

def heappop(heap):
    return heap.pop(0)

def heapify(heap):
    heap.sort()