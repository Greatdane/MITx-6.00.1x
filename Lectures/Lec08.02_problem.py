#L8 Problem 2

# Part 1
def FancyDivide(numbers,index):
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError, e:
        print "-1"
    else:
        print "1"
    finally:
        print "0"

#print FancyDivide([0, 2, 4], 1)

#print FancyDivide([0, 2, 4], 4)

#print FancyDivide([0, 2, 4], 0)