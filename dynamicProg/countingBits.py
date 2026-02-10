def counting_bits(n):
    dp = [0] * (n+1)
    
    dp[0] = 0
    if (n<1):
        return dp
    dp[1] = 1
    
    for i in range(2, n+1):
        dp[i] = dp[i//2] + i%2
    return dp

def main():
    input_bits = [1, 2, 3, 4, 5, 10]

    for i in range(len(input_bits)):
        print(i + 1, ".\t Bits: ", input_bits[i], sep="")
        print("\t Counting bits: ", counting_bits(input_bits[i]), sep="")
        print("-" * 100)


if __name__ == '__main__':
    main()
