def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    return aTup[::2]

#test
x = ('I', 'am', 'a', 'test', 'tuple')
print oddTuples(x) 
    
    