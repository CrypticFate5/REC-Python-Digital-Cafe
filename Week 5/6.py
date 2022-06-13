# Write a program that takes as input a string (sentence), and returns its second word in uppercase.

# For example:

# If input is “Wipro Technologies Bangalore” the function should return “TECHNOLOGIES”

# If input is “Hello World” the function should return “WORLD”

# If input is “Hello” the program should return “LESS”

# NOTE 1: If input is a sentence with less than 2 words, the program should return the word “LESS”.

# NOTE 2: The result should have no leading or trailing spaces.


# For example:

# Input	Result
# Wipro Technologies Bangalore
# TECHNOLOGIES
# Hello World
# WORLD
# Hello
# LESS

l=[]
st=input()
l=st.split()
if(len(l)==1):
    print("LESS")
else:
    print(l[1].upper())
