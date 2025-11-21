def max_sub_array(nums):
    dp = [-10000] * len(nums)

    if (len(nums) == 1):
        return nums[0]
    dp[0] = nums[0]
    max_sum = dp[0]
    for i in range(1, len(nums)):
        dp[i] = max(nums[i], dp[i-1] + nums[i])
        max_sum = max(max_sum, dp[i])
    return max_sum

# Driver code
def main():
    inputs = [[1, 2, 2, 3, 3, 1, 4], [2, 2, 1], [4, 1, 2, 1, 2], [-4, -1, -2, -1, -2], [25]]

    for i in range(len(inputs)):
        print(i + 1, ".\tArray: ", inputs[i], sep="")
        print("\tResult: ", max_sub_array(inputs[i]), sep="")
        print("-" * 100)


if __name__ == "__main__":
    main()

