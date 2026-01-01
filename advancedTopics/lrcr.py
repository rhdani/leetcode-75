def longest_repeating_character_replacement(s, k) -> int:
    start_window = 0
    end_window = 1
    
    max_length = 0
    count = {}
    result = 0
    
    length = len(s)
    
    for end_window in range(length):
        count[s[end_window]] = count.get(s[end_window], 0) + 1
        max_length = max(max_length, count[s[end_window]])

        # If more than k replacements needed, shrink window
        while (end_window - start_window + 1) - max_length > k:
            count[s[start_window]] -= 1
            start_window += 1

        result = max(result, end_window - start_window + 1)

    return result
# Driver code
def main():
    # Base cases and previously included examples
    input_strings = [
        "aabccbb",
        "abbcb",
        "abccde",
        "abbcab",
        "bbbbbbbbb",
        "",                  # empty string
        "a",                 # single character
        "abcdef",            # all unique characters
        "AAAAaaaAAA",        # mixed case (case-sensitive test)
        "aaabbbbcccddeeeee", # multiple repeated groups
        "a!a!a!@#",          # symbols and punctuation
        "ñññáá",             # unicode characters
        "ababa" * 10        # longer alternating pattern
    ]

    values_of_k = [2, 1, 1, 2, 4, 0, 0, 2, 3, 2, 3, 1, 5]

    for i in range(len(input_strings)):
        s = input_strings[i]
        k = values_of_k[i]
        print(f"Test {i+1}:")
        print("\tInput String:", repr(s))
        print("\tk:", k)
        print("\tLength of longest substring with repeating characters:", longest_repeating_character_replacement(s, k))
        print("-" * 100)

if __name__ == '__main__':
    main()
