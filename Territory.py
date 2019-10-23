
class Territory:

    


    def getStone(self,posx,posy,color,freedom,board):
       self.posx = posx
       self.posy = posy
       self.color = color
       self.freedom = freedom
       self.board = board

    def checkFreedom(self):
        if  self.board.printBoard[self.posx +1][self.posy] == 'bl' or self.board.printBoard[self.posx +1][self.posy] == 'wh' :
            if  self.board.playBoard[self.posx +1][self.posy].color == self.color: 
                freedom = self.freedom + self.board.playBoard[self.posx +1][self.posy].freedom -2
                self.board.playBoard[self.posx +1][self.posy].freedom = freedom
        
        if  self.board.printBoard[self.posx -1][self.posy] == 'bl' or self.board.printBoard[self.posx +1][self.posy] == 'wh' :
            if  self.board.playBoard[self.posx -1][self.posy].color == self.color: 
                freedom = self.freedom + self.board.playBoard[self.posx -1][self.posy].freedom -2
                self.board.playBoard[self.posx -1][self.posy].freedom = freedom
                

    # def Suicide():