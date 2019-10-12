from abc import ABCMeta, abstractmethod
class Stone(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self,color,pos_x,pos_y):
        self.color = color 
        self.pos_x = pos_x
        self.pos_y = pos_y


class WhiteStone(Stone):
    def __init__(self,color,pos_x,pos_y,board,board2):
        Stone.__init__(self,color,pos_x,pos_y)
        color = 'w'
        board[pos_x][pos_y]= self.color
        board2[pos_x][pos_y]= self

class BlackStone(Stone):
    def __init__(self,color,pos_x,pos_y,board,board2):
        Stone.__init__(self,color,pos_x,pos_y)
        board[pos_x][pos_y]= self.color
        board2[pos_x][pos_y]= self