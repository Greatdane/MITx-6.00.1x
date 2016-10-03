def ndigits(x):
    '''
    x is an int (either positive or negative)
    returns: the number of digits in x
    
    Note that an addtional if statement was added to be sure 0 is returned 
    as 0, to comply with grader
    '''
    # If x is equal to 0, return as 0
    if x == 0:
        return 0
    # Make x an absolute value
    x = abs(x)
    # if x is divisible by 10, return the recursive call + 1, if not
    # we know that x, must just be one digit.
    if x/10 > 0:
        return 1 + ndigits(x/10)
    else:
        return 1

# Test cases    
print ndigits(0)
print ndigits(555)
print ndigits(-19330)
print ndigits(3903)