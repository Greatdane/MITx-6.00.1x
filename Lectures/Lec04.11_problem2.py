def isVowel2(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    char = char.lower() #move to lower case
    return char in ('aiueo') #return True if the variable char is in the string aiueo
    
print(isVowel2('a')) #testing
print(isVowel2('b'))
print(isVowel2('A'))
print(isVowel2('Z'))
