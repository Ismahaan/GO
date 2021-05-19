import string
import random

class Set:
    def __init__(self,stone,freedom):
        self.stoneList = [stone]
        self.freedomList = freedom
        self.teamTag = ''.join(random.choice(string.ascii_letters) for x in range(5))
        if stone.color == 'white':
            stone.board.whiteSet.append(self)
        elif stone.color == 'black':
            stone.board.blackSet.append(self)
        