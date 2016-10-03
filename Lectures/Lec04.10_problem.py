def isVowel(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    char = char.lower() #changes char string to all lower
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char =='u': #
        return True
    else:
        return False

print(isVowel('a')) #testing
print(isVowel('b'))
print(isVowel('A'))
print(isVowel('Z'))