def square(x):
    '''
    x: int or float.
    Note that square is already defined in the test case.
    '''
    sqr = x**2
    return sqr

def fourthPower(x):
    '''
    x: int or float.
    Condition was not to use ** and square(x) had to be used twice
    '''
    ans = square(x) * square(x)
    return ans
 
print(fourthPower(2)) #Simple check to see if it is 16!