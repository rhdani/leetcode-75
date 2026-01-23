"""
Compress consecutive equal elements in a list.

Example:
    Input: ["a","a","a","b","c","c","a"]
    Output: [("a", 3), ("b", 1), ("c", 2), ("a", 1)]
"""

from typing import Any, List, Tuple


def compress_list(input_list: List[Any]) -> List[Tuple[Any, int]]:
    """Return a list of (value, count) for consecutive equal values.

    This implementation is simple, avoids indexing pitfalls, and
    correctly handles empty and single-element lists.
    """
    if not input_list:
        return []

    result: List[Tuple[Any, int]] = []
    current = input_list[0]
    count = 1

    for item in input_list[1:]:
        if item == current:
            count += 1
        else:
            result.append((current, count))
            current = item
            count = 1

    result.append((current, count))
    return result


if __name__ == "__main__":
    input_list = ["a", "a", "a", "b", "c", "c", "a"]
    print(compress_list(input_list))
    input_list = []
    print(compress_list(input_list))
    input_list = ["a", "a", "a", "a"]
    print(compress_list(input_list))
