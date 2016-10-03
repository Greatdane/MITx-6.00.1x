# Quiz, Problem 6 - Summer 2016

# Write a function to flatten a list. The list contains other lists, strings, or ints. 
# For example, [[1,'a',['cat'],2],[[[3]],'dog'],4,5] is flattened into [1,'a','cat',2,3,'dog',4,5]

def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    currentList = []
    for n in aList:
        if type(n) == list:
            currentList += flatten(n)
        else:
            currentList.append(n)
    return currentList
        
        
#Testing..        
print flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5])