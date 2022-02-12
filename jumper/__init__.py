""" The game package contains specific classes for playing jumper.
"""

# Elizeu Silva
# Shawn Yang
from game.jumper import Jumper
from game.parachute import Parachute
from game.word import Word

class Director:


    """A person who directs the game
    Attributes:
        jumper (Jumper): the game's jumper
        is_guessing (boolean): whether or not to keep playing
        parachute (Parachute): Player's parachute
        jumper (Jumper): For getting and displaying information on the terminal        
    """
    def __init__(self):
        """Constructs a new Director
        Args: 
            self(Director): an instance of Director.
        """
        self._parachute = Parachute()
        self._is_guessing = True
        self._word = Word()
        self._jumper = Jumper()
        self.guessed_word = ""
        


    def start_game(self):
        """Starts the game by running the main game loop
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_guessing:
            guess = self._get_inputs()
            self._do_updates(guess)
            self._do_outputs()

    def _get_inputs(self):
        tries = 5
        self.guessed_word = self._word.new_word()
        hidden_word = self._word.hide_word()
        print(hidden_word)
        self._parachute.show_parachute(tries=tries)
        tries -= 1 
        guess_letter = input("Guess a letter [a-z]: ")
        return guess_letter

    def _do_updates(self, guess):
        chosen_word = []
        for letter in self.guessed_word:
            chosen_word.append(letter)
        for i in range(0, len(chosen_word)):
            letter = chosen_word[i]
            if guess == letter:
                chosen_word[i] = letter

            

    def _do_outputs(self):
        self._is_guessing = False

class Jumper:
    #Brenner

    #Code that Will Construct the Jumper.
    def init_jumper():
        global head,arms,legs
        head=("   O")
        arms=("  /|\ ")
        legs=("  / \ ")
        print(head)
        print(arms)
        print(legs)
    
    #Code that will first check
    def fail_check():
        lives=-1
        if  lives >=0:
            return True
        else:
            head=("   X")
            print(head)
            print(arms)
            print(legs)
            print()
            print("Game Over!")
            return False

class parachute:
    
    #Alexander
    
    pass

class word:
    lives=-1
    #Josefini
    
    pass
    
Jumper.init_jumper()
Jumper.fail_check()
