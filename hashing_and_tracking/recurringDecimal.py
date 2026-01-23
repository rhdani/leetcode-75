def fraction_to_decimal(numerator, denominator):
    result = []
    if numerator == 0:
        return "0"
    if (numerator < 0) ^ (denominator < 0):
        result.append('-')

    numerator, denominator = abs(numerator), abs(denominator)
    q, remainder = divmod(numerator, denominator)
    result.append(str(q))
    if (remainder == 0):
        return "".join(result)
    result.append('.')
    seen = {}

    while remainder != 0:
        if remainder in seen:
            idx = seen[remainder]
            result.insert(idx, '(')
            result.append(')')
            break

        seen[remainder] = len(result)

        remainder *= 10
        digit = remainder // denominator
        result.append(str(digit))
        remainder %= denominator

    return "".join(result)
# Driver code
def main():
    inputs = [(0, 4), (4, 2), (5, 333), (2, 3), (47, 18),
              (93, 7), (-5, 333), (47, -18), (-4, -2)]

    for i in range(len(inputs)):

        print(i + 1,  ".\tInput: fraction_to_decimal", inputs[i], sep="")
        result = fraction_to_decimal(inputs[i][0], inputs[i][1])
        print("\tOutput: ", result, sep="")
        print("-"*100)
if __name__ == '__main__':
    main()
