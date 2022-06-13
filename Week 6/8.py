# A teacher want to get the sum of the marks of the students stored in a list. The sum should be calculated for the rounded values given in an array. Students can also have a negative marks. Write a python code to her the teacher to get the rounded sum of values given in the list.

# Sample test case

# sample input

# 2

# 2

# 10.33

# -2.56

# 2.44

# 3.45

# sample output

# 7

# 5

# ROUND SUM
t=int(input())
n=int(input())
l=[]
for i in range(0,t):
    s=0
    for j in range(0,n):
        x=float(input())
        s+=round(x)
    print(s)
