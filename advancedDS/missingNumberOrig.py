def find_missing_number(nums):
  
  length = len(nums)
  index = 0

  while index < length:
    # Get the correct index for the current element
    correctIndex = nums[index]
    if (nums[index] >= length):
      index += 1
      continue
    # Swap if the element is not in its correct position
    if nums[index] != nums[correctIndex]:
      tmp = nums[index]
      nums[index] = nums[correctIndex]
      nums[correctIndex] = tmp
    else:
      index += 1  # Move to the next index when no swap is needed
      
  for i in range(length):
    if nums[i] != i:
      return i
        
  return -1

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


