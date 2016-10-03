# Problem Set 4 - Valid Words

wordList = ['hello', 'bob', 'rapture']

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # Create a copy of the dictionary hand
    handCopy = hand.copy()
    if word in wordList: # First checks to see if word is in wordlist, returns False if not
        for x in word: # Run through each letter in the string word.
            if x in handCopy: # If the letter is in the dictionary handCopy, first check it doest not equal 0
                if handCopy[x] == 0:
                    return False # Return False if the letter equals 0 - its already been used.
                handCopy[x] = handCopy.get(x, 0) -1 # Minus the letter to make sure it can't  be falsely used again.
            else:
                return False
        return True # If the word is in handCopy, and in wordList, its True!
    else:
        return False # Not in the wordlist.


hand = {'r': 1, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u':1}
word = "rapture"        
print isValidWord(word, hand, wordList)