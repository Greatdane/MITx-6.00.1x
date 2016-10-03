# Final Exam - Problem 4, Part 1

# Write a function called getSublists, which takes as parameters a list of integers named L and an integer named n.
#
# assume L is not empty
# assume 0 < n <= len(L)
# This function returns a list of all possible sublists in L of length n without skipping elements in L. The sublists 
# in the returned list should be ordered in the way they appear in L, with those sublists starting from a smaller index 
# being at the front of the list.

def getSublists(L, n):
    '''
    Assumes L is not empty, and 0 < n <= len(L)
    Returns a list of all possible sublists in L of length n without skipping elements in L
    '''
    end_list = []    
    while n != (len(L) + 1) :        
        current_list = []
        for x in L[0:n]:
            current_list.append(x)
        L.remove(L[0])    
        end_list.append(current_list)         
    return end_list
    
# Example 1, Should return the list [[10, 4, 6, 8], [4, 6, 8, 3], [6, 8, 3, 4], [8, 3, 4, 5], [3, 4, 5, 7], [4, 5, 7, 7], [5, 7, 7, 2]]
L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2]
n = 4
print getSublists(L, n)

# Example 2, Should return the list [[1, 1], [1, 1], [1, 1], [1, 4]]
L = [1, 1, 1, 1, 4]
n = 2 
print getSublists(L, n)
