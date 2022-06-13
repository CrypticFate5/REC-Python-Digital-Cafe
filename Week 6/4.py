# Create a program that reads integers from the user until a blank line is entered. Once all of the integers have been read your program should display all of the negative numbers, followed by all of the zeros, followed by all of the positive numbers. Within each group the numbers should be displayed in the same order that they were entered by the user. For example, if the user enters the values 3, -4, 1, 0, -1, 0, and -2 then your program should output the values -4, -1, -2, 0, 0, 3, and 1. Your program should display each value on its own line.

# Sample Input

# 0

# 5

# 10

# -15

# -20



# Sample Output

# -15

# -20

# 0

# 5

# 10


l=[]
x=input()
l.append(x)
while(x!='\n'):
    try:
        x=input()
        l.append(x)
    except EOFError:
        break
l.pop()
for i in l:
    if(int(i)<0):
        print(i)
for i in l:
    if(int(i)==0):
        print(i)
for i in l:
    if(int(i)>0):
        print(i)
