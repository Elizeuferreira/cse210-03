from word import Word

class Jumper:
    def __init__(self):
       self._word = Word()
       self._hidden_word = self._word.random_word()
       self._guess_word = ""
    

    def compare_word(self, listWord, guess_letter):
        
        for i in range(len(self._hidden_word)):
            if guess_letter == self._hidden_word[i]:
                listWord[i] = guess_letter

    def _show_word_revelado(self, listWord):
        guessWord = "".join(listWord)
        self._guess_word = guessWord
        word = " ".join(listWord)
        print(word)
