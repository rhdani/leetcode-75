def sort_colors(colors):
    left = 0
    two = len(colors) - 1
    i = 0

    while i <= two:
        current = colors[i]
        if current == 0:
            colors[i], colors[left] = colors[left], colors[i]
            left += 1
            i += 1
        elif current == 2:
            colors[i], colors[two] = colors[two], colors[i]
            two -= 1
            # do not increment i here; the swapped-in value must be processed
        else:
            i += 1

    return colors


def _run_driver_tests():
    cases = [
        ([], []),
        ([0], [0]),
        ([2, 1, 0], [0, 1, 2]),
        ([2, 2, 1, 1, 0, 0], [0, 0, 1, 1, 2, 2]),
        ([1, 1, 1], [1, 1, 1]),
        ([0, 2, 1, 2, 0, 1], [0, 0, 1, 1, 2, 2]),
    ]

    for inp, expected in cases:
        arr = list(inp)
        before_id = id(arr)
        res = sort_colors(arr)
        print('input ->', inp, ' sorted ->', arr)
        assert arr == expected, f'expected {expected}, got {arr}'
        # ensure function sorts in-place and returns the same list
        assert id(arr) == before_id, 'sort_colors should sort in-place'
        assert res == arr

    # random-ish extra checks
    arr = [2, 0, 1, 2, 1, 0, 0, 2]
    sort_colors(arr)
    assert arr == [0, 0, 0, 1, 1, 2, 2, 2]

    print('All color_sort tests passed')


if __name__ == '__main__':
    _run_driver_tests()
