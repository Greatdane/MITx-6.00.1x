# Problem Set 4 - Dealing with Hands - update hand

def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # Make a copy of the dictionary hand.
    newHand = hand.copy()
    # For each letter in the string word, take it out of the dictionary newHand
    for x in word:
        newHand[x] = newHand.get(x, 0) -1
    return newHand

# Testing        
hand = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
print updateHand(hand, 'hello')