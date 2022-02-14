import random

class Word:
    """
    The instrument to create random word
    """
    def __init__(self):
        """
        Constructs a list of words.
        
        Args:
        self (Word): An instance of Word
        """
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
        """
        Choose and return random word.
        
        Args:
        self: an instance of Word
        """
        randomWord = random.choice(self._words)
        return randomWord

