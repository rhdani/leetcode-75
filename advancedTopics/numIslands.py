"""
⬅️ We have provided a union_find.py file under the "Files" tab 
of this widget. You can use this file to build your solution.
"""
from UnionFind import UnionFind


def num_islands(grid):

    numRows = len(grid)
    numCols = len(grid[0])
    
    DIRECTIONS = [
        (-1, 0),  # North
        (1, 0),   # South
        (0, -1),  # West
        (0, 1),   # East
    ]
    islandMap = UnionFind(grid)
    for i in range(numRows):
        for j in range(numCols):
            if (grid[i][j] == "1"):
                for dr, dc in DIRECTIONS:
                    nr, nc = i + dr, j + dc
                    if 0 <= nr < numRows and 0 <= nc < numCols:
                        # valid neighbor
                        if (grid[nr][nc] == "1"):
                            origIndex = i*numCols + j
                            neighborIndex = nr*numCols + nc
                            if (islandMap.find(origIndex) != islandMap.find(neighborIndex)):
                                islandMap.union(origIndex, neighborIndex)
    return islandMap.get_count()
                            
grid = [["1","1","1"],["0","1","0"],["1","0","0"],["1","0","1"]]
print(num_islands(grid))                        
                
    
