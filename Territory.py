
from Set import Set 
class Territory:

    


    def getStone(self, stone):
      self.stone = stone

    def checkFreedom(self):
        bordMax = 8
        bordMin = 0
        
        #this check if theres a stone piece in front of behind him. If that's true and it is the same color
        #than those pieces will share there freedoms
        if self.stone.posx != bordMax:
            if  self.stone.board.printBoard[self.stone.posx +1][self.stone.posy] == 'bl' or self.stone.board.printBoard[self.stone.posx +1][self.stone.posy] == 'wh' :
                if  self.stone.board.playBoard[self.stone.posx +1][self.stone.posy].color == self.stone.color: 
                    self.stone.set=self.stone.board.playBoard[self.stone.posx +1][self.stone.posy].set
                    self.stone.set.freedom = self.stone.set.freedom + self.stone.freedom -2
                    if self.stone.posy != bordMax:
                        if  self.stone.board.printBoard[self.stone.posx +1][self.stone.posy+1] == 'bl' or self.stone.board.printBoard[self.stone.posx +1][self.stone.posy+1] == 'wh' :
                            if self.stone.board.playBoard[self.stone.posx +1][self.stone.posy+1].color == self.stone.color:
                                self.stone.set.freedom =self.stone.set.freedom -1
                    if self.stone.posy != bordMin:
                        if  self.stone.board.printBoard[self.stone.posx +1][self.stone.posy-1] == 'bl' or self.stone.board.printBoard[self.stone.posx +1][self.stone.posy-1] == 'wh' :
                            if self.stone.board.playBoard[self.stone.posx +1][self.stone.posy-1].color == self.stone.color:
                                self.stone.set.freedom =self.stone.set.freedom -1
                    print(self.stone.set.freedom)

        if self.stone.posx != bordMin:
            if  self.stone.board.printBoard[self.stone.posx -1][self.stone.posy] == 'bl' or self.stone.board.printBoard[self.stone.posx -1][self.stone.posy] == 'wh' :
                if  self.stone.board.playBoard[self.stone.posx -1][self.stone.posy].color == self.stone.color: 
                    self.stone.set=self.stone.board.playBoard[self.stone.posx -1][self.stone.posy].set
                    self.stone.set.freedom = self.stone.set.freedom + self.stone.freedom -2
                    if self.stone.posy != bordMax:
                        if  self.stone.board.printBoard[self.stone.posx -1][self.stone.posy+1] == 'bl' or self.stone.board.printBoard[self.stone.posx -1][self.stone.posy+1] == 'wh' :
                            if self.stone.board.playBoard[self.stone.posx -1][self.stone.posy+1].color == self.stone.color:
                                self.stone.set.freedom =self.stone.set.freedom -1
                    if self.stone.posy != bordMin:
                        if  self.stone.board.printBoard[self.stone.posx -1][self.stone.posy-1] == 'bl' or self.stone.board.printBoard[self.stone.posx -1][self.stone.posy-1] == 'wh' :
                            if self.stone.board.playBoard[self.stone.posx -1][self.stone.posy-1].color == self.stone.color:
                                self.stone.set.freedom =self.stone.set.freedom -1
                    print(self.stone.set.freedom)
                else:
                    self.stone.set = Set()
            else:
                self.stone.set = Set()    
        else:
            self.stone.set = Set()

        
      
        
                
        print(self.stone.set.teamTag)
    # def Suicide():