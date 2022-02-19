class Jumper():
​
    def __init__(self):
        self._guess_word = ""
        
​
    def _compare_word(self, listWord, guess_letter, hidden_word):
        """
        Compares letters in hiden word with a letter that the user guessed and 
        make updates to the word to show
        """
        
        for i in range(len(hidden_word)):
            if guess_letter == hidden_word[i]:
                listWord[i] = guess_letter
​
        guessWord = "".join(listWord)
        self._guess_word = guessWord
        word = " ".join(listWord)
        return(word)
