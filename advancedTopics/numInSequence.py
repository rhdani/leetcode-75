"""Union-find based longest consecutive sequence.

This file implements a UnionFind adapted for a list of unique numbers
and uses it to compute the longest run of consecutive integers.
"""

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return False
        # union by size
        if self.size[rx] < self.size[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        self.size[rx] += self.size[ry]
        return True


def longest_consecutive_sequence(nums):
    # empty list
    if not nums:
        return 0

    # Build mapping from number to a unique index (ignore duplicates)
    integerMap = {}
    unique = []
    for num in nums:
        if num in integerMap:
            continue
        integerMap[num] = len(unique)
        unique.append(num)

    n = len(unique)
    uf = UnionFind(n)

    # Union adjacent numbers (num with num+1 if present)
    for num, idx in integerMap.items():
        if num + 1 in integerMap:
            uf.union(idx, integerMap[num + 1])
        if num - 1 in integerMap:
            uf.union(idx, integerMap[num - 1])

    # Find maximum component size
    max_size = 0
    for i in range(n):
        if uf.find(i) == i:
            if uf.size[i] > max_size:
                max_size = uf.size[i]

    return max_size


def _run_test_case(name, inp, expect=None):
    try:
        result = longest_consecutive_sequence(inp)
        status = "OK" if (expect is None or result == expect) else "FAIL"
        print(f"{name}: input={inp} -> result={result} expected={expect} [{status}]")
    except Exception as e:
        status = "ERROR"
        print(f"{name}: input={inp} -> raised {type(e).__name__}: {e} [{status}]")


if __name__ == '__main__':
    # Edge cases
    _run_test_case('Empty list', [], 0)
    _run_test_case('Single element', [7], 1)
    _run_test_case('All duplicates', [2, 2, 2], 1)
    _run_test_case('Simple consecutive', [100, 4, 200, 1, 3, 2], 4)
    _run_test_case('Unsorted with duplicates', [1, 2, 0, 1], 3)
    _run_test_case('Negative consecutive', [-1, 0, 1, 2], 4)
    _run_test_case('Large consecutive range', list(range(1000, 1010)), 10)

    # Error / invalid input conditions (should not crash - report behavior)
    _run_test_case('None input', None)
    _run_test_case('Mixed types (str inside)', [1, 2, '3', 4])
    _run_test_case('Mixed numeric types', [1, 2, 2.0, 3], 3)

    print('\nManual spot checks:')
    print('Expect 4 ->', longest_consecutive_sequence([100,4,200,1,3,2]))

# driver code
def main():
    input_nums = [
        [150, 14, 200, 1, 3, 2],
        [1, 2, 3, 4, 5, 6, 7],
        [1, 3, 5, 7],
        [7, 6, 5, 4, 3, 2, 1],
        [7, 6, 5, 1],
    ]

    for i in range(0, len(input_nums)):
        print(i+1, ".\tnums = ", input_nums[i], sep="")
        print("\tThe length of the longest consecutive sequence is:", longest_consecutive_sequence(input_nums[i]))
        print("-"*100)
    
    # Edge cases
    _run_test_case('Empty list', [], 0)
    _run_test_case('Single element', [7], 1)
    _run_test_case('All duplicates', [2, 2, 2], 1)
    _run_test_case('Simple consecutive', [100, 4, 200, 1, 3, 2], 4)
    _run_test_case('Unsorted with duplicates', [1, 2, 0, 1], 3)
    _run_test_case('Negative consecutive', [-1, 0, 1, 2], 4)
    _run_test_case('Large consecutive range', list(range(1000, 1010)), 10)

    # Error / invalid input conditions (should not crash - report behavior)
    _run_test_case('None input', None)
    #_run_test_case('Mixed types (str inside)', [1, 2, '3', 4])
    _run_test_case('Mixed numeric types', [1, 2, 2.0, 3], 3)

    print('\nManual spot checks:')
    print('Expect 4 ->', longest_consecutive_sequence([100,4,200,1,3,2]))

if __name__ == '__main__':
    main()
