"""
⬅️ We have provided a union_find.py file under the "Files" tab 
of this widget. You can use this file to build your solution.
"""
from UnionFind import UnionFind


def num_islands(grid):
    # validation
    if not grid or not grid[0]:
        return 0
    numRows = len(grid)
    numCols = len(grid[0])
    for row in grid:
        if len(row) != numCols:
            raise ValueError("grid must be rectangular (all rows same length)")

    def is_land(cell):
        return cell == "1" or cell == 1

    DIRECTIONS = [
        (-1, 0),  # North
        (1, 0),   # South
        (0, -1),  # West
        (0, 1),   # East
    ]
    islandMap = UnionFind(grid)
    for i in range(numRows):
        for j in range(numCols):
            if not is_land(grid[i][j]):
                continue
            for dr, dc in DIRECTIONS:
                nr, nc = i + dr, j + dc
                if 0 <= nr < numRows and 0 <= nc < numCols and is_land(grid[nr][nc]):
                    origIndex = i * numCols + j
                    neighborIndex = nr * numCols + nc
                    if islandMap.find(origIndex) != islandMap.find(neighborIndex):
                        islandMap.union(origIndex, neighborIndex)
    return islandMap.get_count()
                
def main():

    def print_grid(grid):
        for i in grid:
            print("\t", i)

    grid1 = [
        ['1', '1', '1'],
        ['0', '1', '0'],
        ['1', '0', '0'],
        ['1', '0', '1']
    ]

    grid2 = [
        ['1', '1', '1', '1', '0'],
        ['1', '0', '0', '0', '1'],
        ['1', '0', '0', '1', '1'],
        ['0', '1', '0', '1', '0'],
        ['1', '1', '0', '1', '1']
    ]

    grid3 = [
        ['1', '1', '1', '1', '0'],
        ['1', '0', '0', '0', '1'],
        ['1', '1', '1', '1', '1'],
        ['0', '1', '0', '1', '0'],
        ['1', '1', '0', '1', '1']
    ]

    grid4 = [
        ['1', '0', '1', '0', '1'],
        ['0', '1', '0', '1', '0'],
        ['1', '0', '1', '0', '1'],
        ['0', '1', '0', '1', '0'],
        ['1', '0', '1', '0', '1']
    ]

    grid5 = [
        ['1', '0', '1'],
        ['0', '0', '0'],
        ['1', '0', '1']
    ]

    inputs = [grid1, grid2, grid3, grid4, grid5]
    num = 1
    for i in inputs:
        print(num, ".\tGrid:\n", sep = "")
        print_grid(i)
        print('\n\tOutput :', num_islands(i))
        print('-' * 100)
        num += 1


if __name__ == "__main__":
    main()
