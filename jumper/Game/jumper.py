from word import Word

class Jumper():
    def __init__(self):
        self._word = Word()
        self._hidden_word = self._word.random_word()  
        self._guess_word = ""

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

   
