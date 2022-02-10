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
        indexRandom = randint(0,9)
        word = self._words[indexRandom]
        return word
