# In many jurisdictions a small deposit is added to drink containers to encourage people to recycle them. In one particular jurisdiction, drink containers holding one liter or less have a $0.10 deposit, and drink containers holding more than one liter have a $0.25 deposit.

# Write a program that reads the number of containers (less and more) of each size from the user. Your program should continue by computing and displaying the refund that will be received for returning those containers. Format the output so that it includes a dollar sign and always displays exactly two decimal places.

# Sample Input

# 10

# 20

# Sample Output

# Your total refund will be $6.00.

a=int(input())
b=int(input())
ans=a*0.1 + b*0.25
print("Your total refund will be ${:.2f}.".format(ans))
