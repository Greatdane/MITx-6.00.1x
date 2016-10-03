def odd(x):
    '''
    x: int or float.

    returns: True if x is odd, False otherwise
    Cannot use if, have to use % (mod function) for the problem
    '''
    while x % 2 == 0:
        return False
        break
    return True
#    return bool(x%2) #better - one line

print(odd(3)) #check to be True
print(odd(4)) #check to be False