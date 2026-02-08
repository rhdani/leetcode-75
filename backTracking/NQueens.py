def totalNQueens(n):
    """
    Count the total number of valid solutions to the N-Queens problem.
    
    The N-Queens problem asks to place n queens on an n×n chessboard such that
    no two queens threaten each other. Queens can attack horizontally, vertically,
    and diagonally.
    
    This function uses backtracking with three sets to track occupied columns and
    diagonals for O(1) conflict detection:
    - cols: tracks occupied columns
    - pos_diag: tracks occupied positive diagonals (row + col)
    - neg_diag: tracks occupied negative diagonals (row - col)
    
    Args:
        n (int): The size of the chessboard (n×n) and number of queens to place.
    
    Returns:
        int: The total count of valid N-Queens solutions for a board of size n×n.
    
    Time Complexity: O(N!) - explores all valid placements
    Space Complexity: O(N) - for the recursion stack and tracking sets
    """
    
    # Keeps track of occupied columns
    cols = set() 
    
    # Keeps track of occupied positive diagonals (row + col is constant)
    pos_diag = set() 
    
    # Keeps track of occupied negative diagonals (row - col is constant)
    neg_diag = set()
    
    def backtrack(row, numSolutions):
        if row == n:
            numSolutions[0] += 1
            return

        for col in range(n):
            # Check Safety (O(1) lookup in sets)
            if col in cols or \
               (row + col) in pos_diag or \
               (row - col) in neg_diag:
                # Conflict found, skip to the next column
                continue
            # 1. Update the state (sets and board)
            cols.add(col)
            pos_diag.add(row + col)
            neg_diag.add(row - col)
            backtrack(row + 1, numSolutions)
            cols.remove(col)
            pos_diag.remove(row + col)
            neg_diag.remove(row - col)
    
    numSolutions = []
    numSolutions.append(0)
    backtrack(0, numSolutions)
    
    return numSolutions[0]

# Driver code
def main():
    n = [4, 5, 6, 7, 8]
    for i in range(len(n)):
        print(i+1, ".\t Queens: ",
              n[i], ", Chessboard: (", n[i], "x", n[i], ")", sep="")
        res = totalNQueens(n[i])
        global tab
        tab = 2
        print("\n\t Total solutions count for ",
              n[i], " queens on a ", n[i], "x", n[i], " chessboard: ", res, sep="")
        print("-"*100, "\n", sep="")

if __name__ == '__main__':
    main()