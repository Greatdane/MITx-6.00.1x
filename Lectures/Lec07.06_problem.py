#L7 Problem 6

# Original Code
def integerDivisionOrg(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the integer division of x divided by a.
    """
    while x >= a:
        count += 1
        x = x - a
    return count
    
# Debugged code
def integerDivision(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the integer division of x divided by a.
    """
    count = 0 #count was not defined before it was called upon. Now an int of zero.
    while x >= a:
        count += 1
        x = x - a
    return count

print integerDivision(5, 3)