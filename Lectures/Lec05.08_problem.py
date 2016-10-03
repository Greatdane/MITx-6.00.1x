#We can use the idea of bisection search to determine if a character is in a string, so long as the string is sorted in alphabetical order.
#Implement the function isIn(char, aStr) which implements the above idea recursively to test if char is in aStr. char will be a single 
#character and aStr will be a string that is in alphabetical order. The function should return a boolean value

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''    
    aStr = aStr.lower() #changes to lower case - needed for word comparison
    
# 'c' < 'd' : True, 'x' > 'a' : True
# By char1 smaller than char2 they mean char1 comes before char2 in the alphabet.
# And all lowercase characters are 'larger' than uppercase, 'Z' < 'a' : True

    if aStr == "": # base case of a zero string, has to be false
        return False
    if len(aStr) == 1: #if string is 1, just check if this 1 charcter is the same we are looking for
        if char == aStr:
            return True
        else:
            return False

    middle = len(aStr)/2 #find the middle of the length of aStr
    newChar = aStr[middle] #use that middle as NewChar
             
    if char == newChar: #if the middle is the correct one, return True
        return True       
    elif char > newChar: #if char is greater than newChar, we know we have to use 'middle' as the 'low' in bisection search. high is the end
        return isIn(char, aStr[middle:])
    else: #if char is less than newChar, we know to use 'middle' as the 'high' for bisection search. low is the start
        return isIn(char, aStr[:middle])
    
#test        
print isIn("h", "abcdefh")
