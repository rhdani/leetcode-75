def longest_subsequence(nums):
    length = len(nums)

    tails = []
    for x in nums:
        # --- Binary search for first element >= x ---
        left, right = 0, len(tails)
        while left < right:
            mid = (left + right) // 2
            if tails[mid] < x:
                left = mid + 1
            else:
                right = mid
        # left is now the insertion index
        if left == len(tails):
            tails.append(x)
        else:
            tails[left] = x
    return (len(tails))

def main():
        lists = [[10, 9, 2, 5, 3, 7, 101, 18], [7, 7, 7, 7, 7, 7, 7], [0, 1, 0, 3, 2, 3],
        [3, 2], [6, 9, 8, 2, 3, 5, 1, 4, 7], [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15],
        [9, 2, 5, 3, 6, 14, 11, 7, 9, 5, 13, 3, 15, 0, 8, 4, 1, 9, 5, 13, 3, 11, 7, 15, 0, 10, 6, 14, 9, 2, 5, 3, 2, 10, 6, 10, 6, 5, 13, 3, 11, 7, 15, 3, 11, 7, 15]]

        for i, input_list in enumerate(lists):
                print(i+1, ".\tInput array: ", input_list, sep="")
                print("\tLength of LIS is:", longest_subsequence(input_list))
                print("-"*100)

if __name__ == '__main__':
        main()

