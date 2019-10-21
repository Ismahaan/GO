class Move:

    def makeMove(self,color,board):
        
        move = input('\n' + color + ', insert a move\n')
        
        position = {
            'A' : 0,
            'B' : 1,
            'C' : 2,
            'D' : 3,
            'E' : 4,
            'F' : 5,
            'G' : 6,
            'H' : 7,
            'I' : 8,
        }
        iets =position[move]()
        print(iets)
    #print(board.printBoard[iets][0])
