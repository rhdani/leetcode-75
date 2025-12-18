from Trie import *

class WordFinder():
    def __init__(self, grid, words):
        self.grid = grid
        self.words = words
        self.wordTree = Trie()
        self.numRows = 0
        self.numCols = 0
        self.visitedGrid = None
        if (grid):
            self.numRows = len(grid)
            self.numCols = len(grid[0])
            self.visitedGrid = [[False for _ in range(self.numCols)] for _ in range(self.numRows)]
        if (words):
            for word in words:
                self.wordTree.insert(word)

    def findWord(self, word):
        for i in range (self.numRows):
            for j in range (self.numCols):
                if self.grid[i][j] == word[0]:
                    retVal = self._searchWordHelper(word, word[0], 1, i, j)
                    if retVal:
                        return True
        return False

    def _searchWordHelper(self, word, prefix, index, row, col) -> bool:
        self.visitedGrid[row][col] = True
        if (index == len(word)):
            self.visitedGrid[row][col] = False
            return self.wordTree.search(word)
        newChar = word[index]
        newPrefix = prefix + newChar
        found = False
        #Check for new char in neighbors
        if (self.numRows > row + 1):
            if (not self.visitedGrid[row + 1][col] and self.grid[row + 1][col] == newChar):
                found = self._searchWordHelper(word, newPrefix, index + 1, row + 1, col)
        if (not found and row > 0):
            if (not self.visitedGrid[row - 1][col] and self.grid[row - 1][col] == newChar):
                found = self._searchWordHelper(word, newPrefix, index + 1, row - 1 , col)
        if (not found and self.numCols > col + 1):
            if (not self.visitedGrid[row][col + 1] and self.grid[row][col + 1] == newChar):
                found = self._searchWordHelper(word, newPrefix, index + 1, row, col + 1)
        if (not found and col > 0):
            if (not self.visitedGrid[row][col - 1] and self.grid[row][col - 1] == newChar):
                found = self._searchWordHelper(word, newPrefix, index + 1, row, col - 1)
        self.visitedGrid[row][col] = False
        return found

    def findWords(self):
        retVal = []
        for word in self.words:
            if self.findWord(word):
                retVal.append(word)
        return retVal

def print_grid(grid):
    for i in grid:
        output = '   '.join(i)
        print("\t", output)

def find_strings(grid, words):
    obj = WordFinder(grid, words)
    retVal = obj.findWords()
    return retVal

# Driver Code
def main():
    test_case_grid = [
        [['B', 'S', 'L', 'I', 'M'],
        ['R', 'I', 'L', 'M', 'O'],
        ['O', 'L', 'I', 'E', 'O'],
        ['R', 'Y', 'I', 'L', 'N'],
        ['B', 'U', 'N', 'E', 'C']],

        [['C', 'S', 'L', 'I', 'M'],
        ['O', 'I', 'B', 'M', 'O'],
        ['O', 'L', 'U', 'E', 'O'],
        ['N', 'L', 'Y', 'S', 'N'],
        ['S', 'I', 'N', 'E', 'C']],

        [['C', 'O', 'L', 'I', 'M'],
        ['I', 'N', 'L', 'M', 'O'],
        ['A', 'L', 'I', 'E', 'O'],
        ['R', 'T', 'A', 'S', 'N'],
        ['S', 'I', 'T', 'A', 'C']],

        [['P', 'S', 'L', 'A', 'M'],
        ['O', 'P', 'U', 'R', 'O'],
        ['O', 'L', 'I', 'E', 'O'],
        ['R', 'T', 'A', 'S', 'N'],
        ['S', 'I', 'T', 'A', 'C']],

        [['O', 'A', 'A', 'N'],
        ['E', 'T', 'A', 'E'],
        ['I', 'H', 'K', 'R'],
        ['I', 'F', 'L', 'V']],

        [['S', 'T', 'R', 'A', 'C'],
        ['I', 'R', 'E', 'E', 'E'],
        ['N', 'G', 'I', 'T', 'C'],
        ['I', 'T', 'S', 'R', 'A']],

        [['A', 'A', 'A'],
        ['A', 'A', 'A'],
        ['A', 'A', 'A']]
    ]

    strings_to_search = [
        ["BUY", "SLICK", "SLIME", "ONLINE", "NOW"],
        ["BUY", "STUFF", "ONLINE", "NOW"],
        ["REINDEER", "IN", "RAIN"],
        ["TOURISM", "DESTINY", "POPULAR"],
        ["OATH", "PEA", "EAT", "RAIN"],
        ["STREET", "STREETCAR", "STRING", "STING", "RING", "RACECAR"],
        ["A", "AA", "AAA", "AAAA"]
    ]

    for i in range(len(test_case_grid)):
            if i > 0:
                print()
            print(i + 1, ".\t 2D Grid:\n", sep="")
            print_grid(test_case_grid[i])
            print("\n\t Input list: ", strings_to_search[i])
            print("\n\t Output: ", find_strings(test_case_grid[i], strings_to_search[i]))
            print("-"*100)


if __name__ == '__main__':
    main()

