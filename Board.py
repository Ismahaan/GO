import numpy as np
from Player import Player
class Board:
    #for creating a 9 by 9 board with official positions
    def __init__(self):
        self.printBoard = np.full([9,9],'++',dtype = object)        #board for commandline
        
        charString = 'ABCDEFGHI'
        numString = '123456789'
        
        for i in range (9) :
            cs = charString[i]
            for m in range (9):
                ns = numString[m]
                self.printBoard[i][m] = cs + ns
        #print(self.printBoard)
            
        self.playBoard =  np.full([9,9],'0',dtype = object)    #board for actual game
    
    def startGame(self,board):
        while True:
            color = input("choose your color\n").lower()
            if color == 'white' or color == 'black':
                break
            else:
                print("\nyou can only choose between black or white")
        player1 = Player(color, self)
        if color == 'black':
            player2 = Player('white', board)
            player1.askMove(player2)

        else:
            player2 = Player('black', board)
            player2.askMove(player1)
    
   