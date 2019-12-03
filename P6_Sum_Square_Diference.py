import time

def sum_first_n(n):
    return ((n*(n+1))/2)

def sum_squares(n):
    return (2*(n**3) + 3*(n**2) + n)/6

ans = sum_first_n(100)**2 - sum_squares(100)

start = time.time()
elapsed = (time.time() - start)
print(ans, "found in", elapsed, "seconds")
print("Our Check: ", ans == 25164150)

# right answer: 25164150