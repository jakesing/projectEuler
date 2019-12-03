import math
import time


def isPrime(x):
    for i in range(2, int(x // math.sqrt(x)) + 1):
        if x % i == 0:
            return False

    return True


def getFactors(y):
    results = []
    if y % 2 != 0:
        lower = 3
    else:
        lower = 2
    for i in range(lower, int(y // math.sqrt(y)) + 1, 2):
        if y % i == 0:
            results.append(i)
            results.append(y / i)

    return results


def primeFactors(x):
    return filter(isPrime, getFactors(x))


def largestPrimeFactor(x):
    return max(primeFactors(x))


def main():
    start = time.time()
    ans = largestPrimeFactor(600851475143)
    elapsed = (time.time() - start)
    print(ans, "found in", elapsed, "seconds")

if __name__ == "__main__":
    main()

# correct answer is: 6857