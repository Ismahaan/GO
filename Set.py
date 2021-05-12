import string
import random
class Set:
    def __init__(self,stone):
        self.freedom = stone
        self.teamTag = ''.join(random.choice(string.ascii_letters) for x in range(5))
        print (self.teamTag)

        # Een lijst van stenen wordt aangemaakt
        # Nieuwe stenen worden aan lijst toegevoegd
        # Een lijst van vrijheden wordt aangemaakt