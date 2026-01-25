class Player:
    def __init__(self, id, n):
        self.id = id
        self.rowCount = [0]*n
        self.columnCount = [0]*n
        self.l2RDiag = 0
        self.r2LDiag = 0
        self.n = n
    
    def addEntry(self, rowId, columnId):
        self.rowCount[rowId] += 1
        self.columnCount[columnId] += 1
        if (rowId == columnId):
            self.l2RDiag += 1
        if (rowId + columnId) == (self.n - 1):
            self.r2LDiag += 1
        if (self.l2RDiag == self.n) or (self.r2LDiag == self.n):
            return True
        if (self.rowCount[rowId] == self.n) or (self.columnCount[columnId] == self.n):
            return True
        return False
        
class TicTacToe:
    # Constructor will be used to initialize TicTacToe data members 
    def __init__(self, n): 
        self.player1 = Player(1, n)
        self.player2 = Player(2, n)

    # move will be used to play a move by a specific player and identify who
    # wins at each move
    def move(self, row, col, player):
        if (player == 1):
            if (self.player1.addEntry(row, col)):
                return 1
        else:
            if (self.player2.addEntry(row, col)):
                return 2
        return 0

# Driver code
def main():
    n = 3
    inputs = [  [[0, 1, 1], [1, 0, 2], [2, 1, 1], [1, 2, 2], [0, 2, 1], [2, 2, 2], [1, 1, 1]], 
                [[0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [1, 0, 1], [2, 0, 2], [1, 2, 1]] ]
    
    for game in range(2):
        fill_grid = []
        print("Game ",(game+1), ": \n", sep="")
        tic_tac_toe_obj = TicTacToe(n)
        win = 0
        for i in range(0, len(inputs[game])):
            print("Move ", (i+1), ":\tPlayer ", inputs[game][i][2], " places their mark at ", inputs[game][i][0], ", ", inputs[game][i][1] , sep="", end="")

            win = tic_tac_toe_obj.move(inputs[game][i][0], inputs[game][i][1], inputs[game][i][2])

            if (win == 0):
                print("\tNo one wins the game")
                print("-" * 100)
            else:
                print("\tPlayer", win, "wins the game")
                print("-" * 100)
                break


if __name__ == '__main__':
    main() 
