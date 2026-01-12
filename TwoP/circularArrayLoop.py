'''
There is a circular list of non-zero integers called nums. Each number in the list tells you how many steps to move forward or backward from your current position:
If nums[i] is positive, move nums[i] steps forward.
If nums[i] is negative, move nums[i] steps backward.
As the list is circular:
Moving forward from the last element takes you back to the first element.
Moving backward from the first element takes you to the last element.
A cycle in this list means:
You keep moving according to the numbers, and you end up repeating a sequence of indexes.
All numbers in the cycle have the same sign (either all positive or all negative).
The cycle length is greater than 1 (it involves at least two indexes).
Return true if such a cycle exists in the list or false otherwise.
Constraints:

1 ≤ nums.length ≤ 10³
−5000 ≤ nums[i] ≤ 5000
nums[i] != 0
'''
def circularArrayLoop(nums):
    n = len(nums)

    def next_index(i):
        return (i + nums[i]) % n

    for i in range(n):
        if nums[i] == 0:
            continue

        slow, fast = i, next_index(i)
        while nums[fast] * nums[i] > 0 and nums[next_index(fast)] * nums[i] > 0:
            if slow == fast:
                if slow == next_index(slow):
                    break
                return True
            slow = next_index(slow)
            fast = next_index(next_index(fast))

        marker = i
        sign = nums[i]
        while nums[marker] * sign > 0:
            next_marker = next_index(marker)
            nums[marker] = 0
            marker = next_marker

    return False


if __name__ == "__main__":
    # Test cases: (input, expected)
    tests = [
        ([2, -1, 1, 2, 2], True),          # positive: a valid forward cycle exists
        ([-1, 2], False),                  # negative: directions differ, no valid cycle
        ([1], False),                      # edge: single element cannot form length>1 cycle
        ([1, 1], True),                    # positive: two-element forward cycle
        ([-2, 1, -1, -2, -2], False),      # negative: no valid same-direction cycle
        ([1, 1, 1, 1, 1], True),           # positive: all forward, cycle exists
    ]

    for arr, expected in tests:
        res = circularArrayLoop(arr.copy())
        assert res == expected, f"Failed for {arr}: expected {expected}, got {res}"

    print("All tests passed.")
