def reverse_bits(n):
    result = 0
    for i in range(32):
        x = n & 1;
        result = result | x
        n = n >> 1
        if i != 31:
            result = result << 1
    
    return result

# Driver code
def main():
    inputs = [91697, 41596, 5, 4294967293, 43261596]
    for i in range(len(inputs)):
        print(i + 1, ".\tInteger:", inputs[i])
        print("\n\tInteger after Bit Reversal:", reverse_bits(inputs[i]))
        print("-" * 100)


if __name__ == "__main__":
    main()
