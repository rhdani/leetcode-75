def word_search(grid, word):

    rows = len(grid)
    cols = len(grid[0])
    print ("rows is ", rows, "cols is ", cols)
    results = []

    def backtrack(r, c, idx):
        # If all characters found
        if idx == len(word):
            return True

        # Out of bounds or character mismatch
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return False

        if grid[r][c] != word[idx]:
            return False

        # Mark visited by using a placeholder
        temp = grid[r][c]
        grid[r][c] = '#'

        # Explore all 4 directions
        found = (backtrack(r+1, c, idx+1) or
                 backtrack(r-1, c, idx+1) or
                 backtrack(r, c+1, idx+1) or
                 backtrack(r, c-1, idx+1))

        # Restore character
        grid[r][c] = temp

        return found

    # Try starting from every cell
    retVal = False
    for i in range(rows):
        for j in range(cols):
            if backtrack(i, j, 0):
                retVal = True

    return retVal

def main():
    input = [
             ([['E', 'D', 'X', 'I', 'W'],
              ['P', 'U', 'F', 'M', 'Q'],
              ['I', 'C', 'Q', 'R', 'F'],
              ['M', 'A', 'L', 'C', 'A'],
              ['J', 'T', 'I', 'V', 'E']], "EDUCATIVE"),

             ([['E', 'D', 'X', 'I', 'W'],
              ['P', 'A', 'F', 'M', 'Q'],
              ['I', 'C', 'A', 'S', 'F'],
              ['M', 'A', 'L', 'C', 'A'],
              ['J', 'T', 'I', 'V', 'E']], "PACANS"),

              ([['h', 'e', 'c', 'm', 'l'],
              ['w', 'l', 'i', 'e', 'u'],
              ['a', 'r', 'r', 's', 'n'],
              ['s', 'i', 'i', 'o', 'r']], "warrior"),

              ([['C', 'Q', 'N', 'A'],
              ['P', 'S', 'E', 'I'],
              ['Z', 'A', 'P', 'E'],
              ['J', 'V', 'T', 'K']], "SAVE"),

             ([['O', 'Y', 'O', 'I'],
              ['B', 'Y', 'N', 'M'],
              ['K', 'D', 'A', 'R'],
              ['C', 'I', 'M', 'I'],
              ['Z', 'I', 'T', 'O']], "DYNAMIC"),
            ]
    num = 1

    for i in input:
        print(num, ".\tGrid =", sep="")
        for j in range(len(i[0])):
            print("\t\t", i[0][j])
        if i[1] == "":
            print('\n\tWord = ""')
        else:
            print(f"\n\tWord =  {i[1]}")
        print("\n\tProcessing...")
        search_result = word_search(i[0], i[1])
        if search_result:
            print("\n\tSearch result = Found Word")
        else:
            print("\n\tSearch result = Word could not be found")
        num += 1
        print("-"*100, "\n")


if __name__ == "__main__":
    main()

