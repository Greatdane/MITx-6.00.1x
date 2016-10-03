# Quiz, Problem 8 - Summer 2016

# Testing.. 
def f(s):
    return 'a' in s

def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    for x in reversed(L): # Reverse L, otherwise it skips indexes when it deletes!
        if f(x) == True:
            x #mute value..
        else:
            L.remove(x)  # Remove from the list if f function is False.  
    return len(L)

#run_satisfiesF(L, satisfiesF) # Call in test.

# Testing
#L = ['a', 'b', 'a']
# Should print..
# 2
# ['a', 'a']

L = ['z', 'b', 'a', 'a', 'a', 'l', 'm']
print satisfiesF(L)
print L




