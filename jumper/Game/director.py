#from jumper import word
from random import randint

class Director:
    def __init__(self):
        self.state = True
        self.errors = 0
        self._words = [
            "green",
            "brown",
            "blues",
            "apple",
            "books",
            "magic",
            "house",
            "horse",
            "uncle",
            "angle"
        ]
    
    def chosenLetter(self):
        # Get random number 
        indexRandom = randint(0,9)
        # Word chosen from list based on random number
        word = self._words[indexRandom]
        return word


