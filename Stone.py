from Territory import Territory

class Stone:  
    def __init__(self,posx,posy,board,color):
        self.posx = posx
        self.posy = posy
        self.color = color
        self.board = board
        initFreedom = []
        
        if posx != 0:
            initFreedom.append(board.printBoard[posx-1][posy])
        if posx != 8:
            initFreedom.append(board.printBoard[posx+1][posy])
        if posy != 0:
            initFreedom.append(board.printBoard[posx][posy-1])
        if posy != 8:
            initFreedom.append(board.printBoard[posx][posy+1])

        while 'bl' in initFreedom: initFreedom.remove('bl')
        while 'wh' in initFreedom: initFreedom.remove('wh')
        
        if color == 'white': 
            board.printBoard[posx][posy] = 'wh'    
        else:
            board.printBoard[posx][posy] = 'bl'
        board.playBoard[posx][posy]=self
        print(initFreedom)
        # territory.getStone(self)
        # territory.checkFreedom(1,0,1,1,1,-1,False)# check beneath
        # territory.checkFreedom(-1,0,-1,-1,-1,1,False)# check above
        # territory.checkFreedom(0,1,1,1,-1,1,False)# check right 
        # territory.checkFreedom(0,-1,-1,-1,1,-1,True)# check left
        
   