'''
Docstring for floodFill
You are given a 2D grid of size m x n, where grid[i][j] represents the pixel value at
position (i, j). Additionally, you are given three integers:
sr: The row index of the starting pixel
sc: The column index of the starting pixel
target: The new color to apply

Perform a flood fill starting from `grid[sr][sc]`. If the starting pixel already has the
value `target`, the grid is returned unchanged. Otherwise, change the color of the starting
pixel and all 4-directionally connected pixels (up, down, left, right) that have the same
original color to `target`.

Return the updated grid (modified in-place).

Constraints:
1 ≤ len(grid), len(grid[i]) ≤ 30
0 ≤ grid[i][j], target ≤ 2**16
0 ≤ sr < len(grid)
0 ≤ sc < len(grid[i])
'''

import random

def flood_fill(grid, sr, sc, target):
    if not grid or not grid[0]:
        return grid
    nrows, ncols = len(grid), len(grid[0])
    if not (0 <= sr < nrows and 0 <= sc < ncols):
        raise IndexError("sr/sc out of bounds")
    orig = grid[sr][sc]
    if orig == target:
        return grid

    # Iterative DFS using an explicit stack to avoid recursion limits
    stack = [(sr, sc)]
    while stack:
        r, c = stack.pop()
        if grid[r][c] != orig:
            continue
        grid[r][c] = target
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < nrows and 0 <= nc < ncols and grid[nr][nc] == orig:
                stack.append((nr, nc))
    return grid

# Driver code
def main():
    grids = [[ 
                [1, 1, 0, 1, 0], 
                [0, 0, 0, 0, 1], 
                [0, 0, 0, 1, 1], 
                [1, 1, 1, 1, 0], 
                [1, 0, 0, 0, 0]
            ],
            [   
                [1, 1, 0, 1], 
                [0, 0, 0, 0], 
                [0, 0, 0, 1], 
                [1, 1, 1, 1]
            ],
            [   
                [9, 9, 6, 9], 
                [6, 9, 9, 6], 
                [6, 9, 9, 9], 
                [9, 9, 9, 9]
            ],
            [   
                [1, 1, 0, 1], 
                [0, 1, 0, 0], 
                [0, 1, 1, 0], 
                [1, 0, 1, 1]
            ],
            [   
                [1, 2, 0, 0], 
                [3, 1, 3, 6], 
                [7, 2, 1, 5], 
                [1, 9, 2, 1]
            ]]

    starting_row = [4, 2, 2, 2, 1]
    starting_col = [3, 3, 1, 3, 1]
    new_target = [3, 2, 1, 0, 4]

    for i in range(len(grids)):
        print(i + 1, ".\t Grid before flood fill: ", grids[i], sep = "")
        print("\t Starting row and column are: (" , starting_row[i], ", ", starting_col[i], ")", sep = "")
        print("\t Target value: ", new_target[i], sep = "")
        print("\t After perform flood fill: ", flood_fill(grids[i], starting_row[i], starting_col[i], new_target[i]), sep = "")
        print("-" * 100)

    # Unit tests for edge cases
    # 1) Empty grid
    assert flood_fill([], 0, 0, 1) == []

    # 2) Grid with empty row
    assert flood_fill([[]], 0, 0, 1) == [[]]

    # 3) Single cell change
    g = [[0]]
    assert flood_fill(g, 0, 0, 2) == [[2]]

    # 4) Starting pixel already target (no change)
    g = [[3]]
    assert flood_fill(g, 0, 0, 3) == [[3]]

    # 5) Out of bounds indices should raise IndexError
    try:
        flood_fill([[1]], 1, 0, 2)
        assert False, "Expected IndexError for out-of-bounds sr"
    except IndexError:
        pass

    # 6) Full grid replacement
    g = [[1, 1], [1, 1]]
    assert flood_fill(g, 0, 0, 9) == [[9, 9], [9, 9]]

    # 7) Large random grid (deterministic) - verify only connected component changes
    random.seed(42)
    N = 30
    large = [[random.randint(0, 100) for _ in range(N)] for _ in range(N)]
    sr = random.randrange(N)
    sc = random.randrange(N)
    orig = large[sr][sc]

    # compute connected component of cells equal to orig
    stack = [(sr, sc)]
    comp = set()
    while stack:
        r, c = stack.pop()
        if (r, c) in comp:
            continue
        if large[r][c] != orig:
            continue
        comp.add((r, c))
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N:
                stack.append((nr, nc))

    # run flood fill and assert only component cells changed
    large_copy = [row[:] for row in large]
    tgt = 12345
    flood_fill(large, sr, sc, tgt)
    for r in range(N):
        for c in range(N):
            if (r, c) in comp:
                assert large[r][c] == tgt
            else:
                assert large[r][c] == large_copy[r][c]

    print("Unit tests passed")


if __name__ == '__main__':
    main()