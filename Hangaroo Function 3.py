#FUNCTION 3: return lowercase letters that have'nt been guessed yet
def getAvailableLetters(lettersGuessed):
    string = "abcdefghijklmnopqrstuvwxyz"
    temp = ""
    for i in string:
        if i not in lettersGuessed:
            temp += i
    return temp