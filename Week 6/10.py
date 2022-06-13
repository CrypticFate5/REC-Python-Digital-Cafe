# Write a program to add maximum number in both its row and column of a matrix. Find the maximum element row wise and maximum element column wise and add both the elements.

# Sample test case

# sample input

# 1  2  3

# 2  5  4

# 4  3  6

# Sample Output

# 11

# Explanation

# in first row 3 is maximum element but it is not maximum element in that column, so leave it and take second row 5 is maximum element in the row and also in that column so take 6 and move to third row 6 is maximum element in row as well as column so take it. now add 5 and 6 which is 11.


#ADDING MAX NUMBERS
l=[]
# n can be changed to input
n=3 
for i in range(0,n):
    sl=[]
    for j in range(0,n):
        x=int(input())
        sl.append(x)
    l.append(sl)
s=0
for i in range(0,n):
    m=max(l[i])
    ind=l[i].index(m)
    c=0
    for j in range(0,n):
        if(l[j][i]>m):
            break
        else:
            c+=1
    if(c==n):
        s+=m
print(s)
