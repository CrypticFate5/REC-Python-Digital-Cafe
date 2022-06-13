# Write a program to return the nth number in the fibonacci series.

# The value of N will be passed to the program as input.

# NOTE: Fibonacci series looks like –

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, . . . and so on.

# i.e. Fibonacci series starts with 0 and 1, and continues generating the next number as the sum of the previous two numbers.

# • first Fibonacci number is 0,

# • second Fibonacci number is 1,

# • third Fibonacci number is 1,

# • fourth Fibonacci number is 2,

# • fifth Fibonacci number is 3,

# • sixth Fibonacci number is 5,

# • seventh Fibonacci number is 8, and so on.



# For example:

# Input

# Result

# 1

# 0

# 4

# 2

# 7

# 8

x=int(input())
a=0
b=1
sum=a
for i in range(2,x):
    sum=a+b
    a=b
    b=sum
print(b)
