# A Number is said to be Disarium number when the sum of its digit raised to the power of their respective positions becomes equal to the number itself. Write a program to print number is Disarium or not.

# Input Format:

# Single Integer Input from stdin.

# Output Format:

# Yes or No.

# Example Input:

# 175

# Output:

# Yes

# Explanation

# 1^1 + 7^2 +5^3 = 175

# Example Input:

# 123

# Output:

# No

# For example:

# Input

# Result

# 175

# Yes

# 123

# No


n=int(input())
x=n
l=[]
c=0
while(x>0):
    l.append(x%10)
    x=x//10
    c+=1
sum=0
for i in l:
    j=pow(i,c)
    sum=sum+j
    c-=1
if(sum==n):
    print("Yes")
else:
    print("No")
