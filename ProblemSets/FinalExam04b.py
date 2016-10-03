# Final Exam - Problem 4, Part 2

# Write a function called longestRun, which takes as a parameter a list of integers named L (assume L is not empty). 
# This function returns the length of the longest run of monotonically increasing numbers occurring in L. A run of 
# monotonically increasing numbers means that a number at position k+1 in the sequence is either greater than or equal 
# to the number at position k in the sequence.

def longestRun(L):
    '''
    Assumes L is not empty
    Returns the length of the longest run of monotonically increasing numbers occurring in L
    
    '''
    total = 0 # running total
    longest = 0 # longest length 
    last_num = L[0]
    for x in L:
        if x >= last_num: # if x is greater than the last number, add 1 to the total
            total += 1
        else: 
            if longest > total: # check to see of the current total is smaller than longest, if so pass
                pass
            else: 
                longest = total # otherwise, current total is the longest run to date, equals longest
            total = 1 # result total back to 1. 
        last_num = x # last number defined at the end of the loop to give us last number used in list.
        
    # additonal check at the end to make sure total is not a larger number than longest
    if total > longest:
        longest = total    
    return longest
    
# Example - Should return the value 5 because the longest run of monotonically increasing integers in L is [3, 4, 5, 7, 7]
L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2]
print longestRun(L)

L = [4, 4, 4, 4, 11, 17, 999, 3, 4, 6, 13, -1, -4 , -7 ]
print longestRun(L)