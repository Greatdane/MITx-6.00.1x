# Quiz, Problem 7 - Summer 2016

# Write a function called dict_interdiff that takes in two dictionaries (d1 and d2). 
# The function will return a tuple of two dictionaries: a dictionary of the intersect 
# of d1 and d2 and a dictionary of the difference of d1 and d2
#
# intersect: The keys to the intersect dictionary are keys that are common in both d1 and d2. 
# To get the values of the intersect dictionary, look at the common keys in d1 and d2 and apply the function f 
# to these keys' values -- the value of the common key in d1 is the first parameter to the function and the value of 
# the common key in d2 is the second parameter to the function. Do not implement f inside your 
# dict_interdiff code -- assume it is defined outside.
# 
# difference: a key-value pair in the difference dictionary is (a) every key-value pair in d1 whose key appears 
# only in d1 and not in d2 or (b) every key-value pair in d2 whose key appears only in d2 and not in d1.


# f in example 1..
def f(a, b):
    return a + b
    
# f in example 2..
def f2(a, b):
    return a > b

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    dictA = {} # intersect
    dictB = {} # difference
    for n in d1:
        if n in d2:
            dictA[n] = f(d1[n], d2[n]) #f and f2 for example
        else:
            dictB[n] = d1[n]
    for n in d2:
        if n in d1:
            n
        else:
            dictB[n] = d2[n]    
    return (dictA, dictB)

# Example 1    
#d1 = {1:30, 2:20, 3:30, 5:80}
#d2 = {1:40, 2:50, 3:60, 4:70, 6:90}

# Example 2
d1 = {1:30, 2:20, 3:30}
d2 = {1:40, 2:50, 3:60}

# Returns tuple, ({1: 70, 2: 70, 3: 90}, {4: 70, 5: 80, 6: 90}) - Example 1
# Returns tuple, ({1: False, 2: False, 3: False}, {}) - Example 2
print dict_interdiff(d1, d2)