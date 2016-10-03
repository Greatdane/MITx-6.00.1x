# Quiz, Problem 4 - Summer 2016

# Write a Python function that returns True if aString is a palindrome (reads the same forwards or reversed) 
# and False otherwise. Do not use Python's built-in reverse function or aString[::-1] to reverse strings.


#This function takes in a string and returns a boolean.
def isPalindrome(aString):
    '''
    aString: a string
    '''
    def equals(x, y):
        return x == y

    #aString = aString.lower() # Grader did not want us to change to lower letters
    if len(aString) <= 1:
        return True
    # Set a start and end point for x and y
    start = 0
    end = len(aString) - 1
    # While start is less than the length of the string..
    while start < (len(aString) - 1):
        x = aString[start]
        y = aString[end]
        if equals(x, y) == True:
            start += 1
            end -= 1
        else:
            return False
    return True
        
print isPalindrome("chC")