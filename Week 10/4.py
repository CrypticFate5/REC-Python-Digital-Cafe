# Write a Python function sumofsquares(m) that takes an integer m returns True if m is a sum of squares and False otherwise. (If m is not positive, your function should return False.)

 

# Here are some examples to show how your function should work.

# >>> sumofsquares(41)

# True

 

# >>> sumofsquares(30)

# False

 

# >>> sumofsquares(17)

# True

 
from math import *

def issquare(n):
    k = int(sqrt(n))
    return(k*k == n)
    
def sumofsquares(n):
    i = 1
    while i * i <= n :
        j = 1
        while(j * j <= n) :
            if (i * i + j * j == n) :
                return True
            j = j + 1
        i = i + 1
         
    return False

