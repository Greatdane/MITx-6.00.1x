def isVowel2(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    char = char.lower() #move to lower case
    if char in ('aiueo'):
        return True
    else:
        return False
    
print(isVowel2('a')) #testing
print(isVowel2('b'))
print(isVowel2('A'))
print(isVowel2('Z'))