def unique_paths(m, n):
    rows = m
    cols = n
    dp =  [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range (cols):
            if (i == 0 or j == 0):
                dp[i][j] = 1
                continue
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    # Replace this placeholder return statement with your code
    return dp[rows-1][cols-1]
# Driver code
def main():
        input = (
                [1, 1],
        [2, 3],
        [4, 4],
        [2, 5],
                [10, 10],
                [1, 30]
    )
        print("S: Source, D: Destination")
        print("-"*100)
        for i in range(len(input)):
                print(i + 1, ".\tm = ", input[i][0], ", n = ", input[i][1], sep="")
                ans = unique_paths(input[i][0], input[i][1])
                print("\n\tTotal unique paths: ", ans)
                print("-"*100)

if __name__ == '__main__':
    main()

