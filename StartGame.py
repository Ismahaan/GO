from Player import Player

class StartGame:
    def __init__(self, board):
        self.board = board

        while True:
            color = input("choose your color\n")
            if color == 'white' or color == 'black':
                break
            else:
                print("\nyou can only choose between black or white")
        player1 = Player(color, board)
        if color == 'black':
            player2 = Player('white', board)
            player1.makeMove()

        else:
            player2 = Player('black', board)
            player2.makeMove()