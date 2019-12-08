from helpers import *

def is_pythag(a, b, c):
    if a**2 + b**2 == c**2:
        return True
    else:
        return False

for a in range(1,1000):
    for b in range(1,1000):
        for c in range(1,1000):
            if a + b + c == 1000 and is_pythag(a,b,c):
                print (a,b,c), a*b*c
