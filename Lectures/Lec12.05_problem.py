# L12 Problem 5
# Write a generator, genPrimes, that returns the sequence of prime numbers on successive calls to its next() method: 2, 3, 5, 7, 11, ...

def genPrimes():
    primes = [] #starts as an empty list
    num = 1 #num starts at one so we get the first prime 2 to start with
    while True:
        num += 1 #increase num by one each time
        for p in primes:
            if num % p == 0: #if num is divsible by any number in the primes list, it is not a prime, so break
                break
        else:
            primes.append(num) #if num is not divisible by primes list, add it to the list!
            yield num #yield the current num. And start from here next time .next method is used.
            
p = genPrimes()
print p.next()
print p.next()
print p.next()
print p.next()
print p.next()