
class Stone:  
    def __init__(self,posx,posy,board,color):
        self.posx = posx
        self.posy = posy
        self.color = color
        if color == 'white': 
            board.printBoard[posx][posy] = 'wh'
        else:
            board.printBoard[posx][posy] = 'bl'