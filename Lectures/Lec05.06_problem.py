def lenIter(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    ans = 0
    for n in aStr: #for each string in aStr, add +1 to ans
        ans += 1
    return ans
    
print lenIter("hello") #example - should return 5