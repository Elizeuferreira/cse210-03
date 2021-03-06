from jumper import Jumper
from parachute import Parachute
from word import Word

class Director:
    """A person who directs the game
    Attributes:
        jumper (Jumper): the game's jumper
        _playing (boolean): whether or not to keep playing
        parachute (Parachute): Player's parachute    
        _hidden_word
        _guess_word
        _guess_is_true
        tries 
    """
    def __init__(self):
        """Constructs a new Director
        Args: 
            self(Director): an instance of Director.
        """
        self._playing = True
        self._parachute = Parachute()
        self._word = Word()
        self._jumper = Jumper()
        self._hidden_word = self._word.random_word()
        self._guess_word = ""
        self._guess_is_true = None
        self.tries = 5
    
    def start_game(self):
        """Starts the game by running the main game loop
        
        Args:
            self (Director): an instance of Director.
        """
        print()
        print("="*30)
        print("   WELCOME TO THE JUMPER GAME!  ")
        print("="*30)
        print()
        print(" Find out the secret word, you have 5 tries.. Have fun.")
        print()
        print("_ _ _ _ _")   
        self._parachute.show_parachute(self.tries)
        listWord = list(len(self._hidden_word) * "_")
        hidden_word = self._hidden_word
        while self._playing:  
            print()
            guess_letter = self._get_inputs()
            self._guess_is_true = guess_letter in self._hidden_word
            if self._guess_is_true:
                print()
                word = self._jumper._compare_word(listWord, guess_letter, hidden_word)
                print(word)
                self._parachute.show_parachute(self.tries)
                if (str(word)).replace(" ","") == self._hidden_word:
                    print()
                    print("YOU WIN!!!!")
                    print()
                    self._playing = False
            else:
                self.tries -= 1
                print()
                word = self._jumper._compare_word(listWord, guess_letter, hidden_word)
                print(word)
                print()
                print("You still have",self.tries, "tries" )
                print()
                self._parachute.show_parachute(self.tries)
                if self.tries == 0:
                    print("GAME OVER!")
                    print("    _______________         ")
                    print("   /               \       ")
                    print("  /                 \      ")
                    print("//                   \/\  ")
                    print("\|   XXXX     XXXX   | /   ")
                    print(" |   XXXX     XXXX   |/     ")
                    print(" |   XXX       XXX   |      ")
                    print(" |                   |      ")
                    print(" \__      XXX      __/     ")
                    print("   |\     XXX     /|       ")
                    print("   | |           | |        ")
                    print("   | I I I I I I I |        ")
                    print("   |  I I I I I I  |        ")
                    print("   \_             _/       ")
                    print("     \_         _/         ")
                    print("       \_______/           ")
                    self._playing = False
        
    def _get_inputs(self):
        """Prompts the user to choose letter and returns it.
        """
        guess_letter = input("Guess a letter [a-z]: ")
        return guess_letter
        
