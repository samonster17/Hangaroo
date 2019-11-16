#FUNCTION 1: return true or false
def isWordGuessed(secretWord, lettersGuessed):

    for i in secretWord:
        if i not in lettersGuessed:
            return False
    return True

#FUNCTION 2: set underscores
def getGuessedWord(secretWord, lettersGuessed):
    string = ""
    for i in secretWord:
        if i in lettersGuessed:
            string += i
        else:
            string += " _ "
    return string

#FUNCTION 3: return lowercase letters that have'nt been guessed yet
def getAvailableLetters(lettersGuessed):
    string = "abcdefghijklmnopqrstuvwxyz"
    temp = ""
    for i in string:
        if i not in lettersGuessed:
            temp += i
    return temp

#FUNCTION 4: hangaroo 
def Hangaroo(secretWord):
    print ("H A N G A R O O ")
    print ("THE WORD IS " + str(len(secretWord)) + " LETTERS LONG.")
    lettersGuessed = ''
    guessesLeft = 26
    print ("------------")
    while True:
        print ("YOU HAVE  " + str(guessesLeft) + " GUESSES LEFT.")
        print ("AVAILABLE LETTERS: " + getAvailableLetters(lettersGuessed))
        guess = input("GUESS A LETTER: ")
        if guess in secretWord and guess not in lettersGuessed:
            lettersGuessed += guess
            print ("GOOD GUESS: " + getGuessedWord(secretWord, lettersGuessed))
        elif guess in lettersGuessed:
            print ("THAT LETTER HAS ALREADY BEEN USED/ GUESSED" + getGuessedWord(secretWord, lettersGuessed))
        else:
            lettersGuessed += guess
            print ("OOPS! THAT LETTER IS NOT INCLUDED IN THE WORD " + getGuessedWord(secretWord, lettersGuessed))
            guessesLeft -= 1
        print ("------------")
        if guessesLeft <= 0:
            print ("OOPS! YOU EXEEDED THE NUMBER OF GUESSES. THE WORD IS: " + secretWord + ".")
            break
        if isWordGuessed(secretWord, lettersGuessed):
            print ("CONGRATULATIONS! YOU GUESSED THE WORD!")
            break