# It is commonly said that one human year is equivalent to 7 dog years. However this simple conversion fails to recognize that dogs reach adulthood in approximately two years. As a result, some people believe that it is better to count each of the first two human years as 10.5 dog years, and then count each additional human year as 4 dog years.

# Write a program that implements the conversion from human years to dog years described in the previous paragraph. Ensure that your program works correctly for conversions of less than two human years and for conversions of two or more human years. Your program should display an appropriate error message if the user enters a negative number.

# Sample Input 1:

# 10

# Sample Output 1:

# The dog is 53.0 years old in dog years.

# Sample Input 2:

# 2

# Sample Output 2:

# The dog is 21.0 years old in dog years.

# Sample Input 3:

# -5

# Sample Output 3:

# Please enter a positive integer. 

n=int(input())
if(n<0):
    print("Please enter a positive integer.")
elif(n>1):
    print("The dog is",2*10.5 +(n-2)*4,"years old in dog years.")
else:
    print("The dog is",1*10.5 +(n-1)*4,"years old in dog years.")
