#Week 4 Code Grader: Python Loves Fruits

def nfruits(fruits, eaten):
    '''
    eaten = A string pattern of the fruits eaten by Python on his journey as observed by Cobra.
    fruits = A non-empty dictionary containing type of fruit and its quantity initially with Python when he leaves home  
    '''
    # Take off the last value of eaten, as this is only ate at the campus
    eatenWalk = eaten[0:(len(eaten)-1)]
    for x in eatenWalk:
        for y in fruits:
            # Add plus 1 to all values in fruits
            fruits[y] += 1
        # Minus 2 to the value of the fruit in eatenWalk, to counteract the plus 1 added
        fruits[x] -= 2
    # Minus 1 from the last fruit eaten at the campus
    fruits[eaten[(len(eaten)-1):len(eaten)]] -= 1
    # Return the maxium of fruit values
    return max(fruits.values())
    
# Code Grader example                   
fruits = {'A': 1, 'B': 2, 'C': 3}
eaten = 'AC'

print nfruits(fruits, eaten)
