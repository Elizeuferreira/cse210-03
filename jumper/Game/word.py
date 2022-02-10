import random
from random import randint

class Guesser:
    def __init__(self):
        self.state = True
        self.errors = 0
        self.words = [
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
        self.letter0 = '_'
        self.letter1 = "_"
        self.letter2 = "_"
        self.letter3 = "_"
        self.letter4 = "_"
        self.letters = [self.letter0,self.letter1,self.letter2,self.letter3,self.letter4]

    def random_word(self):
        indexRandom = randint(0,9)
        word = self.words[indexRandom]
        return word

    def get_letters(self, random_word, chosen_letter):
        letters = list(random_word)
        for letter in letters:
            index = letters.index(letter)
            if chosen_letter == letter:
                letter = chosen_letter
            else:
                letters[index] = "_"
        return letters
        #print(letters[0], letters[1], letters[2], letters[3], letters[4])

        #print(self.letter0,self.letter1,self.letter2,self.letter3,self.letter4)

    def display_prompt(self, prompt):
        chosen_letter = str(input(prompt))
        return chosen_letter

    
            

guesser = Guesser()
random_word = guesser.random_word()
#chosen_letter = guesser.display_prompt("Choose a letter: ")
letters_final = ["_","_","_","_","_"]
while letters_final[0] == "_" or letters_final[1] == "_" or letters_final[2] == "_" or letters_final[3] == "_" or letters_final[4] == "_":
    chosen_letter = guesser.display_prompt("\nChoose a letter: ")
    letters = guesser.get_letters(random_word, chosen_letter)
    for letter in letters:
        if letter in letters != "_":
            index = letters.index(letter)
            letters_final[index] = letter
    print(letters_final[0], letters_final[1], letters_final[2], letters_final[3], letters_final[4])
#def start_game(self):
#        while self.letter0 != "-":
