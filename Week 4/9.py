# The user is given two integer numbers, lower value, and upper value. The task is to write the Python program for printing all the prime numbers between the given interval (or range).



# Sample Input and Output

# 2

# 7

# 2 3 5

def prime(n):
    flag=0
    for i in range(2,int(pow(n,0.5))+1):
        if(n%i)==0:
            flag=1
            break
    if(flag==0):
        print(n,end=' ')
            
x=int(input())
y=int(input())
flag=0
for i in range(x,y):
    prime(i)
