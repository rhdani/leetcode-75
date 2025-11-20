def num_of_decodings(decode_str):
    n = len(decode_str)
    if n == 0 or decode_str[0] == '0':
        return 0
    dp = [0] * (n+1)
    dp[0] = 1               # empty string
    dp[1] = 1

    for i in range(2, n+1):
        if decode_str[i - 1] != '0':
            dp[i] += dp[i - 1]
        cur_num = int(decode_str[i-2:i])
        if (cur_num >= 10 and cur_num <= 26):
            dp[i] += dp[i-2]

    return (dp[n])
def main():
    decode_str = ["124", "123456", "11223344", "0", "0911241", "10203", "999901"]

    for i in range(len(decode_str)):
        print(i + 1, f".\t There are {num_of_decodings(decode_str[i])} ways in which we can decode the string: '",
                        decode_str[i], "'", sep="")
        print("-" * 100)

if __name__ == '__main__':
    main()

