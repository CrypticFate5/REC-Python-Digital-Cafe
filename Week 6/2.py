# Write a program that reads integers from the user and stores them in a list. Use 0 as a sentinel value to mark the end of the input. Once all of the values have been read your program should display them (except for the 0) in reverse order, with one value appearing on each line.

# Sample Input


# 33
# 11
# 22
# 55
# 44
# 0
# Sample Output
# 55
# 44
# 33
# 22
# 11

l=[]
n=int(input())
while(n!=0):
    l.append(n)
    n=int(input())
l.sort()
for i in range(len(l)-1,-1,-1):
    print(l[i])
