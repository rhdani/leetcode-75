def integer_addition(a, b):
    MASK = 0xFFFFFFFF        # 32 bits of 1s
    MAX_INT = 0x7FFFFFFF     # max positive 32-bit int

    while b != 0:
        carry = (a & b) & MASK
        a = (a ^ b) & MASK
        b = (carry << 1) & MASK

    # convert to signed integer
    return a if a <= MAX_INT else ~(a ^ MASK) 

# Driver code
def main():
    nums = [[1, -1], [2, 5], [3, 10], [-10, -40], [13, 16]]

    for i in range(len(nums)):
        print(str(i+1),".\tThe sum of", nums[i], "is:", integer_addition(nums[i][0], nums[i][1]))
        print("-"*100)

if __name__ == '__main__':
    main()


