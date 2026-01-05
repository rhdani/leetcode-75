from numIslands import num_islands


def run_tests():
    tests = [
        ([], 0),
        ([[]], 0),
        ([['0']], 0),
        ([['1']], 1),
        (
            [['1','1','1'],['0','1','0'],['1','0','0'],['1','0','1']],
            3
        ),
        (
            [['1','0','1'],['0','0','0'],['1','0','1']],
            4
        ),
    ]
    for grid, expected in tests:
        result = num_islands(grid)
        print('grid ->', grid, ' expected:', expected, ' got:', result)
        assert result == expected
    # non-rectangular should raise
    try:
        num_islands([['1','0'], ['1']])
    except ValueError:
        print('non-rectangular test passed')
    else:
        raise AssertionError('non-rectangular should raise ValueError')
    print('All tests passed')


if __name__ == '__main__':
    run_tests()
