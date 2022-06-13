# Write a program that reads integers from the user and stores them in a list. Your program should continue reading values until the user enters 0. Then it should display all of the values entered by the user (except for the 0) in ascending order, with one value appearing on each line. Use either the sort method or the sorted function to sort the list.

# Sample Input

# 20
# 30
# 40
# 50
# 10
# 0
# Sample Output
# 10
# 20
# 30
# 40
# 50

n=int(input())
l=[]
l.append(n)
while(n!=0):
    n=int(input())
    l.append(n)
    
l.sort()
for i in range(1,len(l)):
    print(l[i])
