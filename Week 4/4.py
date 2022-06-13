# Write a program to find the count of ALL digits in a given number N. The number will be passed to the program as an input of type int.

# Assumption: The input number will be a positive integer number>= 1 and<= 25000.

# For e.g.

# If the given number is 292, the function should return 3 because there are 3 digits in this number

# If the given number is 1015, the function should return 4 because there are 4 digits in this number



# For example:

# Input

# Result

# 292

# 3

# 1015

# 4

x=int(input())
c=0
while(x>0):
    x=x//10
    c+=1
print(c)
