x = 3
y = 2
def f(x):
    y = 1
    x = x + y
    print ('x = ' + str(x))
    return x
z = f(x)
print("z = " + str(z))
print("x = " + str(x))
print("y = " + str(y))

