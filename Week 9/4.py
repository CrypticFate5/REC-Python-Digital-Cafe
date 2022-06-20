# You are given an array of N integers, A1, A2, . . . , AN and an integer K. Return the of count of distinct numbers in all windows of size K.

# Input :

# 1 2 1 3 4 3

# 3

# Output :

# 2

# 3

# 3

# 2

# Explanation

# All windows of size K are

# [1, 2, 1]

# [2, 1, 3]

# [1, 3, 4]

# [3, 4, 3]

l=input().split()
n=int(input())
x=[]
for i in range(0,len(l)-2):
    x.append(l[i:i+3])
for i in x:
    c=0
    d={}
    for j in i:
        if j in d.keys():
            d[j]+=1
        else:
            d[j]=1
    for j in d.keys():
        if d[j]>=1:
            c+=1
    print(c)
