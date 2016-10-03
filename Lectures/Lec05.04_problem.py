def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    
    div is the divisor. Set to the lowest input first, and decreasing by one each time
    '''
    if a > b:
        div = b
    else: div = a #can also use div = min(a, b) instead of if/else         
    while a % div != 0 or b % div != 0 : #have to use or not and, because the correct answer the both equal 0, so the equation would be wrong with and (and do not, and do not)
            div -= 1
    return div
            
print gcdIter(17, 12) 
