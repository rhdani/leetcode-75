def is_isomorphic(string1, string2):
    # Treat None consistently: both None -> True, one None -> False
    if string1 is None or string2 is None:
        return string1 == string2
    if len(string1) != len(string2):
        return False
    
    myMap1 = {}
    myMap2 = {}
    for i in range(len(string1)):
        c1 = string1[i]
        c2 = string2[i]
        if c1 not in myMap1:
            myMap1[c1] = c2
        else:
            if myMap1[c1] != c2:
                return False
        if c2 not in myMap2:
            myMap2[c2] = c1
        else:
            if myMap2[c2] != c1:
                return False
    return True


def main():
    # Inline test cases using simple asserts (run as a script)
    cases = [
        (None, None, True),
        (None, "", False),
        ("", None, False),
        ("egg", "add", True),
        ("foo", "bar", False),
        ("paper", "title", True),
        ("ab", "aa", False),
        ("", "", True),
        ("a", "b", True),
        ("abab", "cdcd", True),
        ("abc", "ddd", False),
        # additional edge cases
        ("aaaa", "bbbb", True),
        ("aa", "ab", False),
        ("abca", "zbxz", True),
        ("abca", "zbxx", False),
        ("123 123", "abc abc", True),
        (" \t\n", " \t\n", True),
        (" ", " ", True),
        ("\t", "\t", True),
        ("\n\n", "\n\n", True),
        ("你好你好", "世界世界", True),
        ("àççà", "ßââß", True),
        ("😊😊", "😂😂", True),
        ("abcdefghijklmnopqrstuvwxyz", "mnopqrstuvwxyzabcdefghijkl", True),
        ("a" * 1000, "b" * 1000, True),
        ("ab" * 500, "cd" * 500, True),
    ]

    for a, b, expected in cases:
        result = is_isomorphic(a, b)
        assert result == expected, f"is_isomorphic({a!r}, {b!r}) == {result}, expected {expected}"

    print("is_isomorphic: all inline tests passed")


if __name__ == "__main__":
    main()
