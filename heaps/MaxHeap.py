
import heapq

class MaxHeap:
  def __init__(self):
    self.heap = []

  def push(self, val):
    heapq.heappush(self.heap, -val)

  def pop(self):
    return -heapq.heappop(self.heap)

  def peek(self):
    return -self.heap[0]

  def __len__(self):
    return len(self.heap)