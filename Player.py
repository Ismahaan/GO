class Player:
    def __init__(self, color, board):
        self.color = color
        self.board = board

    def makeMove(self):
        print(self.board.printBoard)
        move = input('\n' + self.color + ', insert a move\n')