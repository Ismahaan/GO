from Stone import Stone
class Move:
    
    def makeMove(self,color,board):
        character = 'ABCDEFGHI'
        number = '123456789'
        while True:
            print(board.printBoard)
            move = input('\n' + color + ', insert a move\n').upper()
            
            if any(move.startswith(x) for x in character) and len(move) == 2:
                if any(move.endswith(y) for y in number):
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
                    if  board.printBoard[posx][posy] != 'wh'and  board.printBoard[posx][posy] != 'bl':
                    
                        Stone(posx,posy,board,color)
                            
                        break
                    print('invalid move')
                else:
                    print('invalid position')
            else:
                print('invalid position')
    
