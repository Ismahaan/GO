from Territory import Territory
class Stone:  
    def __init__(self,posx,posy,board,color):
        self.posx = posx
        self.posy = posy
        self.color = color
        self.freedom = 4
        territory = Territory()
        if posx == 0 or posx == 8:
            self.freedom = self.freedom -1
        if posy == 0 or posy == 8:
            self.freedom = self.freedom -1
        
        if color == 'white': 
            board.printBoard[posx][posy] = 'wh'
            
        else:
            board.printBoard[posx][posy] = 'bl'
        board.playBoard[posx][posy]=self
        print(self.freedom)
        territory.getStone(posx,posy,color,self.freedom)