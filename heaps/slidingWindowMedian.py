import heapq

def median_sliding_window(nums, k):
    if k <= 0:
        return []
    # Use two heaps with lazy deletion by value (counts) — handles duplicates simply.
    import collections
    maxHeap = []   # max-heap as negatives
    minHeap = []   # min-heap as positives
    delayed = collections.Counter()
    result = []

    small_size = 0
    large_size = 0

    def prune_max():
        # remove elements scheduled for deletion from maxHeap
        while maxHeap and delayed[-maxHeap[0][0]] > 0:
            val = -heapq.heappop(maxHeap)[0]
            delayed[val] -= 1
            if delayed[val] == 0:
                del delayed[val]

    def prune_min():
        while minHeap and delayed[minHeap[0][0]] > 0:
            val = heapq.heappop(minHeap)[0]
            delayed[val] -= 1
            if delayed[val] == 0:
                del delayed[val]

    def balance():
        nonlocal small_size, large_size
        if small_size > large_size + 1:
            val = -heapq.heappop(maxHeap)[0]
            heapq.heappush(minHeap, (val,))
            small_size -= 1
            large_size += 1
        elif large_size > small_size + 1:
            val = heapq.heappop(minHeap)[0]
            heapq.heappush(maxHeap, (-val,))
            large_size -= 1
            small_size += 1
        prune_max()
        prune_min()

    def get_median():
        prune_max()
        prune_min()
        if k % 2 == 1:
            if small_size > large_size:
                return float(-maxHeap[0][0])
            else:
                return float(minHeap[0][0])
        else:
            return (-maxHeap[0][0] + minHeap[0][0]) / 2.0

    # helper to push to heaps
    def push(num):
        nonlocal small_size, large_size
        if not maxHeap or num <= -maxHeap[0][0]:
            heapq.heappush(maxHeap, (-num,))
            small_size += 1
        else:
            heapq.heappush(minHeap, (num,))
            large_size += 1

    # initialize
    n = len(nums)
    for i in range(min(k, n)):
        num = nums[i]
        if not maxHeap or num <= -maxHeap[0][0]:
            heapq.heappush(maxHeap, (-num,))
            small_size += 1
        else:
            heapq.heappush(minHeap, (num,))
            large_size += 1
        # balance after each insert
        if small_size > large_size + 1:
            val = -heapq.heappop(maxHeap)[0]
            heapq.heappush(minHeap, (val,))
            small_size -= 1
            large_size += 1
        elif large_size > small_size + 1:
            val = heapq.heappop(minHeap)[0]
            heapq.heappush(maxHeap, (-val,))
            large_size -= 1
            small_size += 1

    if k <= n:
        result.append(get_median())

    for i in range(k, n):
        out_num = nums[i - k]
        in_num = nums[i]

        # mark out_num for lazy deletion and update sizes
        delayed[out_num] += 1
        if maxHeap and out_num <= -maxHeap[0][0]:
            small_size -= 1
        else:
            large_size -= 1

        # push incoming
        if not maxHeap or in_num <= -maxHeap[0][0]:
            heapq.heappush(maxHeap, (-in_num,))
            small_size += 1
        else:
            heapq.heappush(minHeap, (in_num,))
            large_size += 1

        # rebalance and prune
        if small_size > large_size + 1:
            val = -heapq.heappop(maxHeap)[0]
            heapq.heappush(minHeap, (val,))
            small_size -= 1
            large_size += 1
        elif large_size > small_size + 1:
            val = heapq.heappop(minHeap)[0]
            heapq.heappush(maxHeap, (-val,))
            large_size -= 1
            small_size += 1

        prune_max()
        prune_min()
        result.append(get_median())

    return result

# driver code
def main():
    input = (
            ([1,3,-1,-3,5,3,6,7],3),
            ([3, 1, 2, -1, 0, 5, 8],4), 
            ([1, 2], 1), 
            ([4, 7, 2, 21], 2), 
            ([22, 23, 24, 56, 76, 43, 121, 1, 2, 0, 0, 2, 3, 5], 5), 
            ([1, 1, 1, 1, 1], 2))
    x = 1
    for i in input:
        print(x, ".\tInput array: ", i[0],  ", k = ", i[1], sep = "")
        print("\tMedians: ", median_sliding_window(i[0], i[1]), sep = "")
        print(100*"-", "\n", sep = "")
        x += 1


if __name__ == "__main__":
    main()
