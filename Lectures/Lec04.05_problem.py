def clip(lo, x, hi):
    '''
    Takes in three numbers and returns a value based on the value of x.
    Returns:
     - lo, when x < lo
     - hi, when x > hi
     - x, otherwise
    '''
    while x < lo:
        return max(x,lo)
        break
    return min(x,hi)
    
#print(clip(4,1,5))
#print('should be 4 (lo)')
#print (clip(4,12,10))
#print('should be 10 (hi)')
#print(clip(4,6,10))
#print('should be 6 (x)')

