from helpers import *

def summation_of_primes(n):
    total = 5
    i = 5
    while i <= n:
        if isPrime(i):
            total += i
        i += 2

    return total


#run_and_register_time(summation_of_primes(2000000))

start = time.time()
ans = summation_of_primes(2000000)
elapsed = (time.time() - start)
print(ans, "found in", elapsed, "seconds")


#142913828922