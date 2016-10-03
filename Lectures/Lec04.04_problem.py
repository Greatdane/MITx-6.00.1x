def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    ans = a * x**2 + b * x + c 
    return ans
    # can just use one line return a * x**2 + b * x + c