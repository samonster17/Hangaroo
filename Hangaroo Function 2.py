#FUNCTION 2: set underscores
def getGuessedWord(secretWord, lettersGuessed):
    string = ""
    for i in secretWord:
        if i in lettersGuessed:
            string += i
        else:
            string += " _ "
    return string