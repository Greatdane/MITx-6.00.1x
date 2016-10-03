def isVowel(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    char = char.lower() 
    return char=='a' or char=='e' or char=='i' or char=='o' or char=='u' or char=='y'
    
print(isVowel('a')) #testing
print(isVowel('b'))
print(isVowel('A'))
print(isVowel('Z'))