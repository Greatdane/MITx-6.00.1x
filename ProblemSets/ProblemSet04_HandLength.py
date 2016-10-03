# Problem Set 4 - Hand Length

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    handLen = 0
    # Go through each value in dictionary hand, and add them together in the variable handLen
    for x in hand.values():
        handLen += x
    return handLen

# Testing
hand = {'r': 1, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u':1}    
print calculateHandlen(hand)