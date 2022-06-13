# Determine the factors of a number (i.e., all positive integer values that evenly divide into a number).



# Sample Input and Output


# 20

# 1 2 4 5 10 20

x=int(input())
for i in range(1,x+1):
    if(x%i==0):
        print(i,end=' ')
