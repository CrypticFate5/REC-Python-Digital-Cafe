# Given a sorted linked list, delete all duplicates such that each element appear only once.

# Example 1:

# Input: 
# 1 1 2
# Output: 
# 1 2
# Example 2:

# Input: 
# 1 1 2 3 3
# Output: 
# 1 2 3

# l=input().split()
# ans=[]
# for i in range(0,len(l)):
#     if(l[i] not in ans):
#         ans.append(l[i])
# for i in ans:
#     print(i,end=' ')
s=set(input().split())
s=sorted(s)
for i in s:
    print(i,end=' ')
