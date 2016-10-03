#L6 Problem 7

# For each of the following questions (which you may assume is evaluated independently of the previous questions, so that 
# testList has the value indicated above), provide an expression using applyToEach, so that after evaluation testList has 
# the indicated value. You may need to write a simple procedure in each question to help with this process.

def applyToEach(L, f):
   for i in range(len(L)):
       L[i] = f(L[i])

#test list
testList = [1, -4, 8, -9]

#Example - testList should print [5, -20, 40, -45]
def timesFive(a):
    return a * 5

applyToEach(testList, timesFive)

#Problem 7a - testList should print [1, 4, 8, 9]

applyToEach(testList, abs)

#Problem 7b - testList should print [2, -3, 9, -8]

def plus(a):
    return a + 1
 
applyToEach(testList, plus)

#Problem 7c - testList should print [1, 16, 64, 81]

def square(a):
    return abs(a * a)

applyToEach(testList, square)



