# Write a function that takes three numbers as parameters, and returns the median value of those parameters as its result.

def median(a, b, c):
    l=[a,b,c]
    l.sort()
    return l[1]
