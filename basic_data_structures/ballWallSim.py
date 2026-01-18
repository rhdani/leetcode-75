from PrintList import print_grid
def find_exit_column(grid):
    
    nrows = len(grid)
    ncols = len(grid[0])
    result = [0] * ncols
    
    for col in range(ncols):
        currentCol = col
        for row in range(nrows):
            if (grid[row][currentCol] == -1 and currentCol == 0): #hits left wall
                result[col] = -1
                break
            if (grid[row][currentCol] == 1 and currentCol == (ncols - 1)): #hits right wall
                result[col] = -1
                break
            if ((currentCol < (ncols - 1)) and (grid[row][currentCol] == 1) and (grid[row][currentCol + 1] == -1)): #hits V with right cell
                result[col] = -1
                break
            if ((currentCol > 0) and (grid[row][currentCol] == -1 and (grid[row][currentCol - 1] == 1))): #hits V with left call
                result[col] = -1
                break
            if (grid[row][currentCol] == 1):
                currentCol += 1
            else:
                currentCol -= 1
        if (result[col] != -1):
            result[col] = currentCol
                
    return result

# Driver Code
def main():


    grids = [[[1, 1, 1, -1, -1], [1, 1, 1, -1, -1], [-1, -1, -1, 1, 1], [1, 1, 1, 1, -1], [-1, -1, -1, -1, -1]],
                 [[1 , 1, 1, -1, 1, 1, 1 , 1, 1, -1, 1, 1], [-1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1], [1, 1, 1, -1, 1, 1, 1, 1, 1, -1, 1, 1], [-1, -1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1]],
                 [[-1 ,-1, -1, -1], [1, 1, 1, 1], [-1, -1, -1, -1], [1, 1, 1, 1]],
                 [[1]],
                 [[-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1]]]

    for i in range(len(grids)):
        print("Test Case #", i+1, "\n\nInput grid: ")
        print_grid(grids[i])
        print("\nOutput: " , find_exit_column(grids[i]))
        print("-" * 100)

if __name__ == '__main__':
    main()
