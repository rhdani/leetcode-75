from collections import Counter

def min_window(s: str, t: str) -> str:
    if not s or not t:
        return ""

    dict_t = Counter(t)
    required = len(dict_t)

    # window pointers and state
    l, r = 0, 0
    formed = 0
    window_counts = {}

    # (window length, left, right)
    ans = float("inf"), None, None

    while r < len(s):
        ch = s[r]
        window_counts[ch] = window_counts.get(ch, 0) + 1

        if ch in dict_t and window_counts[ch] == dict_t[ch]:
            formed += 1

        # Try and contract the window till the point it ceases to be 'desirable'
        while l <= r and formed == required:
            ch = s[l]

            # Save the smallest window so far
            if r - l + 1 < ans[0]:
                ans = (r - l + 1, l, r)

            window_counts[ch] -= 1
            if ch in dict_t and window_counts[ch] < dict_t[ch]:
                formed -= 1

            l += 1

        r += 1

    return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]


if __name__ == '__main__':
    tests = [
        ("ABDFGDCKAB", "ABCD", "DCKAB"),          # reported failing case
        ("ADOBECODEBANC", "ABC", "BANC"),        # classic example
        ("", "A", ""),                          # empty s
        ("A", "", ""),                          # empty t
        ("A", "A", "A"),                        # single char match
        ("AA", "AA", "AA"),                     # duplicates in t
        ("a", "A", ""),                         # case-sensitive
        ("aA", "A", "A"),                       # case-sensitive pick
    ]

    for i, (s, t, expected) in enumerate(tests, 1):
        result = min_window(s, t)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test {i}: s={repr(s)}, t={repr(t)} -> result={repr(result)}, expected={repr(expected)} [{status}]")
