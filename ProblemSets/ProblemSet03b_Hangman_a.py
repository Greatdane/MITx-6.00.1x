#Problem Set 3 - Hangman - Is the Word Guessed

# implement the function isWordGuessed that takes in two parameters - a string, secretWord, and 
# a list of letters, lettersGuessed. This function returns a boolean - True if secretWord has been 
# guessed (ie, all the letters of secretWord are in lettersGuessed) and False otherwise.

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    ans = 0
    for guess in secretWord:
        if guess in lettersGuessed:
            ans += 1
        else:
            return False
    if ans == len(secretWord):
        return True
    else:
        return False

#tests..
isWordGuessed('apple', ['a', 'e', 'i', 'k', 'p', 'r', 's']) #False

isWordGuessed('durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u']) #True

isWordGuessed('carrot', ['i', 'o', 'l', 'z', 'q', 'g', 'r', 'v', 't', 'c']) #False

isWordGuessed('pineapple', ['l', 'm', 'a', 'e', 'w', 'x', 't', 's', 'b', 'n']) #False

isWordGuessed('lettuce', []) #False

isWordGuessed('pineapple', ['z', 'x', 'q', 'p', 'i', 'n', 'e', 'a', 'p', 'p', 'l', 'e']) #True