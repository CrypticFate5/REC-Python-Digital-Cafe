# Create a program that reads two integers, a and b, from the user. Your program should compute and display:

# • The sum of a and b

# • The difference when b is subtracted from a

# • The product of a and b

# • The quotient when a is divided by b

# • The remainder when a is divided by b

# Sample Input:

# 10

# 20

# Sample Output:

# 10 + 20 is 30

# 10 - 20 is -10

# 10 * 20 is 200

# 10 / 20 is 0.5

# 10 % 20 is 10

a=int(input())
b=int(input())
print(a,"+",b,"is",a+b)
print(a,"-",b,"is",a-b)
print(a,"*",b,"is",a*b)
print(a,"/",b,"is",a/b)
print(a,"%",b,"is",a%b)
