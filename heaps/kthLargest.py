"""Utilities for maintaining the k-th largest element in a stream.

This module implements `KthLargest(k, nums)` which keeps track of the
k-th largest element as values are added via `add(val)`.

Expected behavior (current implementation):
- `k` is expected to be a positive integer (> 0). The implementation does
    not validate `k`; using `k <= 0` leads to undefined behavior (IndexError
    observed).
- `nums` should be an iterable of values that are mutually comparable
    (typically numbers). Non-comparable types will raise during heap ops.
- If `len(nums) < k`, the heap will grow as `add()` is called; until the
    internal heap reaches size `k`, `add()` returns the current smallest
    element seen so far (the heap root), which is not the true k-th largest
    until at least `k` elements have been provided.

Complexity:
- Constructor: O(n log k) in the worst case (pushing up to `k` items,
    then processing remaining items via `add`).
- `add(val)`: O(log k) per call.

Note: callers should validate `k` and input types if stricter semantics
are required; this module intentionally preserves the original runtime
behavior.
"""

import heapq

class KthLargest:
    # Constructor to initialize heap and add values in it
    def __init__(self, k, nums):
        self.my_heap = []
        self.k = k
        x = min(k, len(nums))
        for i in range (x):
            heapq.heappush(self.my_heap, nums[i])
        if len(nums) > k:
            for j in range(k, len(nums)):
                _ = self.add(nums[j])
        
    # Adds element in the heap and return the Kth largest
    def add(self, val):
        if len(self.my_heap) < self.k:
            heapq.heappush(self.my_heap, val)
            return self.my_heap[0]
        if val > self.my_heap[0]:
            _ = heapq.heapreplace(self.my_heap, val)
        return self.my_heap[0]
# Driver code
def main():
    nums = [3, 6, 9, 10]
    temp = [3, 6, 9, 10]
    print("Initial stream: ", nums, sep = "")
    print("k: ", 3, sep = "")
    k_largest = KthLargest(3, nums)
    val = [4, 7, 10, 8, 15]
    for i in range(len(val)):
        print("\tAdding a new number ", val[i], " to the stream", sep = "")
        temp.append(val[i])
        print("\tNumber stream: ", temp, sep = "")
        print("\tKth largest element in the stream: ", k_largest.add(val[i]))
        print("-"*100)

    # Additional tests for edge cases
    print("\nTest: k=1 with empty nums")
    nums2 = []
    print("Initial stream:", nums2)
    k1 = KthLargest(1, nums2)
    for v in [5, -1, 10]:
        print("\tAdding:", v)
        print("\tKth largest:", k1.add(v))
    print("-"*100)

    print("\nTest: k=0 (invalid k) — expect error or undefined behavior")
    try:
        k0 = KthLargest(0, [1,2])
        print("Created KthLargest with k=0 — adding 3 returns:", k0.add(3))
    except Exception as e:
        print("\tCaught exception for k=0:", type(e).__name__, e)
    print("-"*100)

    print("\nTest: k larger than initial nums")
    nums3 = [2, 3]
    print("Initial stream:", nums3)
    k_large = KthLargest(5, nums3)
    for v in [4, 6, 1, 10, 8]:
        print("\tAdding:", v)
        print("\tKth largest:", k_large.add(v))
    print("-"*100)

if __name__ == "__main__":
    main()
