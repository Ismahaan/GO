from Board import Board
from Player import Player
class Program:
    board = Board()
    

    while True:
        color = input("choose your color\n")
        if color == 'white' or color == 'black':
            
            break
        else:
            print("you only can choose between black or white")
    player1 = Player(1,color)
    if color == 'black':
        player2 = Player(2,'white')
        print(player2.color)
    else:
        player2 = Player(2,'black')
        print(player2.color)
    print(board.board)