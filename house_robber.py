def rob_houses(nums):

    N = len(nums)
    dp = [0]*N

    if (N == 1):
        return nums[0]
    if (N == 2):
        return max(nums[0], nums[1])
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, N):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    return dp[N-1]
    ''' Optimized for memory solution
    prev2 = nums[0]
    prev = max(nums[0], nums[1])
   
    for i in range(2, N):
        curr = max(prev, prev2 + nums[i])
        prev2 = prev
        prev = curr
    return prev
    '''
# Driver code
def main():
        lists = [[2, 7, 9, 31, 33, 4, 99, 1 , 2, 3, 15, 34, 23, 11, 9, 1, 4], [1, 2, 3, 1],
        [4, 6, 3, 9, 3, 8, 3], [1, 5, 7, 3, 7 , 2, 3], [2, 7, 9, 3, 1]]
        for i in lists:
                print('Maximum robbery in example',i , 'is' , rob_houses(i))
                print("-"*100, "\n", sep="")

if __name__ == '__main__':
        main()

