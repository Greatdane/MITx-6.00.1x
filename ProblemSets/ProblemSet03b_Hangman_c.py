#Problem Set 3 - Hangman - Printing Out all Available Letters

# implement the function getAvailableLetters that takes in one parameter - a list of letters, lettersGuessed. 
# This function returns a string that is comprised of lowercase English letters - all lowercase English 
# letters that are not in lettersGuessed.

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string 
    ans = "" #ans is empty string
    for guess in string.ascii_lowercase: # string.ascii_lowercase is a string comprised of all lowercase letters - could just use alphabet
        if guess in lettersGuessed:
            ans = ans #not sure how to give no input, so just said ans = ans and moving on... 
        else:
            ans += guess #if letter is not lettersGuessed, add is to ans
    return ans
            

#tests..
print getAvailableLetters(['e', 'i', 'k', 'p', 'r', 's']) # 'abcdfghjlmnoqtuvwxyz'

getAvailableLetters([]) # 'abcdefghijklmnopqrstuvwxyz'

getAvailableLetters(['d', 'q', 'f']) # 'abceghijklmnoprstuvwxyz'

getAvailableLetters(['e', 'z', 'f']) # 'abcdghijklmnopqrstuvwxy'

getAvailableLetters(['v', 'f', 'p', 'n', 'c', 'o', 's', 'h']) # 'abdegijklmqrtuwxyz'

getAvailableLetters(['e', 'j', 'q', 'g', 'a', 'p', 'b', 'y', 'd']) # 'cfhiklmnorstuvwxz'