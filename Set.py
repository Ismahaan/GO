import string
import random
class Set:
    def __init__(self):
        self.freedom = 4
        self.teamTag = ''.join(random.choice(string.ascii_letters) for x in range(5))
        print (self.teamTag)