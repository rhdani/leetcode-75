def jump_game(nums):
    
    count = len(nums)
    if ((count == 0) or (count == 1)):
        return True
        
    target_index = count - 1
    current_index = count - 2
    while (current_index >= 0):
        value_at_current = nums[current_index]
        if (value_at_current+current_index >= target_index):
            target_index = current_index
        current_index -= 1
    if (target_index == 0):
        return True
    else:
        return False
    
def main():
    nums = [
        [3, 2, 2, 0, 1, 4],
        [2, 3, 1, 1, 9],
        [3, 2, 1, 0, 4],
        [0],
        [1],
        [4, 3, 2, 1, 0],
        [1, 1, 1, 1, 1],
        [4, 0, 0, 0, 1],
        [3, 3, 3, 3, 3],
        [1, 2, 3, 4, 5, 6, 7]
    ]

    for i in range(len(nums)):
        print(i + 1, ".\tInput array: ", nums[i], sep="")
        print("\tCan we reach the very last index? ",
              "Yes" if jump_game(nums[i]) else "No", sep="")
        print("-" * 100)


if __name__ == '__main__':
    main()