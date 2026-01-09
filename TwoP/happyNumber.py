'''
Function which given an input number n, returns the sum of the squares of its digits.
'''
def sum_of_squares(n):
    total = 0
    while n > 0:
        digit = n % 10
        total += digit * digit
        n //= 10
    return total

def is_happy_number(n):
    slowP = sum_of_squares(n)
    fastP = sum_of_squares(slowP)
    while fastP != 1 and slowP != fastP:
        slowP = sum_of_squares(slowP)
        fastP = sum_of_squares(sum_of_squares(fastP))
    return fastP == 1

def main():
    tests = [
        (1, True),        # smallest happy
        (0, False),       # zero is not happy
        (7, True),        # known happy
        (19, True),       # known happy
        (2, False),       # known unhappy
        (20, False),      # leads to unhappy cycle
        (1000000, True),  # large number that reduces to 1
        (-7, False),      # negative numbers treated as not happy
    ]

    for idx, (val, expected) in enumerate(tests, start=1):
        result = is_happy_number(val)
        print(idx, ".\tInput Number: ", val, sep="")
        print("\n\tIs it a happy number? ", result)
        print("\tExpected: ", expected)
        assert result == expected, f"Test failed for {val}: expected {expected} got {result}"
        print("-" * 100)

    # non-integer should raise TypeError
    try:
        is_happy_number("19")
    except TypeError:
        print('non-integer test passed')
    else:
        raise AssertionError('Passing non-integer should raise TypeError')

    print('All tests passed')


if __name__ == '__main__':
    main()
