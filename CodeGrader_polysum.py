#Code Grader: polysum

def polysum(n, s):
    import math #imports maths module - standard in Python
    area = (0.25 * n * s**2)/(math.tan(math.pi/n)) #tan and pi imported from math.py
    perimeter = n * s
    return round(float(area + (perimeter ** 2)), 4) #round(number, number of decimal places) - 4 in this case
    
print(polysum(60, 56)) #test - answer should be 12187176.6698