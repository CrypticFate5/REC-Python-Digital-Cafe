# A prime number is an integer greater than one that is only divisible by one and itself. Write a function that determines whether or not its parameter is prime, returning True if it is, and False otherwise. 

def isPrime(n):
    flag=0;
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            flag=1
            break
    if(flag==1 or n==1):
        return False
    else:
        return True
    
