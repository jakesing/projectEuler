import math
import time

# returns whether an input number is prime, true or false
def isPrime(x):
    evens = [0, 2, 4, 6, 8]
    if x == 2 or x == 5:
        return True

    if x % 10 == 5 or x % 10 in evens:
        return False

    for i in range(2, int(x // math.sqrt(x)) + 1):
        if x % i == 0:
            return False

    return True

# returns the factors of an input number
def getFactors(x):
    results = []
    if x % 2 != 0:
        lower = 3
    else:
        lower = 2
    for i in range(lower, int(x // math.sqrt(x)) + 1, 2):
        if x % i == 0:
            results.append(i)
            results.append(y / i)

    return results

# returns the prime factors of an input number.
def primeFactors(x):
    return filter(isPrime, getFactors(x))

# returns the largest prime factor of an input number
def largestPrimeFactor(x):
    return max(primeFactors(x))

# recursive function to determine palindromicity
def is_palindrome(x):
    x = str(x)
    if len(x) == 1:
        return True
    elif len(x) == 2:
        return x[0] == x[len(x)-1]
    else:
        return x[0] == x[len(x)-1] and is_palindrome(x[1:len(x)-1])

def run_and_register_time(function):
    start = time.time()
    ans = function
    elapsed = (time.time() - start)
    print(ans, "found in", elapsed, "seconds")


