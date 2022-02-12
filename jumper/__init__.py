""" The game package contains specific classes for playing jumper.
"""
from jumper import word
from random import randint

class Director:
    
    #Elizeu Silva
    #Shawn yang
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
    

class Jumper:
    
    #Brenner
    #Mahonrri Mendez
    
    pass

class parachute:
    
    #Alexander
    
    pass

class word:
    
    #Josefini
    
    pass
    