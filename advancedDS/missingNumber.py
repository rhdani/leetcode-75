from typing import Sequence

def find_missing_number(nums: Sequence[int]) -> int:
    """Return the missing number from an array containing n distinct numbers
    taken from the range 0..n. The input sequence is NOT modified.

    Uses XOR which runs in O(n) time and O(1) extra space.
    """
    n = len(nums)
    missing = 0
    # XOR all indices 0..n
    for i in range(n + 1):
        missing ^= i
    # XOR with all numbers in the array
    for v in nums:
        missing ^= v
    return missing

# Driver code
def main() -> None:
  examples = [
    [3, 0, 1],
    [0, 1],
    [9, 6, 4, 2, 3, 5, 7, 0, 1],
    [0],
    [1],
  ]
  for idx, arr in enumerate(examples, start=1):
    print(f"{idx}.\tInput array: {arr}")
    print(f"\tMissing number: {find_missing_number(arr)}")
    print("-" * 100)


if __name__ == "__main__":
  main()
