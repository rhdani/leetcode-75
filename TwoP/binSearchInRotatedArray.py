"""Utilities for searching in rotated, sorted arrays.

Provides `binary_search_rotated` which returns the index of `target`
in a rotated sorted list `nums`, or -1 if not present. Assumes no
duplicates in `nums`.
"""

from typing import List

def binary_search_rotated(nums: List[int], target: int) -> int:
    """Return index of `target` in rotated sorted `nums`, or -1 if missing.

    Assumes no duplicate values in `nums`.

    Time: O(log n) on average, Space: O(1).
    """
    if not nums:
        return -1

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid

        # If left..mid is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # mid..right is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1
def main():
    nums_list = [[5, 6, 7, 1, 2, 3, 4],
                 [40, 50, 60, 10, 20, 30],
                 [47, 58, 69, 72, 83, 94, 12, 24, 35], 
                 [77, 82, 99, 105, 5, 13, 28, 41, 56, 63], 
                 [48, 52, 57, 62, 68, 72, 5, 7, 12, 17, 21, 28, 33, 37, 41]]

    target_list = [1, 50, 12, 56, 5]

    for i in range(len(target_list)):
        print((i + 1), ".\tRotated array: ", nums_list[i], "\n\ttarget", target_list[i], "found at index ", \
              binary_search_rotated(nums_list[i], target_list[i]))
        print("-"*100)


if __name__ == '__main__':
    main()
