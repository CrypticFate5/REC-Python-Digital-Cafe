# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

# Input Format:

# The first line of the input contains a statement.

# Output Format:

# Print the number of upper case and lower case respectively separated by a space.

# Example:

# Input:

# Hello world!

# Output:

# 1 9

st=input()
l=0
u=0
for i in range(0,len(st)):
    if(st[i].islower()):
        l+=1
    elif(st[i].isupper()):
        u+=1
print(u,l)
