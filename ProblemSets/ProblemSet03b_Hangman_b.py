#Problem Set 3 - Hangman - Printing Out the User's Guess

# implement the function getGuessedWord that takes in two parameters - a string, secretWord, 
# and a list of letters, lettersGuessed. This function returns a string that is comprised of letters 
# and underscores, based on what letters in lettersGuessed are in secretWord

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    ans = "" # set answer as empty string
    for guess in secretWord: # go through the secret word
        if guess in lettersGuessed: # if the letter gueeses is in the sercet word, add it to ans
            ans += guess
        else:
            ans += "_ " # otherwise add a _ to indicate a missing character
    return ans

#tests..
getGuessedWord('apple', ['e', 'i', 'k', 'p', 'r', 's']) # '_ pp_ e'

getGuessedWord('durian', ['a', 'c', 'd', 'h', 'i', 'm', 'n', 'r', 't', 'u']) # 'durian'

getGuessedWord('broccoli', ['g', 'b', 'h', 'r', 'k', 'i', 'c', 'm', 'p', 'u']) # 'br_ cc_ _ i'

getGuessedWord('pineapple', ['a', 'b', 'o', 'x', 'c', 'z', 'h', 'm', 's', 'e']) # '_ _ _ ea_ _ _ e'

getGuessedWord('pineapple', []) # '_ _ _ _ _ _ _ _ _ '

getGuessedWord('mangosteen', ['r', 'x', 'z', 'b', 'h', 's', 'f', 'm', 'n', 'k']) # 'm_ n_ _ s_ _ _ n'