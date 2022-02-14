import random

class Word:

    def __init__(self):
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
            "angle",
            "house"
        ]
    
    def random_word(self):
        randomWord = random.choice(self._words)
        return randomWord

    
