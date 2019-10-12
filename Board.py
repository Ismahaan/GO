import numpy as np
from Stone import WhiteStone
from Stone import BlackStone
class Board:
    def __init__(self):
        self.board = np.full([9,9],'+',dtype = str)
        self.board2 =  np.full([9,9],'+',dtype = object)
       
       