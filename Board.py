import numpy as np

class Board:
    def __init__(self):
        self.playBoard =  np.full([9,9],None,dtype = object)     #board for actual game
        self.printBoard = np.full([9,9],'+',dtype = str)    #board for commandline
