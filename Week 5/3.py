# Write a program to get 3 strings as input.

# In the 1st string, replace the vowels with “
# In the 2nd string, replace the consonants with *
# In the third string, convert the lowercase letters to upper case.

# Input Format:

# Take 3 Strings from stdin

# Output Format:

# In the 1st string, replace the vowels with "
# In the 2nd string, replace the consonants with *
# In the third string, convert the lowercase letters to upper case.
# Example Input:
# Hello
# Hi
# GoodMorning

# Output:
# H"ll"
# *i
# GOODMORNING

s1=input()
s2=input()
s3=input()
vowels="AEIOUaeiou"
for i in s1:
    if(i in vowels):
        print('''"''',end='')
    else:
        print(i,end='')
print()
for i in s2:
    if(i in vowels):
        print(i,end='')
    else:
        print("*",end='')
print()
print(s3.upper())
