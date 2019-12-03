from functools import reduce
from P3_Largest_Prime_Factor import *


def get_prime_factors(x):
    thefactors = []
    if x == 16:
        return [2,2,2,2]
    else:
        for factor in getFactors(x):
            if isPrime(factor):
                thefactors.append(factor)
            else:
                for doubleFactor in getFactors(factor):
                    thefactors.append(doubleFactor)
        return thefactors


def calc_small_multiple(start,end):
    results = []
    for i in range(start, end):
        if isPrime(i):
            results.append(i)
        else:
            factors = get_prime_factors(i)
            tempResults = results[:]
            for x in factors[:]:
                if x in tempResults:
                    factors.remove(x)
                    tempResults.remove(x)
                else:
                    results.append(x)

    return reduce(lambda a,b: a* b, results)



start = time.time()
ans = calc_small_multiple(2,20)
elapsed = (time.time() - start)
print(ans, "found in", elapsed, "seconds")


# correct answer is: 232792560


