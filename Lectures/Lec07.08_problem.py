#L7 Problem 8

# Original Code
def fOrg(n):
   """
   n: integer, n >= 0.
   """
   if n == 0:
      return n
   else:
      return n * fOrg(n-1)
      
# Debugged Code
def f(n):
   """
   n: integer, n >= 0.
   """
   if n == 0:
      return 1 # This function is a factorial.  3 is 6, because 3 x 2 x 1 (3 x 2 is 6, 6 x 1 is 6)
               # See https://en.wikipedia.org/wiki/Factorial
   else:
      return n * f(n-1)
      
print f(3) # we expect the result 6, but we get 0.

print f(1) # we expect the result 1, but we get 0.

print f(0) # we expect the result 1, but we get 0.