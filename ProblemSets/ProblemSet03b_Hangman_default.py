# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

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
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")
    print ("------------")   
    print("You have 8 guesses left.")
    print("Available letters: abcdefghijklmnopqrstuvwxyz") 
    #answer = ""
    lettersGuessed = [] #or string?
    mistakesMade = 0
    availableLetters = ""
    while isWordGuessed(secretWord, lettersGuessed) == False:
        currentLetter = raw_input("Please guess a letter: ")
        currentLetter = currentLetter.lower()
        currentLetter = currentLetter[0:1]
        if currentLetter in lettersGuessed:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
            print("------------")
            print("You have " + str(8 - mistakesMade) + " guesses left.")
            print("Available letters: " + getAvailableLetters(lettersGuessed))
        else:
            lettersGuessed += currentLetter
            if currentLetter in secretWord:
                print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
                print("------------")
                if isWordGuessed(secretWord, lettersGuessed) == True:
                    print("Congratulations, you won!")
                    break
                print("You have " + str(8 - mistakesMade) + " guesses left.")
                print("Available letters: " + getAvailableLetters(lettersGuessed))        
            else:
                print("Oops! That letter is not in my word:" + getGuessedWord(secretWord, lettersGuessed))
                print("------------")
                mistakesMade += 1 #need to add plus one to this each time
                if mistakesMade == 8:
                    print("Sorry, you ran out of guesses. The word was " + secretWord + ".")
                    break
                print("You have " + str(8 - mistakesMade) + " guesses left.")
                print("Available letters: " + getAvailableLetters(lettersGuessed))
        

secretWord = chooseWord(wordlist)
hangman("sea")





# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
