import math
import time

def is_palindrome(x):   # recursive function to determine palindromicity
    x = str(x)
    if len(x) == 1:
        return True
    elif len(x) == 2:
        return x[0] == x[len(x)-1]
    else:
        return x[0] == x[len(x)-1] and is_palindrome(x[1:len(x)-1])


def has_three_digit_factors(x):
    for i in range(int(x // math.sqrt(x))+1,100,-1):
        if x % i == 0 and len(str(x / i)) == 3:
            return True

    return False


def largest_palindrome_product():
    start = 999 * 999
    end = 100 * 100
    increment = -1

    for i in range(start, end, increment):
        if is_palindrome(i) and has_three_digit_factors(i):
            return i


start = time.time()
ans = largest_palindrome_product()
elapsed = (time.time() - start)
print(ans, "found in", elapsed, "seconds")

# correct answer is 906609
