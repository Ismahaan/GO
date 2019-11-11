
from Set import Set 
class Territory:

    


    def getStone(self, stone):
      self.stone = stone

    def checkFreedom(self,x1,y1,x2,y2,x3,y3,name):
        bordMax = 8
        bordMin = 0
        
        #this check if theres a stone piece in front of behind him. If that's true and it is the same color
        #than those pieces will share there freedoms
        if self.stone.posx != bordMax:
            if  self.stone.board.printBoard[self.stone.posx +x1][self.stone.posy+y1] == 'bl' or self.stone.board.printBoard[self.stone.posx +x1][self.stone.posy+y1] == 'wh' :
                if  self.stone.board.playBoard[self.stone.posx +x1][self.stone.posy+y1].color == self.stone.color: 
                    self.stone.set=self.stone.board.playBoard[self.stone.posx +x1][self.stone.posy+y1].set
                    # print(self.stone.set.freedom)
                    self.stone.set.freedom = self.stone.set.freedom + self.stone.freedom -2
                    if self.stone.posy != bordMax:
                        if  self.stone.board.printBoard[self.stone.posx +x2][self.stone.posy+y2] == 'bl' or self.stone.board.printBoard[self.stone.posx +x2][self.stone.posy+y2] == 'wh' :
                            if self.stone.board.playBoard[self.stone.posx +x2][self.stone.posy+y2].color == self.stone.color:
                                self.stone.set.freedom =self.stone.set.freedom -1
                    if self.stone.posy != bordMin:
                        if  self.stone.board.printBoard[self.stone.posx +x3][self.stone.posy+y3] == 'bl' or self.stone.board.printBoard[self.stone.posx +x3][self.stone.posy+y3] == 'wh' :
                            if self.stone.board.playBoard[self.stone.posx +x3][self.stone.posy+y3].color == self.stone.color:
                                self.stone.set.freedom =self.stone.set.freedom -1
                   
                elif name:
                    self.stone.set = Set(self.stone.freedom)
            elif name:
                self.stone.set = Set(self.stone.freedom)    
        elif name:
            self.stone.set = Set(self.stone.freedom)        
        if name:         
            print(self.stone.set.teamTag)
            print(self.stone.set.freedom)
