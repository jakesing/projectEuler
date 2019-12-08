from helpers import *

def nth_prime(x):
    primes = []
    i = 2
    while len(primes) < x:
        if isPrime(i):
            primes.append(i)
            i += 1
        else:
            i += 1
    return primes[x-1]

print nth_prime(10001)
