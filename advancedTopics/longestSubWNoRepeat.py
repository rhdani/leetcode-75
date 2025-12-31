def find_longest_substring(input_str):
    last_index = {}
    left = 0
    max_len = 0
    for i, ch in enumerate(input_str):
        if ch in last_index and last_index[ch] >= left:
            left = last_index[ch] + 1
        last_index[ch] = i
        max_len = max(max_len, i - left + 1)
    return max_len

# Driver code
def main():
    string = [
        "abcabcbb",
        "pwwkew",
        "bbbbb",
        "ababababa",
        "",
        "ABCDEFGHI",
        "ABCDEDCBA",
        "AAAABBBBCCCCDDDD",
    ]
    for i in range(len(string)):
        print(i + 1, ". \t Input String: ", string[i], sep="")
        print("\t Length of longest substring: ",
                (find_longest_substring(string[i])))
        print("-" * 100)


if __name__ == "__main__":
    main()
