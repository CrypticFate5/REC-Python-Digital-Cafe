# Write a python program to read a string and a character, print the number of occurrence of the character in the string and the location of the first occurrence.

# Note: To convert an input string to tuple use tuple(variablename).

# Sample Input

# Apple

# p

# Sample Output

# 2

# 1

st=tuple(input())
ch=input()
print(st.count(ch))
print(st.index(ch))
