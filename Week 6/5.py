# An integer, n, is said to be perfect when the sum of all of the proper divisors of n is equal to n. For example, 28 is a perfect number because its proper divisors are 1, 2, 4, 7 and 14, and 1 + 2 + 4 + 7 + 14 = 28. 

# If the given number is a perfect number then your program will return True. Otherwise it will return False.

sum=0
n=int(input())
for i in range(1,n):
    if(n%i==0):
        sum+=i
if(sum==n):
    print(True)
else:
    print(False)
