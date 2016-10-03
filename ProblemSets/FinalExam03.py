# Final Exam - Problem 3

# Write a function called dict_invert that takes in a dictionary with immutable values and 
# returns the inverse of the dictionary. The inverse of a dictionary d is another dictionary 
# whose keys are the unique dictionary values in d. The value for a key in the inverse dictionary 
# is a sorted list of all keys in d that have the same value in d.

def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    inverse = {} # Dictionary to return
    count = [] # An emtpy list, used to count whether a key has been used before or not
    for x in d.items():    
        if x[1] in count: # if a key has already been used
            current_list = inverse[x[1]] # we take a new list called current_list and make it the current value associated with the key
            current_list.append(x[0]) # we then add the value for this for loop to the key
            current_list.sort() # we then sort the values, as requested
            inverse[x[1]] = current_list #we set the value to the key
        else: # if a key has not yet been used, we add it, and its value, and append count.
            inverse[x[1]] = [x[0]]
            count.append(x[1])    
    return inverse
    
# Testing Examples;
# Example 1 - Should return {10: [1], 20: [2], 30: [3]}
d = {1:10, 2:20, 3:30}
print dict_invert(d)

# Example 2 - Should return {10: [1], 20: [2], 30: [3, 4]}
d = {1:10, 2:20, 3:30, 4:30}
print dict_invert(d)

# Example 3 - Should return {True: [0, 2, 4]}
d = {4:True, 2:True, 0:True}
print dict_invert(d)