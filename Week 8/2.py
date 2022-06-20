# Given two lists, print all the common element of two lists.

# Note: Sort the list before printing.

# Examples:

# Input : 
# 1 2 3 4 5 
# 5 6 7 8 9
# Output : 
# 5

# Input : 
# 1 2 3 4 5 
# 6 7 8 9
# Output : 
# No common elements 

# Input : 
# 1 2 3 4 5 6
# 5 6 7 8 9
# Output : 
# 5 6

l1=input().split()
l2=input().split()
s1=set(l1)
s2=set(l2)
if(s1 & s2):
    s=s1&s2
    s=sorted(s)
    for i in s:
        print(i,end=' ')
else:
    print("No common elements")
