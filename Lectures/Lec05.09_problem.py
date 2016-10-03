def semordnilap(str1, str2):
    '''
    str1: a string
    str2: a string
    
    returns: True if str1 and str2 are semordnilap;
             False otherwise.
    '''
    #check to make sure strings are the same length
    if len(str1) != len(str2):
        return False

    #Base case, if str1 and str2 are equal, return True, else False - NOTE, this can be condensed to 'return str1 == str2'    
    if len(str1) == 1:
        if str1 == str2:
            return True
        else:
            return False

    #Recurvsive case. Keep checking to see if the first letter of str1 equals the last letter of str2            
    if str1[0] == str2[-1]:
        return semordnilap(str1[(+1):], str2[:(-1)])
    else:
        return False
        
#test        
print semordnilap("dog", "god") #true
print semordnilap("poop", "helllooo") #false
print semordnilap('desserts', 'stressed') #true