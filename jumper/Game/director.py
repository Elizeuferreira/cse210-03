from parachute import Parachute
from word import Word
from jumper import Jumper # *Brenner will still write the code for this class


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
        self._hidden_word = self._word.random_word()
        self._guess_word = ""
        self._guess_is_true = None
        self.tries = 5
      

    

    def start_game(self):
        """Starts the game by running the main game loop
        
        Args:
            self (Director): an instance of Director.
        """
        self._parachute._show_parachute(self.tries)
        listWord = list(len(self._hidden_word) * "_")
        while self._playing:            
            guess_letter = self._get_inputs()
            self._guess_is_true = guess_letter in self._hidden_word
            if self._guess_is_true:
                self._compare_word(listWord, guess_letter)
                self._show_word_revelado(listWord)
                self._parachute.show_parachute(self.tries)
                if self._guess_word == self._hidden_word:
                    print("YOU WIN!!!!")
                    self._playing = False
            else:
                self.tries -= 1
                print("You still have",self.tries, "tries" )
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


    def _compare_word(self, listWord, guess_letter):
        """
        Compares letters in hiden word with a letter that the user guessed and 
        make updates to the word to show
        """
        
        for i in range(len(self._hidden_word)):
            if guess_letter == self._hidden_word[i]:
                listWord[i] = guess_letter

    def _show_word_revelado(self, listWord):
        """
        Makes updates to display the correct word and displays it
        """
        guessWord = "".join(listWord)
        self._guess_word = guessWord
        word = " ".join(listWord)
        print(word)
        
    def _get_inputs(self):
        """Prompts the user to choose letter and returns it.
        """
        guess_letter = input("Guess a letter [a-z]: ")
        return guess_letter


                    
