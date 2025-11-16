def count_palindromic_substrings(s):
    count = 0
    length = len(s)
    
    if (length == 1):
        return 1
    dp = [[False] * length for _ in range(length)]
    for i in range(length):
        dp[i][i] = True
    count = length
    
    #check 2 letter strings
    for i in range(length-1):
        if(s[i] == s[i+1]):
            dp[i][i+1] = True
            count += 1
    for j in range(3, length+1):
        for i in range(length - j +1):
            if (s[i] == s[i+j-1]):
                if (dp[i+1][i+j-2] == True):
                    dp[i][i+j-1] = True
                    count += 1
    return count

# Driver code
def main():
    strings = ['cat', 'lever', 'xyxxyz', 'wwwwwwwwww', 'tattarrattat']

    for i in range(len(strings)):
        print(i + 1, ".\t Input string: '", strings[i], "'", sep="")
        result = count_palindromic_substrings(strings[i])
        print("\t Number of palindromic substrings: ", result, sep="")
        print("-" * 100)

if __name__ == '__main__':
    main()
