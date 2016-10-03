#L6 Problem 11

# This time, write a procedure, called biggest, which returns the key corresponding to 
# the entry with the largest number of values associated with it. If there is more than 
# one such entry, return any one of the matching keys.

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    biggestValue = 0 #intitally set the biggest value to zero
    ans = None #answer starts at None (not zero as grader had this wrong, and answer is not an int!)
    for n in aDict.keys():
        if len(aDict[n]) >= biggestValue: #if the lngth of key n is greater than the current biggest value, change the biggest to this and make the answer n
            biggestValue = len(aDict[n])
            ans = n            
    return ans
        
#test
print biggest(animals)