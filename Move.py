from Stone import Stone
class Move:
    
    def makeMove(self,color,board):
        print(board.printBoard)
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
        posx = position.get(move[0])
        posy = int(move[1]) - 1
        Stone(posx,posy,board,color)
        
    #print(board.printBoard[iets][0])
