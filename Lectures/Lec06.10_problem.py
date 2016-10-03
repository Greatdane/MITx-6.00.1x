#L6 Problem 10

# First, write a procedure, called howMany, which returns the sum of the number 
# of values associated with a dictionary. For example:

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    numValue = 0 #set the initial number of values to zero.
    for n in aDict:
        numValue += len(aDict[n]) #takes the length of n, which goes through each dictionary key and gives the number of values in each key
    return numValue
    
#test            
print howMany(animals)


#Can also use
def howMany2(aDict):
    result = 0
    for value in aDict.values():
        # Since all the values of aDict are lists, aDict.values() will 
        #  be a list of lists
        result += len(value)
    return result