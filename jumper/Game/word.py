import random
#Elizeu
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
            "angle"
        ]
        self._random_word = ''
        
    def new_word(self):
        self._word = random.choice(self._words)
        return self._word    
        

    def hide_word(self):
        letters = []
        letters = ', '.join(letters)
        letters = ''.join(str(letters).split(','))
        return letters
  
