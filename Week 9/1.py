# Create a program that determines and displays the number of unique characters in a string entered by the user. For example, Hello, World! has 10 unique characters while zzz has only one unique character. Use a dictionary or set to solve this problem.

# For example:

# Input	Result
# Hello, World!
# 10

st=input()
d={}
c=0
for i in st:
    if i in d.keys():
        d[i]+=1
    else:
        d[i]=1
print(len(d.values()))
