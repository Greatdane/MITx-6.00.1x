def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float; base^exp
    '''
    if exp == 0:
        return 1.0 #to cover for the powers of 0 - which always equal 1
    elif exp % 2 == 0:
        return recurPowerNew(base * base, exp/2) #formula for even numbers
    else:
        return base * recurPowerNew(base, exp - 1)
