from Game.director import Director
from parachute import showParachute

di = Director()
word = di.chosenLetter()
print("_ _ _ _ _")
showParachute("0")
print("^^^^^^^")
while di.state:
    
    letterGuess = input("Guess a letter [a-z]: ")
    listWord = list()
    for letter in word:
        if letterGuess == letter:
            listWord.append(letterGuess)
        else:
            listWord.append("_")
    wordRevelado = ' '.join(listWord)
    print(wordRevelado)
    if wordRevelado == word:
        print("YOU WIN!")
        di.state = False
    if letterGuess in wordRevelado:
        showParachute("0")
        print("^^^^^^^")
    else:
        di.errors += 1 
        showParachute(str(di.errors))
        if di.errors == 4:
            print("GAME OVER, YOU DIED!")
            di.state = False