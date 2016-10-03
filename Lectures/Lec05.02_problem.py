def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1.0 #to cover for the powers of 0 - which always equal 1
    elif exp == 1:
        return base #return just the base number, as it is * 1
    return base * recurPower(base, exp-1)