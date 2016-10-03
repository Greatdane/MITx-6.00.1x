#Week 3 - Problem Set 3a - Radiation exposure

# Already defined on problem set.
def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)
 
       
def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
      between start and stop times.
    '''
    total = 0 #define a start for total
    current = start #current period starts at start.
    while current < stop: #while the current period is less than the end period;
        total += step * f(current) #total equals total plus step size multiplied by f(current)
        current += step #add the step size to current
    return total #return the answer!


# All answers need to be within 0.01 of correct answer
        
# Test case 1. Answer should be 39.10318784326239     
print radiationExposure(0, 5, 1)

# Test case 2. Answer should be 22.94241041057671
print radiationExposure(5, 11, 1)

# Test case 3. Answer shoud be 62.0455982538
print radiationExposure(0, 11, 1)

# Test case 4. Answer shoould be 0.434612356115
print radiationExposure(40, 100, 1.5)